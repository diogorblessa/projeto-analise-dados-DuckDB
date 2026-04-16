-- Q3.c: Clientes com compras em pelo menos 3 meses consecutivos.
-- Tecnica: LAG sobre grao mensal para detectar continuidade.
-- Fonte esperada: view `vendas` no DuckDB in-memory com coluna `receita` derivada em Q2.

WITH vendas_validas AS (
    -- Apenas pedidos concluidos de clientes identificados.
    SELECT
        pedido_id,
        cliente_id,
        data_pedido,
        receita
    FROM vendas
    WHERE status NOT IN ('cancelado', 'devolvido')
      AND cliente_anonimo = FALSE
),
meses_cliente AS (
    -- Deduplicacao cliente-mes: 1 linha por par, independente do numero de pedidos no mes.
    SELECT DISTINCT
        cliente_id,
        CAST(EXTRACT(YEAR FROM data_pedido) AS INTEGER) * 12
            + CAST(EXTRACT(MONTH FROM data_pedido) AS INTEGER) AS mes_num
    FROM vendas_validas
),
meses_com_gap AS (
    -- Gap = 1 indica mes imediatamente consecutivo; NULL marca primeira linha do cliente.
    SELECT
        cliente_id,
        mes_num,
        mes_num - LAG(mes_num) OVER (
            PARTITION BY cliente_id
            ORDER BY mes_num
        ) AS gap_meses
    FROM meses_cliente
),
grupos_consecutivos AS (
    -- Soma cumulativa cria grupo_id unico por sequencia continua dentro do cliente.
    SELECT
        cliente_id,
        mes_num,
        SUM(
            CASE WHEN gap_meses IS NULL OR gap_meses <> 1 THEN 1 ELSE 0 END
        ) OVER (
            PARTITION BY cliente_id
            ORDER BY mes_num
        ) AS grupo_id
    FROM meses_com_gap
),
sequencias AS (
    SELECT
        cliente_id,
        grupo_id,
        COUNT(*) AS meses_consecutivos
    FROM grupos_consecutivos
    GROUP BY
        cliente_id,
        grupo_id
),
clientes_qualificados AS (
    -- DISTINCT evita dupla contagem caso o cliente tenha mais de uma sequencia de 3+ meses.
    SELECT DISTINCT
        cliente_id
    FROM sequencias
    WHERE meses_consecutivos >= 3
)
SELECT
    cq.cliente_id,
    COUNT(DISTINCT vv.pedido_id) AS pedidos_totais,
    ROUND(SUM(vv.receita), 2) AS receita_total
FROM clientes_qualificados AS cq
JOIN vendas_validas AS vv
    ON vv.cliente_id = cq.cliente_id
GROUP BY cq.cliente_id
ORDER BY receita_total DESC;

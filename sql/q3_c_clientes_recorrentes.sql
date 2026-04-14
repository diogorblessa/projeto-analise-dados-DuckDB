-- Q3.c: Clientes com pedidos em pelo menos 3 meses consecutivos em 2024.
-- Usa LAG para identificar sequências contínuas de meses; filtra sequência máxima >= 3.
-- Fonte: dataset tratado em Q2 (view `vendas`).

WITH meses AS (
    -- Meses distintos de compra por cliente (pedidos concluídos)
    SELECT DISTINCT
        cliente_id,
        EXTRACT(YEAR FROM data_pedido)::INTEGER * 12
            + EXTRACT(MONTH FROM data_pedido)::INTEGER AS mes_num
    FROM vendas
    WHERE status NOT IN ('cancelado', 'devolvido')
),
com_gap AS (
    -- Distância entre meses consecutivos do mesmo cliente
    SELECT
        cliente_id,
        mes_num,
        mes_num - LAG(mes_num) OVER (PARTITION BY cliente_id ORDER BY mes_num) AS gap
    FROM meses
),
grupos AS (
    -- Numera cada sequência contínua: novo grupo quando gap IS NULL ou gap > 1
    SELECT
        cliente_id,
        mes_num,
        SUM(CASE WHEN gap IS NULL OR gap <> 1 THEN 1 ELSE 0 END)
            OVER (PARTITION BY cliente_id ORDER BY mes_num) AS grupo_id
    FROM com_gap
),
sequencias AS (
    -- Tamanho de cada sequência contínua por cliente
    SELECT
        cliente_id,
        grupo_id,
        COUNT(*) AS meses_consecutivos
    FROM grupos
    GROUP BY cliente_id, grupo_id
),
clientes_qualificados AS (
    SELECT DISTINCT cliente_id
    FROM sequencias
    WHERE meses_consecutivos >= 3
)
SELECT
    cq.cliente_id,
    COUNT(DISTINCT v.pedido_id) AS pedidos_totais,
    ROUND(SUM(v.qtd * v.valor_unit * (1 - v.desconto_pct / 100.0)), 2) AS receita_total
FROM clientes_qualificados cq
JOIN vendas v ON cq.cliente_id = v.cliente_id
    AND v.status NOT IN ('cancelado', 'devolvido')
GROUP BY cq.cliente_id
ORDER BY receita_total DESC;

-- Q3.a: Top 5 produtos por receita liquida nos ultimos 90 dias.
-- Janela: MAX(data_pedido) - INTERVAL 90 DAY.
-- Fonte esperada: view `vendas` no DuckDB in-memory com coluna `receita` derivada em Q2.

WITH vendas_validas AS (
    -- Remove pedidos nao concluidos e aplica janela de 90 dias a partir da data mais recente.
    SELECT
        pedido_id,
        produto,
        qtd,
        receita
    FROM vendas
    WHERE status NOT IN ('cancelado', 'devolvido')
      AND data_pedido >= (SELECT MAX(data_pedido) FROM vendas) - INTERVAL 90 DAY
),
receita_por_produto AS (
    SELECT
        produto,
        ROUND(SUM(receita), 2) AS receita_liquida,
        SUM(qtd) AS unidades_vendidas,
        COUNT(DISTINCT pedido_id) AS pedidos
    FROM vendas_validas
    GROUP BY produto
)
SELECT
    produto,
    receita_liquida,
    CAST(unidades_vendidas AS INTEGER) AS unidades_vendidas,
    pedidos
FROM receita_por_produto
ORDER BY receita_liquida DESC
LIMIT 5;

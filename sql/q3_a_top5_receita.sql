-- Q3.a: Top 5 produtos por receita líquida nos últimos 90 dias do dataset.
-- Referência temporal: MAX(data_pedido) do próprio dataset (não data de execução).
-- Fonte: dataset tratado em Q2 (registrado como view `vendas` no DuckDB in-memory).

WITH janela AS (
    -- Última data disponível no dataset como âncora dos 90 dias
    SELECT MAX(data_pedido) - INTERVAL 90 DAYS AS data_inicio
    FROM vendas
),
receita_produto AS (
    SELECT
        produto,
        SUM(qtd * valor_unit * (1 - desconto_pct / 100.0)) AS receita_liquida,
        SUM(qtd) AS unidades_vendidas,
        COUNT(DISTINCT pedido_id) AS pedidos
    FROM vendas, janela
    WHERE data_pedido >= janela.data_inicio
      AND status NOT IN ('cancelado', 'devolvido')
    GROUP BY produto
)
SELECT
    produto,
    ROUND(receita_liquida, 2) AS receita_liquida,
    unidades_vendidas,
    pedidos
FROM (
    SELECT
        produto,
        receita_liquida,
        unidades_vendidas,
        pedidos,
        ROW_NUMBER() OVER (ORDER BY receita_liquida DESC) AS rn
    FROM receita_produto
) AS ranking
WHERE rn <= 5
ORDER BY receita_liquida DESC;

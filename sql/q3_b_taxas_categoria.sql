-- Q3.b: Taxa de cancelamento e devolucao por categoria.
-- Numerador: status `cancelado` + `devolvido`.
-- Fonte esperada: view `vendas` no DuckDB in-memory.

WITH resumo_categoria AS (
    SELECT
        categoria,
        COUNT(*) AS total_pedidos,
        SUM(CASE WHEN status IN ('cancelado', 'devolvido') THEN 1 ELSE 0 END) AS nao_concluidos
    FROM vendas
    GROUP BY categoria
)
SELECT
    categoria,
    total_pedidos,
    CAST(nao_concluidos AS INTEGER) AS nao_concluidos,
    ROUND(
        100.0 * nao_concluidos / NULLIF(total_pedidos, 0),
        2
    ) AS taxa_cancelamento_devolucao_pct
FROM resumo_categoria
ORDER BY taxa_cancelamento_devolucao_pct DESC;

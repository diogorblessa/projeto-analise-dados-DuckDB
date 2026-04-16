-- Q3.d: Ticket medio por UF com pedidos entregues.
-- Filtro: apenas status `entregue`. Pedidos sem UF sao excluidos (DI-006 em Q2: sem imputacao).
-- Fonte esperada: view `vendas` no DuckDB in-memory com coluna `receita` derivada em Q2.

WITH pedidos_entregues AS (
    SELECT
        pedido_id,
        uf,
        receita
    FROM vendas
    WHERE status = 'entregue'
      AND uf IS NOT NULL
)
SELECT
    uf,
    COUNT(DISTINCT pedido_id) AS pedidos_entregues,
    ROUND(SUM(receita), 2) AS receita_total,
    ROUND(
        SUM(receita) / NULLIF(COUNT(DISTINCT pedido_id), 0),
        2
    ) AS ticket_medio
FROM pedidos_entregues
GROUP BY uf
ORDER BY ticket_medio DESC;

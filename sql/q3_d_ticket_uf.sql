-- Q3.d: Ticket médio por UF em 2024.
-- Fonte: dataset tratado em Q2 (view `vendas`).

SELECT
    uf,
    COUNT(DISTINCT pedido_id) AS pedidos,
    ROUND(
        SUM(qtd * valor_unit * (1 - desconto_pct / 100.0))
        / COUNT(DISTINCT pedido_id),
        2
    ) AS ticket_medio
FROM vendas
WHERE status = 'entregue'
GROUP BY uf
ORDER BY ticket_medio DESC;

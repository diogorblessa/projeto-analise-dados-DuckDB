# Q3 - SQL

## Objetivo
Responder quatro perguntas do comercial via DuckDB in-memory sobre o dataset tratado.

## Subquestões
- **Q3.a:** Top 5 produtos por receita líquida nos **últimos 90 dias** do dataset (âncora: `MAX(data_pedido) - 90 DAYS`); excluir cancelados e devolvidos.
- **Q3.b:** Taxa de **cancelamento e devolução** por categoria (`status IN ('cancelado', 'devolvido')`).
- **Q3.c:** Clientes com pedidos em **pelo menos 3 meses consecutivos**; usar LAG para detectar sequências contínuas de meses.
- **Q3.d:** Ticket médio por UF filtrando apenas `status = 'entregue'`.

## Padrões
- DuckDB in-memory exclusivo. Nunca SQLite ou banco externo.
- Cada query também mora em `sql/q3_*.sql` como artefato reproduzível.
- No notebook, carregar via `duckdb.sql(open("sql/q3_x.sql").read())` ou equivalente.
- Siga `.claude/rules/sql-conventions.md` para estilo.

## Entregáveis por subquestão
- `[MD explicacao]` com a pergunta e o critério da métrica.
- `[CODE]` executando a query e mostrando o resultado.
- `[MD analise]` interpretando o ranking ou número, não apenas repetindo o output.

## Restrições
- Use o dataset tratado de Q2; não reexecute tratamento aqui.
- Cancelamento deve usar o valor de `status` definido em Q2.

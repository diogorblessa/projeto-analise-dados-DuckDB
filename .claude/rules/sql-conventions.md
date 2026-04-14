---
paths:
  - "sql/**/*.sql"
---

# SQL Conventions

Use em qualquer tarefa que escreva ou revise SQL.

## Motor
- Exclusivamente DuckDB in-memory. Nunca SQLite, Postgres ou outro banco externo.
- No notebook, preferir registrar o DataFrame tratado e consultar via `duckdb.sql(...)`.

## Estilo
- Palavras-chave SQL em maiusculas.
- Nomes de colunas e tabelas em `snake_case` minusculas.
- Uma coluna por linha em `SELECT` quando houver mais de tres.
- Indentacao consistente; alinhe `ON` abaixo do `JOIN`.
- Comentários curtos em português explicando a intenção, não a sintaxe.
- Aliases descritivos.

## Arquivos
- Queries Q3 vivem em `sql/q3_*.sql`.
- Cada `.sql` deve ser executavel isoladamente sobre `data/raw/ecommerce_vendas.csv` ou `data/interim/*.parquet`, assumindo o dataset tratado.
- Cabeçalho do arquivo com comentário indicando a pergunta respondida e a tabela ou fonte assumida.

## Nomes canônicos de colunas
- `desconto_%` do CSV é renomeado para `desconto_pct` no tratamento (Q2). Usar `desconto_pct` em todas as queries.

## Restrições
- Não usar `SELECT *` em query final.
- Não usar funções específicas de outros dialetos sem equivalente em DuckDB.
- Evitar subqueries aninhadas profundas; prefira CTEs.

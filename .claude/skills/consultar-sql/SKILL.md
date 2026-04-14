---
name: consultar-sql
description: Executa Q3 - queries DuckDB (subquestões a-d)
argument-hint: <a|b|c|d|all>
disable-model-invocation: true
---

Execute a questão Q3 do `docs/PRD.md` no notebook.

`$ARGUMENTS` define a subquestão: `a`, `b`, `c`, `d` ou `all`. Se vier vazio ou ambíguo, não assuma `all`; peça clarificação antes de executar.

Use [reference.md](reference.md) como checklist detalhado da questão.

## Fluxo
1. Carregue apenas a seção Q3 do `docs/PRD.md`, o notebook, os arquivos `sql/q3_*.sql` relevantes e [reference.md](reference.md).
2. Produza cada subquestão no padrão `[MD explicacao] -> [CODE] -> [MD analise]`.
3. Garanta que cada query tambem exista em `sql/q3_*.sql`.
4. Use DuckDB in-memory sobre o dataset tratado de Q2.

## Restrições
- Nenhum banco externo ou SQLite.
- Não duplicar tratamento já feito em Q2.

---
name: diagnosticar
description: Executa Q1 - diagnóstico de qualidade do dataset
argument-hint: (sem argumentos)
disable-model-invocation: true
---

Execute a questão Q1 do `docs/PRD.md` no `notebooks/case_techshop.ipynb`.

Use [reference.md](reference.md) como checklist detalhado deste workflow.

## Fluxo
1. Carregue apenas a seção Q1 do `docs/PRD.md`, o notebook e [reference.md](reference.md).
2. Produza o bloco Q1 no padrão `[MD explicacao] -> [CODE] -> [MD analise]`.
3. Catalogue os achados em `memory-bank/data-issues.md`.
4. Preserve as demais questões intactas.

## Restrições
- Não aplicar tratamento nesta etapa.
- Não alterar outras questões sem dependência quebrada comprovada.

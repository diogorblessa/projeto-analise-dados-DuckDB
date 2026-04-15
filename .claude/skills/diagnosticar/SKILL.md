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
2. **Fase 1 — código**: escreva `[MD explicacao]` e `[CODE]`. Pare aqui e peça ao usuário para executar a célula.
3. **Fase 2 — análise**: somente após confirmação de outputs visíveis, leia os resultados reais do notebook e escreva `[MD analise]` com referência explícita a esses outputs. Não antecipe valores.
4. Catalogue os achados em `memory-bank/data-issues.md`.
5. Preserve as demais questões intactas.

## Restrições
- Não aplicar tratamento nesta etapa.
- Não alterar outras questões sem dependência quebrada comprovada.

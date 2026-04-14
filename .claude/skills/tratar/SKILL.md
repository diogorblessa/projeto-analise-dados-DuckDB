---
name: tratar
description: Executa Q2 - tratamento de dados com justificativa
argument-hint: (sem argumentos)
disable-model-invocation: true
---

Execute a questão Q2 do `docs/PRD.md` no notebook.

Use [reference.md](reference.md) como checklist detalhado deste workflow.

## Fluxo
1. Carregue apenas a seção Q2 do `docs/PRD.md`, o notebook, `memory-bank/data-issues.md` e [reference.md](reference.md).
2. Aplique tratamentos com antes e depois para cada decisão.
3. Salve o dataset tratado em `data/interim/`.
4. Atualize `memory-bank/decisions.md` com decisões não triviais.

## Restrições
- `data/raw/` e imutável.
- Cada tratamento exige justificativa explícita.

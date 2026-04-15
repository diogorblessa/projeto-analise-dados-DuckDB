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
2. **Fase 1 — código**: para cada tratamento, escreva o `[CODE]` com verificação antes/depois. Pare e peça ao usuário para executar.
3. **Fase 2 — justificativa**: somente após outputs visíveis, escreva a narrativa de decisão com referência explícita aos valores reais do output.
4. Salve o dataset tratado em `data/interim/`.
5. Atualize `memory-bank/decisions.md` com decisões não triviais.

## Restrições
- `data/raw/` é imutável.
- Cada tratamento exige justificativa explícita.

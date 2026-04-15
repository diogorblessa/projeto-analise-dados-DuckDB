---
name: encontrar-erro
description: Executa Q5 - debug do script scripts/análise_crescimento.py
argument-hint: (sem argumentos)
disable-model-invocation: true
---

Execute a questão Q5 do `docs/PRD.md` no notebook.

Use [reference.md](reference.md) como guia detalhado deste workflow.

## Fluxo
1. Carregue apenas a seção Q5 do `docs/PRD.md`, `scripts/analise_crescimento.py`, o notebook e [reference.md](reference.md).
2. Identifique no mínimo `2` erros graves.
3. **Fase 1 — código**: mostre o trecho original (comentado) e o código corrigido em `[CODE]`. Pare e peça ao usuário para executar.
4. **Fase 2 — análise do impacto**: somente após outputs visíveis, escreva a explicação do erro, impacto e validação da correção com base no resultado real.
5. Atualize `memory-bank/decisions.md` se conclusões anteriores mudarem.

## Restrições
- Não editar `scripts/analise_crescimento.py` original.
- As correções vivem no notebook.

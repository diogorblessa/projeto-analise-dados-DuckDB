---
name: revisao-final
description: Auditoria final global do notebook completo
argument-hint: [--auditar|--corrigir]
disable-model-invocation: true
---

Audite o notebook inteiro `notebooks/case_techshop.ipynb` contra os critérios de aceite do `docs/PRD.md`.

Modo opcional `--auditar` (padrão) ou `--corrigir`. Não recebe escopo posicional.

Use [reference.md](reference.md) como fluxo principal e [../shared/review-memory.md](../shared/review-memory.md) para registrar, reaproveitar ou fechar achados.

## Fluxo
1. Valide o modo pedido.
2. Carregue a seção de critérios de aceite do `docs/PRD.md`, o notebook, `memory-bank/review-checklist.md`, `memory-bank/question-status.md`, [reference.md](reference.md) e [../shared/review-memory.md](../shared/review-memory.md).
3. Aplique o checklist global PASS/FAIL com evidência explícita.
4. Em `--corrigir`, aplique apenas correção `objetiva` ainda valida.
5. Atualize `memory-bank/handoff.md` com o estado final.

## Restrições
- Não gerar nova análise nem nova evidência.
- `Resultado geral = PASS` apenas se não houver `FAIL` crítico.

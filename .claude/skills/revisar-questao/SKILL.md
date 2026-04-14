---
name: revisar-questao
description: Audita ou corrige uma questão específica do notebook
argument-hint: <Q1..Q7> [--auditar|--corrigir]
disable-model-invocation: true
---

Revise uma ou mais questões do notebook.

`$ARGUMENTS`: `QN` ou lista `QN,QM`. Modo opcional `--auditar` (padrão, não edita) ou `--corrigir`.

Use [reference.md](reference.md) como fluxo principal e [../shared/review-memory.md](../shared/review-memory.md) para registrar, reaproveitar ou fechar achados.

## Fluxo
1. Valide escopo e modo.
2. Carregue `memory-bank/review-checklist.md`, `memory-bank/question-status.md`, [reference.md](reference.md) e [../shared/review-memory.md](../shared/review-memory.md).
3. Consulte as referências das questões em escopo antes de auditar ou corrigir.
4. Em `--auditar`, registre apenas achados acionáveis e rastreáveis.
5. Em `--corrigir`, aplique somente correções `objetiva` que continuem válidas.

## Restrições
- Escopos inválidos interrompem a tarefa.
- Não criar nova análise; apenas auditar ou ajustar o existente.

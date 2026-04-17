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
2. Carregue `memory-bank/review-checklist.md`, `memory-bank/question-status.md`, [reference.md](reference.md) e [../shared/review-memory.md](../shared/review-memory.md). Carregue também `README.md` e qualquer `.md` narrativo em `docs/` quando esses arquivos estiverem explicitamente em escopo para revisão.
3. Consulte as referências das questões em escopo antes de auditar ou corrigir.
4. Quando `README.md` ou outro `.md` narrativo estiver em escopo, audite se o texto está claro para leitor não técnico, sem jargão desnecessário e com explicação curta para termos inevitáveis.
5. Em `--auditar`, registre apenas achados acionáveis e rastreáveis.
6. Em `--corrigir`, aplique somente correções `objetiva` que continuem válidas.
7. Na resposta final, mantenha o resumo da revisão e inclua uma seção `Checklist PASS/FAIL` com tabela Markdown compacta `requisito | status`, baseada no `Final Checklist Cache`.
8. Em escopo `QN` ou `QN,QM`, filtre a tabela por prefixo de requisito (`Q1 —`, `Q2 —`, etc.) para exibir apenas as questões pedidas, preservando a ordem já registrada no `Final Checklist Cache`.
9. Se não houver critérios cacheados compatíveis com o escopo, declare isso explicitamente em vez de inventar uma tabela vazia.

## Restrições
- Escopos inválidos interrompem a tarefa.
- Não criar nova análise; apenas auditar ou ajustar o existente.

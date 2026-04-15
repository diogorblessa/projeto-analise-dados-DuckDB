---
name: insight-livre
description: Executa Q7 - insight adicional não pedido
argument-hint: (sem argumentos)
disable-model-invocation: true
---

Execute a questão Q7 do `docs/PRD.md` no notebook.

Use [reference.md](reference.md) como guia detalhado deste workflow.

## Fluxo
1. Carregue apenas a seção Q7 do `docs/PRD.md`, o notebook e [reference.md](reference.md).
2. Escolha um único insight com hipótese declarada.
3. **Fase 1 — código**: escreva o `[CODE]` com o agregado e o gráfico ou tabela. Pare e peça ao usuário para executar.
4. **Fase 2 — narrativa**: somente após outputs visíveis, escreva a narrativa do insight e implicação prática com referência aos valores reais.
5. Encerre com implicação prática para o negócio.

## Restrições
- Não repetir achados de Q3 ou Q4.
- Profundidade vale mais que varredura.

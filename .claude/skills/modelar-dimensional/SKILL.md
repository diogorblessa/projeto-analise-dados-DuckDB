---
name: modelar-dimensional
description: Executa Q6 - modelagem dimensional (markdown-only)
argument-hint: (sem argumentos)
disable-model-invocation: true
---

Execute a questão Q6 do `docs/PRD.md` no notebook.

Use [reference.md](reference.md) como guia detalhado deste workflow.

## Fluxo
1. Carregue apenas a seção Q6 do `docs/PRD.md`, o notebook e [reference.md](reference.md).
2. Produza um bloco markdown-only com diagrama.
3. Declare o grao da fato explícitamente.
4. Entregue dicionário de dimensões, chaves e métricas.

## Restrições
- Não exigir o padrão `[MD explicacao] -> [CODE] -> [MD analise]`.
- Apenas desenho; sem DDL ou ETL implementado.

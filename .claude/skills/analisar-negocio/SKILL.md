---
name: analisar-negocio
description: Executa Q4 - decisão de campanha região Sul
argument-hint: (sem argumentos)
disable-model-invocation: true
---

Execute a questão Q4 do `docs/PRD.md` no notebook.

Use [reference.md](reference.md) como guia detalhado deste workflow.

## Fluxo
1. Carregue apenas a seção Q4 do `docs/PRD.md`, o notebook e [reference.md](reference.md).
2. **Fase 1 — código**: escreva o `[CODE]` com as comparações Sul vs. resto. Pare e peça ao usuário para executar.
3. **Fase 2 — recomendação**: somente após outputs visíveis, escreva análise e recomendação explícita com limitações, referenciando os valores reais.
4. Atualize `memory-bank/decisions.md` com a recomendação final.

## Restrições
- Use o dataset tratado de Q2.
- Não invente elasticidade, lift ou efeito de campanha sem evidência.

# Q1 - Diagnóstico

## Carregamento recomendado
- Seção Q1 de `docs/PRD.md`
- `notebooks/case_techshop.ipynb`
- `memory-bank/data-issues.md`

## Objetivo
Mapear problemas de qualidade do dataset que podem comprometer decisões futuras.

## Entregáveis mínimos
- Shape, tipos e amostra comentada.
- Valores ausentes por coluna, incluindo missing disfarcado.
- Duplicatas por `pedido_id` e heuristica de registros repetidos.
- Inconsistências entre colunas, incluindo `uf`, `status`, `data_pedido`, `valor_unit`, `qtd` e `desconto_%`.
- Resumo estatístico numérico com min, max, mediana, média, desvio e nulos.
- Distribuição de categóricas relevantes.

## Restrições
- Não aplicar tratamento neste bloco; apenas diagnosticar.
- Cada achado deve estar apoiado em output visível.
- Catalogue achados em `memory-bank/data-issues.md` com id, severidade e evidência.

## Saída
- `[MD analise]` final de Q1 lista os achados priorizados que entram em Q2.

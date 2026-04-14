# Q2 - Tratamento

## Objetivo
Tornar o dataset confiável, com cada decisão de tratamento justificada e auditável.

## Princípios
- `data/raw/ecommerce_vendas.csv` é imutável.
- Saída tratada vai em `data/interim/`.
- Cada tratamento segue: descrever problema, mostrar antes, aplicar, mostrar depois e justificar.
- Preferir correção determinística a descarte.
- Descartar apenas com justificativa explícita e contagem de registros afetados.

## Tratamentos esperados
- Padronização de `uf`, `status` e `categoria`.
- Conversão de `data_pedido` para `datetime`.
- Coerção numérica de `qtd`, `valor_unit`, `desconto_%` e `avaliacao`. Renomear `desconto_%` para `desconto_pct` no DataFrame tratado — esse é o nome canônico usado em todas as queries e referências downstream.
- Tratamento de nulos por coluna, com política declarada.
- Tratamento de duplicatas com critério explícito.
- Derivação mínima necessária, como `receita = qtd * valor_unit * (1 - desconto_pct/100)` quando usada adiante.

## Saída
- DataFrame final salvo em `data/interim/`.
- `[MD analise]` final com diff de shape e lista de decisões.
- Atualize `memory-bank/decisions.md` com cada decisão não trivial.

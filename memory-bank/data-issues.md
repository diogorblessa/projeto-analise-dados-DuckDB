# Data Issues

Catálogo de problemas de qualidade identificados em Q1 e tratados em Q2.

## Schema
| id | questao | coluna | tipo | severidade | descricao | evidencia | tratamento | status |
|---|---|---|---|---|---|---|---|---|

Tipos típicos: `nulo`, `missing_disfarcado`, `fora_dominio`, `duplicata`, `tipo_errado`, `inconsistencia_cruzada`, `outlier`.
Severidade: `H`, `M`, `L`.
Status: `open`, `in_progress`, `applied`, `wont_fix`.

## Registros

| id | questao | coluna | tipo | severidade | descricao | evidencia | tratamento | status |
|---|---|---|---|---|---|---|---|---|
| DI-001 | Q1 | cliente_id | nulo | H | 25 registros (2,07%) sem cliente_id — impede rastreio de comportamento por cliente | `df['cliente_id'].isnull().sum()` → 25 | pendente Q2 | open |
| DI-002 | Q1 | pedido_id | duplicata | H | 10 linhas duplicadas (5 pedido_ids) — contagem de pedidos e receita total ficam infladas | `df[df.duplicated('pedido_id', keep=False)]` → 10 linhas | pendente Q2 | open |
| DI-003 | Q1 | qtd | outlier | H | 5 registros com qtd <= 0 (mínimo -1) — volume vendido e receita distorcidos | `(df['qtd'] <= 0).sum()` → 5 | pendente Q2 | open |
| DI-004 | Q1 | desconto_% | nulo | M | 30 nulos (2,49%) — margem líquida subestimada para esses pedidos | `df['desconto_%'].isnull().sum()` → 30 | pendente Q2 | open |
| DI-005 | Q1 | avaliacao | nulo | M | 241 nulos (20%); todos em cancelado (138) e em_transito (103) — esperado, mas requer filtro por status antes de qualquer análise de NPS | groupby status × avaliacao: cancelado=0/138, em_transito=0/103, entregue=872/872, devolvido=82/82 | pendente Q2 | open |
| DI-006 | Q1 | uf | nulo | M | 15 nulos (1,24%) — pedidos sem UF excluídos da análise geográfica | `df['uf'].isnull().sum()` → 15 | pendente Q2 | open |
| DI-007 | Q1 | qtd | nulo | M | 12 nulos (1,00%) — linhas sem quantidade não contribuem para volume nem receita | `df['qtd'].isnull().sum()` → 12 | pendente Q2 | open |
| DI-008 | Q1 | status | fora_dominio | M | 8 registros "Entregue" e 2 "Devolvido" com inicial maiúscula — filtros por status falham silenciosamente para esses 10 casos | `df['status'].value_counts()` → Entregue:8, Devolvido:2 | pendente Q2 | open |
| DI-009 | Q1 | categoria | fora_dominio | M | 15 registros com categoria em lowercase (periféricos:6, armazenamento:3, acessórios:2, monitores:2, câmeras:1, impressoras:1) — agrupamentos distorcem contagens | `df['categoria'].value_counts()` → 15 variantes lowercase | pendente Q2 | open |
| DI-010 | Q1 | data_pedido | tipo_errado | M | 20 datas no formato dd/mm/yyyy em vez de yyyy-mm-dd — parse padrão produz NaT para esses registros | `pd.to_datetime(df['data_pedido'], errors='coerce').isna().sum()` → 20; ex: pedido 2146 → "11/02/2024" | pendente Q2 | open |
| DI-011 | Q1 | qtd | tipo_errado | L | Coluna armazenada como float64; todos os valores válidos são inteiros — problema de ingestão sem impacto direto nos cálculos | `df['qtd'].dtype` → float64; `(df['qtd'].dropna() % 1 != 0).sum()` → 0 | pendente Q2 | open |

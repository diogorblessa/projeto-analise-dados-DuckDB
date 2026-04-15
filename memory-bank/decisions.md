# Decisions

Decisões técnicas e de negócio com justificativa. Registre apenas escolhas não triviais e overrides explícitos quando existirem.

## Schema
| id | data | escopo | decisao | motivo | impacto | fonte | status | override_of | aprovacao |
|---|---|---|---|---|---|---|---|---|---|

Status: `proposed`, `accepted`, `rejected`, `superseded`.

`override_of`: use `-` em decisões comuns; preencha com o item do PRD quando houver override explícito.
`aprovacao`: use `-` em decisões comuns; preencha com aprovador ou fonte de aprovação quando `override_of` estiver preenchido.

Decisões comuns documentam interpretação e continuidade operacional. Só um registro `accepted` com `override_of` e `aprovacao` explícitos ajusta o item referenciado do PRD.

## Registros

| id | data | escopo | decisao | motivo | impacto | fonte | status | override_of | aprovacao |
|---|---|---|---|---|---|---|---|---|---|
| DT-001 | 2026-04-15 | Q2/pedido_id | Deduplicar mantendo cópia com cliente_id preenchido; demais: keep='first' | Pedido 1113 tem uma cópia sem cliente_id; descartar a incompleta preserva rastreabilidade do cliente | KPIs de pedidos e receita ficam corretos | DI-002 | accepted | - | - |
| DT-002 | 2026-04-15 | Q2/valor_unit | Dividir por 10 o valor_unit inflado dos 6 produtos com razão 10x exata | Padrão determinístico de erro de cadastro (vírgula decimal deslocada): razão exata, sem ambiguidade | Receita, ticket médio e análise de categoria corrigidos | DI-012 | accepted | - | - |
| DT-003 | 2026-04-15 | Q2/qtd | Remover 5 registros com qtd <= 0 | Quantidade negativa ou zero não representa transação real; não há como imputar valor de negócio | Volume de pedidos e receita sem distorção | DI-003 | accepted | - | - |
| DT-004 | 2026-04-15 | Q2/cliente_id | Manter 25 pedidos sem cliente_id; adicionar flag cliente_anonimo=True | Pedido existe e tem receita real; descartá-lo subestima volume e faturamento | Análises comportamentais por cliente devem filtrar cliente_anonimo=False | DI-001 | accepted | - | - |
| DT-005 | 2026-04-15 | Q2/desconto_% | Imputar 0 nos 30 nulos de desconto_% | Sem registro de desconto, assumir ausência de desconto é a hipótese mais conservadora e reversível | Margem líquida calculada pelo valor cheio nesses pedidos | DI-004 | accepted | - | - |
| DT-006 | 2026-04-15 | Q2/qtd | Remover 12 linhas com qtd nulo | Receita não pode ser calculada sem quantidade; imputar seria especulativo | Volume e receita sem linhas incalculáveis | DI-007 | accepted | - | - |
| DT-007 | 2026-04-15 | Q2/avaliacao | Manter 241 nulos de avaliacao como NaN | Padrão estrutural: apenas pedidos entregues/devolvidos têm avaliação; NaN é informativo | Análises de satisfação devem filtrar por status antes de calcular médias | DI-005 | accepted | - | - |
| DT-008 | 2026-04-15 | Q2/uf | Manter 15 nulos de uf como NaN | Sem dado externo para imputar UF; impor uma UF fictícia distorceria análises regionais | Pedidos sem UF ficam de fora de relatórios regionais | DI-006 | accepted | - | - |

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
| DT-004 | 2026-04-15 | Q2/cliente_id | Manter 24 pedidos sem cliente_id; adicionar flag cliente_anonimo=True | Pedido existe e tem receita real; descartá-lo subestima volume e faturamento | Análises comportamentais por cliente devem filtrar cliente_anonimo=False | DI-001 | accepted | - | - |
| DT-005 | 2026-04-15 | Q2/desconto_% | Imputar 0 nos 28 nulos de desconto_% | Sem registro de desconto, assumir ausência de desconto é a hipótese mais conservadora e reversível | Margem líquida calculada pelo valor cheio nesses pedidos | DI-004 | accepted | - | - |
| DT-006 | 2026-04-15 | Q2/qtd | Remover 12 linhas com qtd nulo | Receita não pode ser calculada sem quantidade; imputar seria especulativo | Volume e receita sem linhas incalculáveis | DI-007 | accepted | - | - |
| DT-007 | 2026-04-15 | Q2/avaliacao | Manter 236 nulos de avaliacao como NaN | Padrão estrutural: apenas pedidos entregues/devolvidos têm avaliação; NaN é informativo | Análises de satisfação devem filtrar por status antes de calcular médias | DI-005 | accepted | - | - |
| DT-008 | 2026-04-15 | Q2/uf | Manter 15 nulos de uf como NaN | Sem dado externo para imputar UF; impor uma UF fictícia distorceria análises regionais | Pedidos sem UF ficam de fora de relatórios regionais | DI-006 | accepted | - | - |
| Q4-001 | 2026-04-16 | Q4/campanha-sul | Recomendar `não prosseguir` com campanha de descontos para região Sul (RS, SC, PR); reavaliar apenas com (i) dados de margem por categoria, (ii) teste controlado pequeno focado em estado e mês de vale (ex.: RS em novembro) e (iii) ao menos um segundo ano de histórico | Sul tem desempenho comparável ou ligeiramente superior ao restante em ticket (`R$ 793,98` vs `R$ 763,62`), cancelamento (`17,60%` vs `18,74%`) e avaliação (`3,87` vs `3,93`); não há evidência de underperformance a corrigir por desconto e base de `250` pedidos/ano é pequena para mensurar efeito | Sustenta a resposta de Q4 no notebook e alinha o time comercial quanto aos condicionantes para retomar a discussão | notebooks/case_techshop.ipynb célula q4_sul_fase1 (execução 19) | superseded | - | - |
| Q4-002 | 2026-04-16 | Q4/campanha-sul | Recomendar `prosseguir com ressalvas`: avançar no planejamento segmentado por estado (SC: retenção/upsell; RS: alvo prioritário de ticket; PR: intermediário); não prosseguir com campanha única Sul-agregado | Reescrita da análise Q4 com base em nota executiva revelou que a heterogeneidade interna (SC `R$ 1.122` vs RS `R$ 583`, amplitude `1,93×`) é o achado dominante — campanha única sacrifica margem em SC sem resolver RS; `prosseguir com ressalvas` é mais acionável que `não prosseguir` mantendo os mesmos condicionantes (margem, segmentação por estado, experimento controlado) | Altera a recomendação final exibida no notebook e o alinhamento com o time comercial | notebooks/case_techshop.ipynb célula q4_sul_fase1_analise (reescrita por nota executiva @business-reporter) | accepted | - | - |

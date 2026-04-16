# Review Checklist

Schema e estado do checklist de aceite. Atualizado por `/revisar-questao` e `/revisao-final`.

## Header
- `schema_version`: 1
- `notebook`: `notebooks/case_techshop.ipynb`
- `last_updated`: 2026-04-16
- `last_writer`: /revisar-questao Q3 --auditar

## Open Findings
Nenhum achado aberto.

## Final Checklist Cache
| requisito | status | evidencia | observacao | source | updated_at |
|---|---|---|---|---|---|
| Notebook executa Restart & Run All | PASS | Execução completa via `nbconvert --execute --inplace` em `2026-04-16` | Notebook salvo sem erro; outputs sincronizados após correções de Q3 | /revisar-questao Q3 --corrigir | 2026-04-16 |
| Q1 — estrutura [MD explicação] → [CODE] → [MD análise] | PASS | 5a904771 → f103d4c0 → ee3d6570 | - | /revisao-final Q1 | 2026-04-15 |
| Q1 — cobertura de tipos de problema (ausentes, duplicatas, inconsistências, outliers, formato) | PASS | Seções 2-3 (nulos/missing), 4 (duplicatas), 5/7a/7c (inconsistências), 7b/7c (outliers), 9 (formato) | - | /revisao-final Q1 | 2026-04-15 |
| Q1 — impacto downstream documentado por achado | PASS | Tabela de nulos com coluna de impacto; seção "O que isso significa para o negócio" | - | /revisao-final Q1 | 2026-04-15 |
| Q1 — afirmações rastreáveis a output visível | PASS | ee3d6570 corrigido: 4/6 outliers IQR identificados como erro 10x; bloco 7c referenciado na narrativa | RF-001 aplicado | /revisar-questao Q1 --corrigir | 2026-04-15 |
| Q1 — data-issues.md cataloga todos os achados (DI-001..DI-012) | PASS | DI-012 adicionado: dispersão 10x, 6 produtos, 8 registros, severidade H | RF-002 aplicado | /revisar-questao Q1 --corrigir | 2026-04-15 |
| Q1 — bloco 7c referenciado na narrativa | PASS | Parágrafo "Consistência interna de preço por produto (bloco 7c)" adicionado em ee3d6570 | RF-003 aplicado | /revisar-questao Q1 --corrigir | 2026-04-15 |
| Q1 — código PEP8, nomenclatura descritiva | PASS | dispersao_valor_unit, produtos_divergentes, avaliacao_por_status — conformes com code-style.md | - | /revisao-final Q1 | 2026-04-15 |
| Q2 — estrutura [MD explicação] → [CODE] → [MD análise] | PASS | 24167198 → ae4bb233 → da751df3 | - | /revisar-questao Q2 --auditar | 2026-04-15 |
| Q2 — cobertura de todos os tratamentos (DI-001..DI-012) | PASS | ae4bb233 cobre todos os 12 DIs; DI-005, DI-006 mantidos com justificativa | - | /revisar-questao Q2 --auditar | 2026-04-15 |
| Q2 — antes e depois por tratamento com justificativa explícita | PASS | RQ-Q2-001 aplicado: DI-010 before-count adicionado em ae4bb233 | - | /revisar-questao Q2 --corrigir | 2026-04-15 |
| Q2 — afirmações rastreáveis a output visível (célula imediata) | PASS | RQ-Q2-001 e RQ-Q2-002 aplicados | - | /revisar-questao Q2 --corrigir | 2026-04-15 |
| Q2 — código PEP8, nomes descritivos, imports centralizados | PASS | linhas_antes_dedup, registros_formato_dmy, produtos_10x, precos_corrigidos — conformes | - | /revisar-questao Q2 --auditar | 2026-04-15 |
| Q2 — desconto_pct canônico, receita derivada, UTF-8 | PASS | rename aplicado; receita = qtd × valor_unit × (1 - desconto_pct/100); encoding='utf-8' no save | - | /revisar-questao Q2 --auditar | 2026-04-15 |
| Q3 — implementada (a/b/c/d) com `[MD explicação] → [CODE] → [MD análise]` | PASS | `5018432c→8a098bbf→ed84982c` (Q3.a); `f23a8f0c→f64d2ab1→473e73d9` (Q3.b); `153a985c→f692c88f→2bf23d63` (Q3.c); `202b9438→23a34e6d→6e8b4428` (Q3.d) | 4 subquestões entregues com Fase 1 e Fase 2 | /revisar-questao Q3 --auditar | 2026-04-16 |
| Q3 — SQL presente em `sql/q3_*.sql` e reproduzível sobre view `vendas` | PASS | `sql/q3_a_top5_receita.sql`, `sql/q3_b_taxas_categoria.sql`, `sql/q3_c_clientes_recorrentes.sql`, `sql/q3_d_ticket_uf.sql` | Cada arquivo com cabeçalho identificando pergunta respondida e fonte esperada | /revisar-questao Q3 --auditar | 2026-04-16 |
| Q3 — aderência ao PRD §Q3 (janela 90 dias, taxa cancel+devol, LAG, status entregue) | PASS | Q3.a: `INTERVAL 90 DAY` sobre `MAX(data_pedido)`; Q3.b: `status IN ('cancelado','devolvido')` ordem DESC; Q3.c: `LAG` em grão mensal + gap + grupos acumulados; Q3.d: `status = 'entregue'` | - | /revisar-questao Q3 --auditar | 2026-04-16 |
| Q3 — afirmações rastreáveis a output visível | PASS | `8a098bbf`, `f64d2ab1`, `f692c88f`, `23a34e6d` | RQ-Q3-004 fechado; `f64d2ab1` agora mostra sanity-check DI-007 com `delta total = 12` e comparativo por categoria (`Periféricos` `270 -> 269`) | /revisar-questao Q3 --auditar | 2026-04-16 |
| Q3 — uso de `receita` canônica e `cliente_anonimo = FALSE` onde aplicável | PASS | `SUM(receita)` em Q3.a/Q3.c/Q3.d; filtro `cliente_anonimo = FALSE` em Q3.c; Q3.b usa contagens porque métrica é taxa | Consistente com decisão de Q2 (DI-001, coluna canônica `receita`) | /revisar-questao Q3 --auditar | 2026-04-16 |
| Q3 — código Python PEP8 com nomenclatura descritiva | PASS | `top5_receita_90d`, `taxas_cancelamento_por_categoria`, `clientes_recorrentes`, `ticket_medio_por_uf`, `total_clientes_identificados`, `pedidos_entregues_total`, `pedidos_considerados` | snake_case, descritivas, sem `n_*`/`mask_*` (feedback de memória respeitado) | /revisar-questao Q3 --auditar | 2026-04-16 |
| Q3 — consistência de filtros de status entre subquestões | PASS | Q3.a e Q3.c: `NOT IN ('cancelado','devolvido')`; Q3.b: todos os status (denominador); Q3.d: `= 'entregue'` (receita realizada) | Cada filtro coerente com a métrica pedida pelo PRD | /revisar-questao Q3 --auditar | 2026-04-16 |
| Q4–Q7 — implementadas | FAIL | Q4, Q5, Q6 e Q7 com placeholders apenas (`a4831bc2`, `d24bda53`, `f1961177`, `76f81a84`) | Blocker global; não impede fechamento de Q1, Q2 e Q3 isolados | /revisar-questao Q3 --auditar | 2026-04-16 |

## Applied/Closed
| id | source | status_final | resolucao | updated_at |
|---|---|---|---|---|
| RQ-Q1-001 | /revisar-questao | stale | Era linha de template do schema sem evidência real; nunca correspondeu a achado ativo | 2026-04-14 |
| RQ-Q1-002 | /revisar-questao | applied | Blockquote adicionado no [MD análise] (ee3d6570) explicando que a tabela IQR exibe 8 linhas porque Monitor 32" 4K e Monitor 27" 144Hz aparecem duas vezes por causa de DI-009 (categoria lowercase) | 2026-04-14 |
| RQ-Q1-003 | /diagnosticar | applied | Três adições em ee3d6570: (1) blockquote após avaliacao×status explicando as 6 linhas do output (vs 4 grupos na narrativa) e DI-008; (2) frase com baseline avaliacao mean=3,92/5, std=1,16, count=964; (3) frase com padrão qtd mediana=1, p75=2, max=5 | 2026-04-15 |
| RQ-Q1-004 | /revisar-questao | applied | Frase adicionada em ee3d6570 após missing disfarçado: desconto_% sem violações de domínio, máximo observado 20% sugere teto de política — referência para Q2 | 2026-04-15 |
| RF-001 | /revisao-final | applied | ee3d6570 corrigido: dois trechos "produtos legítimos" substituídos por distinção explícita entre Monitor 32" 4K/Monitor 27" 144Hz (legítimos, 113 registros) e 4 produtos com erro 10x (5 registros candidatos a correção em Q2) | 2026-04-15 |
| RF-002 | /revisao-final | applied | DI-012 adicionado em memory-bank/data-issues.md: valor_unit, inconsistencia_cruzada, H, 6 produtos, 8 registros, razao_max_min=10.0 | 2026-04-15 |
| RF-003 | /revisao-final | applied | Parágrafo "Consistência interna de preço por produto (bloco 7c)" adicionado em ee3d6570 após o blockquote da tabela IQR de 8 linhas; descreve 6 produtos, 8 registros, distinção IQR vs. abaixo do limite | 2026-04-15 |
| RQ-Q3-001 | /revisar-questao Q3 --corrigir | applied | Parágrafo de `ed84982c` reescrito para remover as contagens `270` e `231` e a referência cruzada a Q2; leitura qualitativa mantida com base no output local de `8a098bbf` | 2026-04-16 |
| RQ-Q3-002 | /revisar-questao Q3 --corrigir | applied | Células `f692c88f` e `23a34e6d` receberam prints intermediários: Q3.c agora mostra `Receita top 2: R$ 24049.53 | Receita 3o ao 5o: R$ 19716.89` e Q3.d mostra `Razao topo/ultimo ticket: 3.67x | Participacao SP no volume: 28.3% | Razao SC/RS: 2.12x` | 2026-04-16 |
| RQ-Q3-003 | /revisar-questao Q3 --corrigir | applied | `CAST(... AS INTEGER)` aplicado em `sql/q3_a_top5_receita.sql` (`unidades_vendidas`) e `sql/q3_b_taxas_categoria.sql` (`nao_concluidos`); outputs reexecutados sem `.0` | 2026-04-16 |
| RQ-Q3-004 | /revisar-questao Q3 --auditar | applied | `f64d2ab1` recebeu sanity-check local que reconstrói a base após DI-009 e antes de DI-007, exibindo `delta total = 12` e comparativo por categoria (`Acessórios` 231→228, `Armazenamento` 219→215, `Câmeras` 121→120, `Impressoras` 171→169, `Monitores` 183→182, `Periféricos` 270→269) | 2026-04-16 |
| RQ-Q3-005 | /revisar-questao Q3 --corrigir | applied | Célula `202b9438` (Q3.d [MD explicação]): `15 pedidos sem UF` corrigido para `12`; `98,7%` corrigido para `98,6%`. Valores agora consistentes com output de célula `23a34e6d` e análise de célula `6e8b4428`. | 2026-04-16 |

## Errata — Reconciliação CODE vs MD (2026-04-15)

| id | source | status_final | resolucao | updated_at |
|---|---|---|---|---|
| ER-Q1-001 | /reconciliar-q1 | applied | `[MD análise]` de Q1 (`ee3d6570`) atualizado com matriz de rastreabilidade e listas obrigatórias (calculado e não comentado; relevante para negócio; inconsistências), removendo contagens sem evidência explícita no output | 2026-04-15 |
| ER-Q1-002 | /reconciliar-q1 | applied | DI-012 em `memory-bank/data-issues.md` ajustado para evidência estrita: mantidos `6` produtos com razão `10x`, `118` acima do limite IQR e `5` suspeitos acima do limite; sem afirmar total consolidado não visível no output | 2026-04-15 |
| RQ-Q2-001 | /revisar-questao Q2 --corrigir | applied | Adicionado `registros_formato_dmy = df['data_pedido'].str.match(r'^\d{2}/\d{2}/\d{4}$').sum()` e print do before-count antes do regex+parse em ae4bb233. DI-010 agora mostra antes (20) e depois (0 NaT) na própria célula. | 2026-04-15 |
| RQ-Q2-002 | /revisar-questao Q2 --corrigir | applied | Adicionado `print(f"DI-012 \| valor_unit range antes: R$...")` antes do loop de correção em ae4bb233. Before-range agora visível no output de Q2. | 2026-04-15 |

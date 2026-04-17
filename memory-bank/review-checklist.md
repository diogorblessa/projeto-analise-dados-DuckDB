# Review Checklist

Schema e estado do checklist de aceite. Atualizado por `/revisar-questao` e `/revisao-final`.

## Header
- `schema_version`: 1
- `notebook`: `notebooks/case_techshop.ipynb`
- `last_updated`: 2026-04-17
- `last_writer`: /revisar-questao Q5 --corrigir

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
| Q4 - estrutura [MD explicação] → [CODE] → [MD análise] | PASS | `a4831bc2` → `q4_sul_fase1` → `q4_sul_fase1_analise` | 3 células presentes com conteúdo completo | /revisar-questao Q4 --auditar | 2026-04-16 |
| Q4 - entregáveis mínimos (KPI 1-5: volume/receita/ticket, cancelamento, avaliação, mix categoria, tendência mensal) | PASS | `q4_sul_fase1`: KPI 1 agregado + desdobramento UF; KPI 2 taxa cancel+devol; KPI 3 avaliação; KPI 4 mix categoria; KPI 5 tendência mensal + gráfico | Todos os 5 KPIs exigidos pela reference.md presentes e com output | /revisar-questao Q4 --auditar | 2026-04-16 |
| Q4 - recomendação explícita (`prosseguir`/`prosseguir com ressalvas`/`não prosseguir`) com fundamentação numérica | PASS | `q4_sul_fase1_analise`: "Recomendação: `prosseguir com ressalvas`..." com H1-H4 testadas e números rastreáveis ao output de `q4_sul_fase1` | Todos os números cross-checados sem divergência; checklist sincronizado com a decisão vigente | /revisar-questao Q4 --auditar | 2026-04-16 |
| Q4 - limitações declaradas e decisions.md atualizado | PASS | `q4_sul_fase1_analise`: 6 limitações explícitas (incl. disclosure KPI 1/4 status); `memory-bank/decisions.md` Q4-002 como decisão aceita | RQ-Q4-002 aplicado e evidência sincronizada | /revisar-questao Q4 --auditar | 2026-04-16 |
| Q4 - afirmações rastreáveis a output visível (célula imediata) | PASS | H1-H3, interpretação de mix e volatilidade mensal: todos os valores batem com tabelas/prints de `q4_sul_fase1` | - | /revisar-questao Q4 --auditar | 2026-04-16 |
| Q4 - código PEP8, nomenclatura descritiva | PASS | `kpis_regiao`, `kpis_por_uf_sul`, `taxas_cancelamento_regiao`, `avaliacao_media_regiao`, `mix_categoria_sul_vs_resto`, `tendencia_mensal_sul_vs_resto` | RQ-Q4-001 aplicado: `SUL` constant morta removida | /revisar-questao Q4 --corrigir | 2026-04-16 |
| Q5 - Fase 1 alinhada ao workflow (`MD explicação -> CODE`) | PASS | `d24bda53 -> q5_debug_code` | RQ-Q5-002 aplicado: frase stale removida; célula 24 agora aponta para a próxima célula | /revisar-questao Q5 --corrigir | 2026-04-17 |
| Q5 - gráfico original histórico reproduzido e identificado | PASS | `q5_debug_code` output_2 | Duas figuras principais apenas; gráfico histórico com rótulos numéricos, legenda e rodapé compatíveis com o artefato | /revisar-questao Q5 --corrigir | 2026-04-16 |
| Q5 - gráfico corrigido padronizado com eixo `jan/2024 -> dez/2024` | PASS | `q5_debug_code` output_3 | Mesmo template visual-base do histórico; sem figura anual complementar | /revisar-questao Q5 --corrigir | 2026-04-16 |
| Q5 - comparação artefato histórico vs script versionado vs corrigido | PASS | `q5_debug_code` output_1 | Divergência entre imagem histórica e `scripts/analise_crescimento.py` explicitada em tabela comparativa | /revisar-questao Q5 --corrigir | 2026-04-16 |
| Q5 — Fase 2: [MD análise] com erros numerados, impacto e correção | PASS | célula 26 (`q5_debug_analise`) | "Correção recomendada" lista Erro 1, 2 e 3 (label YoY); impacto em "O que isso significa para o negócio"; recursos de correção explicitados | /revisar-questao Q5 --auditar | 2026-04-17 |
| Q5 — afirmações rastreáveis a output visível | PASS | célula 26 cruzada com outputs de célula 25 | R$ 175.599,53 / R$ 731.085,80 / 24,0% / 6 de 6 categorias / divergências pp: todas batem com output_1 de `q5_debug_code` | /revisar-questao Q5 --auditar | 2026-04-17 |
| Q5 — código PEP8, nomenclatura descritiva | PASS | `formatar_brl`, `calcular_variacao_mensal_ordenada`, `reproduzir_script_literal`, `df_bruto_original`, `df_valido`, `status_validos` | sem `n_*`/`mask_*`; constantes em UPPER_CASE; snake_case descritivo | /revisar-questao Q5 --auditar | 2026-04-17 |
| Q5-Q7 - implementadas | FAIL | Q6 e Q7 seguem placeholders (`f1961177`, `76f81a84`); Q5 Fase 1 e Fase 2 completas | Blocker remanescente apenas para Q6 e Q7; não invalida Q1-Q5 | /revisar-questao Q5 --auditar | 2026-04-17 |

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
| RQ-Q4-001 | /revisar-questao Q4 --corrigir | applied | `SUL = ("RS", "SC", "PR")` removido de `q4_sul_fase1`; variável definida mas nunca usada (todas as queries hardcodeiam os valores). | 2026-04-16 |
| RQ-Q4-002 | /revisar-questao Q4 --corrigir | applied | Bullet adicionado nas limitações de `q4_sul_fase1_analise`: KPI 1 e KPI 4 incluem pedidos de todos os status; comparações são internamente consistentes mas totais de `receita_total` não equivalem a receita realizada; KPI 5 usa apenas pedidos concluídos conforme declarado no [MD explicação]. | 2026-04-16 |
| RQ-Q4-003 | /revisar-questao Q4 --auditar | applied | Checklist Q4 sincronizado com a recomendação vigente `prosseguir com ressalvas` e com `Q4-002` como decisão aceita. | 2026-04-16 |
| RQ-Q4-004 | /revisar-questao Q4 --auditar | applied | Travessões longos removidos do bloco 5 da Q4 e das linhas novas desta rodada no memory-bank; números e achados preservados. | 2026-04-16 |
| RQ-Q5-001 | /revisar-questao Q5 --corrigir | applied | `q5_debug_code` refeito para reproduzir o artefato histórico, padronizar o gráfico corrigido, remover a figura anual e explicitar a divergência entre artefato histórico e script versionado; `scripts/inserir_bloco6.py` alinhado à Fase 1 sem `q5_debug_analise`. | 2026-04-16 |
| RQ-Q5-002 | /revisar-questao Q5 --corrigir | applied | Última linha de `d24bda53` substituída: "ficará para a Fase 2 do workflow" → "está na próxima célula"; célula 24 agora consistente com a presença de célula 26. | 2026-04-17 |

## Errata — Reconciliação CODE vs MD (2026-04-15)

| id | source | status_final | resolucao | updated_at |
|---|---|---|---|---|
| ER-Q1-001 | /reconciliar-q1 | applied | `[MD análise]` de Q1 (`ee3d6570`) atualizado com matriz de rastreabilidade e listas obrigatórias (calculado e não comentado; relevante para negócio; inconsistências), removendo contagens sem evidência explícita no output | 2026-04-15 |
| ER-Q1-002 | /reconciliar-q1 | applied | DI-012 em `memory-bank/data-issues.md` ajustado para evidência estrita: mantidos `6` produtos com razão `10x`, `118` acima do limite IQR e `5` suspeitos acima do limite; sem afirmar total consolidado não visível no output | 2026-04-15 |
| RQ-Q2-001 | /revisar-questao Q2 --corrigir | applied | Adicionado `registros_formato_dmy = df['data_pedido'].str.match(r'^\d{2}/\d{2}/\d{4}$').sum()` e print do before-count antes do regex+parse em ae4bb233. DI-010 agora mostra antes (20) e depois (0 NaT) na própria célula. | 2026-04-15 |
| RQ-Q2-002 | /revisar-questao Q2 --corrigir | applied | Adicionado `print(f"DI-012 \| valor_unit range antes: R$...")` antes do loop de correção em ae4bb233. Before-range agora visível no output de Q2. | 2026-04-15 |

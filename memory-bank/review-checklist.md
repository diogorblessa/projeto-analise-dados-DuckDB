# Review Checklist

Schema e estado do checklist de aceite. Atualizado por `/revisar-questao` e `/revisao-final`.

## Header
- `schema_version`: 1
- `notebook`: `notebooks/case_techshop.ipynb`
- `last_updated`: 2026-04-15
- `last_writer`: /revisar-questao Q1 --corrigir

## Open Findings
| id | source | escopo | severidade | tipo | celulas | evidencia | sugestao | fix_class | status |
|---|---|---|---|---|---|---|---|---|---|

## Final Checklist Cache
| requisito | status | evidencia | observacao | source | updated_at |
|---|---|---|---|---|---|
| Notebook executa Restart & Run All | - | - | Pendente re-execução após adição de bloco 7c e limite_inferior_valor em 7b | /revisao-final Q1 | 2026-04-15 |
| Q1 — estrutura [MD explicação] → [CODE] → [MD análise] | PASS | 5a904771 → f103d4c0 → ee3d6570 | - | /revisao-final Q1 | 2026-04-15 |
| Q1 — cobertura de tipos de problema (ausentes, duplicatas, inconsistências, outliers, formato) | PASS | Seções 2-3 (nulos/missing), 4 (duplicatas), 5/7a/7c (inconsistências), 7b/7c (outliers), 9 (formato) | - | /revisao-final Q1 | 2026-04-15 |
| Q1 — impacto downstream documentado por achado | PASS | Tabela de nulos com coluna de impacto; seção "O que isso significa para o negócio" | - | /revisao-final Q1 | 2026-04-15 |
| Q1 — afirmações rastreáveis a output visível | PASS | ee3d6570 corrigido: 4/6 outliers IQR identificados como erro 10x; bloco 7c referenciado na narrativa | RF-001 aplicado | /revisar-questao Q1 --corrigir | 2026-04-15 |
| Q1 — data-issues.md cataloga todos os achados (DI-001..DI-012) | PASS | DI-012 adicionado: dispersão 10x, 6 produtos, 8 registros, severidade H | RF-002 aplicado | /revisar-questao Q1 --corrigir | 2026-04-15 |
| Q1 — bloco 7c referenciado na narrativa | PASS | Parágrafo "Consistência interna de preço por produto (bloco 7c)" adicionado em ee3d6570 | RF-003 aplicado | /revisar-questao Q1 --corrigir | 2026-04-15 |
| Q1 — código PEP8, nomenclatura descritiva | PASS | dispersao_valor_unit, produtos_divergentes, avaliacao_por_status — conformes com code-style.md | - | /revisao-final Q1 | 2026-04-15 |
| Q2–Q7 — implementadas | FAIL | Não iniciadas (placeholders apenas) | Blocker global; não impede fechamento de Q1 isolado | /revisao-final Q1 | 2026-04-15 |

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

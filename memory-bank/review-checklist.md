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
| Notebook executa Restart & Run All | - | - | Pendente re-execução após adição de limite_inferior na seção 7b | /revisar-questao Q1 | 2026-04-14 |

## Applied/Closed
| id | source | status_final | resolucao | updated_at |
|---|---|---|---|---|
| RQ-Q1-001 | /revisar-questao | stale | Era linha de template do schema sem evidência real; nunca correspondeu a achado ativo | 2026-04-14 |
| RQ-Q1-002 | /revisar-questao | applied | Blockquote adicionado no [MD análise] (ee3d6570) explicando que a tabela IQR exibe 8 linhas porque Monitor 32" 4K e Monitor 27" 144Hz aparecem duas vezes por causa de DI-009 (categoria lowercase) | 2026-04-14 |
| RQ-Q1-003 | /diagnosticar | applied | Três adições em ee3d6570: (1) blockquote após avaliacao×status explicando as 6 linhas do output (vs 4 grupos na narrativa) e DI-008; (2) frase com baseline avaliacao mean=3,92/5, std=1,16, count=964; (3) frase com padrão qtd mediana=1, p75=2, max=5 | 2026-04-15 |
| RQ-Q1-004 | /revisar-questao | applied | Frase adicionada em ee3d6570 após missing disfarçado: desconto_% sem violações de domínio, máximo observado 20% sugere teto de política — referência para Q2 | 2026-04-15 |

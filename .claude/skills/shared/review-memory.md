# Memoria de Revisao Compartilhada

Use este arquivo quando a revisao precisar registrar, reaproveitar ou fechar achados ao longo de `/revisar-questao` ou `/revisao-final`.

## Arquivos
- `memory-bank/review-checklist.md`: checklist persistente de aceite e achados.
- `memory-bank/question-status.md`: status por questao.
- `memory-bank/data-issues.md`: catalogo de problemas de qualidade de Q1 e Q2.
- `memory-bank/decisions.md`: decisoes tecnicas com justificativa.
- `memory-bank/handoff.md`: continuidade da auditoria global quando relevante.
- `state/session-log.md`: log opcional e nao normativo da sessao.

## Principios
- Revalide todo achado no notebook atual antes de corrigir ou fechar.
- Nao duplique achado aberto; atualize o registro existente.
- Registre apenas achados acionaveis, com evidencia rastreavel.
- Diferencie correcoes `objetiva` e `manual`.
- Ao fechar, mova para `Applied/Closed` com status final.

## IDs de achados
- `/revisar-questao`: `RQ-{Q}-NNN` (`RQ-Q1-001`, `RQ-Q2-002`).
- `/revisao-final`: `RF-NNN`.
- `NNN` e sequencial global dentro de `memory-bank/review-checklist.md`: partir do maior existente + 1. Nunca reiniciar por sessao.

## Fluxo
- `/revisar-questao --auditar`: grava ou atualiza achados em `memory-bank/review-checklist.md` e `memory-bank/question-status.md`.
- `/revisar-questao --corrigir`: aplica somente `fix_class=objetiva` que continuem validas.
- `/revisao-final --auditar`: atualiza checklist global e grava achados criticos novos.
- `/revisao-final --corrigir`: aplica somente `fix_class=objetiva` que continuem validos.
- Itens que exigem decisao ficam como `blocked`; itens nao mais aplicaveis ficam como `stale`.

# Active Context

Ponto de entrada de cada sessão. Curto, sempre sincronizado com `question-status.md` e `handoff.md`.

> Autoridade: `docs/PRD.md` define escopo, padrões e aceite. `docs/instrucoes_desafio.md` é contexto histórico. `memory-bank/` registra toda a continuidade operacional persistente. Só um registro aceito em `decisions.md` com `override_of` e `aprovacao` explícitos pode ajustar o item correspondente do PRD. Status vivo fora de `memory-bank/` deve ser tratado como descritivo ou potencialmente desatualizado.

> _status: template pré-execução — aguardando primeira sessão de trabalho no notebook. Campos abaixo ainda não preenchidos por design._

## Foco atual
- _Q?: nome curto — em `not_started` / `in_progress` / `review` / `done`_
- _Data: yyyy-mm-dd_

## Skill ou fluxo ativo
- _ex.: `/diagnosticar --draft`, `/revisar-questao Q1`_

## Decisões aguardando validação
- _Liste itens de `decisions.md` com `status=proposed`, resumidos em 1 linha._

## Próximo marco
- _Próxima questão, revisão ou entrega prevista._

## Ponteiros
- Status por questão: [question-status.md](question-status.md)
- Decisões: [decisions.md](decisions.md)
- Qualidade dos dados: [data-issues.md](data-issues.md)
- Handoff: [handoff.md](handoff.md)
- Checklist de revisão: [review-checklist.md](review-checklist.md)

# Memory Bank Format

Formato mínimo das entradas persistentes em `memory-bank/`. Aplicada ao escrever ou atualizar arquivos sob `memory-bank/**`.

## Princípio
- `docs/PRD.md` define escopo, padrões e aceite.
- `memory-bank/` registra toda a continuidade operacional persistente: o que foi decidido, o que foi descoberto, onde o projeto parou e qual é o estado da revisão.
- Decisões comuns não redefinem o PRD. Override só existe quando um registro aceito declarar explicitamente `override_of` e `aprovacao`.
- `memory-bank/review-checklist.md` é o checklist persistente da revisão formal.
- `state/current-task.md` e `state/session-log.md` são scratch opcional; não são fonte de verdade.

## `decisions.md`
Cada decisão em linha de tabela com:
- `id`, `data` absoluta (`yyyy-mm-dd`) e `escopo`.
- `decisao`: o que foi escolhido, em uma frase.
- `motivo`: restrição, evidência ou trade-off que levou à escolha.
- `impacto`: onde a decisão aparece.
- `fonte`: célula, query, conversa ou artefato que sustenta a decisão.
- `status`: `proposed`, `accepted`, `rejected` ou `superseded`.
- `override_of`: `-` para decisão comum; preencher com o item do PRD quando houver override explícito.
- `aprovacao`: `-` para decisão comum; preencher com aprovador ou fonte de aprovação quando `override_of` estiver preenchido.

Regra de autoridade:
- Só um registro com `status=accepted`, `override_of` preenchido e `aprovacao` explícita ajusta o item referenciado do PRD.
- Override com `aprovacao = -` é inválido mesmo que `override_of` esteja preenchido.
- Fora disso, `decisions.md` documenta interpretação, contexto ou continuidade operacional.

## `data-issues.md`
Cada problema em linha de tabela com:
- `id`, `questao`, `coluna`, `tipo` e `severidade`.
- `descricao`: o problema em linguagem curta e auditável.
- `evidencia`: célula do notebook, contagem ou artefato reproduzível.
- `tratamento`: ação escolhida, pendência ou justificativa para manter.
- `status`: `open`, `in_progress`, `applied` ou `wont_fix`.

## `question-status.md`
Uma linha por questão `Q1..Q7` com:
- `questao`, `status`, `last_updated`, `nota`.
- `status`: `not_started`, `in_progress`, `review`, `done`.

Não registrar `README` aqui; status de artefatos auxiliares fica em `handoff.md` ou `active-context.md` quando relevante.

## `active-context.md`
Ponto de entrada curto, no máximo meia tela. Deve conter:
- foco atual;
- skill ou fluxo ativo;
- decisões aguardando validação, usando itens `proposed` de `decisions.md`;
- próximo marco;
- ponteiros para os arquivos realmente úteis da continuidade.

## `handoff.md`
Atualizado ao encerrar sessão:
- o que foi concluído;
- o que ficou pendente;
- blockers abertos;
- próximo passo concreto;
- referência cruzada com `active-context.md` e `question-status.md`.

## `review-checklist.md`
Checklist persistente da revisão formal:
- `Open Findings`: achados abertos, acionáveis e rastreáveis.
- `Final Checklist Cache`: cache do PASS/FAIL global contra o aceite do PRD.
- `Applied/Closed`: histórico de itens resolvidos, bloqueados ou tornados obsoletos.

## Regras de atualização
- Data sempre absoluta (`yyyy-mm-dd`), nunca relativa.
- Não apagar histórico; marcar status final (`applied`, `wont_fix`, `superseded`, etc.).
- Se houver override explícito do PRD, o registro deve citar exatamente o item ajustado e a aprovação correspondente.

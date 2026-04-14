Atalho para abrir uma sessão de trabalho. Execute, em sequência, o equivalente a `/contexto` e depois `/status`, e imprima tudo em um único painel.

1. Leia `memory-bank/active-context.md` e `memory-bank/handoff.md` para a parte de contexto.

2. Leia `memory-bank/question-status.md` para a parte de status.

3. Mostre em uma tela, sem texto extra, nesta ordem:

## Contexto

**Foco atual** — questão ou skill em andamento (de `active-context.md`)

**Pendências** — de `handoff.md`; se não houver, escreva "nenhuma"

**Bloqueios** — de `handoff.md`; se não houver, escreva "nenhum"

**Próxima ação** — de `handoff.md`

**Decisões aguardando validação** — de `active-context.md`, se houver

## Status das questões

Uma linha por questão no formato:
`Q{N} [{status}] {last_updated} — {nota}`

Use ícones: `✓` done · `→` in_progress · `○` not_started · `⚑` review

Ao final, linha de resumo: `{N} concluídas · {N} em progresso · {N} não iniciadas`

E uma linha de foco: `Foco: {questão ou skill ativo}`

Não invente informações ausentes. Se um arquivo não existir ou estiver vazio, diga explicitamente.

# Case TechShop - E-commerce Analytics

## Projeto
- Entrega: `notebooks/case_techshop.ipynb` + `README.md`.
- Dataset imutável: `data/raw/ecommerce_vendas.csv`.
- Script auxiliar de Q5: `scripts/analise_crescimento.py`.
- Fonte normativa de requisitos: `docs/PRD.md`.
- Enunciado original do case: `docs/instrucoes_desafio.md`.

## Prioridade de instruções
1. Pedido atual do usuário.
2. Skill invocado em `.claude/skills/`.
3. Regras em `.claude/rules/` (persistentes ou escopadas por caminho).
4. `docs/PRD.md`.
5. Agentes, comandos e templates locais como apoio dentro do envelope acima.

## Hierarquia de autoridade
- `docs/PRD.md`: única fonte normativa de escopo, padrões e critérios de aceite.
- `docs/instrucoes_desafio.md`: contexto histórico do case; use para background quando não conflitar com o PRD.
- `memory-bank/`: única fonte de verdade operacional persistente para continuidade, decisões, review state e handoff entre sessões.
- `memory-bank/decisions.md` não redefine o PRD por padrão. Só há override válido quando um registro aceito declarar explicitamente `override_of` e `aprovacao`.
- `memory-bank/review-checklist.md`: checklist persistente da revisão formal.
- Notebook `case_techshop.ipynb`: evidência final de outputs, análises e artefatos avaliáveis.
- `README.md`: documento descritivo do projeto; não carrega status vivo de execução.
- `state/current-task.md` e `state/session-log.md`: scratch opcional da sessão; não são fonte de verdade.

## Contexto modular
- `@code-reviewer`: apoio ad hoc para notebook `[CODE]` e `sql/q3_*.sql`, priorizando achados acionaveis, contexto tecnico curto e sugestoes seguras; nao substitui `/revisar-questao` nem `/revisao-final`.
- `docs/playbook_subagentes.md`: contrato operacional para decidir quando invocar `@code-reviewer` e `@business-reporter`, com escopo por bloco e templates de prompt.
- `.claude/rules/project-globals.md`: regras globais do repo, incluindo premissas, simplicidade, escopo cirúrgico e verificação.
- `.claude/rules/notebook-base.md`: estrutura do notebook e roteamento por skill.
- `.claude/rules/analysis-writing.md`, `visualization.md`, `sql-conventions.md` e `code-style.md`: regras escopadas por caminho.
- `.claude/rules/memory-bank-format.md`: schema e política de atualização de `memory-bank/**`.
- `.claude/skills/*/SKILL.md`: workflows canônicos de execução por questão ou revisão.
- `.claude/skills/*/reference.md`: critérios detalhados carregados sob demanda.
- `.claude/skills/shared/review-memory.md`: suporte compartilhado aos fluxos de revisão.
- `.claude/agents/`: agentes de apoio especializados em saída ou revisão ad hoc; não substituem skills. Invocáveis via `@business-reporter` e `@code-reviewer`.
- `.claude/commands/`: slash-commands de leitura rápida. Invocáveis via `/contexto` e `/status`.
- `.claude/settings.json`: hooks e permissions versionados do projeto.
- `.claude/settings.local.json`: preferências locais não versionadas.
- `docs/case-notes.md`: scratch contextual; não é fonte de verdade.

## Política de carregamento
- Não carregue notebook, PRD ou memory-bank inteiros por padrão.
- Localize a questão alvo e carregue só dependências imediatas.
- Ao iniciar uma sessão, leia `memory-bank/active-context.md` e `memory-bank/question-status.md`.
- Consulte `memory-bank/decisions.md`, `data-issues.md`, `handoff.md` ou `review-checklist.md` apenas quando forem relevantes para a tarefa atual.
- Use `README.md` como visão descritiva do projeto, nunca como fonte de status vivo.
- Se `README.md`, `state/` ou notas locais divergirem de `memory-bank/`, prevalece `memory-bank/`.
- Use `rules` para contexto persistente ou escopado por caminho.
- Use `skills` para workflows manuais e instruções task-specific.
- Agentes não devem forçar leitura ampla de `memory-bank/` se a tarefa puder ser resolvida com evidência local.
- Só amplie contexto com evidência de dependência quebrada.

## Estado e memória
- Núcleo persistente: `memory-bank/active-context.md`, `decisions.md`, `data-issues.md`, `question-status.md`, `handoff.md` e `review-checklist.md`.
- `state/current-task.md` e `state/session-log.md` podem ser usados como scratch, mas são opcionais.
- `state/` é scratch efêmero de sessão e nunca prevalece sobre `memory-bank/` em caso de divergência.
- Achados abertos, cache de aceite e histórico de revisão ficam em `memory-bank/review-checklist.md`.
- Qualquer status vivo fora de `memory-bank/` deve ser tratado como ruído até sincronização explícita.
- Ao iniciar: leia `memory-bank/active-context.md` e `memory-bank/question-status.md`; registre a questão atual como `in_progress` em `question-status.md` antes de iniciar qualquer skill.
- Ao encerrar: sincronize `memory-bank/question-status.md`, `memory-bank/handoff.md` e `memory-bank/active-context.md`.

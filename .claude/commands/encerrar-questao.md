Encerra a questão `$ARGUMENTS`. Formato esperado: `QN review` ou `QN done` (dois argumentos: a questão e o estado final).

Execute, nesta ordem:

1. Valide os argumentos:
   - `QN` deve estar em `Q1..Q7`;
   - o estado final deve ser `review` ou `done`.
   Se inválido, pare e informe o formato esperado.

2. Atualize `memory-bank/question-status.md`:
   - marque a questão alvo com o estado recebido;
   - preencha `last_updated` com a data de hoje em `yyyy-mm-dd`;
   - se for `done`, preencha `nota` com `concluida`; se for `review`, mantenha ou ajuste a `nota` para refletir o motivo da revisão em andamento.
   - não toque em outras questões.

3. Atualize `memory-bank/handoff.md` acrescentando um bloco de encerramento com:
   - **Concluído**: o que foi entregue nesta sessão para a questão alvo.
   - **Pendente**: o que ainda não fechou, se `review`; se `done`, escreva `nenhum`.
   - **Bloqueios**: se houver; se não, escreva `nenhum`.
   - **Próximo passo**: a próxima questão lógica do fluxo Q1..Q7, ou, se a questão encerrada já for Q7, sugira `/revisao-final --auditar`.

4. Atualize `memory-bank/active-context.md`:
   - ajuste o foco atual para a próxima questão lógica (ou para revisão global, se for o caso).

5. Mostre em uma tela, sem texto extra:

**Questão encerrada** — `QN` como `{review|done}`
**Sincronizado** — `question-status.md`, `handoff.md`, `active-context.md`
**Próximo foco** — `{próxima questão ou revisão}`
**Sugestão de git add** — liste os caminhos prováveis: `memory-bank/`, e, conforme a questão: `notebooks/case_techshop.ipynb`, `sql/` (apenas Q3), `data/interim/` (apenas Q2), `artifacts/diagrams/` (apenas Q6).

Não execute `git add`, `git commit` nem `git push`. Apenas sugira.

Não invente informações ausentes. Se um arquivo não existir, diga qual está faltando.

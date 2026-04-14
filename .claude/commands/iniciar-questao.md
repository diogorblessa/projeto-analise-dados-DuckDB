Inicia a questão `$ARGUMENTS` (formato esperado: `Q1`..`Q7`).

Execute, nesta ordem:

1. Valide o argumento. Se não estiver no conjunto `Q1..Q7`, pare e informe o formato esperado.

2. Atualize `memory-bank/question-status.md`:
   - marque a linha da questão alvo como `in_progress`;
   - preencha `last_updated` com a data de hoje em `yyyy-mm-dd`;
   - se `nota` estiver vazia, preencha com `iniciando`.
   - não toque em outras questões.

3. Atualize `memory-bank/active-context.md`:
   - ajuste o campo de foco atual para a questão alvo e o skill dono correspondente.

4. Identifique o skill dono pela tabela:
   - Q1 -> `/diagnosticar`
   - Q2 -> `/tratar`
   - Q3 -> `/consultar-sql`
   - Q4 -> `/analisar-negocio`
   - Q5 -> `/encontrar-erro`
   - Q6 -> `/modelar-dimensional`
   - Q7 -> `/insight-livre`

5. Mostre em uma tela, sem texto extra:

**Questão** — `QN`
**Skill dono** — `/<nome>`
**Status anterior** — `{status antes da atualização}`
**Status atual** — `in_progress`
**Próximo passo** — sugira invocar o skill dono com o prompt padrão do bloco correspondente.

Não invente informações ausentes. Se um arquivo não existir, diga qual está faltando.

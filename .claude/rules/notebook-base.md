---
paths:
  - "notebooks/**/*.ipynb"
---

# Notebook Base

Use esta regra para qualquer tarefa que edite, gere, analise ou revise `notebooks/case_techshop.ipynb`.

## Fonte de verdade
- `docs/PRD.md` define os requisitos das 7 questões.
- Para workflow por questão ou revisão, use o skill correspondente em `.claude/skills/`.
- Agentes de apoio podem revisar ou sintetizar saídas, mas não substituem o skill dono do workflow.
- Carregue apenas a seção da questão alvo e a referência do skill em uso.

## Estrutura e numeração
- Cada bloco usa `# Bloco N: Nome`.
- Cada questão usa `## QN - Nome da Questão`.
- Subseções usam `### QN.S Nome`.
- Preserve a ordem narrativa existente.
- Padrão de células: `[MD explicacao] -> [CODE] -> [MD analise]`.
- Exceção: Q6 e markdown-only com diagrama.

## Workflows por skill
- Q1 -> `/diagnosticar`
- Q2 -> `/tratar`
- Q3 -> `/consultar-sql`
- Q4 -> `/analisar-negocio`
- Q5 -> `/encontrar-erro`
- Q6 -> `/modelar-dimensional`
- Q7 -> `/insight-livre`
- Revisão parcial -> `/revisar-questao`
- Revisão global -> `/revisao-final`

## Rules transversais
- `.claude/rules/analysis-writing.md`: células `[MD analise]`.
- `.claude/rules/visualization.md`: gráficos.
- `.claude/rules/sql-conventions.md`: queries DuckDB.

## Continuidade e limites
- Preserve células fora do escopo.
- Só altere outra questão com dependência quebrada comprovada.
- Reutilize evidências anteriores por referência, sem duplicar análise.

## Política de carregamento
Ver definição canônica em `CLAUDE.md` (seção "Política de carregamento").

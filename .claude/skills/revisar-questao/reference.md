# Revisão por Questão

## Carregamento recomendado
- `notebooks/case_techshop.ipynb`
- `memory-bank/review-checklist.md`
- `memory-bank/question-status.md`
- Referências das questões em escopo

## Mapa Q -> referência
- Q1 -> [../diagnosticar/reference.md](../diagnosticar/reference.md)
- Q2 -> [../tratar/reference.md](../tratar/reference.md)
- Q3 -> [../consultar-sql/reference.md](../consultar-sql/reference.md)
- Q4 -> [../analisar-negocio/reference.md](../analisar-negocio/reference.md)
- Q5 -> [../encontrar-erro/reference.md](../encontrar-erro/reference.md)
- Q6 -> [../modelar-dimensional/reference.md](../modelar-dimensional/reference.md)
- Q7 -> [../insight-livre/reference.md](../insight-livre/reference.md)

## Escopo
- Validar cobertura, rastreabilidade e suficiência da questão alvo.
- Em `--auditar`, registrar achados em `memory-bank/review-checklist.md` com IDs `RQ-{Q}-NNN`, sem editar notebook.
- Em `--corrigir`, aplicar somente correções `objetiva` que continuem válidas; deixar `manual` como `blocked`.
- Atualizar `memory-bank/question-status.md`.

## Restrições
- Escopos inválidos interrompem a tarefa.
- Não criar nova análise; apenas auditar ou ajustar o existente.

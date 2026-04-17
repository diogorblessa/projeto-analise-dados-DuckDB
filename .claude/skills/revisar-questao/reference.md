# Revisão por Questão

## Carregamento recomendado
- `notebooks/case_techshop.ipynb`
- `memory-bank/review-checklist.md`
- `memory-bank/question-status.md`
- `README.md`, quando a revisão incluir narrativa de entrega ou linguagem de documentação
- `.md` em `docs/`, apenas quando esses arquivos estiverem explicitamente em escopo
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
- Ao revisar código, consultar `.claude/rules/code-style.md` para encoding, `PEP 8` pragmático e nomenclatura.
- Ao revisar `README.md` ou `.md` narrativo em `docs/`, consultar `.claude/rules/analysis-writing.md` para clareza, jargão e explicação de termos técnicos inevitáveis.
- Quando `README.md` ou `.md` em `docs/` estiver em escopo, validar se o texto está compreensível para leitor não técnico, com linguagem direta e sem operacionalismo desnecessário.
- Não promover `.md` operacional ou interno em `docs/` a critério automático de aceite; revise esses arquivos apenas quando o usuário os colocar em escopo.
- Em `--auditar`, registrar achados em `memory-bank/review-checklist.md` com IDs `RQ-{Q}-NNN`, sem editar notebook.
- Em `--corrigir`, aplicar somente correções `objetiva` que continuem válidas; deixar `manual` como `blocked`.
- Atualizar `memory-bank/question-status.md`.
- Na resposta final, sempre incluir uma seção `Checklist PASS/FAIL` com tabela Markdown compacta `requisito | status`, usando `memory-bank/review-checklist.md` como fonte de verdade.
- Em `/revisar-questao QN` ou `/revisar-questao QN,QM`, filtrar o `Final Checklist Cache` por prefixo de requisito (`Q1 —`, `Q2 —`, etc.) para manter apenas linhas das questões em escopo.
- Preservar a ordem já existente no `Final Checklist Cache` e excluir itens globais fora do escopo atual.
- Se não houver linhas compatíveis com o escopo, escrever explicitamente que não há critérios cacheados para a revisão atual.
- Manter resumo, achados abertos e observações existentes; a tabela complementa a resposta, não substitui o restante da auditoria.

## Restrições
- Escopos inválidos interrompem a tarefa.
- Não criar nova análise; apenas auditar ou ajustar o existente.

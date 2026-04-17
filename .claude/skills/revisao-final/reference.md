# Revisão Final Global

## Carregamento recomendado
- Seção 5, critérios de aceite, de `docs/PRD.md`
- `notebooks/case_techshop.ipynb`
- `README.md`
- `memory-bank/review-checklist.md`
- `memory-bank/question-status.md`
- `memory-bank/handoff.md`
- `.md` em `docs/`, apenas se o pedido ampliar o escopo da revisão final

## Escopo
- Aplicar checklist global PASS/FAIL contra os critérios de aceite do PRD.
- Cada item com evidência explícita, por questão, seção ou célula.
- Ao revisar código, consultar `.claude/rules/code-style.md` para encoding, `PEP 8` pragmático e nomenclatura.
- Validar `README.md` não apenas por cobertura, mas também por clareza para leitor não técnico, com jargão técnico reduzido e termos inevitáveis explicados em uma frase curta.
- Revisar `.md` em `docs/` somente quando esses arquivos fizerem parte do pedido; não tratar documentação operacional interna como critério global de aceite por padrão.
- Em `--corrigir`, aplicar somente itens `open` com `fix_class=objetiva` que continuem válidos.
- Em `--corrigir`, marcar `stale` o que já não se aplica e `blocked` o que exigir decisão.
- Na resposta final, sempre incluir uma seção `Checklist PASS/FAIL` com tabela Markdown compacta `requisito | status`.
- Em `/revisao-final`, a tabela deve espelhar todo o `Final Checklist Cache`, na ordem persistida em `memory-bank/review-checklist.md`.
- Manter resumo, achados e observações existentes; a tabela é um resumo de saída, não substitui a evidência persistida.

## Mapa de referências por questão
- Q1 -> [../diagnosticar/reference.md](../diagnosticar/reference.md)
- Q2 -> [../tratar/reference.md](../tratar/reference.md)
- Q3 -> [../consultar-sql/reference.md](../consultar-sql/reference.md)
- Q4 -> [../analisar-negocio/reference.md](../analisar-negocio/reference.md)
- Q5 -> [../encontrar-erro/reference.md](../encontrar-erro/reference.md)
- Q6 -> [../modelar-dimensional/reference.md](../modelar-dimensional/reference.md)
- Q7 -> [../insight-livre/reference.md](../insight-livre/reference.md)

## Restrições
- Não criar análise nova.
- Revalidar todo achado no notebook atual antes de corrigir ou fechar.

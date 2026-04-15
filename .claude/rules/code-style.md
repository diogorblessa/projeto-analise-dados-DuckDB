---
paths:
  - "notebooks/**/*.ipynb"
  - "scripts/**/*.py"
  - "sql/**/*.sql"
  - "README.md"
  - "docs/**/*.md"
---

# Code Style

Use esta regra ao escrever, editar ou revisar código, notebooks e documentos do projeto.

## Encoding
- Preserve arquivos textuais e notebooks em `UTF-8`.
- Ao ler ou escrever texto em Python, use `encoding="utf-8"` quando a API permitir.
- Trate mojibake como problema de revisão. Exemplos típicos são sequências com os codepoints `U+00C3`, `U+00C2` ou o caractere de substituição `U+FFFD`.

## Python e notebooks
- Use `PEP 8` como referência pragmática, sem reformatar o notebook inteiro apenas por estilo.
- Use `snake_case`, indentação de 4 espaços e imports centralizados no topo do bloco/script.
- Aplique estas regras em células novas, células alteradas e scripts editados.
- Não renomeie variáveis existentes em massa sem necessidade funcional ou achado de revisão.

## Nomenclatura
- O nome deve explicar o papel do objeto no fluxo analítico.
- Prefira nomes como `pedidos_entregues`, `receita_liquida`, `limite_superior_valor` e `avaliacao_por_status`.
- Evite abreviações opacas como `tmp`, `aux`, `x`, `res` e `calc`, salvo em contexto trivial e curto.
- Abreviações consolidadas ou herdadas do domínio continuam permitidas: `df`, `sql`, `uf`, `id`, `qtd`, `pct`, `q1`, `q3` e `iqr`.
- Quando uma abreviação nova for inevitável, defina o sentido no nome, em comentário curto ou no markdown próximo.

## Revisão
- Classifique achados locais e seguros como `objetiva`.
- Classifique renomeações amplas, refatorações de células ou ajustes que exijam reexecução analítica como `manual`.
- Qualquer correção posterior no notebook deve preservar execução completa via `Restart & Run All`.

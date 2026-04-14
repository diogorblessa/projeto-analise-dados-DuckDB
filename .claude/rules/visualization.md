---
paths:
  - "notebooks/**/*.ipynb"
---

# Visualization

Use em células de código ou revisão que envolvam gráficos.

## Convencoes de código
- `fig` para a figura, `eixos` para colecao de eixos.
- `for i, coluna` em iteracoes por colunas quando fizer sentido.
- `eixos[i]` para acessar eixos.
- `eixo_x`, `eixo_y` para limites ou referencias.
- `barra` para elementos de barras.

## Convencoes visuais
- Titulos curtos e descritivos, nunca interpretativos.
- A interpretação vive na célula `[MD analise]`, não no título.
- Inclua unidade nos rótulos quando aplicável.
- Em gráficos categoricos do seaborn, use `order=` explícito quando a ordem importar.
- `sns.despine()` ao final de cada gráfico.
- Prefira barras horizontais quando rótulos forem longos no eixo x.
- Evite sobreposicao de anotacoes.

## Exportacao
- Figuras exportadas vao em `artifacts/figures/` com nome descritivo.
- Só exporte quando a figura for referenciada no README ou for entregável.

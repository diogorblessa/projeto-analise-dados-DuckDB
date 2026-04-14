# PRD — Case TechShop

## 1. Resumo
Análise exploratória, tratamento, consultas SQL e modelagem dimensional sobre o histórico de vendas 2024 da TechShop (e-commerce de eletrônicos). O analista entrega um notebook Jupyter e um README respondendo 7 questões técnicas e de negócio, com raciocínio explícito e decisões justificadas.

## 2. Contexto
A TechShop cresceu de 3 para 13 estados atendidos em 2 anos, com catálogo triplicado. Os dados vêm de dois sistemas diferentes com migração parcial feita por fornecedor externo, então inconsistências são esperadas. A diretoria quer expandir para o Sul e dobrar investimento em categorias de "alto desempenho", mas ninguém sabe quais são. O analista é o primeiro contratado para a área de dados e começa entendendo o que existe, validando confiabilidade e extraindo as primeiras respostas.

## 3. Objetivos (Q1..Q7 em linguagem de negócio)
- **Q1 — Confiar ou não nos dados:** mapear problemas de qualidade que podem comprometer qualquer decisão baseada no dataset.
- **Q2 — Limpar o que dá para limpar:** tornar o dataset confiável, documentando cada decisão de tratamento para auditoria futura.
- **Q3 — Responder perguntas recorrentes do comercial:** produtos campeões de receita, categorias com mais cancelamentos, clientes fiéis e ticket por estado.
- **Q4 — Apoiar a decisão de expansão para o Sul:** avaliar se uma campanha de desconto para RS, SC e PR faz sentido com os dados atuais.
- **Q5 — Validar relatórios herdados:** revisar o script de crescimento por categoria que gerou decisões estratégicas anteriores.
- **Q6 — Preparar o terreno para o data warehouse:** propor modelo dimensional que sustente análises futuras.
- **Q7 — Descobrir algo que ninguém pediu:** encontrar um insight adicional relevante para o negócio.

## 4. Entregáveis
- `notebooks/case_techshop.ipynb`: notebook executável do início ao fim, com as 7 questões respondidas, evidências visíveis e análises interpretativas.
- `README.md`: visão geral, principais descobertas, como executar e estrutura do repositório.
- `sql/*.sql`: queries Q3 isoladas e reproduzíveis fora do notebook.
- `artifacts/diagrams/`: diagrama dimensional de Q6, se exportado como imagem.
- `artifacts/figures/`: figuras exportadas relevantes para o README.

## 5. Critérios de aceite
- Notebook executa do início ao fim sem erro (`Restart & Run All`) sobre `data/raw/ecommerce_vendas.csv` original.
- Cada questão segue `[MD explicação] -> [CODE] -> [MD análise]`, exceto Q6.
- Cada afirmação analítica é rastreável a output visível na célula imediatamente anterior.
- Q2 apresenta antes e depois de cada tratamento com justificativa explícita.
- Q3 executa via DuckDB in-memory, com SQL também presente em `sql/`.
- Q4 entrega recomendação fundamentada com limitações declaradas.
- Q5 identifica pelo menos `2` erros graves com correção mostrada.
- Q6 apresenta diagrama legível (texto, Mermaid ou imagem) com granularidade da fato declarada.
- README cobre projeto, descobertas, execução e estrutura.
- Código sem redundância, imports centralizados, nomes descritivos.

## 6. Fora de escopo
- Modelagem preditiva (classificação, regressão, clustering).
- Dashboards, BI tools ou frontends.
- Implementação física do data warehouse proposto em Q6; apenas o desenho.
- Integração com APIs ou bancos de dados externos.
- Testes automatizados ou CI/CD.
- Tratamento de dados fora do arquivo `ecommerce_vendas.csv`.

## 7. Padrões
- **Banco SQL:** exclusivamente DuckDB in-memory. SQLite ou banco externo estão proibidos.
- **Idioma:** português brasileiro para todo conteúdo analítico e markdown; inglês apenas em nomes de arquivos, variáveis e palavras-chave técnicas consolidadas.
- **Artefato principal:** `notebooks/case_techshop.ipynb` é a única entrega técnica avaliável. Scripts `.py` e `.sql` são insumos reproduzíveis.
- **Dataset imutável:** `data/raw/ecommerce_vendas.csv` nunca é sobrescrito. Saídas tratadas vão para `data/interim/`.
- **Célula:** padrão `[MD explicação] -> [CODE] -> [MD análise]`, exceto Q6.
- **Formatação markdown:** números, percentuais e valores monetários entre crases.
- **Nível analítico:** analista pleno; decisões fundamentadas, trade-offs declarados, limitações explícitas.

## Dataset (referência rápida)
- Colunas: `pedido_id`, `data_pedido`, `cliente_id`, `uf`, `produto`, `categoria`, `qtd`, `valor_unit`, `desconto_%`, `status`, `avaliacao`.
- Período: `2024`. Histórico do sistema legado com migração parcial.

## Estrutura do notebook
| Bloco | Conteúdo | Tipo |
|---|---|---|
| 1 | Capa, imports e carga | Setup |
| 2 | Q1: Diagnóstico | EDA |
| 3 | Q2: Tratamento | Cleaning |
| 4 | Q3: SQL | Queries |
| 5 | Q4: Negócio | Analysis |
| 6 | Q5: Debug | Review |
| 7 | Q6: Modelagem | Design (MD-only) |
| 8 | Q7: Insight | Discovery |

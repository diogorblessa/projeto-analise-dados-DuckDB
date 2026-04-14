# PRD — Case TechShop

## 1. Resumo
Análise exploratória, tratamento, consultas SQL e modelagem dimensional sobre o histórico de vendas 2024 da TechShop (e-commerce de eletrônicos). O analista entrega um notebook Jupyter e um README respondendo 7 questões técnicas e de negócio, com raciocínio explícito e decisões justificadas.

## 2. Contexto
A TechShop cresceu de 3 para 13 estados atendidos em 2 anos, com catálogo triplicado. Os dados vêm de dois sistemas diferentes com migração parcial feita por fornecedor externo, então inconsistências são esperadas. A diretoria quer expandir para o Sul e dobrar investimento em categorias de "alto desempenho", mas ninguém sabe quais são. O analista é o primeiro contratado para a área de dados e começa entendendo o que existe, validando confiabilidade e extraindo as primeiras respostas.

## 3. Questões
### Questão 1. Diagnóstico inicial (Q1)
Faça uma análise exploratória inicial do dataset. Identifique e documente todos os problemas de
qualidade  encontrados: valores ausentes, inconsistências, duplicatas, outliers  e anomalias de
formato. Para cada problema, explique brevemente qual seria o impacto de ignorá-lo em uma
análise downstream.

### Questão 2. Tratamento e justificativa (Q2)
Trate os problemas encontrados. Para cada decisão tomada (imputar, remover, corrigir, manter),
explique o raciocínio. Não existe resposta única correta — o que se avalia é a consistência e a
justificativa das escolhas.

### Questão 3. Consultas SQL (Q3)
Escreva queries SQL para responder:
a) Quais são os 5 produtos com maior receita líquida (após desconto) nos últimos 90 dias do
dataset?
b) Qual é a taxa de cancelamento e devolução por categoria? Ordene da maior para a menor.
c) Identifique clientes que compraram em meses consecutivos por pelo menos 3 meses
seguidos (use window functions).
d) Compare o ticket médio por UF, filtrando apenas pedidos com status "entregue".

### Questão 4. Análise de negócio aberta (Q4)
O time comercial quer decidir se vale a pena criar uma campanha de descontos específica para a
região Sul (RS, SC, PR). Com base nos dados disponíveis, que análise você conduziria? Quais
métricas usaria, quais hipóteses levantaria e quais limitações o dataset impõe para essa decisão?
Apresente os resultados de forma que um gerente não-técnico consiga entender.

### Questão 5. Encontre o erro (Q5)
O gráfico abaixo foi apresentado numa reunião com a diretoria e gerou decisões estratégicas. Ele
mostra "Receita total por categoria — crescimento YoY". Há pelo menos dois problemas graves
na análise. Identifique-os, explique o impacto e proponha como corrigir.
Obs.: o código gerador desse gráfico está no arquivo `scripts/analise_crescimento.py`

![Gráfico de Receita Total por Categoria](<../artifacts/figures/imagem_grafico_receita_tota_ por_categoria_crescimento_YoY.jpg>)


### Questão 6. Modelagem (Q6)
A tabela ecommerce_vendas.csv representa o estado atual dos dados — tudo numa estrutura flat,
como saiu do sistema legado. O time de engenharia vai construir um data warehouse e precisa
da  sua  orientação  para  modelar  esses  dados  dimensionalmente. Proponha  um  modelo
dimensional (estrela ou floco de neve) para essa tabela: quais tabelas você criaria? Por que essa
escolha de modelagem?

Obs. 1: Não necessita de implementação em código, faça apenas um diagrama em texto ou
desenho livre, justificando suas escolhas.

Obs. 2: Para essa questão de modelagem, você pode apresentar o diagrama diretamente no
notebook em formato texto, usando uma célula Markdown. Caso prefira usar uma ferramenta de
diagrama como draw.io ou dbdiagram.io, exporte como imagem e insira no notebook com
`![modelo](nome_do_arquivo.png)` ou inclua o link do diagrama publicado.

### Questão 7. Pergunta livre (Q7)
Qual insight que você encontrou no dataset que não foi pedido em nenhuma das questões
anteriores?  Apresente  a  descoberta,  o  método  usado  para  encontrá-la  e  por  que  ela  seria
relevante para o negócio.

## 4. Objetivos (Q1..Q7 em linguagem de negócio)
- **Q1 — Confiar ou não nos dados:** mapear problemas de qualidade que podem comprometer qualquer decisão baseada no dataset.
- **Q2 — Limpar o que dá para limpar:** tornar o dataset confiável, documentando cada decisão de tratamento para auditoria futura.
- **Q3 — Responder perguntas recorrentes do comercial:** produtos campeões de receita, categorias com mais cancelamentos, clientes fiéis e ticket por estado.
- **Q4 — Apoiar a decisão de expansão para o Sul:** avaliar se uma campanha de desconto para RS, SC e PR faz sentido com os dados atuais.
- **Q5 — Validar relatórios herdados:** revisar o script de crescimento por categoria que gerou decisões estratégicas anteriores.
- **Q6 — Preparar o terreno para o data warehouse:** propor modelo dimensional que sustente análises futuras.
- **Q7 — Descobrir algo que ninguém pediu:** encontrar um insight adicional relevante para o negócio.

## 5. Entregáveis
- `notebooks/case_techshop.ipynb`: notebook executável do início ao fim, com as 7 questões respondidas, evidências visíveis e análises interpretativas.
- `README.md`: visão geral, principais descobertas, como executar e estrutura do repositório.
- `sql/*.sql`: queries Q3 isoladas e reproduzíveis fora do notebook.
- `artifacts/diagrams/`: diagrama dimensional de Q6, se exportado como imagem.
- `artifacts/figures/`: figuras exportadas relevantes para o README.

## 6. Critérios de aceite
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

## 7. Fora de escopo
- Modelagem preditiva (classificação, regressão, clustering).
- Dashboards, BI tools ou frontends.
- Implementação física do data warehouse proposto em Q6; apenas o desenho.
- Integração com APIs ou bancos de dados externos.
- Testes automatizados ou CI/CD.
- Tratamento de dados fora do arquivo `ecommerce_vendas.csv`.

## 8. Padrões
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

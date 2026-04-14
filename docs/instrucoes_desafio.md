




# Teste técnico – Case TechShop

## Situação-problema
A TechShop é um e-commerce de eletrônicos e periféricos que cresceu rápido nos últimos dois
anos — de 3 para 13 estados atendidos, com o catálogo triplicando de tamanho. O problema é
que o crescimento veio antes da estrutura de dados: os pedidos foram registrados em dois
sistemas diferentes ao longo do tempo, com pouca padronização, e parte do histórico foi migrada
manualmente por um fornecedor externo.

Hoje o time comercial toma decisões com base em relatórios feitos no Excel por uma pessoa que
saiu da empresa. Ninguém sabe ao certo se os números batem. A diretoria quer expandir para a
região  Sul  e  dobrar  o  investimento  em  categorias  "de  alto  desempenho" — mas  ninguém
consegue dizer com confiança quais são essas categorias.

Você foi contratado como o primeiro analista de dados do time. Seu trabalho começa pelo
começo: entender o que temos, confiar (ou não) nos dados, e extrair as primeiras respostas que
o negócio precisa.

## Sobre os dados
Você receberá um arquivo ecommerce_vendas.csv com o histórico de pedidos de 2024. Os dados
foram exportados diretamente do sistema legado e passaram por uma migração parcial — é
esperado que haja inconsistências. Parte do seu trabalho é identificá-las e decidir o que fazer com elas antes de qualquer análise.

## O que esperamos da entrega
Entregue um notebook .ipynb com o código e as análises, acompanhado de um README.md
curto explicando suas decisões principais. Não existe resposta única correta — o que avaliamos é
o seu raciocínio, a clareza das suas escolhas e a sua capacidade de comunicar resultados para
quem não é técnico.

Para as questões de SQL, sugerimos DuckDB ou SQLite em memória — mas fique à vontade para
usar a ferramenta que preferir, desde que o resultado seja reproduzível no notebook.

**Sobre o uso de IA:** é permitido e até esperado. O que avaliamos não é se você usou, mas como — se você valida os outputs, questiona resultados estranhos e adapta para o contexto. Numa entrevista de devolutiva, vamos pedir que você explique suas decisões.
Prazo: 5 dias corridos a partir do recebimento deste documento.

### Questão 1. Diagnóstico inicial
Faça uma análise exploratória inicial do dataset. Identifique e documente todos os problemas de
qualidade  encontrados: valores ausentes, inconsistências, duplicatas, outliers  e anomalias de
formato. Para cada problema, explique brevemente qual seria o impacto de ignorá-lo em uma
análise downstream.

### Questão 2. Tratamento e justificativa
Trate os problemas encontrados. Para cada decisão tomada (imputar, remover, corrigir, manter),
explique o raciocínio. Não existe resposta única correta — o que se avalia é a consistência e a
justificativa das escolhas.

### Questão 3. Consultas SQL
Escreva queries SQL para responder:
a) Quais são os 5 produtos com maior receita líquida (após desconto) nos últimos 90 dias do
dataset?
b) Qual é a taxa de cancelamento e devolução por categoria? Ordene da maior para a menor.
c) Identifique clientes que compraram em meses consecutivos por pelo menos 3 meses
seguidos (use window functions).
d) Compare o ticket médio por UF, filtrando apenas pedidos com status "entregue".

### Questão 4. Análise de negócio aberta
O time comercial quer decidir se vale a pena criar uma campanha de descontos específica para a
região Sul (RS, SC, PR). Com base nos dados disponíveis, que análise você conduziria? Quais
métricas usaria, quais hipóteses levantaria e quais limitações o dataset impõe para essa decisão?
Apresente os resultados de forma que um gerente não-técnico consiga entender.

### Questão 5. Encontre o erro
O gráfico abaixo foi apresentado numa reunião com a diretoria e gerou decisões estratégicas. Ele
mostra "Receita total por categoria — crescimento YoY". Há pelo menos dois problemas graves
na análise. Identifique-os, explique o impacto e proponha como corrigir.
Obs.: o código gerador desse gráfico está no arquivo `scripts/analise_crescimento.py`

![Gráfico de Receita Total por Categoria](<../artifacts/figures/imagem_grafico_receita_tota_ por_categoria_crescimento_YoY.jpg>)


### Questão 6. Modelagem
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

### Questão 7. Pergunta livre
Qual insight que você encontrou no dataset que não foi pedido em nenhuma das questões
anteriores?  Apresente  a  descoberta,  o  método  usado  para  encontrá-la  e  por  que  ela  seria
relevante para o negócio.

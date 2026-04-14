




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

Este documento preserva o enunciado original como contexto histórico. Para escopo, padrões e
critérios de aceite vigentes, consulte `docs/PRD.md`. Em caso de divergência, o PRD prevalece.

Para as questões de SQL, use DuckDB in-memory, conforme definido em `docs/PRD.md`.

**Sobre o uso de IA:** é permitido e até esperado. O que avaliamos não é se você usou, mas como — se você valida os outputs, questiona resultados estranhos e adapta para o contexto. Numa entrevista de devolutiva, vamos pedir que você explique suas decisões.
Prazo: 5 dias corridos a partir do recebimento deste documento.

## Questões
As questões vigentes Q1 a Q7 foram consolidadas em `docs/PRD.md`, na seção `## 3. Questões`.

Este arquivo não replica mais esse bloco para evitar divergência entre o enunciado histórico e o
contrato normativo do projeto.

Use o PRD como referência única para:
- texto completo das questões;
- objetivos de negócio;
- entregáveis;
- critérios de aceite e padrões.

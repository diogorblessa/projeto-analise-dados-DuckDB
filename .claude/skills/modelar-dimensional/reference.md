# Q6 - Modelagem Dimensional

## Exceção estrutural
- Q6 e markdown-only.
- Pode conter diagrama em texto, Mermaid ou imagem em `artifacts/diagrams/`.

## Entregáveis
- Modelo dimensional, estrela ou floco, sustentando Q3 e Q4 como casos de uso.
- Tabela fato com granularidade declarada explícitamente.
- Dimensoes: `dim_cliente`, `dim_produto`, `dim_tempo`, `dim_localidade`, `dim_status`, ou justificativa para supressao.
- Chaves surrogate vs natural declaradas.
- Métricas da fato: `qtd`, `valor_bruto`, `desconto`, `receita_liquida` e similares.

## Estrutura sugerida
1. Objetivo analítico do modelo.
2. Grao da fato.
3. Diagrama.
4. Dicionario das tabelas.
5. Exemplos de perguntas respondiveis.
6. Limitacoes e próximos passos.

## Restrições
- Apenas desenho; não implementar DDL executavel nem ETL.
- Justificar escolhas de desnormalizacao ou normalizacao.

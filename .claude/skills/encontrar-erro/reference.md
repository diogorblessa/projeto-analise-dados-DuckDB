# Q5 - Debug (`scripts/analise_crescimento.py`)

## Objetivo
Auditar `scripts/analise_crescimento.py` e identificar no mínimo `2` erros graves que invalidaram decisões passadas.

## Procedimento
- Ler o script como um todo antes de apontar erros.
- Para cada erro: descrever a falha, mostrar o trecho, explicar o impacto no resultado e propor a correção.
- Executar a versão corrigida no notebook e comparar com a original quando viável.
- Não editar o script original; mostrar a correção em célula do notebook.

## Categorias típicas a investigar
- Agregações erradas, incluindo double counting via join.
- Filtros que removem casos válidos, inclusive `status` incorreto.
- Comparações temporais com períodos não equivalentes.
- Cálculo de crescimento em base errada.
- Uso de dataset bruto em vez de tratado.

## Saída
- `[MD analise]` final com a lista numerada de erros, impacto e correção.
- Registrar achados em `memory-bank/decisions.md` se alterarem conclusões anteriores.

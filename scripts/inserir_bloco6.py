"""
inserir_bloco6.py

Normaliza o bloco 6 (Q5) no notebook `notebooks/case_techshop.ipynb` para a
Fase 1 do workflow:
- atualiza a célula markdown de explicação (`d24bda53`);
- garante a célula code `q5_debug_code` logo em seguida;
- remove a célula `q5_debug_analise`, que fica reservada para a Fase 2.

O `source` da célula de código é importado de `atualizar_bloco6_code.py`, que
passa a ser a fonte canônica do bloco.

Execute: `uv run python scripts/inserir_bloco6.py`
"""
from pathlib import Path

import nbformat

from atualizar_bloco6_code import SOURCE_CODE

NOTEBOOK_PATH = Path("notebooks/case_techshop.ipynb")
TARGET_MD_ID = "d24bda53"
TARGET_CODE_ID = "q5_debug_code"
TARGET_ANALISE_ID = "q5_debug_analise"

SOURCE_MD_EXPLICACAO = """\
# Bloco 6: Q5 - Debug

## Q5 - Encontre o Erro

O script `scripts/analise_crescimento.py` foi usado para produzir o gráfico
"Receita total por categoria — crescimento YoY" apresentado à diretoria, que
gerou decisões estratégicas sobre quais categorias receberiam maior investimento.

O script afirma calcular o **crescimento Year-over-Year (YoY) da receita por
categoria** — isto é, quanto cada categoria cresceu em relação ao mesmo período
do ano anterior.

Foram identificados **dois erros graves** que invalidam os resultados:

1. **Erro 1 — Dataset bruto sem filtro de status:** o script lê o arquivo bruto
   (`ecommerce_vendas.csv`) sem nenhum filtro de `status`, incluindo pedidos
   `cancelado` e `devolvido` na soma de receita.

2. **Erro 2 — "YoY" não é YoY e a base é indefinida:** a variável `primeiro_mes`
   é calculada mas jamais utilizada (*dead code*), revelando a intenção original
   nunca implementada. A função `crescimento` usa `grupo.iloc[0]["receita"]` como
   base sem ordenar o grupo por data, tornando a base dependente da ordem dos
   dados. Além disso, o dataset contém apenas o ano de 2024 — cálculo YoY
   (mesmo período, ano anterior) é **impossível por definição** sem dados de 2023.

Nesta **Fase 1**, o código abaixo:
- reproduz o gráfico histórico apresentado à diretoria;
- compara esse artefato com a saída literal do script versionado;
- mostra a leitura corrigida com base determinística e filtro de status válido.

A análise narrativa consolidada ficará para a **Fase 2** do workflow.\
"""


def encontrar_indice_por_id(cells, target_id):
    return next((i for i, cell in enumerate(cells) if cell.get("id") == target_id), None)


def main() -> None:
    nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

    idx_md = encontrar_indice_por_id(nb.cells, TARGET_MD_ID)
    if idx_md is None:
        raise ValueError(f"Celula markdown {TARGET_MD_ID!r} nao encontrada.")

    nb.cells[idx_md]["source"] = SOURCE_MD_EXPLICACAO

    indices_code = [
        i for i, cell in enumerate(nb.cells) if cell.get("id") == TARGET_CODE_ID
    ]
    if indices_code:
        idx_code = indices_code[0]
        nb.cells[idx_code]["source"] = SOURCE_CODE
        nb.cells[idx_code]["outputs"] = []
        nb.cells[idx_code]["execution_count"] = None
        for idx_extra in reversed(indices_code[1:]):
            del nb.cells[idx_extra]
    else:
        celula_code = nbformat.v4.new_code_cell(source=SOURCE_CODE)
        celula_code["id"] = TARGET_CODE_ID
        nb.cells.insert(idx_md + 1, celula_code)
        idx_code = idx_md + 1

    if idx_code != idx_md + 1:
        celula_code = nb.cells.pop(idx_code)
        nb.cells.insert(idx_md + 1, celula_code)

    indices_analise = [
        i for i, cell in enumerate(nb.cells) if cell.get("id") == TARGET_ANALISE_ID
    ]
    for idx_analise in reversed(indices_analise):
        del nb.cells[idx_analise]

    nbformat.validate(nb)
    nbformat.write(nb, NOTEBOOK_PATH)

    print(f"Notebook atualizado: {NOTEBOOK_PATH}")
    print("Bloco 6 normalizado para Fase 1: markdown + code; sem [MD analise].")
    for i, cell in enumerate(nb.cells[23:27], start=23):
        print(f"[{i:02d}] {cell['cell_type']:8s} id={cell.get('id', 'no-id')}")


if __name__ == "__main__":
    main()

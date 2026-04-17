"""
inserir_bloco6_analise.py
Fase 2 do Q5: insere/atualiza a célula [MD análise] (id `q5_debug_analise`)
logo após a célula [CODE] (`q5_debug_code`) e antes do bloco Q6.

Rastreabilidade: todos os valores numéricos vêm do output imediatamente
anterior da célula `q5_debug_code` na execução desta sessão. Conteúdo
reescrito em tom executivo seguindo `.claude/rules/analysis-writing.md`.

Execute: uv run python scripts/inserir_bloco6_analise.py
"""
from pathlib import Path

import nbformat

NOTEBOOK_PATH = Path("notebooks/case_techshop.ipynb")
TARGET_CODE_ID = "q5_debug_code"
TARGET_ANALISE_ID = "q5_debug_analise"

SOURCE_MD_ANALISE = """\
### Q5, análise consolidada (Fase 2)

#### Achado principal

O gráfico "Receita total por categoria, crescimento YoY" que sustentou decisões de investimento da diretoria foi gerado a partir de um script com duas falhas graves. A primeira incluiu receita de pedidos `cancelados` e `devolvidos` como se fossem venda realizada, inflando a receita em `24,0%`. A segunda calculou a variação de crescimento usando como ponto de partida uma base de comparação dependente da ordem em que os dados chegam, em vez de ancorar em `jan/2024`. O rótulo `YoY` (crescimento ano contra ano) é ainda tecnicamente impossível, já que o dataset contém apenas `2024`.

#### Evidências-chave

Receita indevidamente somada pelo filtro ausente: `R$ 175.599,53` sobre `R$ 731.085,80` de receita válida (pedidos `entregue` e `em_transito`).

Base de comparação instável: em `6 de 6` categorias testadas, o ponto de partida difere de `jan/2024` quando os dados chegam em ordem diferente. Por exemplo, `Impressoras` passa a ancorar em `ago/2024` (`R$ 12.984,90`) em vez de `jan/2024` (`R$ 3.994,85`), distorcendo a leitura de crescimento de forma integral.

Comparativo entre o gráfico histórico e a leitura corrigida (base `jan/2024` a `dez/2024`, dataset tratado, apenas pedidos válidos):

| Categoria | Histórico (diretoria) | Corrigido | Divergência |
|---|---:|---:|---|
| `Impressoras` | `-52,9%` | `+259,5%` | `-312,4 pp`, inversão de sinal |
| `Câmeras` | `-48,8%` | `+17,8%` | `-66,6 pp`, inversão de sinal |
| `Monitores` | `+129,5%` | `+103,2%` | `+26,3 pp`, magnitude menor |
| `Armazenamento` | `+46,8%` | `+81,7%` | `-34,9 pp`, magnitude maior |
| `Acessórios` | `-7,1%` | `-6,4%` | `-0,7 pp`, praticamente equivalente |
| `Periféricos` | `-32,7%` | `-34,4%` | `+1,7 pp`, praticamente equivalente |

#### Impacto no gráfico original

O gráfico apresentado à diretoria destacou `Monitores` e `Armazenamento` como categorias a expandir e posicionou `Impressoras`, `Câmeras` e `Periféricos` como quedas significativas. A leitura corrigida inverte duas dessas leituras de forma direta. `Impressoras` deixa de ser apresentada como a maior queda e passa a ser a maior alta (`+259,5%`). `Câmeras` sai de queda pronunciada (`-48,8%`) e vira leve alta (`+17,8%`). Metade das categorias apresentadas ao comitê muda de sinal ou muda sensivelmente de magnitude quando os dois erros do script são corrigidos.

#### O que isso significa para o negócio

Nenhuma decisão de alocação de investimento por categoria deve seguir baseada no gráfico original sem revalidação. As leituras mais críticas são `Impressoras` e `Câmeras`: ambas foram apresentadas ao comitê como queda relevante e aparecem com sinal oposto na leitura corrigida, portanto qualquer corte de investimento nessas categorias precisa ser reavaliado antes da execução. `Monitores` e `Armazenamento` mantêm sinal positivo, mas o dimensionamento do investimento precisa ser refeito com a magnitude correta. `Acessórios` e `Periféricos` ficam praticamente equivalentes entre as duas leituras.

#### Ressalvas

A base contém apenas `2024`. O rótulo `YoY` é impossível por definição sem dados de `2023`. A métrica corrigida é explicitamente "variação de receita de `jan/2024` a `dez/2024`", não `YoY`.

Ancorar a leitura em dois meses extremos é frágil. A evolução mensal é altamente volátil: `Impressoras` oscila de `+507,7%` em `mai/2024` a `-2,4%` em `jul/2024` e volta a `+319,2%` em `out/2024`. `Câmeras` oscila entre `+74,7%` (`out/2024`) e `-69,0%` (`ago/2024`). Qualquer métrica ancorada em apenas dois meses herda esse ruído.

Inconsistência adicional de auditoria: o gráfico histórico apresentado à diretoria não é totalmente reproduzível hoje a partir do script versionado. A causa não foi identificada nesta auditoria e não deve ser atribuída a nenhum fator sem investigação. Trata-se de um problema de governança analítica, não de um terceiro erro causal do script.

O filtro `status` em (`entregue`, `em_transito`) inclui pedidos ainda em trânsito, que podem ser futuramente cancelados ou devolvidos. Aceitável para leitura retrospectiva de `2024`, revisável se a análise passar a suportar decisão operacional.

#### Correção recomendada

**O que estava errado no script original (`scripts/analise_crescimento.py`):**
1. Leitura do dataset bruto sem filtro de `status`, incluindo pedidos `cancelado` e `devolvido` na soma de receita. Consequência: receita inflada em `24,0%`.
2. Base de comparação calculada pela primeira linha do grupo sem ordenar por mês. Consequência: base varia em `6 de 6` categorias quando os dados chegam desordenados.
3. Rótulo `YoY` sobre base que contém apenas `2024`. Métrica impossível por definição.

**O que foi corrigido na Fase 1 (célula `q5_debug_code`):**
1. Leitura passa a ser do dataset tratado de Q2, com filtro para apenas pedidos `entregue` e `em_transito`.
2. Cálculo ancora a base de comparação em `jan/2024` de forma determinística em todas as categorias.
3. Métrica é renomeada para "crescimento de receita de `jan/2024` a `dez/2024`", explicitamente não `YoY`. O gráfico corrigido usa a mesma escala de Y do artefato histórico para permitir comparação visual direta.

**O que ainda depende de validação adicional:**
1. Investigar a causa da divergência entre o gráfico histórico e a saída literal do script versionado. Hipóteses possíveis (script editado após a geração da figura, base de dados diferente à época, outro pipeline) não têm evidência no output desta auditoria.
2. Definir uma métrica de crescimento mais robusta que não dependa de dois meses âncora, dada a volatilidade mensal observada. Alternativas razoáveis: totais anuais, médias móveis trimestrais ou `CAGR` parcial.
3. Revalidar especificamente as decisões estratégicas já tomadas com base no artefato original, em especial para `Impressoras` e `Câmeras`, cujas leituras corrigidas invertem de sinal.

**Recomendação final:** a análise de crescimento por categoria no formato apresentado à diretoria não é confiável o suficiente para sustentar decisão de alocação de investimento. O artefato precisa ser reconstruído a partir do dataset tratado, com métrica robusta, antes de ser reutilizado em comitê.\
"""


def main() -> None:
    nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

    idx_code = next(
        (i for i, cell in enumerate(nb.cells) if cell.get("id") == TARGET_CODE_ID),
        None,
    )
    if idx_code is None:
        raise ValueError(f"Celula code {TARGET_CODE_ID!r} nao encontrada.")

    indices_existentes = [
        i for i, cell in enumerate(nb.cells) if cell.get("id") == TARGET_ANALISE_ID
    ]
    if indices_existentes:
        idx_analise = indices_existentes[0]
        nb.cells[idx_analise]["source"] = SOURCE_MD_ANALISE
        for idx_extra in reversed(indices_existentes[1:]):
            del nb.cells[idx_extra]
        if idx_analise != idx_code + 1:
            celula = nb.cells.pop(idx_analise)
            nb.cells.insert(idx_code + 1, celula)
        acao = "atualizada"
    else:
        celula = nbformat.v4.new_markdown_cell(source=SOURCE_MD_ANALISE)
        celula["id"] = TARGET_ANALISE_ID
        nb.cells.insert(idx_code + 1, celula)
        acao = "inserida"

    nbformat.validate(nb)
    nbformat.write(nb, NOTEBOOK_PATH)

    print(f"Celula {TARGET_ANALISE_ID} {acao} apos {TARGET_CODE_ID}.")
    print(f"Total de celulas: {len(nb.cells)}")
    for i, cell in enumerate(nb.cells[23:28], start=23):
        cid = cell.get("id", "no-id")
        print(f"  [{i:02d}] {cell['cell_type']:8s} id={cid}")


if __name__ == "__main__":
    main()

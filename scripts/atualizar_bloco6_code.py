"""
atualizar_bloco6_code.py

Reescreve apenas o `source` da célula [CODE] de Q5 (id `q5_debug_code`) em
`notebooks/case_techshop.ipynb`.

Escopo desta versão:
- manter Q5 em Fase 1 (`MD explicação + CODE`);
- reproduzir o gráfico histórico apresentado à diretoria;
- comparar artefato histórico, saída literal do script versionado e leitura corrigida;
- remover a figura anual complementar de 2024;
- deixar a `[MD análise]` para a Fase 2 do workflow.

Execute: `uv run python scripts/atualizar_bloco6_code.py`
"""
from pathlib import Path

import nbformat

NOTEBOOK_PATH = Path("notebooks/case_techshop.ipynb")
TARGET_ID = "q5_debug_code"

SOURCE_CODE = """\
# =============================================================
# Q5 — Debug: scripts/analise_crescimento.py
# =============================================================
# Fase 1 da auditoria:
#   1. reproduz o gráfico histórico apresentado à diretoria;
#   2. contrasta esse artefato com a saída literal do script versionado;
#   3. apresenta o gráfico corrigido com base determinística e filtro de status.
# A [MD análise] fica reservada para a Fase 2.
# =============================================================

from matplotlib.patches import Patch


ORDEM_CATEGORIAS = [
    "Monitores",
    "Armazenamento",
    "Acessórios",
    "Periféricos",
    "Câmeras",
    "Impressoras",
]

ARTEFATO_HISTORICO_PCT = {
    "Monitores": 129.5,
    "Armazenamento": 46.8,
    "Acessórios": -7.1,
    "Periféricos": -32.7,
    "Câmeras": -48.8,
    "Impressoras": -52.9,
}


def formatar_brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_pct(valor):
    return f"{valor:.1f}%"


def reordenar_por_categoria(df, coluna_valor):
    return (
        df[["categoria", coluna_valor]]
        .drop_duplicates(subset=["categoria"])
        .set_index("categoria")
        .reindex(ORDEM_CATEGORIAS)
        .reset_index()
    )


def calcular_variacao_mensal_ordenada(df_cat_mes, coluna_saida):
    partes = []
    for _, grupo in df_cat_mes.groupby("categoria"):
        grupo = grupo.sort_values("mes").copy()
        base = grupo.iloc[0]["receita"]
        grupo[coluna_saida] = (grupo["receita"] / base - 1) * 100
        partes.append(grupo)

    resultado = pd.concat(partes, ignore_index=True)
    ultimo_mes = resultado[resultado["mes"] == resultado["mes"].max()].copy()
    return resultado, reordenar_por_categoria(ultimo_mes, coluna_saida)


def reproduzir_script_literal(df_bruto):
    receita_mes = df_bruto.groupby(["categoria", "mes"])["receita"].sum().reset_index()
    partes = []
    for _, grupo in receita_mes.groupby("categoria"):
        grupo = grupo.copy()
        base = grupo.iloc[0]["receita"]
        grupo["script_literal_pct"] = (grupo["receita"] / base - 1) * 100
        partes.append(grupo)

    resultado = pd.concat(partes, ignore_index=True)
    ultimo_mes = resultado[resultado["mes"] == resultado["mes"].max()].copy()
    return reordenar_por_categoria(ultimo_mes, "script_literal_pct")


def plotar_grafico_q5(
    ax,
    dados_plot,
    coluna_percentual,
    identificacao,
    subtitulo,
    eixo_y,
    legenda,
    rodape,
    categorias_destacadas,
    y_limites,
):
    azul = "#2f67d8"
    cinza = "#6e7f99"
    cores = [
        azul if categoria in categorias_destacadas else cinza
        for categoria in dados_plot["categoria"]
    ]

    barras = ax.bar(
        dados_plot["categoria"],
        dados_plot[coluna_percentual],
        color=cores,
        edgecolor="white",
        linewidth=0.8,
        width=0.62,
        zorder=3,
    )

    ax.set_title(
        f"{identificacao}\\nCrescimento de receita por categoria — 2024\\n{subtitulo}",
        fontsize=13,
        fontweight="bold",
        pad=14,
    )
    ax.set_ylabel(eixo_y)
    ax.set_ylim(*y_limites)
    ax.axhline(0, color="#495057", linewidth=0.8, zorder=2)
    ax.grid(axis="y", color="#d9dee7", linewidth=0.9, alpha=0.9, zorder=1)
    ax.set_facecolor("#fbfcfe")
    ax.tick_params(axis="x", rotation=23, labelsize=9)
    ax.tick_params(axis="y", labelsize=9)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#d9dee7")
    ax.spines["bottom"].set_color("#d9dee7")

    rotulos = [formatar_pct(valor) for valor in dados_plot[coluna_percentual]]
    ax.bar_label(barras, labels=rotulos, padding=3, fontsize=9, fontweight="bold")
    ax.legend(
        handles=[Patch(facecolor=azul, edgecolor="white", label=legenda)],
        loc="upper right",
        frameon=False,
        fontsize=8,
    )
    ax.text(
        0.0,
        -0.19,
        rodape,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
        color="#7a7f87",
    )


# ---------------------------------------------------------------
# Carga das bases
# ---------------------------------------------------------------
df_bruto_original = pd.read_csv(RAW_PATH)
df_bruto_original["data_pedido"] = pd.to_datetime(
    df_bruto_original["data_pedido"], dayfirst=True, errors="coerce"
)
df_bruto_original["mes"] = df_bruto_original["data_pedido"].dt.to_period("M")
df_bruto_original["receita"] = (
    df_bruto_original["qtd"]
    * df_bruto_original["valor_unit"]
    * (1 - df_bruto_original["desconto_%"].fillna(0) / 100)
)

df_tratado = pd.read_csv(INTERIM_DIR / "ecommerce_tratado.csv")
df_tratado["data_pedido"] = pd.to_datetime(df_tratado["data_pedido"])
df_tratado["mes"] = df_tratado["data_pedido"].dt.to_period("M")

status_validos = ["entregue", "em_transito"]
status_invalidos = ["cancelado", "devolvido"]
df_valido = df_tratado[df_tratado["status"].isin(status_validos)].copy()


# ---------------------------------------------------------------
# Evidência objetiva dos dois erros já identificados
# ---------------------------------------------------------------
print("=== EVIDÊNCIA — ERRO 1: receita inflada por status inválido ===")
print(df_tratado["status"].value_counts().to_string())

receita_invalida = df_tratado[df_tratado["status"].isin(status_invalidos)]["receita"].sum()
receita_valida = df_valido["receita"].sum()
inflacao_total_pct = receita_invalida / receita_valida * 100

print(f"\\nReceita inválida (cancelado + devolvido): {formatar_brl(receita_invalida)}")
print(f"Receita válida (entregue + em_transito): {formatar_brl(receita_valida)}")
print(f"Inflação total causada pelo Erro 1: {inflacao_total_pct:.1f}%")

print("\\n=== EVIDÊNCIA — ERRO 2: 'YoY' impossível + base dependente da ordem ===")
anos_disponiveis = sorted(int(ano) for ano in df_tratado["data_pedido"].dt.year.unique())
print(f"Anos presentes no dataset: {anos_disponiveis}")
print("YoY real exigiria o mesmo período de 2023, que não existe nesta base.")

receita_mes_tratado = (
    df_tratado.groupby(["categoria", "mes"])["receita"].sum().reset_index()
)
receita_mes_desordenado = receita_mes_tratado.sample(frac=1, random_state=7).reset_index(drop=True)

print("\\nSensibilidade do `iloc[0]` quando a ordem dos dados muda:")
print(
    f"{'Categoria':<16} {'Base jan/2024':>18} "
    f"{'Base iloc[0]':>18} {'Mês escolhido':>15}"
)
for categoria in sorted(receita_mes_tratado["categoria"].unique()):
    base_ordenada = (
        receita_mes_tratado[receita_mes_tratado["categoria"] == categoria]
        .sort_values("mes")
        .iloc[0]["receita"]
    )
    grupo_desordenado = receita_mes_desordenado[receita_mes_desordenado["categoria"] == categoria]
    base_iloc = grupo_desordenado.iloc[0]["receita"]
    mes_iloc = grupo_desordenado.iloc[0]["mes"]
    alerta = " <- DIFERENTE" if base_ordenada != base_iloc else ""
    print(
        f"{categoria:<16} {formatar_brl(base_ordenada):>18} "
        f"{formatar_brl(base_iloc):>18} {str(mes_iloc):>15}{alerta}"
    )


# ---------------------------------------------------------------
# Série histórica: artefato apresentado, script literal e leitura corrigida
# ---------------------------------------------------------------
historico_df = pd.DataFrame(
    {
        "categoria": ORDEM_CATEGORIAS,
        "artefato_historico_pct": [ARTEFATO_HISTORICO_PCT[c] for c in ORDEM_CATEGORIAS],
    }
)

script_literal_df = reproduzir_script_literal(df_bruto_original)

receita_mes_corrigida = (
    df_valido.groupby(["categoria", "mes"])["receita"].sum().reset_index()
)
resultado_corrigido, corrigido_df = calcular_variacao_mensal_ordenada(
    receita_mes_corrigida,
    coluna_saida="corrigido_pct",
)

cobertura_corrigida = (
    receita_mes_corrigida.groupby("categoria")["mes"]
    .agg(primeiro_mes="min", ultimo_mes="max", meses_distintos="nunique")
    .reset_index()
    .set_index("categoria")
    .reindex(ORDEM_CATEGORIAS)
    .reset_index()
)

comparativo_q5 = (
    historico_df.merge(script_literal_df, on="categoria", how="left")
    .merge(corrigido_df, on="categoria", how="left")
)
comparativo_q5["dif_hist_vs_script_pp"] = (
    comparativo_q5["artefato_historico_pct"] - comparativo_q5["script_literal_pct"]
).round(1)
comparativo_q5["dif_hist_vs_corrigido_pp"] = (
    comparativo_q5["artefato_historico_pct"] - comparativo_q5["corrigido_pct"]
).round(1)
comparativo_q5["script_vs_corrigido_pp"] = (
    comparativo_q5["script_literal_pct"] - comparativo_q5["corrigido_pct"]
).round(1)

for coluna in [
    "artefato_historico_pct",
    "script_literal_pct",
    "corrigido_pct",
]:
    comparativo_q5[coluna] = comparativo_q5[coluna].round(1)

print("\\nCobertura mensal da base corrigida por categoria:")
print(cobertura_corrigida.to_string(index=False))

print("\\n=== ACHADO FORMAL ADICIONAL — artefato histórico vs. script versionado ===")
print(
    "O gráfico apresentado à diretoria não é totalmente reproduzível a partir "
    "do `scripts/analise_crescimento.py`. A tabela abaixo mostra essa divergência."
)

print("\\nTabela comparativa da auditoria de Q5 (em pontos percentuais):")
print(comparativo_q5.to_string(index=False))


# ---------------------------------------------------------------
# Gráficos padronizados: original histórico vs. corrigido
# ---------------------------------------------------------------
valores_y = pd.concat(
    [
        comparativo_q5["artefato_historico_pct"],
        comparativo_q5["corrigido_pct"],
        comparativo_q5["script_literal_pct"],
    ],
    ignore_index=True,
)
limite_inferior = min(0, valores_y.min())
limite_superior = max(0, valores_y.max())
amplitude = limite_superior - limite_inferior
margem = max(12, amplitude * 0.12)
y_limites = (limite_inferior - margem, limite_superior + margem)

print(
    "\\nOs dois gráficos abaixo usam a mesma escala no eixo Y para permitir "
    "comparação visual direta entre o artefato histórico e a versão corrigida."
)

with plt.style.context("seaborn-v0_8-whitegrid"):
    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    plotar_grafico_q5(
        ax=ax,
        dados_plot=historico_df,
        coluna_percentual="artefato_historico_pct",
        identificacao="Q5 — Gráfico original apresentado à diretoria",
        subtitulo="(base: primeiro mês de registro)",
        eixo_y="Crescimento de receita (%)",
        legenda="Categorias recomendadas para expansão",
        rodape="Fonte: Sistema legado TechShop | Análise: jan-dez 2024",
        categorias_destacadas=["Monitores"],
        y_limites=y_limites,
    )
    plt.tight_layout()
    plt.show()

with plt.style.context("seaborn-v0_8-whitegrid"):
    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    categorias_positivas = corrigido_df[corrigido_df["corrigido_pct"] > 0]["categoria"].tolist()
    plotar_grafico_q5(
        ax=ax,
        dados_plot=corrigido_df,
        coluna_percentual="corrigido_pct",
        identificacao="Q5 — Gráfico corrigido",
        subtitulo="(jan/2024 → dez/2024, com filtro de status válido)",
        eixo_y="Variação da receita mensal (jan/2024 → dez/2024) (%)",
        legenda="Categorias com crescimento positivo na leitura corrigida",
        rodape="Fonte: data/interim/ecommerce_tratado.csv | Status válidos: entregue + em_transito",
        categorias_destacadas=categorias_positivas,
        y_limites=y_limites,
    )
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# Apoio à Fase 2: evolução mensal da leitura corrigida
# ---------------------------------------------------------------
evolucao_corrigida = (
    resultado_corrigido.pivot(index="mes", columns="categoria", values="corrigido_pct")
    .reindex(columns=ORDEM_CATEGORIAS)
    .round(1)
    .sort_index()
)
print("\\nEvolução mensal da leitura corrigida (jan/2024 → dez/2024):")
print(evolucao_corrigida.to_string())\
"""


def main() -> None:
    nb = nbformat.read(NOTEBOOK_PATH, as_version=4)
    idx = next(i for i, cell in enumerate(nb.cells) if cell.get("id") == TARGET_ID)
    assert nb.cells[idx]["cell_type"] == "code", f"Celula idx {idx} nao e code"

    nb.cells[idx]["source"] = SOURCE_CODE
    nb.cells[idx]["outputs"] = []
    nb.cells[idx]["execution_count"] = None
    nbformat.validate(nb)
    nbformat.write(nb, NOTEBOOK_PATH)

    print(f"Celula {TARGET_ID} (idx {idx}) atualizada; outputs limpos.")


if __name__ == "__main__":
    main()

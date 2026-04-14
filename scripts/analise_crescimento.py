import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_vendas.csv")
df["data_pedido"] = pd.to_datetime(df["data_pedido"], dayfirst=True, errors="coerce")
df["mes"] = df["data_pedido"].dt.to_period("M")
df["receita"] = df["qtd"] * df["valor_unit"] * (1 - df["desconto_%"].fillna(0) / 100)

receita_cat = df.groupby(["categoria", "mes"])["receita"].sum().reset_index()

primeiro_mes = receita_cat.groupby("categoria")["mes"].min()

def crescimento(grupo):
    base = grupo.iloc[0]["receita"]
    grupo = grupo.copy()
    grupo["yoy"] = (grupo["receita"] / base - 1) * 100
    return grupo

resultado = receita_cat.groupby("categoria", group_keys=False).apply(crescimento)
ultimo = resultado[resultado["mes"] == resultado["mes"].max()]

plt.figure(figsize=(10, 5))
plt.bar(ultimo["categoria"], ultimo["yoy"])
plt.title("Crescimento de receita por categoria (YoY %)")
plt.ylabel("Crescimento (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("crescimento_categorias.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# ====== LEITURA DOS DADOS ======
df = pd.read_csv("data/store.csv", encoding="latin-1")

# ====== TRATAMENTO DOS DADOS ======

# Criando coluna de faturamento
df["Faturamento"] = df["Quantity"] * df["Sales"]

# Convertendo data e extraindo mês
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Mes"] = df["Order Date"].dt.month

# ====== ANÁLISE POR MÊS ======

# Agrupando faturamento por mês
vendas_mes = df.groupby("Mes")["Faturamento"].sum()

# Identificando melhor e pior mês
melhor_mes = vendas_mes.idxmax()
pior_mes = vendas_mes.idxmin()

valor_melhor = vendas_mes.max()
valor_pior = vendas_mes.min()

print(f"""
===== ANÁLISE MENSAL =====

Melhor mês: {melhor_mes}
Faturamento: R$ {valor_melhor:,.2f}

Pior mês: {pior_mes}
Faturamento: R$ {valor_pior:,.2f}
""")

# ====== GRÁFICO MENSAL ======

plt.figure(figsize=(10,5))

plt.plot(vendas_mes.index, vendas_mes.values, marker='o')

# Destaques
plt.scatter(melhor_mes, valor_melhor)
plt.scatter(pior_mes, valor_pior)

plt.title("Faturamento por Mês")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.grid()

plt.show()

# ====== ANÁLISE POR PRODUTO ======

# Agrupando faturamento por produto
vendas_produto = df.groupby("Product Name")["Faturamento"].sum()

# Produto mais vendido
top_produto = vendas_produto.idxmax()
valor_top = vendas_produto.max()

# Produto menos vendido
pior_produto = vendas_produto.idxmin()
valor_prod = vendas_produto.min()

print(f"""
===== ANÁLISE DE PRODUTOS =====

Produto mais vendido: {top_produto}
Faturamento: R$ {valor_top:,.2f}

Produto menos vendido: {pior_produto}
Faturamento: R$ {valor_prod:,.2f}
""")

# ====== TOP 10 PRODUTOS ======

top10 = vendas_produto.sort_values(ascending=False).head(10)

print("===== TOP 10 PRODUTOS =====\n")

for produto, valor in top10.items():
    print(f"{produto}: R$ {valor:,.2f}")









import pandas as pd

df = pd.DataFrame({
    'Produto': ['Celular', 'Capa', 'Fone', 'Carregador'],
    'Volume_Vendas': [1500, 5000, 3200, 800]
})

# O parâmetro ascending=False garante que quem vendeu mais fique em 1º
df['Ranking_Interno'] = df['Volume_Vendas'].rank(ascending=False).astype(int)

print("--- Força Relativa do Produto ---")
print(df.sort_values(by='Ranking_Interno'))
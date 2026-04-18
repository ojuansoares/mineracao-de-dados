import pandas as pd

dados = {
    'Sistema_Operacional': ['Ubuntu']*90 + ['Debian']*5 + ['Armbian']*3 + ['Ubuntuu']*1 + ['Debiann']*1
}
df = pd.DataFrame(dados)

proporcao = df['Sistema_Operacional'].value_counts(normalize=True)
categorias_raras = proporcao[proporcao < 0.05].index
isoldados = df[df['Sistema_Operacional'].isin(categorias_raras)]

print("--- Categorias com menos de 5% (possíveis erros) ---")
print(isoldados['Sistema_Operacional'].unique())
print("\n--- Linhas com categorias raras ---")
print(isoldados)

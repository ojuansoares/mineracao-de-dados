import pandas as pd

df = pd.DataFrame({
    'Cliente': ['Alice', 'Bob'],
    'Divida_Total': [5000.0, 8000.0],
    'Renda_Mensal': [2500.0, 20000.0]
})

# A proporção é mais valiosa para a IA porque R$ 5.000 de dívida para 
# quem ganha R$ 2.500 é muito mais crítico do que R$ 8.000 para quem ganha R$ 20.000.
df['Razao_Comprometimento'] = df['Divida_Total'] / df['Renda_Mensal']

print("--- Análise de Crédito ---")
print(df)
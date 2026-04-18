import pandas as pd

dados = {
    'Sensor_ID': [1, 2, 3, 4, 5],
    'Temperatura_C': ['25.5', '26.1', 'falha_sinal', '24.8', 'erro_rede']
}
df = pd.DataFrame(dados)

print("--- 1. Dados Originais ---")
print(df, "\n")

df['Temperatura_C'] = pd.to_numeric(df['Temperatura_C'], errors='coerce')

print("--- 2. Dados após conversão (Textos viraram NaN) ---")
print(df, "\n")

falhas = df[df['Temperatura_C'].isna()]

print("--- 3. Apenas as linhas onde a conversão falhou ---")
print(falhas)
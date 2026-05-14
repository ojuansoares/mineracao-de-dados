import pandas as pd

df = pd.DataFrame({
    'Sensor_ID': ['S1', 'S2'],
    'Leitura_T1': [50.0, 120.0], # Momento 1
    'Leitura_T2': [65.0, 90.0]   # Momento 2
})

# Variação bruta
df['Delta'] = df['Leitura_T2'] - df['Leitura_T1']

# Variação percentual
df['Evolucao_Percentual'] = (df['Delta'] / df['Leitura_T1']) * 100

# Sinalizando tendência (1 = Crescimento, 0 = Queda/Estável)
df['Tendencia_Crescimento'] = (df['Delta'] > 0).astype(int)

print("--- Evolução de Leitura ---")
print(df)
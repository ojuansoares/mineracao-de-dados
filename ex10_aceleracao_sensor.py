import pandas as pd

df = pd.DataFrame({
    'Sensor': ['A1', 'B1'],
    'Leitura_1': [10.0, 50.0],
    'Leitura_2': [15.0, 55.0],
    'Leitura_3': [25.0, 58.0]
})

# Calculando os Deltas primários
df['Delta_1'] = df['Leitura_2'] - df['Leitura_1'] # Variação do T1 pro T2
df['Delta_2'] = df['Leitura_3'] - df['Leitura_2'] # Variação do T2 pro T3

# Calculando a Aceleração (Delta do Delta)
df['Aceleracao'] = df['Delta_2'] - df['Delta_1']

# Disparando alerta binário se a aceleração for positiva (tendência exponencial)
df['Alerta_Crescimento_Exponencial'] = (df['Aceleracao'] > 0).astype(int)

print("--- Monitoramento de Aceleração ---")
print(df)
import pandas as pd

df = pd.DataFrame({
    'Acesso_ID': [101, 102, 103],
    'Timestamp': ['2026-04-17 14:30:00', '2026-04-18 09:15:00', '2026-04-19 20:00:00'] 
    # 18 e 19 caem no final de semana (Sábado e Domingo)
})

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extraindo o mês e o dia da semana (0 = Segunda, 6 = Domingo)
df['Mes'] = df['Timestamp'].dt.month
df['Dia_Semana'] = df['Timestamp'].dt.dayofweek

# Flag para acesso no Final de Semana (5 = Sábado, 6 = Domingo)
df['Flag_Fim_De_Semana'] = df['Dia_Semana'].isin([5, 6]).astype(int)

print("--- Análise de Acessos ---")
print(df[['Acesso_ID', 'Timestamp', 'Mes', 'Dia_Semana', 'Flag_Fim_De_Semana']])
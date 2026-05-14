import pandas as pd

df_log = pd.DataFrame({
    'Cliente_ID': [10, 10, 20, 10, 20],
    'Data_Transacao': pd.to_datetime(['2025-10-01', '2026-01-15', '2026-02-20', '2026-04-10', '2026-04-12']),
    'Valor': [100.0, 250.0, 500.0, 50.0, 600.0]
})

data_analise = pd.to_datetime('2026-04-17')

grupo = df_log.groupby('Cliente_ID')

rfm = pd.DataFrame({
    'Frequencia': grupo['Valor'].count(),
    'Valor_Monetario': grupo['Valor'].sum(),
    'Ultima_Compra': grupo['Data_Transacao'].max()
}).reset_index()

# Calculando a Recência em dias
rfm['Recencia_Dias'] = (data_analise - rfm['Ultima_Compra']).dt.days

print("--- Modelo RFM Consolidado ---")
print(rfm[['Cliente_ID', 'Recencia_Dias', 'Frequencia', 'Valor_Monetario']])
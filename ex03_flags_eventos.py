import pandas as pd

df = pd.DataFrame({
    'Transacao_ID': [1, 2, 3],
    'Data': pd.to_datetime(['2026-05-10', '2026-11-27', '2026-12-25']),
    'Valor': [150, 2000, 3500]
})

df['Mes'] = df['Data'].dt.month
df['Dia'] = df['Data'].dt.day

# Mapeando eventos (Ex: Natal no dia 25/12 e simulação de Black Friday em 27/11)
is_natal = (df['Mes'] == 12) & (df['Dia'] == 25)
is_black_friday = (df['Mes'] == 11) & (df['Dia'] == 27)

df['Flag_Evento_Comercial'] = (is_natal | is_black_friday).astype(int)

print("--- Identificação de Picos Sazonais ---")
print(df[['Data', 'Valor', 'Flag_Evento_Comercial']])
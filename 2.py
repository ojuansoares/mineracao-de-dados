import pandas as pd

dados = {
    'Pedido': [101, 102, 103],
    'Data_Compra': ['2026-03-01', '2026-03-05', '2026-03-10'],
    'Data_Entrega': ['2026-03-04', '2026-03-02', '2026-03-12']
}
df = pd.DataFrame(dados)

df['Data_Compra'] = pd.to_datetime(df['Data_Compra'])
df['Data_Entrega'] = pd.to_datetime(df['Data_Entrega'])

erros_data = df[df['Data_Entrega'] < df['Data_Compra']]

print("--- Compras com erro lógico de data ---")
print(erros_data)
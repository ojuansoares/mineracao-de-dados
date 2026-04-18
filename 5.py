import pandas as pd

dados = {
    'Veiculo': ['Carro A', 'Carro B', 'Carro C', 'Carro D'],
    'Placa_Veiculo': ['ABC1234', 'ABC123', 'ABC12345', 'BRA2E19']
}
df = pd.DataFrame(dados)

placas_erradas = df[df['Placa_Veiculo'].str.len() != 7]

print("--- Veículos com tamanho de placa incorreto ---")
print(placas_erradas)
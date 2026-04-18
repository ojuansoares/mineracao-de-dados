import pandas as pd

dados = {
    'Componente': ['Resistor', 'Capacitor', 'LED', 'Transistor'],
    'Quantidade_Estoque': [100, -5, 50.5, 20]
}
df = pd.DataFrame(dados)

falhas_estoque = df[(df['Quantidade_Estoque'] < 0) | (df['Quantidade_Estoque'] % 1 != 0)]

print("--- Componentes com falhas de integridade no estoque ---")
print(falhas_estoque)
import pandas as pd

dados = {
    'Paciente': ['A', 'B', 'C', 'D'],
    'Altura_Metros': [1.75, 170, 0.20, 1.82]
}
df = pd.DataFrame(dados)

fora_do_padrao = df[(df['Altura_Metros'] < 0.50) | (df['Altura_Metros'] > 2.50)]

print("--- Pacientes com alturas fisicamente impossíveis ---")
print(fora_do_padrao)
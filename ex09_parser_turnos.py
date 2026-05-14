import pandas as pd

df = pd.DataFrame({
    'Log_ID': [1, 2, 3, 4],
    'Hora': [3, 11, 16, 21] 
})

# Função para fatiar as horas
def definir_turno(hora):
    if 0 <= hora <= 5:
        return 'Madrugada'
    elif 6 <= hora <= 18:
        return 'Comercial'
    else:
        return 'Noite'

df['Turno'] = df['Hora'].apply(definir_turno)

print("--- Categorização de Comportamento ---")
print(df)
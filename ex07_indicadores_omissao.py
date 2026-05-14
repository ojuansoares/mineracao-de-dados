import pandas as pd

df = pd.DataFrame({
    'Formulario_ID': [1, 2, 3],
    'Telefone': ['9999-1111', None, '8888-2222'],
    'Renda': [3000, 4500, None]
})

# Criando a Flag de erro/omissão ANTES de preencher
df['Omitiu_Telefone'] = df['Telefone'].isnull().astype(int)
df['Omitiu_Renda'] = df['Renda'].isnull().astype(int)

# Realizando a limpeza/preenchimento em seguida
df['Telefone'] = df['Telefone'].fillna('Nao Informado')
df['Renda'] = df['Renda'].fillna(df['Renda'].mean())

print("--- Tratamento de Nulos com Flags ---")
print(df)
import pandas as pd

df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Email': ['joao@gmail.com', 'vendas@sualoja.com.br', 'maria@yahoo.com']
})

print("--- Dados Brutos ---")
print(df, "\n")

# Extraindo o domínio
df['Dominio'] = df['Email'].str.split('@').str[1]

# Criando a Flag para identificar infraestrutura empresarial
df['Flag_Empresarial'] = df['Dominio'].str.contains('.com.br').astype(int)

print("--- Após Engenharia de Texto ---")
print(df)
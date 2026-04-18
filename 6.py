import pandas as pd

dados = {
    'Aluno': ['João', 'Maria', 'José'],
    'Ano Nascimento': [2010, 2005, 2010],
    'Idade_Declarada': [16, 21, 10]
}
df = pd.DataFrame(dados)

ano_atual = 2026
df['Idade_Real'] = ano_atual - df['Ano Nascimento']
contradicoes = df[df['Idade_Real'] != df['Idade_Declarada']]

print("--- Alunos com informações contraditórias ---")
print(contradicoes)
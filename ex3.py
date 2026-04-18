import pandas as pd
from scipy.stats import zscore

vendas = [1200, 1350, 1250, 1300, 13500, 1280]
df = pd.DataFrame({'vendas': vendas})

df['z_score'] = zscore(df['vendas'])

dados_limpos = df[df['z_score'].abs() <= 3]

print(dados_limpos)
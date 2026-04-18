import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Edu'],
    'Idade': [25, np.nan, 30, 22, np.nan],
    'Telefone': ['1111', '2222', np.nan, '4444', np.nan]
}
df = pd.DataFrame(dados)
print("--- Dados Originais ---")
print(df, "\n")

sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title("Mapa de Valores Ausentes (Amarelo = Faltando)")
plt.show()
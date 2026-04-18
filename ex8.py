import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.DataFrame({
    'idade': [18, 20, 19, 21, 22, 150],
    'estudo': [10, 15, 12, 14, 10, 2],
    'nota': [7, 8, 8, 9, 7, 10]
})

floresta = IsolationForest(random_state=42)
df['Outlier'] = floresta.fit_predict(df)

anomalia = df[df['Outlier'] == -1]

print(anomalia)
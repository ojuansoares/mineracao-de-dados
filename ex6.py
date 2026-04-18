import numpy as np
from sklearn.ensemble import IsolationForest

normais = np.random.normal(loc=10, scale=2, size=(1000, 2))
absurdos = np.random.normal(loc=50, scale=5, size=(50, 2))
dados = np.vstack([normais, absurdos])

floresta_5 = IsolationForest(contamination=0.05, random_state=42)
floresta_20 = IsolationForest(contamination=0.20, random_state=42)

res_5 = floresta_5.fit_predict(dados)
res_20 = floresta_20.fit_predict(dados)

anomalias_5 = list(res_5).count(-1)
anomalias_20 = list(res_20).count(-1)

print(anomalias_5)
print(anomalias_20)
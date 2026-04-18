import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

producao = [100, 102, 98, 105, 500, 101]
z_scores = zscore(producao)

limpos = []
for i in range(len(producao)):
    if abs(z_scores[i]) < 3:
        limpos.append([producao[i]])

scala = MinMaxScaler(feature_range=(0, 1))
resultado = scala.fit_transform(limpos)

print(resultado)
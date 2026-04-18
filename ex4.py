import numpy as np
from scipy.stats import zscore

medidas = [10, 12, 11, 10, 10000]

z_scores = zscore(medidas)
media = np.mean(medidas)
desvio = np.std(medidas)

print(z_scores[-1])
print(media)
print(desvio)
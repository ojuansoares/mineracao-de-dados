import numpy as np
from scipy.stats import zscore

temp = [45.5, 46.0, 45.2, 45.8, 46.1, 98.0, 45.9, 45.3]
z_scores = zscore(temp)

for i in range(len(temp)):
    if z_scores[i] > 2.5:
        print(temp[i])
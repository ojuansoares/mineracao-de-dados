from scipy.stats import zscore

voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]
z_scores = zscore(voltagem)

for z in z_scores:
    if z < -2.0:
        print("Falha de Energia!")
        break
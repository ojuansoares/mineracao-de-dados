import numpy as np

tempos = [20, 25, 30, 35, 40, 45, 90]

q1 = np.percentile(tempos, 25)
q2 = np.percentile(tempos, 50)
q3 = np.percentile(tempos, 75)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers_np = [
    valor for valor in sorted(tempos) if valor < limite_inferior or valor > limite_superior
]

print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")
print(f"Outliers (NumPy) = {outliers_np}")

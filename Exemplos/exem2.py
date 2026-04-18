import numpy as np

notas = [5.0, 6.0, 7.0, 8.0, 9.0]

q1, q2, q3 = np.percentile(notas, [25, 50, 75])
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers = [
	valor for valor in sorted(notas) if valor < limite_inferior or valor > limite_superior
]

print(f"Notas = {notas}")
print(f"Q1 = {q1}")
print(f"Q2 (Mediana) = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")
print(f"Outliers = {outliers}")

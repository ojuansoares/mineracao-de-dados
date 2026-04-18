import statistics

tempos = [20, 25, 30, 35, 40, 45, 90]

q2 = statistics.median(tempos)

inferior = tempos[:3]
superior = tempos[4:]

q1 = statistics.median(inferior)
q3 = statistics.median(superior)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Inferior = {inferior}")
print(f"Superior = {superior}")
print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")


####
# 1 - Verificar se no conjunto existe algum outlier (< -5 ou > 75)

outliers = []
for tempo in tempos:
    if tempo < limite_inferior or tempo > limite_superior:
        outliers.append(tempo)
print(f"Outliers: {outliers}")

###
# 2 - Alterar a verificação do conjunto para tornar genérico (para qualquer
# tamanho)
# Exemplo_01_2

def verificar_outliers_iqr(valores):
    ordenados = sorted(valores)
    n = len(ordenados)
    if n < 2:
        raise ValueError("A lista precisa ter pelo menos 2 valores")

    q2 = statistics.median(ordenados)
    meio = n // 2

    if n % 2 == 0:
        inferior = ordenados[:meio]
        superior = ordenados[meio:]
    else:
        inferior = ordenados[:meio]
        superior = ordenados[meio + 1 :]

    q1 = statistics.median(inferior)
    q3 = statistics.median(superior)

    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    outliers = [
        valor
        for valor in ordenados
        if valor < limite_inferior or valor > limite_superior
    ]

    return {
        "ordenados": ordenados,
        "inferior": inferior,
        "superior": superior,
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "iqr": iqr,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "outliers": outliers,
    }


resultado = verificar_outliers_iqr(tempos)
print("\n--- Exemplo_01_2 (generico) ---")
print(f"Inferior = {resultado['inferior']}")
print(f"Superior = {resultado['superior']}")
print(f"Q1 = {resultado['q1']}")
print(f"Q2 = {resultado['q2']}")
print(f"Q3 = {resultado['q3']}")
print(f"IQR = {resultado['iqr']}")
print(f"Limite Inferior = {resultado['limite_inferior']}")
print(f"Limite Superior = {resultado['limite_superior']}")
print(f"Outliers = {resultado['outliers']}")

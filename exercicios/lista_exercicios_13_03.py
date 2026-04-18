import numpy as np
import pandas as pd


def detectar_anomalias(dados, multiplicador=1.5):
    arr = np.array(dados, dtype=float)
    q1 = np.percentile(arr, 25)
    q3 = np.percentile(arr, 75)
    iqr = q3 - q1
    limite_inferior = q1 - multiplicador * iqr
    limite_superior = q3 + multiplicador * iqr
    return [valor for valor in arr.tolist() if valor < limite_inferior or valor > limite_superior]


def exercicio_1_e_2():
    print("\n=== EXERCICIOS 1 e 2 ===")
    tempos = np.array([12, 15, 14, 13, 16, 12, 14, 150, 13, 15], dtype=float)

    p25 = np.percentile(tempos, 25)
    p50 = np.percentile(tempos, 50)
    p75 = np.percentile(tempos, 75)

    print(f"P25: {p25}")
    print(f"P50: {p50}")
    print(f"P75: {p75}")

    iqr = p75 - p25
    limite_inferior = p25 - 1.5 * iqr
    limite_superior = p75 + 1.5 * iqr

    print(f"IQR: {iqr}")
    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")


def exercicio_3():
    print("\n=== EXERCICIO 3 ===")
    dados = sorted([100, 150, 200, 250, 300, 350])

    n = len(dados)
    metade = n // 2

    if n % 2 == 0:
        metade_inferior = dados[:metade]
        metade_superior = dados[metade:]
    else:
        metade_inferior = dados[:metade]
        metade_superior = dados[metade + 1 :]

    q1 = (metade_inferior[len(metade_inferior) // 2 - 1] + metade_inferior[len(metade_inferior) // 2]) / 2
    q3 = (metade_superior[len(metade_superior) // 2 - 1] + metade_superior[len(metade_superior) // 2]) / 2

    print(f"Dados: {dados}")
    print(f"Metade inferior: {metade_inferior}")
    print(f"Metade superior: {metade_superior}")
    print(f"Q1 manual: {q1}")
    print(f"Q3 manual: {q3}")


def exercicio_4():
    print("\n=== EXERCICIO 4 ===")
    tensoes = np.array([110, 115, 120, 118, 112, 220, 116, 114, 119, 12], dtype=float)

    q1 = np.percentile(tensoes, 25)
    q3 = np.percentile(tensoes, 75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    anomalias = [v for v in tensoes.tolist() if v < limite_inferior or v > limite_superior]

    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")
    print(f"Valores anomalos: {anomalias}")


def exercicio_5_e_6():
    print("\n=== EXERCICIOS 5 e 6 ===")
    vetor_teste = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]
    outliers = detectar_anomalias(vetor_teste, multiplicador=1.5)
    print(f"Vetor teste: {vetor_teste}")
    print(f"Outliers detectados: {outliers}")


def exercicio_7_e_8():
    print("\n=== EXERCICIOS 7 e 8 ===")
    dados_maquina = {
        "ID_Maquina": [1, 2, 3, 4, 5],
        "Uso_Memoria_MB": [2048, 2100, 2050, 8192, 2080],
    }
    df = pd.DataFrame(dados_maquina)

    q1 = df["Uso_Memoria_MB"].quantile(0.25)
    q3 = df["Uso_Memoria_MB"].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    df_normal = df[
        (df["Uso_Memoria_MB"] >= limite_inferior)
        & (df["Uso_Memoria_MB"] <= limite_superior)
    ]

    print("DataFrame original:")
    print(df)
    print(f"Q1: {q1} | Q3: {q3} | IQR: {iqr}")
    print(f"Limites: [{limite_inferior}, {limite_superior}]")
    print("DataFrame sem anomalias:")
    print(df_normal)


def exercicio_9():
    print("\n=== EXERCICIO 9 ===")
    df_temp = pd.DataFrame({"temperaturas": [80, 82, 85, 81, 300, 83]})

    q1 = df_temp["temperaturas"].quantile(0.25)
    q2 = df_temp["temperaturas"].quantile(0.50)
    q3 = df_temp["temperaturas"].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    df_temp["temperaturas_ajustada"] = np.where(
        (df_temp["temperaturas"] < limite_inferior)
        | (df_temp["temperaturas"] > limite_superior),
        q2,
        df_temp["temperaturas"],
    )

    print(df_temp)


def exercicio_10():
    print("\n=== EXERCICIO 10 ===")
    df = pd.DataFrame(
        {
            "Sensor_ID": ["A", "A", "A", "B", "B", "B", "A", "B"],
            "Valor_Leitura": [10, 11, 12, 20, 21, 100, 13, 22],
        }
    )

    def marcar_anomalias_grupo(grupo):
        q1 = grupo["Valor_Leitura"].quantile(0.25)
        q3 = grupo["Valor_Leitura"].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        grupo = grupo.copy()
        grupo["Anomalia"] = (grupo["Valor_Leitura"] < limite_inferior) | (
            grupo["Valor_Leitura"] > limite_superior
        )
        return grupo

    df_resultado = df.groupby("Sensor_ID", group_keys=False).apply(marcar_anomalias_grupo)
    print(df_resultado)


def exercicio_11_e_12(caminho_entrada="dados_sensores.csv", caminho_saida="dados_validados.csv"):
    print("\n=== EXERCICIOS 11 e 12 ===")
    df = pd.read_csv(caminho_entrada)

    print("Quantidade de NaN por coluna:")
    print(df.isna().sum())

    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    for col in colunas_numericas:
        mediana = df[col].median()
        df[col] = df[col].fillna(mediana)

    print("\nQuantidade de NaN apos preenchimento:")
    print(df.isna().sum())

    q1_temp = df["temperatura_celsius"].quantile(0.25)
    q3_temp = df["temperatura_celsius"].quantile(0.75)
    iqr_temp = q3_temp - q1_temp
    li_temp = q1_temp - 1.5 * iqr_temp
    ls_temp = q3_temp + 1.5 * iqr_temp

    q1_press = df["pressao_psi"].quantile(0.25)
    q3_press = df["pressao_psi"].quantile(0.75)
    iqr_press = q3_press - q1_press
    li_press = q1_press - 1.5 * iqr_press
    ls_press = q3_press + 1.5 * iqr_press

    mascara_normal = (
        (df["temperatura_celsius"] >= li_temp)
        & (df["temperatura_celsius"] <= ls_temp)
        & (df["pressao_psi"] >= li_press)
        & (df["pressao_psi"] <= ls_press)
    )

    df_validado = df[mascara_normal].copy()
    df_validado.to_csv(caminho_saida, index=False)

    print(f"\nLimites temperatura: [{li_temp}, {ls_temp}]")
    print(f"Limites pressao: [{li_press}, {ls_press}]")
    print(f"Linhas originais: {len(df)}")
    print(f"Linhas validadas: {len(df_validado)}")
    print(f"Arquivo exportado: {caminho_saida}")


def main():
    exercicio_1_e_2()
    exercicio_3()
    exercicio_4()
    exercicio_5_e_6()
    exercicio_7_e_8()
    exercicio_9()
    exercicio_10()
    exercicio_11_e_12()


if __name__ == "__main__":
    main()

from sklearn.ensemble import IsolationForest

dados = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

floresta = IsolationForest(random_state=42)
resultado = floresta.fit_predict(dados)

print(resultado)
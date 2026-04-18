from sklearn.ensemble import IsolationForest

servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

floresta = IsolationForest(random_state=42)
resultado = floresta.fit_predict(servidores)

print(resultado)
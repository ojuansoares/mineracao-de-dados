from sklearn.preprocessing import MinMaxScaler

temps = [[-20], [-10], [0], [20]]

scala = MinMaxScaler()
resultado = scala.fit_transform(temps)

print(resultado)
from sklearn.preprocessing import MinMaxScaler

pressao = [[100], [200], [500]]

scala = MinMaxScaler(feature_range=(0, 1))
resultado = scala.fit_transform(pressao)

print(resultado)
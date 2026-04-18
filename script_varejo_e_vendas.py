import pandas as pd

data_clientes = {
    'id_cliente': [1, 2, 3, 4, 5],
    'nome_cliente': ['Ana Silva', 'Bruno Souza', 'Carla Dias', 'Diego Ramos', 'Elena Luz'],
    'estado': ['SP', 'RJ', 'MG', 'SP', 'SC']
}
df_clientes = pd.DataFrame(data_clientes)

data_produtos = {
    'id_produto': [101, 102, 103, 104],
    'nome_produto': ['SSD 500GB', 'Memória RAM 16GB', 'Placa de Vídeo RTX', 'Processador i7'],
    'preco': [300, 450, 2500, 1800]
}
df_produtos = pd.DataFrame(data_produtos)

data_vendas = {
    'id_venda': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    'id_cliente': [1, 2, 1, 3, 4, 5, 2],
    'id_produto': [101, 102, 103, 101, 104, 101, 103],
    'quantidade': [2, 1, 1, 3, 1, 2, 1]
}
df_vendas = pd.DataFrame(data_vendas)
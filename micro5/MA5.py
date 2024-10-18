import pandas as pd

import sys

arquivo_csv = 'dados.csv'
 
sys.stdout.reconfigure(encoding='utf-8')
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')


pd.set_option('display.max_rows', 9999)

# Imprimir informações gerais sobre o conjunto de dados
print("Informações gerais sobre o conjunto de dados:")
dados.info()

# Calcular e exibir o número de linhas e colunas
total_linhas, total_colunas = dados.shape
print(f"\nTotal de linhas: {total_linhas}")
print(f"Total de colunas: {total_colunas}")

# Exibir a quantidade de dados nulos em cada coluna
print("\nQuantidade de dados nulos em cada coluna:")
print(dados.isnull().sum())

# Imprimir o tipo de dados de cada coluna
print("\nTipos de dados de cada coluna:")
print(dados.dtypes)

# Exibir a quantidade de memória utilizada pelo conjunto de dados
memoria_utilizada = dados.memory_usage(deep=True).sum()
print(f"\nQuantidade de memória utilizada: {memoria_utilizada} bytes")




import pandas as pd

import sys

arquivo_csv = 'dados.csv'
 
sys.stdout.reconfigure(encoding='utf-8')
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')


pd.set_option('display.max_rows', 9999)
# Imprimir o conjunto de dados original completo
#print("Conjunto de dados original:")
#print(dados.to_string())


# Imprimir as primeiras 10 linhas do DataFrame
print("Primeiras 10 linhas do conjunto de dados:")
print(dados.head(10).to_string())

# Imprimir as últimas 10 linhas do DataFrame
print("\nÚltimas 10 linhas do conjunto de dados:")
print(dados.tail(10).to_string())




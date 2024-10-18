import pandas as pd

import sys

arquivo_csv = 'dados.csv'
 
sys.stdout.reconfigure(encoding='utf-8')
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')

# Criar uma nova variável com um subconjunto de colunas
#subconjunto_dados = dados[['Date', 'Pulse', 'Calories']]

# Exibir o subconjunto de dados
#print("Subconjunto de dados com três colunas:")
#print(subconjunto_dados)


pd.set_option('display.max_rows', 9999)
# Imprimir o conjunto de dados original completo
print("Conjunto de dados original:")
print(dados.to_string())


# aki apenas um teste
#pd.set_option('display.max_rows', 10)
#print(dados)





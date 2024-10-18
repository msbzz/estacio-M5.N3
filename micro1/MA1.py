import pandas as pd

import sys

arquivo_csv = 'dados.csv'
 
sys.stdout.reconfigure(encoding='utf-8')
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')

print("Informações gerais sobre o conjunto de dados:")
print(dados.info())

# Exibe o conteúdo completo do DataFrame
print("\nConteúdo completo do arquivo CSV:")
print(dados)
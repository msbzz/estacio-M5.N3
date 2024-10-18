from datetime import datetime
import pandas as pd
import numpy as np
import sys

# 3. Ler o conteúdo do CSV fornecido, especificando separador, engine, e encoding
sys.stdout.reconfigure(encoding='utf-8') 

# 4. Atribua os dados lidos a uma variável;
arquivo_csv = 'dados.csv'
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')

#5 Verifique se os dados foram importados adequadamente:
# b) Imprima as primeiras e últimas N linhas do arquivo.

# Imprimir as primeiras 10 linhas do DataFrame
print("Primeiras 10 linhas do conjunto de dados:")
print(dados.head(10).to_string())

# Imprimir as últimas 10 linhas do DataFrame
print("\nÚltimas 10 linhas do conjunto de dados:")
print(dados.tail(10).to_string())
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
# a) Imprimir as informações gerais sobre o conjunto de dados
print(" 5.a) Informações gerais sobre o conjunto de dados:")
print(dados.info())
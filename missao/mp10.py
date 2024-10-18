from datetime import datetime
import pandas as pd
import numpy as np
import sys

# 3. Ler o conteúdo do CSV fornecido, especificando separador, engine, e encoding
sys.stdout.reconfigure(encoding='utf-8') 

# 4. Atribua os dados lidos a uma variável;
arquivo_csv = 'dados.csv'
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')
 
dados_copia = dados.copy()

calories_copy = dados_copia['Calories']
dados_copia['Calories'] = calories_copy.fillna(0)
 
date_copy = dados_copia['Date']
dados_copia['Date'] = date_copy.fillna('1900/01/01')

 
dados_copia['Date'] = dados_copia['Date'].str.strip()

# Remover aspas simples das datas
dados_copia['Date'] = dados_copia['Date'].str.replace("'", "")

# Corrigir o valor "20201226" para "2020/12/26"
dados_copia['Date'] = dados_copia['Date'].replace('20201226', '2020/12/26')
 
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], errors='coerce')

# 12. Por fim, remova os registros contendo valores nulos. Nesse ponto, apenas a
#     coluna ‘Date’ possui um registro que atende a essa premissa (linha 22). Logo,
#     utilize-a como base para realizar a transformação solicitada;

dados_copia = dados_copia.dropna(subset=['Date'])

# 12. Imprima o dataframe e verifique se todas as transformações foram
#     executadas conforme solicitado nos passos anteriores.

print(dados_copia)


# Aqui foi feita uma adaptção das aspas e o resultado esperado ocorreu 
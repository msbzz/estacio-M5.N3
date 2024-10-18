from datetime import datetime
import pandas as pd
import numpy as np
import sys

# 3. Ler o conteúdo do CSV fornecido, especificando separador, engine, e encoding
sys.stdout.reconfigure(encoding='utf-8') 

# 4. Atribua os dados lidos a uma variável;
arquivo_csv = 'dados.csv'
dados = pd.read_csv(arquivo_csv, sep=';', engine='python', encoding='utf-8')

 # 6 .Crie uma nova variável e atribua a ela uma cópia do conjunto de dados
 #    original (variável criada no passo 4);
dados_copia = dados.copy()

# 7. Na nova variável:
# a) Substituir todos os valores nulos da coluna 'Calories' por 0, sem encadeamento
calories_copy = dados_copia['Calories']
dados_copia['Calories'] = calories_copy.fillna(0)

# 8. Ainda na nova variável:
# a) Substituir os valores nulos da coluna 'Date' por '1900/01/01'
date_copy = dados_copia['Date']
dados_copia['Date'] = date_copy.fillna('1900/01/01')

# c) Transforme os dados da coluna ‘Date’ em datetime usando o método
# ‘to_datetime’;

dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], format='%Y/%m/%d', errors='coerce')

print(dados_copia)

## Com a aplicação da mascara 'format', nenhuma data foi reconhecida

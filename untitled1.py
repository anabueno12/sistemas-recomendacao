# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dl033zEuvcMUCk8jjq60u_f2_-UHEkyJ
"""

#importando as bibliotecas necessarias
import numpy as np
from sklearn.cluster import KMeans

import pandas as pd
# 1° Passo: Especificar o caminho do arquivo 

caminho_arquivo = '/content/filmes_100_usuarios.csv'

#2° Passo: Ler o CSV usando pandas
df = pd.read_csv(caminho_arquivo)

# Exibir o cabeçalho do arquivo para verificar se foi lido corretamente
print(df.head())

                 
#Matriz de filmes assistidos
mv_rating  = df.drop(columns=["Unnamed: 0"]).values

#definindo numeros de cluster(grupos)
num_cluster = 2

#inicializar modelo
kmeans = KMeans(n_clusters=num_cluster, random_state=0, n_init=10)

#treinar modelo
kmeans.fit(filmes_assistidos)

#classificando os usuários
grupos_indice = kmeans.predict(filmes_assistidos)

#exibir os dados
print("Usuário pertece ao seguinte grupo:")

for i, cluster in enumerate(grupos_indice):
  print(f"usuario {i+1} pertence ao grupo {cluster+1}")

print("\nFilmes assistidos:")
for i in range(len(filmes_assistidos)):
  assistidos = np.where(filmes_assistidos[i] == 1)[0] + 1
  print(f"usuario {i+1} assistiu aos filmes: {assistidos}")

#função que recomenda filmes
def recomendar_filme(filmes, filmes_assistidos, grupos_indice):
  filmes = np.array(filmes)

  #encontrar o grupo do usuário com base em seu vetor de filmes assistidos
  usuario_id = len(filmes_assistidos)
  grupo_usuario = kmeans.predict ([filmes])[0]

  #encontrar todos os usuarios
  usuarios_no_mesmo_grupo = [i for i in range(len(grupos_indice)) if grupos_indice[i] == grupo_usuario]

  #filmes assistidos pelos usuarios no mesmo grupo
  filmes_recomendados = set()
  for usuario in usuarios_no_mesmo_grupo:
    filmes_assistidos_usuarios = np.where(filmes_assistidos[usuario] == 1)[0]
    filmes_recomendados.update(filmes_assistidos_usuarios)

  #remover filmes que o usuario ja assistiu
  filmes_recomendados = filmes_recomendados - set(np.where(filmes == 1)[0])

  #ajustar os índices dos filmes recomendados (de volta para 1-based)
  filmes_recomendados = [filme + 1 for filme in filmes_recomendados]

  return sorted(filmes_recomendados)

#exemplo de uso da função recomendar_filmes
filmes_assistidos_usuario = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0] #vetor de filme
#assistidos (por exemplo, assistiu aos filmes 1 e 3)
filmes_recomendados = recomendar_filme(filmes_assistidos_usuario, filmes_assistidos, grupos_indice)

print (f"\nFilmes recomendados: {filmes_recomendados}")
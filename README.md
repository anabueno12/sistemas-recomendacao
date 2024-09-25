Sistema de Recomendação de Filmes com K-Means

O que é e para que serve
No mundo atual, a quantidade de opções de filmes disponíveis é imensa. Para ajudar os espectadores a encontrar novas obras que possam gostar, desenvolvemos um sistema de recomendação de filmes. Este sistema utiliza o algoritmo de agrupamento K-Means para classificar usuários com base nos filmes que assistiram e, assim, sugerir filmes que eles ainda não viram, mas que são populares entre usuários com gostos semelhantes.

Objetivo do Projeto
O principal objetivo deste projeto é criar um modelo que agrupe usuários com base nos filmes que assistiram. Ao identificar padrões de gosto, podemos recomendar novos filmes que ainda não foram assistidos, mas que têm alta probabilidade de agradar. Esse tipo de sistema é fundamental em plataformas de streaming, onde a personalização da experiência do usuário pode aumentar a satisfação e o engajamento.

Algoritmo Utilizado
K-Means
O algoritmo K-Means é uma técnica de aprendizado não supervisionado amplamente utilizada para agrupamento de dados. A ideia básica do K-Means é dividir um conjunto de n observações em k grupos, onde cada observação pertence ao grupo com a média mais próxima.

Funcionamento
Definição da Matriz de Dados: A matriz de filmes assistidos é representada onde cada linha corresponde a um usuário e cada coluna a um filme. O valor 1 indica que o usuário assistiu ao filme, enquanto 0 indica que não assistiu.

Inicialização do Modelo: Definimos o número de grupos (clusters) que desejamos identificar. Neste caso, optamos por 2 grupos.

Treinamento do Modelo: Utilizamos a matriz de filmes assistidos para treinar o modelo K-Means. Após o treinamento, o modelo classifica os usuários em grupos.

Classificação dos Usuários: Através do modelo treinado, cada usuário é classificado em um dos grupos, permitindo a identificação de padrões de gosto.

Recomendação de Filmes: Para recomendar filmes, o sistema verifica a lista de filmes assistidos pelos usuários no mesmo grupo e sugere aqueles que ainda não foram assistidos pelo usuário em questão.

Implementação
A implementação do sistema é feita em Python, utilizando a biblioteca NumPy para manipulação de arrays e a biblioteca Scikit-learn para a aplicação do algoritmo K-Means. 

Copiar código
Ir no CMD e colocar git clone e copiar o código
 Matriz com os filmes assistidos
filmes_assistidos = np.array([
     [1, 0, 0, 1, 1],
     [1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1],
     [0, 0, 1, 1, 0],
     [1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0]
])

 Definindo o número de clusters
num_cluster = 2

 Inicializando e treinando o modelo
kmeans = KMeans(n_clusters=num_cluster, random_state=0, n_init=10)
kmeans.fit(filmes_assistidos)

 Classificando os usuários
grupos_indice = kmeans.predict(filmes_assistidos)

Função de recomendação
def recomendar_filme(filmes, filmes_assistidos, grupos_indice):
  Lógica para encontrar filmes recomendados pass

Exemplo de uso
filmes_assistidos_usuario = [1, 0, 1, 0]
filmes_recomendados = recomendar_filme(filmes_assistidos_usuario, filmes_assistidos, grupos_indice)
Resultados
Após a execução do código, o sistema classifica cada usuário em um grupo e recomenda filmes com base nos interesses comuns. Os resultados mostram como a técnica de agrupamento pode ser eficaz na personalização das recomendações.

Conclusão
Este projeto demonstra como o K-Means pode ser aplicado para criar um sistema de recomendação de filmes. Ao agrupar usuários com gostos semelhantes, conseguimos oferecer sugestões que têm mais chances de agradar. Essa abordagem não só melhora a experiência do usuário, mas também aumenta o tempo que eles passam na plataforma, potencialmente elevando a satisfação e a lealdade.

PASSO A PASSO
1. Preparação dos Dados
Definir o Conjunto de Dados: Crie uma matriz onde cada linha representa um objeto (neste caso, um usuário) e cada coluna representa uma característica (neste caso, filmes assistidos).

Exemplo:

python
Copiar código
import numpy as np

filmes_assistidos = np.array([
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
])
2. Escolher o Número de Clusters (K)
Decidir quantos clusters você deseja: Esse número deve ser definido antes da execução do algoritmo. É comum fazer testes com diferentes valores de K para ver qual gera os melhores resultados.

python
Copiar código
num_cluster = 2  # Definindo o número de clusters
3. Inicializar Centróides
Selecionar os centróides iniciais: O algoritmo escolhe K pontos aleatórios do conjunto de dados como centróides iniciais.

python
Copiar código
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=num_cluster, random_state=0)
4. Atribuir Cada Ponto ao Cluster Mais Próximo
Calcular a distância: Para cada ponto de dados, calcule a distância até cada centróide e atribua o ponto ao cluster correspondente ao centróide mais próximo.

python
Copiar código
kmeans.fit(filmes_assistidos)
grupos_indice = kmeans.predict(filmes_assistidos)
5. Atualizar os Centróides
Recalcular os centróides: Após a atribuição, os centróides são recalculados como a média dos pontos atribuídos a cada cluster.
6. Repetir o Processo
Iterar até a convergência: O processo de atribuição e atualização dos centróides é repetido até que os centróides não mudem mais ou até que um número máximo de iterações seja alcançado.
7. Analisar os Resultados
Exibir os clusters: Após a convergência, você pode analisar a qual cluster cada ponto pertence.

python
Copiar código
print("Usuário pertence ao seguinte grupo:")
for i, cluster in enumerate(grupos_indice):
    print(f"Usuário {i + 1} pertence ao grupo {cluster + 1}")
Conclusão
O K-Means é um método poderoso para agrupamento e pode ser utilizado em diversas aplicações, incluindo sistemas de recomendação. Ao seguir esses passos, você pode implementar o K-Means para classificar usuários com base em suas preferências de filmes.

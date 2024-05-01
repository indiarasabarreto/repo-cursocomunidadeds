# Recapitulando o problema de negócio:

# 1.1. As perguntas do CEO:

    # Quais são as categorias de imóveis que estão cadastradas dentro da base de dados da cidade de Nova York?

    # Quantos usuários (Hosts) únicos cadastrados existem dentro da base de dados da cidade de Nova York?

    # Como é a variação do preços dos imóveis em NY?

    # Existem mais imóveis baratos ou caros?

    # Qual a distribuição do número de Reviews? Existem imóveis com muitos e outro com poucos reviews?
    
# RESOLUÇÃO:

# 2.1. Planejamento do Processo:

    # Quais são os passos para encontrar as respostas?

    # Contar todos os nomes distintos que aparecem na coluna “room_type”.

    # Contar os cadastros únicos da coluna “host_id”.

    # Calcular o desvio padrão em torno da média de preços dos imóveis.

    # Desenhar um histograma para mostrar o número de apartamentos dentro da faixa do valor do aluguel.

    # Desenhar um histograma para mostrar o número de apartamentos dentro de uma faixa de avaliação.


# 2.2 Comando para ler uma planilha de dados:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\guerr\python-ds\AB_NYC_2019.csv')
#print(data.head(5))

# 1. Quais são as categorias de imóveis que estão cadastradas dentro da base de dados da cidade de Nova York?
    # Selecionar a coluna room_type
    # Contagem única dos valores

room_type = data.loc[:, 'room_type']

print(np.unique(room_type))


# 2. Quantos usuários (Hosts) únicos cadastrados existem dentro da base de dados da cidade de Nova York?

data.loc[:, 'host_id']

    # seleção de colunas e linhas
host_id = data.loc[:, 'host_id']

    # separação de valres únicos
host_id_unique = np.unique(host_id)

    # contagem dos valores únicos
print(len(host_id_unique))


# 3. Como é a variação do preços dos imóveis em NY?
price = data.loc[:, 'price']

print('A média dos preços: {}'.format(np.mean(price)))
print('O STD: {}'.format(np.std(price)))


# 4. Existem mais imóveis baratos ou caros?
    #selecionar linhas e colunas
linhas = data.loc[:, 'price'] < 1100
price = data.loc[linhas, 'price']

    # maior valor de aluguel
print('O maior valor de aluguel: {}'.format(np.max(price)))

    #desenhar histograma
    #bins (numero de colunas) = (1200 - 0) / 100); = 12
print(plt.hist(price, bins=11))


# 5. Qual a distribuição do número de Reviews? Existem imóveis com muitos e outro com poucos reviews?

    #selecionar linhas e colunas
linhas = data.loc[:, 'number_of_reviews'] < 300
reviews = data.loc[linhas, 'number_of_reviews']

#desenhar histograma
print(plt.hist(reviews))
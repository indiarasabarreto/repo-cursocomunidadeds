# 1. Qual é o intervalo de variação do preço dos alugueis dos imóveis?
import pandas as pd
import numpy as np
import statistics
from matplotlib import pyplot as plt

data = pd.read_csv(r'C:\Users\guerr\python-ds\AB_NYC_2019.csv')

colunas = 'price'
media = data.loc[:, colunas].mean()
desvio_padrao = data.loc[:, colunas].std()

print('O preço médio é U${:.2f} +/- U${:.2f}'.format(media, desvio_padrao))


# 2. Qual a distribuição dos imóveis de acordo com o número mínimo de pernoites que podem ser agendado?
colunas = 'minimum_nights'
linhas = data.loc[:, colunas] < 100
data_plot = data.loc[linhas, colunas]

print(plt.hist(data_plot, bins=20))


# 3. Qual a média e a mediana de imóveis cadastrado por host (dono do imóvel)?
colunas = 'calculated_host_listings_count'

media = data.loc[:, colunas].mean()
median = data.loc[:, colunas].median()

print('A média de imóveis cadastrados é {:.2f}'.format(media))
print('A mediana de imóveis cadastrados é {:.2f}'.format(median))


# 4. Como você interpretaria o seguinte histograma?
colunas = 'reviews_per_month'

linhas = data.loc[:, 'reviews_per_month'] < 10
data_plot = data.loc[linhas, colunas]

print(plt.hist(data_plot, bins=10))
print(plt.title('Número de Avaliações por Mês'))
print(plt.xlabel('Quantidade de Avaliações'))
print(plt.ylabel('Quantidade de Imóveis'))


# 5. Qual a data mais recente da última avaliação?
colunas = 'last_review'

avaliacoes = data.loc[:, colunas].sort_values(ascending=True)
data_recente = avaliacoes.loc[317]

print('A data mais recente das avaliações é: {}'.format(data_recente))


# 6. Qual valor máximo de pernoites agendadas?
colunas = 'minimum_nights'

maximo_pernoite = data.loc[:, colunas].max()

print('O valor máximo de pernoite é de {}'.format(maximo_pernoite))


# 7. Como você interpretria o seguiinte valor do desvio padrão?
    # Preço médio da concorrência é de U$180 +/- U$20
print('Preço médio da concorrência é de U${} +/- U${}'.format(180, 20))



# 8. Quantos nomes de donos de imóveis são únicos?
colunas = 'host_id'

hosts = data.loc[:, colunas]
host_id_unicos = len(np.unique(hosts))

print('O número de hosts únicos: {}'.format(host_id_unicos))


# 9. Como você interpretaria o seguinte histograma:
colunas = 'latitude'
data_plot = data.loc[:, colunas]

print(plt.hist(data_plot, bins=16))
print(plt.title('Posição geográfica dos imóveis'))
print(plt.xlabel('Valor da Latitude'))
print(plt.ylabel('Quantidade de imóveis'))



# 10. Quantos identificadores únicos existem na base de dados?
colunas = 'id'

id = data.loc[:, colunas]
id_unicos = len(np.unique(id))

print('O número de IDs únicos: {}'.format(id_unicos))


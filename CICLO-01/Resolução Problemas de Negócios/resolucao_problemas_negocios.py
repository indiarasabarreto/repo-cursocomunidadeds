import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\guerr\python-ds\CICLO-01\Resolução Problemas de Negócios\AB_NYC_2019.csv')
#print(data.head(5))

# 1. Calcular a média de todos os valores de aluguel da cidade de Nova Iorque:
    # colunas que mostra o aluguel
    # calcular a média dessa coluna

preco_aluguel = data.loc[:, 'price']
print(np.mean(preco_aluguel))


# 2. Contar todos os nomes distintos que aparecem na coluna região:
    # Selecionar a coluna região
    # Mostrar apenas os nomes não repetidos (únicos)

regiao = data.loc[:, 'neighbourhood_group']
print(pd.unique(regiao))


# 3. Encontrar o valor máximo da coluna que contém os valores dos aluguéis:
    # Selecionar colunas alugueis
    # Encontrar o valor máximo dessa coluna

preco_aluguel = data.loc[:, 'price']
print(np.max(preco_aluguel))


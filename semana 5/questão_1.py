# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:21:16 2021

@author: rafav
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import cross_validate
import matplotlib.pyplot as plt
import scipy.stats

#lendo o arquivo, separando os campos, atribuindo nomes as colunas e pegando o x e y
data = pd.read_csv('Skin_NonSkin.txt',delimiter= '\s+', header=None,names=["a", "b", "c","y"])
data.columns.tolist()
y = y = data['y']
X = data.iloc[:,:3]


scores_list= []

#iniciando o classificador 
knn = KNeighborsClassifier(n_neighbors=1)

#cross valdidation 100 fold usando o knn e retornado accuracia,precisão, e medida F em forma de dicionário
cross_val = cross_validate (knn, X, y, cv=100, return_train_score=(False), scoring=['accuracy','precision','f1'])

#pegando a lista das médias F, o minimo ,maximo e a media delas 
test_f1 =cross_val['test_f1']
minimo= min(test_f1)
maximo = max(test_f1)
media = np.mean(test_f1)

#plotando o histograma

plt.title('histograma medida-F')
plt.xlabel('valor media-F')
plt.ylabel('Frequência ')
plt.hist(test_f1, 8, rwidth=0.8)
plt.show()

#calculando o intervalode confança
desvio_padrao = np.std(test_f1)
intervalo_conf = scipy.stats.norm.interval(0.95, loc=media, scale=desvio_padrao)    

#letra d: Para dados nunca vistos, pelo intervalo de confiaça obtito(95%). Espero obter ao menos a mergem mínima 0.9917 ou 99,17%
# letra e: Para dados nunca vistos, dado o intervalo de confiança achado. Espero uma medida-F entre 0,9917 e 1, que é o intervalo de confiança
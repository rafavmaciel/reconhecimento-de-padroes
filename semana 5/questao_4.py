# -*- coding: utf-8 -*-
"""
a metodologia utilizada para a questão é a de sobreposição de intervalos de confiança. aplicando um houdout do 10
"""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import scipy.stats  


X,y = load_wine(return_X_y = True) # carregando a base com a ultima coluna

k_range = range(1,11) #houdout
j_range = range(1,16) # k(s)

scores_k_list = []
intervalo_conf_list = []

#calculando as taxas de acerto no houdout para cada k
for j in j_range:
    scores_list= []
    for k in k_range:
        X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = k, stratify=y)
        knn = KNeighborsClassifier(n_neighbors= j, metric='euclidean')
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        scores_list.append(metrics.accuracy_score(y_test,y_pred))
    scores_k_list.append(scores_list)

# calculando o intervalo de cofiança de cada k 
for scores_k in scores_k_list:
    media = np.mean(scores_k)
    desvio_padrao = np.std(scores_k)
    intervalo_conf = scipy.stats.norm.interval(0.95, loc=media, scale=desvio_padrao) 
    intervalo_conf_list.append(intervalo_conf)

# através dos testes de sobreposição de intervalos de confiança, chegamos a conclusão 
# que nenhum classificador possui uma taxa de acerto significativamente maior , pois os intervalos de confiança de todos eles se sobrepoem 
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:31:24 2021

@author: rafav
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp                                                         
import scipy.stats         

X,y = load_iris(return_X_y = True)

iris = load_iris()
X_col_1= iris.data[:,:3]#carregando a base sem a ultima coluna
y_col = iris.target
X_col_2 = iris.data[:,:2]#carregando a base sem as duas ultimas colunas


scores_list= []
scores_list_1= []
scores_list_2= []
k_range = range(1,101)
j_range = range(1,101)

#calculando os scores em um houdout com a base completa
for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = k, stratify=y)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test,y_pred))
#calculando os scores em um houdout com a base sem a ultima coluna    
for j in j_range:
    X_train,X_test,y_train,y_test = train_test_split(X_col_1,y_col, test_size = 0.5, random_state = j, stratify=y)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list_1.append(metrics.accuracy_score(y_test,y_pred))
    
#calculando o intervalo de confiança da taxa de acertos para a base com a ultima coluna
media_tax_ac = np.mean(scores_list)
desvio_padrao_tax_ac = np.std(scores_list)
intervalo_conf_dif_tax_ac = scipy.stats.norm.interval(0.95, loc=media_tax_ac, scale= desvio_padrao_tax_ac) 

#calculando o intervalo de confiança da taxa de acertos para a base sem a ultima coluna
media_tax_ac_1 = np.mean(scores_list_1)
desvio_padrao_tax_ac_1 = np.std(scores_list_1)
intervalo_conf_dif_tax_ac_1 = scipy.stats.norm.interval(0.95, loc=media_tax_ac_1, scale= desvio_padrao_tax_ac_1) 


# pelo teste de sobreposição dos intervalos de confiança , temos que, remover a ultima coluna da base iris 
#não diminui significativamente a taxa de acertos, pois os intervalos se sobrepoem 

k_range = range(1,101)

#calculando os scores em um houdout com a base sem as duas  ultimas colunas    
for j in j_range:
    X_train,X_test,y_train,y_test = train_test_split(X_col_2,y_col, test_size = 0.5, random_state = j, stratify=y)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list_2.append(metrics.accuracy_score(y_test,y_pred))
    
#calculando o intervalo de confiança da taxa de acertos para a base sem as duas ultimas colunas
media_tax_ac_2 = np.mean(scores_list_2)
desvio_padrao_tax_ac_2 = np.std(scores_list_2)
intervalo_conf_dif_tax_ac_2 = scipy.stats.norm.interval(0.95, loc=media_tax_ac_2, scale= desvio_padrao_tax_ac_2) 

#comparando a base completa com ela sem as duas ultimas colunas 
# pelo teste de sobreposição dos intervalos de confiança , temos que, remover as  duas ultimas colunas da base iris 
# diminui significativamente a taxa de acertos, pois os intervalos não se sobrepoem

#logo , o numero máximo de caracteristicas a serem retiradas sem reduzir significantemente a taxa de acertos é 1

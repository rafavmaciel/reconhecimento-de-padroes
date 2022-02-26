# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 08:32:33 2021

@author: rafav
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import scipy.stats
from sklearn.model_selection import train_test_split
from sklearn_extra.cluster import KMedoids
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

X,y = load_iris(return_X_y = True)

lista_acuracia = []


lista_k = [9,18,27,45,72]
list_cent = []
list_y = []
list_score =[]
list_medias = []

# compara cada centroide da lista, com cada elemento da lista treino 
# e acha o valor correpodente ao centroide
# através disso pega o indice e consegue o valor y 

def pegar_y (centroides, X_train, y_train):
    list_centroides=[]
    for i in range(len(centroides)): 
        for k in range(len(X_train)):
            if (centroides [i][0] == X_train[k][0] and centroides [i][1] == X_train[k][1]
            and centroides [i][2] == X_train[k][2] and centroides [i][3] == X_train[k][3]):
                list_centroides.append(y_train[k])
    return list_centroides


# usa o classificador para todos os valores de k pedidos 
# com um houdout de 10 rep
for k in lista_k:
    l_y =[]
    l_c = []
    l_acu =[]
    l_s=[]
    for i in range(10):
        X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = i,stratify=y)
        kmedoids = KMedoids(n_clusters=k, random_state=0)
        kmedoids.fit(X_train,y_train)
        centroides = kmedoids.cluster_centers_
        y_cent = pegar_y(centroides, X_train, y_train)
        #
        knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
        knn.fit(centroides, y_cent[0:k])
        y_pred = knn.predict(X_test)
        l_s.append(metrics.accuracy_score(y_test,y_pred))
        l_y.append(y_cent)
        l_c.append(centroides)
        
       
    #lista_acuracia.append(l_c)
    list_cent.append(l_c)
    list_y.append(l_y)
    list_score.append(l_s)
    list_medias.append(np.mean(l_s))
    
        

                
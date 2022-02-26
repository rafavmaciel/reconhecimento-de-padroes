# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 08:21:31 2021

@author: rafav
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import scipy.stats

X,y = load_iris(return_X_y = True)

lista_media_k = []
lista_desvio_k = []


lista_k = [3,6,9]
for k in lista_k: 
    lista_media = []
    lista_desvio = []
    for i in range(10):
        #iniciando o classificador 
        kmeans = KMeans(n_clusters=k, init="random")
        kmeans.fit(X)
        #armazenando a tabela de agrupamento
        y_maeans = kmeans.labels_
        centroides = kmeans.cluster_centers_
        
        #tabela de distancia do valor para cada centroide 
        matriz_distancia = kmeans.fit_transform(X)
        matriz_distancia
        lista_distancia = []
        #pegadnp o menor valor 
        for l_dist in matriz_distancia:
           lista_distancia.append( min(l_dist))
           #           
        lista_media.append( np.mean(lista_distancia))
        lista_desvio.append( np.std(lista_distancia))
        #
    lista_media_k.append(lista_media)
    lista_desvio_k.append(lista_desvio)
    

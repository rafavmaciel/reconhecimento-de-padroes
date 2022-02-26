# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 08:28:10 2021

@author: rafav
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import scipy.stats
import matplotlib.pyplot as plt



def agrupar(y_means, y, k):
    l = np.zeros((k, 3))
    
    for i in range(len(y)):
        k_index = y_means[i]
        if y[i] == 0:
            l[k_index][0] += 1 
        if y[i] == 1:
            l[k_index][1] += 1 
        if y[i] == 2:
            l[k_index][2] += 1 
    return l

def plotar(group_list,k):
    for i in range(k):
        fig = plt.figure()
        fig.suptitle('grupo:'+str(i) + '  para k =' + str(k) , fontsize=10)
        ax = fig.add_axes([0,0,1,1])
        langs = ['setosa', 'versicolor', 'viginica']
        ax.bar(langs,group_list[i])
        plt.show()
  
        
X,y = load_iris(return_X_y = True)
l_g = [] # matriz l_g cada linha corresponde a um numero de k (um grupo) e cada coluna as classes iris originais       
lista_k = [3,6,9]

for k in lista_k:
    #iniciando o classificador 
    kmeans = KMeans(n_clusters=k, init="random")
    kmeans.fit(X)
    #armazenando a tabela de agrupamento
    y_means = kmeans.labels_
    group_list = agrupar(y_means, y, k)
    l_g.append(group_list)
    
    #plotando 
    plotar(group_list, k)
    
    
    
    
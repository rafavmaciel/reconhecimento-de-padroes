# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:27:37 2021

@author: rafav
"""
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import scipy.stats  

wine = load_wine()
X = wine.data[:,:12]#carregando a base wine sem a ultima coluna
y = wine.target

X_1,y_1 = load_wine(return_X_y = True) # carregando a base com a ultima coluna

k_range = range(1,101)
j_range = range(1,101)

scores_list= []
scores_list_1= []
diferença_list = []

#obtendo as tatas de acerto em 100 repetiçoes do roudout 50/50 para a base sem a ultima coluna 
for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = k, stratify=y)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test,y_pred))
 
# obtendo as tatas de acerto em 100 repetiçoes do roudout 50/50 para a base sem a ultima coluna 
# como os valores do parâmetro random_state vão ser os mesmos do laço anterior , as amostras também serão iguais 
for j in j_range:
    X_train,X_test,y_train,y_test = train_test_split(X_1,y_1, test_size = 0.5, random_state = j, stratify=y)
    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list_1.append(metrics.accuracy_score(y_test,y_pred))
    
#calculando a difernça 
for i in range(len(scores_list)):
    diferença_list.append(scores_list[i]-scores_list_1[i])

#calculando o intevalo de confiança das diferenças 
media_dif = np.mean(diferença_list)
desvio_padrao_dif = np.std(diferença_list)
intervalo_conf_dif = scipy.stats.norm.interval(0.95, loc=media_dif, scale=desvio_padrao_dif) 

#letra c : definida as hipóteses H0: μ1– μ2= 0 e H1: μ1– μ2≠ 0
#como o 0 não está no intervalo de confiança das diferenças . A hipótese h0 é rejeitada. 
#Então temos que a base wine sem a ultima coluna tem uma taxa de acertos significativamente maior

#calculando o intervalo de confiança da taxa de acertos para a base sem a ultima coluna
media_tax_ac = np.mean(scores_list)
desvio_padrao_tax_ac = np.std(scores_list)
intervalo_conf_dif_tax_ac = scipy.stats.norm.interval(0.95, loc=media_tax_ac, scale= desvio_padrao_tax_ac) 

#calculando o intervalo de confiança da taxa de acertos para a base com a ultima coluna
media_tax_ac_1 = np.mean(scores_list_1)
desvio_padrao_tax_ac_1 = np.std(scores_list_1)
intervalo_conf_dif_tax_ac_1 = scipy.stats.norm.interval(0.95, loc=media_tax_ac_1, scale= desvio_padrao_tax_ac_1) 

#letra e: 

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 07:05:07 2021

@author: rafav
"""

from sklearn.datasets import load_breast_cancer
from sklearn import preprocessing
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing,model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix                                                     
import scipy.stats   


X,y = load_breast_cancer(return_X_y = True)

kdisc = preprocessing.KBinsDiscretizer(n_bins= 5 , encode="ordinal", strategy="uniform")
X = kdisc.fit_transform(X)

lista_mim_folha = [5,10,15,20,25,30,50]
lista_score_houdout = []
lista_medias = []
lista_confianca = [] 
lista_num_folhas_houdout = []
lista_num_nos_houdout= []
lista_matrix_conf_houdout =[]


for k in lista_mim_folha:
    lista_score = []
    lista_num_folhas = []
    lista_num_nos =[]
    lista_matrix_conf=[]
    for i in range(100):
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state = i)
        tree =DecisionTreeClassifier(criterion='entropy', min_samples_leaf=k)
        tree.fit(X_train,y_train)
        predict = tree.predict(X_test)
        score = tree.score(X_test,y_test)
        lista_score.append(score)
        lista_num_folhas.append(tree.get_n_leaves())   
        lista_num_nos.append(tree.get_depth())
        lista_matrix_conf.append(confusion_matrix(y_test,predict))
    media = np.mean(lista_score)
    lista_medias.append(media)
    desvio_padrao = np.std(lista_score)
    lista_confianca.append(scipy.stats.norm.interval(0.95, loc=media, scale=desvio_padrao))
    lista_score_houdout.append(lista_score)
    lista_num_folhas_houdout.append(lista_num_folhas)
    lista_num_nos_houdout.append(lista_num_nos)
    lista_matrix_conf_houdout.append(lista_matrix_conf)
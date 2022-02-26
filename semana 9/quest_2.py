# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:32:23 2021

@author: rafav
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing,model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix                                                     
import scipy.stats   

data = pd.read_csv("car.data")
data.columns.tolist()
data.rename(columns= {'0':'buying', '1':'maint', '2':'doors', '3':'persons',
                      '4':'lug_boot', '5':'safety', '6':'class'},inplace=True)

data['buying'] = data['buying'].map({'low':0,'med':1,'high':2,'vhigh':3})
data['maint'] = data['maint'].map({'low':0,'med':1,'high':2,'vhigh':3})
data['doors'] = data['doors'].map({'2':0,'3':1,'4':2,'5more':3})
data['persons'] = data['persons'].map({'2':0,'4':1,'more':2})
data['lug_boot'] = data['lug_boot'].map({'small':0,'med':1,'big':2})
data['safety'] = data['safety'].map({'low':0,'med':1,'high':2})
data['class'] = data['class'].map({'unacc':0,'acc':1,'good':2,'vgood':3})

y = data['class']
x = data.iloc[:,:6]
      

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
        X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state = i)
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

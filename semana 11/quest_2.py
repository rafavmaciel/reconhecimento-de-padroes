# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 07:29:53 2021

@author: rafav
"""
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.preprocessing import MaxAbsScaler
import scipy.stats

X,y = load_wine(return_X_y = True)
scores_list= []

#normalizando os dados
p=MaxAbsScaler()
p.fit(X)
X = p.transform(X)

#usando o classificador 
X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,test_size=0.5,random_state = 1)
clf= MLPClassifier(max_iter=1000,learning_rate_init=0.1,verbose=0).fit(X_train, y_train)
y_pred=clf.predict(X_test)
score_a = metrics.accuracy_score(y_test,y_pred)*100

#letra b
#fazedo houdout 30
k_range = range(1,31)
#calculando os scores em um houdout 
for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = k, stratify=y)
    clf= MLPClassifier(max_iter=1000,learning_rate_init=0.1,verbose=0).fit(X_train, y_train)
    y_pred= clf.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test,y_pred))

#calculando o intervalode conf
media = np.mean(scores_list)
desvio_padrao = np.std(scores_list)
intervalo_conf = scipy.stats.norm.interval(0.95, loc=media, scale= desvio_padrao) 
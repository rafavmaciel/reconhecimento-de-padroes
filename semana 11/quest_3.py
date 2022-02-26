# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 08:07:35 2021

@author: rafav
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MaxAbsScaler
import numpy as np

data = pd.read_csv("spiral.csv")
x=data.iloc[:,:2]
y=data['class']
result=[]

p=MaxAbsScaler()
p.fit(x)
x = p.transform(x)
k_range = range(1,31)

lista_acuracia_clf1 = []
lista_acuracia_clf2 = []
lista_acuracia_clf3 = []
lista_acuracia_clf4 = []

#calulando a acurácia para os diferentes classificadores em houdout de 30
for k in k_range:
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=k)
    clf1= MLPClassifier( max_iter=500,learning_rate_init=0.3,solver = 'sgd',
                        verbose=0,hidden_layer_sizes=(4),activation='logistic').fit(X_train, y_train)
    y_pred1=clf1.predict(X_test)
    lista_acuracia_clf1.append(accuracy_score(y_test,y_pred1)*100)   
    #
    clf2 = MLPClassifier(max_iter=500,learning_rate_init=0.3,solver = 'sgd',
                         verbose=0,hidden_layer_sizes=(4,4),activation='logistic').fit(X_train, y_train)
    y_pred2=clf2.predict(X_test)
    lista_acuracia_clf2.append(accuracy_score(y_test,y_pred2)*100)    
    #
    clf3= MLPClassifier(max_iter=500,learning_rate_init=0.3,solver = 'sgd',
                        verbose=0,hidden_layer_sizes=(4,4,4),activation='logistic').fit(X_train, y_train)
    y_pred3=clf3.predict(X_test)
    lista_acuracia_clf3.append(accuracy_score(y_test,y_pred3)*100)  
    #
    clf4= MLPClassifier(max_iter=1000,learning_rate_init=0.3,solver = 'sgd',
                        verbose=0,hidden_layer_sizes=(4,4,4),activation='logistic').fit(X_train, y_train)
    y_pred4=clf4.predict(X_test)
    lista_acuracia_clf4.append(accuracy_score(y_test,y_pred4)*100)    

media_clf1 = np.mean(lista_acuracia_clf1)
media_clf2 = np.mean(lista_acuracia_clf2)
media_clf3 = np.mean(lista_acuracia_clf3)
media_clf4 = np.mean(lista_acuracia_clf4)

###############
clf5= MLPClassifier(max_iter=100000,learning_rate_init=0.3,verbose=0,hidden_layer_sizes=(4,4,4),activation='logistic').fit(X_train, y_train)
y_pred5 =clf5.predict(X_test)
result_d = accuracy_score(y_test,y_pred5)*100      
curva_erro = clf5.loss_curve_


######
#clf6= MLPClassifier(max_iter=1000,learning_rate_init=0.31,solver = 'sgd',verbose=1,hidden_layer_sizes=(4,7),activation='logistic', learning_rate ='adaptive').fit(X_train, y_train)
clf6= MLPClassifier(max_iter=10000,learning_rate_init=0.31,solver = 'sgd',verbose=1,hidden_layer_sizes=(7),activation='logistic', learning_rate ='adaptive').fit(X_train, y_train)
y_pred6 =clf6.predict(X_test)
result_e = accuracy_score(y_test,y_pred6)*100      
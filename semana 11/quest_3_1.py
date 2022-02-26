# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:45:12 2021

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
p=MaxAbsScaler()
p.fit(x)
x = p.transform(x)
scores_list =[]

k_range = range(1,31)
for k in k_range:
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=k)
    clf6= MLPClassifier(max_iter=10000,learning_rate_init=0.31,
                        solver = 'sgd',verbose=0,hidden_layer_sizes=(7),activation='logistic', 
                        learning_rate ='adaptive').fit(X_train, y_train)
    y_pred6 =clf6.predict(X_test)
    scores_list.append(accuracy_score(y_test,y_pred6)*100)
media_clf6 = np.mean(scores_list)

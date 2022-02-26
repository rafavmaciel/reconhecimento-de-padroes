# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:01:01 2021

@author: rafav
"""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import pandas

X,y = load_wine(return_X_y = True)

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 2)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

taxa_acertos = metrics.accuracy_score(y_test,y_pred)

matrix = metrics.confusion_matrix(y_test, y_pred)

recall1 = metrics.recall_score(y_test, y_pred , average= None)

precisão = metrics.precision_score(y_test, y_pred , average= None)

media_f = metrics.f1_score(y_test, y_pred , average= None)


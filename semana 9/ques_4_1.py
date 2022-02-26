# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:41:26 2021

@author: rafav
"""

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing,model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix                                                     
import scipy.stats   
import graphviz 

#a
le = preprocessing.LabelEncoder()
data = pd.read_csv("balance-scale.data")
data.columns.tolist()
data.rename(columns= {'0':'class', '1':'Left-Weight', '2':'Left-Distance', '3':'Right-Weight',
                      '4':'Right-Distance'},inplace=True)
y = data.iloc[:,:1]
x = data.drop(['class'],axis = 1)
y = y.apply(le.fit_transform)


X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state = 1)
clf =DecisionTreeClassifier(criterion='gini', min_samples_leaf=50,max_depth=2)
clf.fit(X_train,y_train)
predict = clf.predict(X_test)
score = clf.score(X_test,y_test)

names = ['Left-Weight','Left-Distance','Right-Weight','Right-Distance']
classes = ['b','r','l']

dot_data = tree.export_graphviz(clf, out_file=None,feature_names= names,class_names=classes,filled=True, rounded=True,special_characters=True) 
graph = graphviz.Source(dot_data) 
graph.render("balance") 

text_representation = tree.export_text(clf, feature_names=names)

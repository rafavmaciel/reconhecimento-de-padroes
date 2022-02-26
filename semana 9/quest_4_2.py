# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:17:27 2021

@author: rafav
"""
from sklearn import tree
from sklearn.datasets import load_breast_cancer
from sklearn import preprocessing
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing,model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix                                                     
import scipy.stats   
import graphviz 


X,y = load_breast_cancer(return_X_y = True)

kdisc = preprocessing.KBinsDiscretizer(n_bins= 5 , encode="ordinal", strategy="uniform")
X = kdisc.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state = 1)
clf =DecisionTreeClassifier(criterion='gini', min_samples_leaf=50,max_depth=2)
clf.fit(X_train,y_train)
predict = clf.predict(X_test)
score = clf.score(X_test,y_test)


dot_data = tree.export_graphviz(clf, out_file=None,filled=True, rounded=True,special_characters=True) 
graph = graphviz.Source(dot_data) 
graph.render("breast") 

text_representation = tree.export_text(clf)

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 07:31:09 2021

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

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state = 1)
clf =DecisionTreeClassifier(criterion='gini', min_samples_leaf=25,max_depth=3)
clf.fit(X_train,y_train)
predict = clf.predict(X_test)
score = clf.score(X_test,y_test)

names = ['buying','maint','doors','persons','lug_boot','safety']
classes = ['unacc','acc','good','vgood']

dot_data = tree.export_graphviz(clf, out_file=None,feature_names= names,class_names=classes,filled=True, rounded=True,special_characters=True) 
graph = graphviz.Source(dot_data) 
graph.render("car") 

text_representation = tree.export_text(clf, feature_names=names)
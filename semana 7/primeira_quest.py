# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:35:05 2021

@author: rafav
"""

import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import scipy as sp                                                         
import scipy.stats     

data = pd.read_csv("student-mat.csv",sep=";")
data.columns.tolist()

#binarios
data['school'] = data['school'].map({'GP':0,'MS':1})
data['sex'] = data['sex'].map({'M':0,'F':1})
data['address'] = data['address'].map({'U':0,'R':1})
data['famsize'] = data['famsize'].map({'LE3':0,'GT3':1})
data['Pstatus'] = data['Pstatus'].map({'T':0,'A':1})
data['schoolsup'] = data['schoolsup'].map({'yes':0,'no':1})
data['paid'] = data['paid'].map({'yes':0,'no':1})
data['activities'] = data['activities'].map({'yes':0,'no':1})
data['nursery'] = data['nursery'].map({'yes':0,'no':1})
data['higher'] = data['higher'].map({'yes':0,'no':1})
data['internet'] = data['internet'].map({'yes':0,'no':1})
data['romantic'] = data['romantic'].map({'yes':0,'no':1})
data['famsup'] = data['famsup'].map({'yes':0,'no':1})

data['Mjob'] = data['Mjob'].map({'teacher':0,'health':1,'services':2,'at_home':3,'other':4})
data['Fjob'] = data['Fjob'].map({'teacher':0,'health':1,'services':2,'at_home':3,'other':4})
data['reason'] = data['reason'].map({'home':0,'reputation':1,'course':2,'other':3})
data['guardian'] = data['guardian'].map({'mother':0,'father':1,'other':2,})


#discretizando a idade
kdisc = preprocessing.KBinsDiscretizer(n_bins= 5 , encode="ordinal", strategy="uniform")
age = data['age']
age = np.array(age).reshape((len(age), 1))
data['age'] = kdisc.fit_transform(age)

#discretizando as faltas
kdisc = preprocessing.KBinsDiscretizer(n_bins= 10 , encode="ordinal", strategy="uniform")
absences = data['absences']
absences = np.array(absences).reshape((len(age), 1))
data['absences'] = kdisc.fit_transform(absences)

#
def binarizar(item):
    if int(item) < 15:
        return int(0)
    else:
        return int(1)

data['G3'] = data['G3'].map(binarizar)

#
X = data.iloc[:,:30]
y = data['G3']
scores_list= []
k_range = range(1,101)


#calculando os scores em um houdout com a base completa
for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.5, random_state = k, stratify=y)
    knn = KNeighborsClassifier(n_neighbors= 1, metric='euclidean')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test,y_pred))

media = np.mean(scores_list)
desvio_padrao = np.std(scores_list)
intervalo_conf = scipy.stats.norm.interval(0.95, loc=media, scale= desvio_padrao) 



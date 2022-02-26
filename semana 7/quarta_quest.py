# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:24:47 2021

@author: rafav
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import scipy as sp                                                         
import scipy.stats            

data = pd.read_csv("processed.hungarian.data")
#data.columns.tolist()
y = data['class']
x = data.iloc[:,:13]


x.drop(['slope','ca','thal'],axis=1, inplace=True)

list_colun = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak"]

# sustituindo os valores faltantes para o padrão pd
for col in list_colun:
    x[col] = x[col].replace("?", "NaN"  )

# calculando a mediana
for col in list_colun:
    mediana = int(x[col].median())
    x[col] = x[col].replace("NaN", str(mediana))


scores_list= []
k_range = range(1,101)


#calculando os scores em um houdout com a base completa
for k in k_range:
    X_train,X_test,y_train,y_test = train_test_split(x,y, test_size = 0.1, random_state = k, stratify=y)
    knn = KNeighborsClassifier(n_neighbors= 1)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores_list.append(metrics.accuracy_score(y_test,y_pred))

media = np.mean(scores_list)
desvio_padrao = np.std(scores_list)
intervalo_conf = scipy.stats.norm.interval(0.95, loc=media, scale= desvio_padrao) 










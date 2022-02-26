# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:27:38 2021

@author: rafav
"""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import pandas
from sklearn.metrics import confusion_matrix

X,y = load_wine(return_X_y = True)

k_range = range(1,10)
scores_list= []
confusion_matrix_manual = [[0,0,0],[0,0,0],[0,0,0]]
recall = []
taxa_acerto = 0
precisão = []
media_f = []
taxa_fp =[]


#for k in k_range:
#   X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = k)
#    knn = KNeighborsClassifier(n_neighbors=1)
#   knn.fit(X_train, y_train)
#    y_pred = knn.predict(X_test)
#    for i in range(len(y_test)):
#        scores.append([y_pred[i],y_test[i]])
#        confusion_matrix_manual[y_test[i]][y_pred[i]] += 1 #   scores_list.append(metrics.accuracy_score(y_test,y_pred))
    


X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 2)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


# montando a matriz de confusão
for i in range(len(y_test)):
    # add 1 na linha da classe correta e na coluna da classe predita
    confusion_matrix_manual[y_test[i]][y_pred[i]] += 1

#calculando o recall por classe 
recall.append(confusion_matrix_manual[0][0]/(confusion_matrix_manual[0][0]+confusion_matrix_manual[0][1]+confusion_matrix_manual[0][2]))
recall.append(confusion_matrix_manual[1][1]/(confusion_matrix_manual[1][1]+confusion_matrix_manual[1][0]+confusion_matrix_manual[1][2]))
recall.append(confusion_matrix_manual[2][2]/(confusion_matrix_manual[2][2]+confusion_matrix_manual[2][0]+confusion_matrix_manual[2][1]))

#calculando a taxa de acerto 
numerador = 0
resto = 0
for i in range(len(confusion_matrix_manual)):
    for j in range(len(confusion_matrix_manual)):
        if i == j:
            numerador = numerador + confusion_matrix_manual[i][j]
        else:
            resto = resto + confusion_matrix_manual[i][j]
taxa_acerto = numerador / (numerador+ resto)

#calculando a precisão

precisão.append(confusion_matrix_manual[0][0]/(confusion_matrix_manual[0][0]+confusion_matrix_manual[1][0]+confusion_matrix_manual[2][0]))
precisão.append(confusion_matrix_manual[1][1]/(confusion_matrix_manual[1][1]+confusion_matrix_manual[0][1]+confusion_matrix_manual[2][1]))
precisão.append(confusion_matrix_manual[2][2]/(confusion_matrix_manual[2][2]+confusion_matrix_manual[0][2]+confusion_matrix_manual[1][2]))

# calculando a media f

for i in range(len(confusion_matrix_manual)):
    media_f.append((2*precisão[i] * recall[i]) / (precisão[i] + recall[i]))
    
    
# calculando a taxa de fp

taxa_fp.append(confusion_matrix_manual[0][1]+confusion_matrix_manual[0][2])
taxa_fp.append(confusion_matrix_manual[1][0]+confusion_matrix_manual[1][2])
taxa_fp.append(confusion_matrix_manual[2][0]+confusion_matrix_manual[2][1])


scores_list.append(metrics.accuracy_score(y_test,y_pred))
    
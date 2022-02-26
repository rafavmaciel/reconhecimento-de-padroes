# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:48:29 2021

@author: rafav
"""
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing,model_selection

#a
le = preprocessing.LabelEncoder()
data = pd.read_csv("balance-scale.data")
data.columns.tolist()
data.rename(columns= {'0':'class', '1':'Left-Weight', '2':'Left-Distance', '3':'Right-Weight',
                      '4':'Right-Distance'},inplace=True)
y = data.iloc[:,:1]
x = data.drop(['class'],axis = 1)
y = y.apply(le.fit_transform)
contador = 0


#para a raiz , escolhi aleatóriamente o

for index, row in data.iterrows():
    #print(row,index)
    if row['class'] == 'L' and row['Left-Distance'] == 2:
        contador+= 1

taxa_acerto = contador/ 625


#b: a base contém 49 resultados de b, 288 de l e 288 de r. Como r e l são os que tem uma taxa maior , eu adotarei r e calcularei qual atributo mais aparece quando a classificação é r
acertos_list = []
data = data.values.tolist()

count_list = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(len(data)):
    if data[i][0] == 'R':
        acertos_list.append(data[i])

for i in range(4):
    for j in range(len(acertos_list)):
        if acertos_list[j][i+1] == 1:
            count_list[i][0] += 1
        if acertos_list[j][i+1] == 2:
            count_list[i][1] += 1
        if acertos_list[j][i+1] == 3:
            count_list[i][2] += 1
        if acertos_list[j][i+1] == 4:
            count_list[i][3] += 1
        if acertos_list[j][i+1] == 5:
            count_list[i][4] += 1
            
# melhor escolha que tem mais acertos com são os atributos Left-Weight e Left-Distance que tem 91 acertos quando a categoria é 1    
        








'''

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state = 1)
clf = tree.DecisionTreeClassifier(max_depth=1)
clf.fit(X_train,y_train)
predict = clf.predict(X_test)
score = clf.score(X_test,y_test)
#tree.plot_tree(clf)    '''    

        
        
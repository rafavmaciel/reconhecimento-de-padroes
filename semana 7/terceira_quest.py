# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:49:46 2021

@author: rafav
"""
import pandas as pd
from sklearn import preprocessing
import numpy as np

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




y = data['class']
x = data.iloc[:,:6]

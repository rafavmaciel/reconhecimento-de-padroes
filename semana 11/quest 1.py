import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import LabelEncoder
from data_flor import FlorData
from sklearn.model_selection import train_test_split
import statistics


data_treino = FlorData.listaTreino
data_teste = FlorData.listaTeste
X_train = []
X_test = []
y_train = []
y_test = []
for data in data_treino:
    X_train.append(data[0:4])
    y_train.append(data[4])
for data in data_teste:
    X_test.append(data[0:4])
    y_test.append(data[4])


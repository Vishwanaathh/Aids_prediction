# -*- coding: utf-8 -*-
"""AIDS_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16jotFxX1OcGWpnYXWs37Am3oPjxdze0F
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split

data=pd.read_csv('/content/AIDS_Classification.csv')

data.head()

X=data.drop(columns='infected',axis=1)
Y=data['infected']

scaler=StandardScaler()
scaler.fit(X)
stdata=scaler.transform(X)

X_train,X_test,Y_train,Y_test=train_test_split(stdata,Y)

classifier=svm.SVC(kernel='linear')

classifier.fit(X_train,Y_train)

data.shape

a=[]
for i in range(22):
  a.append(input())
arr=np.array(a)

classifier.predict(arr.reshape(1,-1))
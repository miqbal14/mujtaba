# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as pit

dataset= pd.read_csv("aids1_Data.csv")
X = dataset.iloc[:,:-1].values
y= dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
regressor.predict(X_test)


plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('1980s to 1992 (Test set)')
plt.xlabel('1980')
plt.ylabel('2000')
plt.show()
print(regressor.predict([[7.2]]))

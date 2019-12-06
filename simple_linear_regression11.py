# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:11:11 2019

@author: Muhammad
"""

# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
mydataset = pd.read_csv('aids1.csv')
X = mydataset.iloc[:, :-1].values
y = mydataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
regressor.predict(X_test)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train,color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'green')
plt.title('Death vs Years (Training set)')
plt.xlabel('Years')
plt.ylabel('Death')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'blue')
plt.plot(X_train, regressor.predict(X_train), color = 'yellow')
plt.title('Death vs Years (Test set)')
plt.xlabel('Years')
plt.ylabel('Death')
plt.show()

print(regressor.predict([[1994]]))
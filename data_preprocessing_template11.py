# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:11:11 2019

@author: Muhammad
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
mydataset = pd.read_csv('aids1.csv')
X = mydataset.iloc[:, :-1].values
y = mydataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.mode_ selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# -*- coding: utf-8 -*-
"""P1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LQAMTW1TmUq-8oodQrmiJfW1ieVdIPDM
"""

from sklearn.datasets import load_boston

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = load_boston()

df

dataset = pd.DataFrame(df.data)
dataset.columns = df.feature_names
print(dataset.head())

dataset['Price'] = df.target

dataset.head()

X = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

X.head()

y.head()

#Linear Regression

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
lin_reg = LinearRegression()
mse = cross_val_score(lin_reg,X,y,scoring = 'neg_mean_squared_error',cv = 5)
mean_mse = np.mean(mse)

mean_mse

#Ridge Regression

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
ridge = Ridge()
params = {'alpha': [1e-15, 1e-10, 1e-8, 1e-3, 1e-2, 1, 5, 10, 20 ]}
ridge_regressor = GridSearchCV(ridge, params, scoring =  'neg_mean_squared_error', cv = 5)
ridge_regressor.fit(X,y)

print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_)

#Lasso Regression

from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
lasso = Lasso()
params = {'alpha':[1e-15, 1e-10, 1e-8, 1e-2, 1, 5, 10, 20]}
lasso_regressor = GridSearchCV(lasso, params, scoring = 'neg_mean_squared_error', cv = 5)
lasso_regressor.fit(X,y)

print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)
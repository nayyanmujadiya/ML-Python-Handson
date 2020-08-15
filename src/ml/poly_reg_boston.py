'''
https://medium.com/next-gen-machine-learning/polynomial-regression-7f27fae98197
'''

'''
Apply polynomial regression using Boston housing dataset
'''

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

'''
Load the data set
Use the pandas module to read the house data from the sklearn API.
'''

# load the dataset
boston = datasets.load_boston()
# column names
boston.feature_names
# add dependent and independent variable
x_data = boston.data
y_data = boston.target
# create a data frame
boston_df = pd.DataFrame(data=x_data, columns=boston.feature_names)
boston_df['target'] = y_data

'''
Feature Selection:
Let’s select one of the numerical fields as independent variable, we will use “LSTAT” ( percentage of the population in the neighborhood which comes under lower economic status)
'''

x = boston_df['LSTAT']
y = boston_df['target']

# converting into new axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]

'''
Train test split :
'''

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.10, random_state=42, shuffle=True)

'''

'''
# Polynomial Regression-nth order
plt.rcParams['figure.figsize'] = 16, 8
plt.scatter(x_test, y_test, s=40, alpha=0.3)
for degree in [1,2,3,4,5, 6, 7]:
   model = make_pipeline(PolynomialFeatures(degree),     LinearRegression())
   model.fit(x_train,y_train)
   y_plot = model.predict(x_test)
   plt.plot(x_test, y_plot, label="degree %d" % degree +'; $R^2$:   %.2f' % model.score(x_test, y_test))

plt.legend(loc='upper right')
plt.xlabel("Test LSTAT Data")
plt.ylabel("Predicted Price")
plt.title("Variance Explained with Varying Polynomial")
plt.show()

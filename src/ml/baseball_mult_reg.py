#Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

'''
data source:
https://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/mlr/frames/frame.html
'''

'''
A random sample of major league baseball players was obtained.
The following data (X1, X2, X3, X4, X5, X6) are by player.
X1 = batting average
X2 = runs scored/times at bat
X3 = doubles/times at bat
X4 = triples/times at bat
X5 = home runs/times at bat
X6 = strike outs/times at bat
'''

'''
Step 2: Read the dataset
'''
df = pd.read_csv("major_league_baseball_players.csv")
df.columns = ['x1','x2','x3','x4','x5','x6']
print(df.describe())

'''
In our dataset x1 is the output variable, which stores the batting average of baseball players. So, we consider all columns except x1 as input X and 0th column(x1) as output Y.
'''

'''
In train_test_split() function, we used test_size as 0.2, which means we use 20% of the data for testing and the remaining 80% for training.
'''

X = df.iloc[:,df.columns != 'x1']
Y = df.iloc[:, 0]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state= 0)


'''
Step 3: Train the model
'''

model = linear_model.LinearRegression()
model.fit(X_train, Y_train)

'''
We use X_train and Y_train for train the linear regression model. The X_test use for predict the output Y.
'''

coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

'''
This means that for a unit increase in x3(doubles/times at bat), there is an increase of 1.02 units in the x1(batting average). Similarly, for a unit increase in the x6(strike outs/times at bat), there is a decrease of 0.24 in x1.
'''

'''
Step 4: Predict the output
'''

y_pred = model.predict(X_test)
df = pd.DataFrame({'Actual': Y_test, 'Predicted': y_pred})
print(df.head(10))

df.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

'''
Step 4: Evaluation
'''

# Root Mean Squared Deviation
rmsd = np.sqrt(mean_squared_error(Y_test, y_pred))      # Lower the rmse(rmsd) is, the better the fit
r2_value = r2_score(Y_test, y_pred)                     # The closer towards 1, the better the fit

print("Y-Intercept: \n", model.intercept_)
print("Root Mean Square Error(rmsd) \n", rmsd)
print("R^2 Value: \n", r2_value)


'''
Here the R² value is 0.8356, which shows the model is almost accurate and can make good predictions. R² value can range from 0 to 1. As the R² value close to 1, the model will make better predictions.
'''

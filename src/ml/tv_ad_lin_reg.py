'''
https://github.com/marcopeix/ISL-linear-regression
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

data = pd.read_csv("Advertising.csv")

data.head()

data.columns

data.drop(['Unnamed: 0'], axis=1)

plt.figure(figsize=(16, 8))
plt.scatter(
    data['TV'],
    data['sales'],
    c='black'
)
plt.xlabel("Money spent on TV ads ($)")
plt.ylabel("Sales ($)")
plt.show()

X = data['TV'].values.reshape(-1,1)
y = data['sales'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(X, y)

print(reg.coef_[0][0])
print(reg.intercept_[0])

print("The linear model is: Y = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))

'''
0.047536640433019764
7.032593549127693
The linear model is: Y = 7.0326 + 0.047537X
'''

predictions = reg.predict(X)

plt.figure(figsize=(16, 8))
plt.scatter(
    data['TV'],
    data['sales'],
    c='black'
)
plt.plot(
    data['TV'],
    predictions,
    c='blue',
    linewidth=2
)
plt.xlabel("Money spent on TV ads ($)")
plt.ylabel("Sales ($)")
plt.show()

'''
Assessing the relevancy of the model
https://towardsdatascience.com/linear-regression-understanding-the-theory-7e53ac2831b5
'''
'''
looking at the R² value, we have 0.612. Therefore, about 60% of the variability of sales is explained by the amount spent on TV ads. This is okay, but definitely not the best we can to accurately predict the sales. Surely, spending on newspaper and radio ads must have a certain impact on sales.
'''

X = data['TV']
y = data['sales']
X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

'''
Let’s see if a multiple linear regression will perform better.
'''

Xs = data.drop(['sales', 'Unnamed: 0'], axis=1)
y = data['sales'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(Xs, y)

print(reg.coef_)
print(reg.intercept_)

print("The linear model is: Y = {:.5} + {:.5}*TV + {:.5}*radio + {:.5}*newspaper".format(reg.intercept_[0], reg.coef_[0][0], reg.coef_[0][1], reg.coef_[0][2]))

reg.score(Xs, y)

'''
Notice that the coefficient for newspaper is negative, but also fairly small. Is it relevant to our model? Let’s see by calculating the F-statistic, R² value and p-value for each coefficient.
'''

'''
Assessing the relevancy of the model
'''

X = np.column_stack((data['TV'], data['radio'], data['newspaper']))
y = data['sales']

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

'''
As you can see, the R² is much higher than that of simple linear regression, with a value of 0.897!

Also, the F-statistic is 570.3. This is much greater than 1, and since our data set if fairly small (only 200 data points), it demonstrates that there is a strong relationship between ad spending and sales.

Finally, because we only have three predictors, we can consider their p-value to determine if they are relevant to the model or not. Of course, you notice that the third coefficient (the one for newspaper) has a large p-value. Therefore, ad spending on newspaper is not statistically significant. Removing that predictor would slightly reduce the R² value, but we might make better predictions.
'''

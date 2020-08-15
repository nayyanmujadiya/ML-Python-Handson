'''
Implementing polynomial regression with scikit-learn is very similar to linear regression. There is only one extra step: you need to transform the array of inputs to include non-linear terms such as 𝑥².
'''

'''
Step 1: Import packages and classes
'''

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

'''
Step 2a: Provide data
'''

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 11, 2, 8, 25, 32])

'''
Now you have the input and output in a suitable format. Keep in mind that you need the input to be a two-dimensional array. That’s why .reshape() is used.
'''

'''
Step 2b: Transform input data
'''

'''
This is the new step you need to implement for polynomial regression!
'''

transformer = PolynomialFeatures(degree=2, include_bias=False)

'''
he variable transformer refers to an instance of PolynomialFeatures which you can use to transform the input x.

You can provide several optional parameters to PolynomialFeatures:

degree is an integer (2 by default) that represents the degree of the polynomial regression function.

interaction_only is a Boolean (False by default) that decides whether to include only interaction features (True) or all features (False).

include_bias is a Boolean (True by default) that decides whether to include the bias (intercept) column of ones (True) or not (False).

This example uses the default values of all parameters, but you’ll sometimes want to experiment with the degree of the function, and it can be beneficial to provide this argument anyway.
'''


'''
Before applying transformer, you need to fit it with .fit():
'''

transformer.fit(x)

'''
Once transformer is fitted, it’s ready to create a new, modified input. You apply .transform() to do that:
'''

x_ = transformer.transform(x)

'''
That’s the transformation of the input array with .transform(). It takes the input array as the argument and returns the modified array.
'''

'''
You can also use .fit_transform() to replace the three previous statements with only one:
'''

x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

print(x_)

'''
Step 3: Create a model and fit it
'''

model = LinearRegression().fit(x_, y)

'''
Step 4: Get results
'''

r_sq = model.score(x_, y)

print('coefficient of determination:', r_sq)

print('intercept:', model.intercept_)

print('coefficients:', model.coef_)

'''
Step 5: Predict response
'''

y_pred = model.predict(x_)

print('predicted response:', y_pred, sep='\n')



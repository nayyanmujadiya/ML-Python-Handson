'''
https://realpython.com/linear-regression-in-python/
'''

import numpy as np
from sklearn.linear_model import LinearRegression

'''
Now, you have two arrays: the input x and output y. You should call .reshape() on x because this array is required to be two-dimensional, or to be more precise, to have one column and as many rows as necessary. That’s exactly what the argument (-1, 1) of .reshape() specifies.
'''

'''
normal example we have not used reshape((-1, 1))
'''
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape((-1, 1))
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])


'''
Let’s create an instance of the class LinearRegression, which will represent the regression model:
'''
model = LinearRegression()

'''
Above statement creates the variable model as the instance of LinearRegression. You can provide several optional parameters to LinearRegression:

fit_intercept is a Boolean (True by default) that decides whether to calculate the intercept 𝑏₀ (True) or consider it equal to zero (False).
normalize is a Boolean (False by default) that decides whether to normalize the input variables (True) or not (False).
copy_X is a Boolean (True by default) that decides whether to copy (True) or overwrite the input variables (False).
n_jobs is an integer or None (default) and represents the number of jobs used in parallel computation. None usually means one job and -1 to use all processors.
This example uses the default values of all parameters.
'''

'''
It’s time to start using the model. First, you need to call .fit() on model:
'''
model.fit(x, y)

'''
With .fit(), you calculate the optimal values of the weights 𝑏₀ and 𝑏₁, using the existing input and output (x and y) as the arguments. In other words, .fit() fits the model. It returns self, which is the variable model itself. That’s why you can replace the last two statements with this one:
'''

model = LinearRegression().fit(x, y)

'''
You can obtain the coefficient of determination (𝑅²) with .score() called on model:
'''
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

'''
The attributes of model are .intercept_, which represents the coefficient, 𝑏₀ and .coef_, which represents 𝑏₁:
'''

print('intercept:', model.intercept_)
print('slope:', model.coef_)

'''
You should notice that you can provide y as a two-dimensional array as well. In this case, you’ll get a similar result. This is how it might look:
'''
#new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
#print('intercept:', new_model.intercept_)
#print('slope:', new_model.coef_)

'''
how to predict and verify?
To obtain the predicted response, use .predict():
'''

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

'''
manually
'''

y_pred = model.intercept_ + model.coef_ * x

print('predicted response:', y_pred, sep='\n')

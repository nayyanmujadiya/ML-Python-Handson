'''
Doc:
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
'''

'''
Now you want to have a polynomial regression (let’s make 2-degree polynomial). We will create a few additional features: x1*x2, x1^2 and x2^2. So we will get your ‘linear regression’:

y = c+ a1 * x1 + a2 * x2 + a3 * x1*x2 + a4 * x1^2 + a5 * x2^2
'''

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
#X = np.arange(6).reshape(3, 2)
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)
print(x)

#poly = PolynomialFeatures(degree=2)
poly = PolynomialFeatures(degree=2,include_bias=False)

'''
In some cases, it’s not necessary to include higher powers of any single feature, but only the so-called interaction features that multiply together at most d distinct features. These can be derived from PolynomialFeatures with the setting interaction_only=True.
'''
#poly = PolynomialFeatures(degree=2,interaction_only=True)
x_ = poly.fit_transform(x)

print(x_)

# Step 3: Create a model and fit it
model = LinearRegression().fit(x_, y)

# Step 4: Get results
r_sq = model.score(x_, y)
intercept, coefficients = model.intercept_, model.coef_

# Step 5: Predict
y_pred = model.predict(x_)

print('coefficient of determination:', r_sq)

print('intercept:', intercept)

print('coefficients:', coefficients, sep='\n')

print('predicted response:', y_pred, sep='\n')

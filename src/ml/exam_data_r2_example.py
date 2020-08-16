
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([2,9,5,5,3,7,1,8,6,2]).reshape((-1, 1))
y = np.array([69,98,82,77,71,84,55,94,84,64])

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

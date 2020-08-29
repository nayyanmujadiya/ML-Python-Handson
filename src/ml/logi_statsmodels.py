'''
You can also implement logistic regression in Python with the StatsModels package. Typically, you want this when you need more statistical details related to models and results. The procedure is similar to that of scikit-learn.
'''

import numpy as np
import statsmodels.api as sm

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])
x = sm.add_constant(x)

model = sm.Logit(y, x)

result = model.fit(method='newton')

result.params

result.predict(x)

(result.predict(x) >= 0.5).astype(int)

result.pred_table()

result.summary()

result.summary2()

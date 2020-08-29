
'''
The first example is related to a single-variate binary classification problem. This is the most straightforward kind of classification problem. There are several general steps you’ll take when you’re preparing your classification models:

Import packages, functions, and classes
Get data to work with and, if appropriate, transform it
Create a classification model and train (or fit) it with your existing data
Evaluate your model to see if its performance is satisfactory
A sufficiently good model that you define can be used to make further predictions related to new, unseen data. The above procedure is the same for classification and regression.
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='liblinear', random_state=0)

'''
LogisticRegression has several optional parameters. Read about it from
https://realpython.com/logistic-regression-python/
'''


model.fit(x, y)

model = LogisticRegression(solver='liblinear', random_state=0).fit(x, y)


model.classes_

model.intercept_

model.coef_

model.predict_proba(x)

model.predict(x)

model.score(x, y)

confusion_matrix(y, model.predict(x))

cm = confusion_matrix(y, model.predict(x))

'''
It’s often useful to visualize the confusion matrix. You can do that with .imshow() from Matplotlib, which accepts the confusion matrix as the argument:
'''
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()


'''
You can get a more comprehensive report on the classification with classification_report():
'''

print(classification_report(y, model.predict(x)))

'''
Improve the Model
You can improve your model by setting different parameters. For example, let’s work with the regularization strength C equal to 10.0, instead of the default value of 1.0:
'''

model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model.fit(x, y)

model.intercept_

model.coef_

model.predict_proba(x)

model.predict(x)

model.score(x, y)

confusion_matrix(y, model.predict(x))

print(classification_report(y, model.predict(x)))




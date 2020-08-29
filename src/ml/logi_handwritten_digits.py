'''
This example is about image recognition. To be more precise, you’ll work on the recognition of handwritten digits. You’ll use a dataset with 1797 observations, each of which is an image of one handwritten digit. Each image has 64 px, with a width of 8 px and a height of 8 px.
'''

'''
Step 1: Import Packages
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

'''
Step 2a: Get Data
'''
x, y = load_digits(return_X_y=True)

'''
Step 2b: Split Data
'''

'''
x_train: the part of x used to fit the model
x_test: the part of x used to evaluate the model
y_train: the part of y that corresponds to x_train
y_test: the part of y that corresponds to x_test
Once your data is split, you can forget about x_test and y_test until you define your model.
'''
x_train, x_test, y_train, y_test =\
    train_test_split(x, y, test_size=0.2, random_state=0)

'''
Step 2c: Scale Data
'''

'''
Standardization is the process of transforming data in a way such that the mean of each column becomes equal to zero, and the standard deviation of each column is one. This way, you obtain the same scale for all columns. Take the following steps to standardize your data:

Calculate the mean and standard deviation for each column.
Subtract the corresponding mean from each element.
Divide the obtained difference by the corresponding standard deviation.
It’s a good practice to standardize the input data that you use for logistic regression, although in many cases it’s not necessary. Standardization might improve the performance of your algorithm. It helps if you need to compare and interpret the weights. It’s important when you apply penalization because the algorithm is actually penalizing against the large values of the weights.

You can standardize your inputs by creating an instance of StandardScaler and calling .fit_transform() on it:
'''

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

'''
Step 3: Create a Model and Train It
'''

model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr',
                           random_state=0)
model.fit(x_train, y_train)

'''
When you’re working with problems with more than two classes, you should specify the multi_class parameter of LogisticRegression. It determines how to solve the problem:

'ovr' says to make the binary fit for each class.
'multinomial' says to apply the multinomial loss fit.
'''

'''
Step 4: Evaluate the Model
'''

x_test = scaler.transform(x_test)

y_pred = model.predict(x_test)

model.score(x_train, y_train)

model.score(x_test, y_test)

confusion_matrix(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

font_size = 6

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.set_xlabel('Predicted outputs', fontsize=font_size, color='black')
ax.set_ylabel('Actual outputs', fontsize=font_size, color='black')
ax.xaxis.set(ticks=range(10))
ax.yaxis.set(ticks=range(10))
ax.set_ylim(9.5, -0.5)
for i in range(10):
    for j in range(10):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='white')
plt.show()

'''
This is a heatmap that illustrates the confusion matrix with numbers and colors. You can see that the shades of purple represent small numbers (like 0, 1, or 2), while green and yellow show much larger numbers (27 and above).

The numbers on the main diagonal (27, 32, …, 36) show the number of correct predictions from the test set. For example, there are 27 images with zero, 32 images of one, and so on that are correctly classified. Other numbers correspond to the incorrect predictions. For example, the number 1 in the third row and the first column shows that there is one image with the number 2 incorrectly classified as 0.

Finally, you can get the report on classification as a string or dictionary with classification_report():
'''

print(classification_report(y_test, y_pred))



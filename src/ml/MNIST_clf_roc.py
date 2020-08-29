'''
Warning: fetch_mldata() is deprecated since Scikit-Learn 0.20. You should use fetch_openml() instead. However, it returns the unsorted MNIST dataset, whereas fetch_mldata() returned the dataset sorted by target (the training set and the test test were sorted separately).
'''
import numpy as np
import sys
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, cache=True)

#print(type(mnist))
#print(type(mnist.data))
#print(mnist.keys())
#print(mnist.data.shape)

'''
Datasets loaded by Scikit-Learn generally have a similar dictionary structure including:

A DESCR key describing the dataset
A data key containing an array with one row per instance and one column per feature
A target key containing an array with the labels
'''

X, y = mnist["data"], mnist["target"]
print(X.shape)

print(y.shape)


'''
There are 70,000 images, and each image has 784 features.
This is because each image is 28×28 pixels, and each feature simply represents one pixel’s intensity, from 0 (white) to 255 (black).

Let’s take a peek at one digit from the dataset.

All you need to do is grab an instance’s feature vector, reshape it to a 28×28 array, and display it using Matplotlib’s imshow() function:

'''

import matplotlib as mpl
import matplotlib.pyplot as plt

some_digit = X[0]
some_digit_image = some_digit.reshape(28, 28)
'''
plt.imshow(some_digit_image, cmap = 'gray', interpolation="nearest")
plt.axis("off")
plt.show()
'''

'''
This looks like a 5, and indeed that’s what the label tells us:
'''
print(y[0])

print(type(y[0]))

'''
Note that the label is a string. We prefer numbers, so let’s cast y to integers:

Géron, Aurélien. Hands-On Machine Learning with Scikit-Learn and TensorFlow . O'Reilly Media. Kindle Edition.
'''
y = y.astype(np.uint8)
print(type(y[0]))


'''
But wait! You should always create a test set and set it aside before inspecting the data closely. The MNIST dataset is actually already split into a training set (the first 60,000 images) and a test set (the last 10,000 images):
'''

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

'''
The training set is already shuffled for us, which is good as this guarantees that all cross-validation folds will be similar (you don’t want one fold to be missing some digits). Moreover, some learning algorithms are sensitive to the order of the training instances, and they perform poorly if they get many similar instances in a row. Shuffling

the dataset ensures that this won’t happen.
'''

'''
Binary classifier
-----------------
Let’s simplify the problem for now and only try to identify one digit — for example, the number 5. This “5-detector” will be an example of a binary classifier, capable of distinguishing between just two classes, 5 and not-5. Let’s create the target vectors for this classification task:

'''
#print(y_test)
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

#print(y_test_5)



'''
Okay, now let’s pick a classifier and train it. A good place to start is with a Stochastic Gradient Descent (SGD) classifier, using Scikit-Learn’s SGDClassifier class. This classifier has the advantage of being capable of handling very large datasets efficiently.

This is in part because SGD deals with training instances independently, one at a time (which also makes SGD well suited for online learning), as we will see later. Let’s create an SGDClassifier and train it on the whole training set:
'''
from sklearn.linear_model import SGDClassifier

sgd_clf = SGDClassifier(max_iter=5, tol=-np.infty, random_state=42)
sgd_clf.fit(X_train, y_train_5)

'''
Now you can use it to detect images of the number 5:
'''

print(sgd_clf.predict([some_digit]))


'''
Measuring Accuracy Using Cross-validation
'''
from sklearn.model_selection import cross_val_score
print(cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy"))



'''
Wow! Above 95% accuracy (ratio of correct predictions) on all cross-validation folds? This looks amazing, doesn’t it? Well, before you get too excited, let’s look at a very dumb classifier that just classifies every single image in the “not-5” class:
'''
#print(X)
#Z = np.zeros((len(X), 1), dtype=bool)
#print(Z)


from sklearn.base import BaseEstimator
class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)

never_5_clf = Never5Classifier()
print(cross_val_score(never_5_clf, X_train, y_train_5, cv=3, scoring="accuracy"))



'''
That’s right, it has over 90% accuracy! This is simply because only about 10% of the images are 5s, so if you always guess that an image is not a 5, you will be right about 90% of the time. Beats Nostradamus.

This demonstrates why accuracy is generally not the preferred performance measure for classifiers, especially when you are dealing with skewed datasets (i.e., when some classes are much more frequent than others).

'''

'''
Confusion Matrix
-----------------

A much better way to evaluate the performance of a classifier is to look at the confusion matrix. The general idea is to count the number of times instances of class A are classified as class B. For example, to know the number of times the classifier confused images of 5s with 3s, you would look in the 5th row and 3rd column of the confusion matrix.

'''

'''
Just like the cross_val_score() function, cross_val_predict() performs K-fold cross-validation, but instead of returning the evaluation scores, it returns the predictions made on each test fold. This means that you get a clean prediction for each instance in the training set (“clean” meaning that the prediction is made by a model that never saw the data during training).
'''
from sklearn.model_selection import cross_val_predict

y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)

'''
Each row in a confusion matrix represents an actual class, while each column represents a predicted class. The first row of this matrix considers non-5 images (the negative class): 53,272 of them were correctly classified as non-5s (they are called true negatives), while the remaining 1,307 were wrongly classified as 5s (false positives).

The second row considers the images of 5s (the positive class): 1,077 were wrongly classified as non-5s (false negatives), while the remaining 4,344 were correctly classified as 5s (true positives). A perfect classifier would have only true positives and true negatives, so its confusion matrix would have nonzero values only on its main diagonal (top left to bottom right):
'''
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_train_5, y_train_pred))



y_train_perfect_predictions = y_train_5

print(confusion_matrix(y_train_5, y_train_perfect_predictions))

#sys.exit("Test")

'''
Precision and Recall
Scikit-Learn provides several functions to
compute classifier metrics, including precision and recall:
'''

from sklearn.metrics import precision_score, recall_score

print(precision_score(y_train_5, y_train_pred))

print(recall_score(y_train_5, y_train_pred))

'''
Now your 5-detector does not look as shiny as it did when you looked at its accuracy. When it claims an image represents a 5, it is correct only 77% of the time. Moreover, it only detects 80% of the 5s.
'''

'''
It is often convenient to combine precision and recall into a single metric called the F1 score, in particular if you need a simple way to compare two classifiers. The F1 score is the harmonic mean of precision and recall

Whereas the regular mean treats all values equally, the harmonic mean gives much more weight to low values. As a result, the classifier will only get a high F1 score if both recall and precision are high.

'''
from sklearn.metrics import f1_score
print(f1_score(y_train_5, y_train_pred))

'''
from sklearn.metrics import accuracy_score
print(accuracy_score(y_true=y_train_5, y_pred=y_train_pred))
'''

y_scores = sgd_clf.decision_function([some_digit])
print(y_scores)

threshold = 0
y_some_digit_pred = (y_scores > threshold)

print(y_some_digit_pred)

threshold = 200000
y_some_digit_pred = (y_scores > threshold)
y_some_digit_pred

print(y_some_digit_pred)


y_scores = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3,
                             method="decision_function")

print(y_scores)

'''Now with these scores you can compute precision and recall for all possible thresholds using the
precision_recall_curve() function:

'''

from sklearn.metrics import precision_recall_curve

precisions, recalls, thresholds = precision_recall_curve(y_train_5, y_scores)


def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision", linewidth=2)
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall", linewidth=2)
    plt.xlabel("Threshold", fontsize=16)
    plt.legend(loc="upper left", fontsize=16)
    plt.ylim([0, 1])

plt.figure(figsize=(8, 4))
plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
plt.xlim([-700000, 700000])
#save_fig("precision_recall_vs_threshold_plot")
plt.show()

'''
Now you can simply select the threshold value that gives you the best precision/recall
tradeoff for your task. Another way to select a good precision/recall tradeoff is to
plot precision directly against recall,
'''

(y_train_pred == (y_scores > 0)).all()

y_train_pred_90 = (y_scores > 70000)

precision_score(y_train_5, y_train_pred_90)

recall_score(y_train_5, y_train_pred_90)

def plot_precision_vs_recall(precisions, recalls):
    plt.plot(recalls, precisions, "b-", linewidth=2)
    plt.xlabel("Recall", fontsize=16)
    plt.ylabel("Precision", fontsize=16)
    plt.axis([0, 1, 0, 1])

plt.figure(figsize=(8, 6))
plot_precision_vs_recall(precisions, recalls)
#save_fig("precision_vs_recall_plot")
plt.show()

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate', fontsize=16)
    plt.ylabel('True Positive Rate', fontsize=16)

plt.figure(figsize=(8, 6))
plot_roc_curve(fpr, tpr)
#save_fig("roc_curve_plot")
plt.show()

from sklearn.metrics import roc_auc_score

roc_auc_score(y_train_5, y_scores)
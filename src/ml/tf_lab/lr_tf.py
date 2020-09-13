#import tensorflow as tf
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#tf.compat.v1.disable_eager_execution()

test_data_size = 2000
iterations = 100000
learn_rate = 0.005
# y = Wx+b

def generate_test_values():
    train_x = []
    train_y = []

    for _ in range(test_data_size):
        x1 = np.random.rand()
        x2 = np.random.rand()
        x3 = np.random.rand()
        y_f = 2 * x1 + 3 * x2 + 7 * x3 + 4
        train_x.append([x1, x2, x3])
        train_y.append(y_f)

    return np.array(train_x), np.transpose([train_y])

x = tf.placeholder(tf.float32, [None, 3], name="x")
W = tf.Variable(tf.zeros([3, 1]), name="W")
b = tf.Variable(tf.zeros([1]), name="b")
y = tf.placeholder(tf.float32, [None, 1])

# y = Wx+b
model = tf.add(tf.matmul(x, W), b)

cost = tf.reduce_mean(tf.square(y - model))
train = tf.train.GradientDescentOptimizer(learn_rate).minimize(cost)

train_dataset, train_values = generate_test_values()

init = tf.global_variables_initializer()
#init = tf.compat.v1.global_variables_initializer()

with tf.Session() as session:
#with tf.compat.v1.Session() as session:
    session.run(init)

    for _ in range(iterations):

        session.run(train, feed_dict={
            x: train_dataset,
            y: train_values
        })

    print ("cost = {}".format(session.run(cost, feed_dict={
        x: train_dataset,
        y: train_values
    })))

    print ("W = {}".format(session.run(W)))
    print ("b = {}".format(session.run(b)))

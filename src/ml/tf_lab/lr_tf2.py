import tensorflow as tf
from tensorflow.keras import Model

import numpy as np
test_data_size = 2000

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


class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.W = tf.Variable(initial_value=[[2.0],[1.0],[2.0]],trainable=True, shape=[3,1], name="W")
        self.b = tf.Variable(initial_value=[1.0], trainable=True, shape=[1], name="b")

    def call(self, x):
        x = tf.add(tf.matmul(x, self.W), self.b)
        return x
model = MyModel()



loss_object = tf.keras.losses.MeanSquaredError()

optimizer = tf.keras.optimizers.Adam()

train_loss = tf.keras.metrics.Mean(name='train_loss')

test_loss = tf.keras.metrics.Mean(name='test_loss')


@tf.function
def train_step(inps, labels):
    with tf.GradientTape() as tape:
        predictions = model(inps, training=True)
        loss = loss_object(labels, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    train_loss(loss)

@tf.function
def test_step(inps, labels):
    predictions = model(inps, training=False)
    t_loss = loss_object(labels, predictions)

    test_loss(t_loss)


train_dataset, train_values = generate_test_values()


EPOCHS = 10

for epoch in range(EPOCHS):
    train_loss.reset_states()
    test_loss.reset_states()


    for inps, labels in zip(train_dataset, train_values):
        train_step(np.array([inps]), labels)

    for test_inps, test_labels in zip(train_dataset, train_values):
        test_step(np.array([test_inps]), test_labels)


    template = 'Epoch {}, Loss: {}, Test Loss: {}'

    print(template.format(epoch + 1,
                          train_loss.result(),
                          test_loss.result()))

print (model.variables)



import tensorflow as tf

#need to do if you are usnig old program
tf.compat.v1.disable_eager_execution()

# y = 5*X + 13
# y = a*X + b

x = tf.constant(-2.0, name="x", dtype=tf.float32)
a = tf.constant(5.0, name="a", dtype=tf.float32)
b = tf.constant(13.0, name="b", dtype=tf.float32)

# from data flow
y = tf.Variable(tf.add(tf.multiply(a, x), b))

init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as session:
    session.run(init)
    print (session.run(y))

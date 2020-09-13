import tensorflow as tf

tf.compat.v1.disable_eager_execution()

x = tf.constant(-2.0, name="x", dtype=tf.float32)
a = tf.constant(5.0, name="a", dtype=tf.float32)
b = tf.constant(13.0, name="b", dtype=tf.float32)

y = tf.Variable(tf.add(tf.multiply(a, x), b))

init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as session:
    #merged = tf.summary.merge_all() # new
    merged = tf.compat.v1.summary.merge_all() # new
    #writer = tf.summary.FileWriter("logs", session.graph) # new
    writer = tf.compat.v1.summary.FileWriter("logs", session.graph) # new
    session.run(init)
    print (session.run(y))

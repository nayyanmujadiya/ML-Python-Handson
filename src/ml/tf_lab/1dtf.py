import numpy as np
import tensorflow as tf
tensor_1d = np.array([1.45, -1, 0.2, 102.1])

tf.compat.v1.disable_eager_execution()

print ("t1d:",tensor_1d)
print ("t1d[0]",tensor_1d[0])
print ("t1d[2]",tensor_1d[2])
print ("dim",tensor_1d.ndim)
print ("s",tensor_1d.shape)
print ("t",tensor_1d.dtype)

tensor = tf.convert_to_tensor(tensor_1d, dtype=tf.float64)
#with tf.Session() as session:
with tf.compat.v1.Session() as session:
    print (session.run(tensor))
    print (session.run(tensor[0]))
    print (session.run(tensor[1]))

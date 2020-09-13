
import tensorflow as tf
print('tensorflow version', tf.__version__)

'''
https://www.tensorflow.org/api_docs/python/tf/Variable
'''

'''
TF.TENSOR
The primary object in TensorFlow that you play with is tf.Tensor. This is a tensor object that is associated with a value. It has two properties bound to it: data type and shape. The data type defines the type and size of data that will be consumed by a tensor. Possible types include float32, int32, string, etc. Shape defines the number of dimensions.
'''

'''
tf.Variable()

The variable constructor requires an argument which could be a tensor of any shape and type. After creating the instance, this variable is added to the TensorFlow graph and can be modified using any of the assign methods. It is declared as follows:
'''

print(tf.Variable("Hello World!", tf.string))

'''
tf.constant()
The tensor is populated with a value, dtype, and, optionally, a shape. This value remains constant and cannot be modified further.

The following code snippet explains the creation of a constant tensor:

'''

print(tf.constant([1,2,3,4], shape=(2,2)))

'''
A few basic operations to start with will give you a glimpse at how TensorFlow works.
'''

'''
DECLARING A SCALAR
Rank-0 tensors can be declared as follows:
'''

float_var = tf.Variable(19.99, tf.float32, name="float")

int_var = tf.Variable(11, tf.int64)

string_var = tf.Variable("Cookie", tf.string)

print("{0}, {1}, {2}".format(float_var, int_var, string_var))

'''
The name parameter assigns an optional name to the tensor.

The shape was empty because the values being printed there are scalars.
'''

'''
Using tf.constant
'''

float_cons = tf.constant(19.99)

int_cons = tf.constant(11, dtype=tf.int32)

string_cons = tf.constant("Cookie", name="string")

print("{0}, {1}, {2}".format(float_cons, int_cons, string_cons))

'''
b around the word Cookie indicates that it is a bytes object.
'''

'''
DECLARING A VECTOR
Rank-1 tensors can be declared as follows:

Using tf.Variable
'''

float_var = tf.Variable([19.99], tf.float32, name="float")

int_var = tf.Variable([11, 19], tf.int64)

string_var = tf.Variable(["Cookie", "Monster"], tf.string)

print("{0}, {1}, {2}".format(float_var, int_var, string_var))

'''
array indicates that the output is a list of values.
'''

'''
Using tf.constant
'''

float_cons = tf.constant([19.99])

int_cons = tf.constant([11, 19], dtype=tf.int32)

string_cons = tf.constant(["Cookie", "Monster"], name="string")

print("{0}, {1}, {2}".format(float_cons, int_cons, string_cons))


'''
DECLARING A MATRIX
Rank-2 tensors can be declared as follows:

Using tf.Variable
'''

float_var=tf.Variable([[19.99],[11.11]],tf.float32,name="float")

int_var = tf.Variable([[11, 19]], tf.int64)

string_var=tf.Variable([["Cookie","Monster"],["Ice","Cream"]], tf.string)

print("{0}, {1}, {2}".format(float_var, int_var, string_var))

'''
The shape parameter in the output was initialized with the respective shapes of the declared tensors. The first one was a 2x1 matrix (2 rows and 1 column). The second one was a 1x2 matrix, and the 3rd one was a 2x2 matrix.
'''

'''
Using tf.constant
'''

float_cons = tf.constant([[19.99], [11.11]])

int_cons = tf.constant([[11, 19]], dtype=tf.int32)

string_cons = tf.constant([["Cookie", "Monster"], ["Ice", "Cream"]], name="string")

print("{0}, {1}, {2}".format(float_cons, int_cons, string_cons))

'''
BASIC OPERATIONS
Now that we’ve thoroughly explored the initializations, have let’s perform some basic operations using TensorFlow.

tf.zeros()/tf.ones()/tf.fill()

tf.zeros() takes the shape as an argument and returns a tensor filled with zeros.

tf.ones() takes the shape as an argument and returns a tensor filled with ones.

tf.fill() allows initializing a tensor with a random value, not limiting to 0 or 1.
'''

zero_tensor = tf.zeros(2,dtype=tf.float32)

print(zero_tensor)

print(zero_tensor.numpy())

one_tensor = tf.ones((2,2),dtype=tf.int32)

print(one_tensor)

print(one_tensor.numpy())

fill_tensor = tf.fill((2,2),value=3.)

print(fill_tensor)

print(fill_tensor.numpy())

'''
zero_tensor, one_tensor, fill_tensor are the references that point to the tensors created. To extract the values stored, numpy() was used. This returned numpy.ndarray objects.
'''

'''
Slicing Tensors

To access a value from a vector, invoke the following code:
'''

float_vector = tf.constant([2,2.3])

float_vector.numpy()[0]

'''
[0] returned the value at the 0th index.

To access a value from a matrix, invoke the following code:
'''

string_matrix = tf.constant([["Hello", "World"]])

string_matrix.numpy()[0,1]

'''
[0, 1] returned the value present at the 0th row and 1st column.

To slice a matrix, invoke the following code:
'''

string_matrix = tf.constant([["Hello", "World", "!"], ["Tensorflow", "is", "here"]])

print(string_matrix.numpy()[1, 2])

print(string_matrix.numpy()[:1])

print(string_matrix.numpy()[:, 1])

print(string_matrix.numpy()[1, :])

'''
[1, 2] extracted the element present at the 1st row and 2nd column.

[:1] extracted the 1st row (all the rows before 1).

[:, 1] extracted the 1st column.

[1, :] extracted the 1st row.

'''

'''
TENSOR SHAPE
To access the shape of a tensor, invoke the following code:
'''

string_matrix = tf.constant([["Hello", "World", "!"], ["Tensorflow", "is", "here"]])

string_matrix.shape

'''
There were two rows and three columns in the given tensor.
'''

'''
MATH OPERATIONS
Let’s look at a few math operations that can be implemented using TensorFlow.

Element-Wise Math

Here’s a code snippet that compares add, subtract, multiply, and division functions:
'''

x = tf.constant([2, 2, 2])

y = tf.constant([3, 3, 3])

print((x+y).numpy())

print(tf.add(x, y).numpy())

print((x-y).numpy())

print(tf.subtract(x, y).numpy())

print((x*y).numpy())

print(tf.multiply(x, y).numpy())

print((x/y).numpy())

print(tf.divide(x, y).numpy())

'''
Both the operators and the TensorFlow functions gave identical outputs. All the operations were implemented element-wise.
'''

'''
Tensor Reshape

tf.reshape() returns a tensor that has values rearranged with respect to the shape given as an argument. Take a look at this code snippet:
'''

x = tf.constant([[1, 2, 3]])

print(x.shape)

x = tf.reshape(x, [3,1])

print(x.shape)

print(x.numpy())

x = tf.reshape(x, [-1])

print(x.shape)

print(x.numpy())

'''
Initially, the shape of the tensor was (1, 3). It was then reshaped to (3, 1). When the tensor was reshaped to [-1], the size was computed such that the total size remained constant. To be precise, the shape flattened to a 1D array.
'''

'''
Matrix Multiplication

Let’s now see how Tensorflow does matrix multiplication using the following code snippet:
'''

x = tf.constant([[3., 3.]])

y = tf.constant([[1., 2., 3.], [4., 5., 6.]])

tf.matmul(x, y).numpy()

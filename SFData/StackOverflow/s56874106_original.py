import tensorflow as tf
import numpy as np


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) =
    mnist.load_data(r'C:\Users\Ati\Downloads\mnist.npz')


# Reshaping the array to 4-dims so that it can work with the Keras API
x_train = x_train.reshape(x_train.shape[0], 784)
x_test = x_test.reshape(x_test.shape[0], 784)

# Making sure that the values are float so that we can get decimal
# points after division
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
# Normalizing the RGB codes by dividing it to the max RGB value.
x_train /= 255
x_test /= 255

print('y_train shape:', y_train.shape)
print('x_train shape:', x_train.shape)

class NeuralNetwork:
    def add_layer(inputs, in_size, out_size, activation_function=None):
        Weights = tf.Variable(tf.random_normal([in_size, out_size]))
        biases = tf.Variable(tf.zeros([out_size]) + 0.1)
        Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


xs = tf.placeholder(tf.float32, [None, 784]) #same with x_train=60000*784
ys = tf.placeholder(tf.float32, [60000, 1])

l1 = NeuralNetwork.add_layer(xs, 784, 10, activation_function=None)

prediction = NeuralNetwork.add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                      reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train_step, feed_dict={xs:x_train, ys:y_train})
    sess.run(train_step, feed_dict={xs:x_test, ys:y_test})
    if i % 50==0: #print loss every 50 step
        print("loss after training =",
              sess.run(loss, feed_dict={xs:x_train,ys:y_train}))
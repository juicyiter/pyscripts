#!/opt/local/bin/python
# _*_ coding: utf-8 _*_

'Softmax Regression'

__author__ = 'Ethan Mengoreo'

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# Placeholders (Tensors)
## Images to be recognized, mutable row
x = tf.placeholder(tf.float32, [None, 784])
## Actual labels
y_ = tf.placeholder(tf.float32, [None, 10])

# Variables
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Output of the model, matmul: matrix multiplication
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Cross-entropy to measure the loss
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y)))

# Using Gradient Descent to optimize the loss with learning rate (0.01)
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# Create a required session, where to run train_step
sess = tf.InteractiveSession()

## Initialize all variables
tf.global_variables_initializer().run()


# Run gradient descent
for _ in range(100):
    # Pick 100 training data
    batch_xs, batch_ys = mnist.train.next_batch(100)

    sess.run(train_step, feed_dict={x:batch_xs, y_:batch_xs})

# Compare the largest value's index
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

# Convert True and False to float32
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Run test
print(sess.run(accuracy, feed_dict={x:mnist.test.images, y_:mnist.test.labels}))

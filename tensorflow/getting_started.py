#!/opt/local/bin/python
# _*_ coding: utf-8 _*_

'Tensorflow'

__author__ = 'Ethan Mengoreo'

from tensorflow.examples.tutorials.mnist import input_data
import PIL.Image as Image
import os

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# show images
save_dir = 'MNIST_data/raw'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i in range(20):
    image_arr = mnist.train.images[i, :]
    iamge_arr = image_arr.reshape(28, 28)

    filename = save_dir + f'mnist_train_{i}.jpg'
    im = Image.fromarray(image_arr)
    im.save(filename, 'L')

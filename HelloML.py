import tensorflow as tf
from tensorflow import keras

mnist = tf.keras.datasets.fashion_mnist
(training_images,training_labels),(test_images,test_labels) = mnist.load_data()




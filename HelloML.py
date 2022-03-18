import tensorflow as tf
from tensorflow import keras

mnist = tf.keras.datasets.fashion_mnist
(training_images,training_labels),(test_images,test_labels) = mnist.load_data()
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),tf.keras.layers.Dense(512, activation = tf.nn.relu),tf.keras.layers(10,activation = tf.nn.softmax)])
model.compile(optimizer = 'adam',loss = 'sparse_categorical_crossentropy')
model.fit(training_images,training_labels)
model.evaluate(test_images,test_labels)
classifications = model.predict(test_images)
print(classifications[0])

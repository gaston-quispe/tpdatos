import numpy as np
import pandas
import utils
import keras.layers.core as core
import keras.layers.convolutional as conv
import keras.models as models
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D

nb_classes = 10
nb_epoch = 1
batch_size = 128
# input image dimensions
img_rows, img_cols = 28, 28
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 3

nb_filters_1 = 64
nb_filters_2 = 128
nb_filters_3 = 256

print("Cargando set de datos.")
set_train = pandas.read_csv('/home/val/mnist/train.csv').values
set_test = pandas.read_csv('/home/val/mnist/test.csv').values

set_train_particion, set_train_test = utils.particionar_train_test(set_train, 0.75)

#Separamos los datos (la primer columna contiene la clase de cada imagen).
Y_train = set_train_particion[:, 0]
X_train = set_train_particion[:, 1:]
X_test = set_train_test[:, 1:]
Y_test = set_train_test[:, 0]

X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

#Normalizacion
X_train /= 255.0
X_test /= 255.0

Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)
modelo = Sequential()

#Aqui inicia la red
modelo.add(conv.ZeroPadding2D((1,1), input_shape=(1, 28, 28),))
modelo.add(conv.Convolution2D(nb_filters_1, nb_conv, nb_conv,  activation="relu"))
modelo.add(conv.MaxPooling2D(strides=(2,2)))

modelo.add(conv.ZeroPadding2D((1, 1)))
modelo.add(conv.Convolution2D(nb_filters_2, nb_conv, nb_conv, activation="relu"))
modelo.add(conv.MaxPooling2D(strides=(2,2)))

modelo.add(core.Flatten())
modelo.add(core.Dropout(0.2))
modelo.add(core.Dense(128, activation="relu"))
modelo.add(core.Dense(nb_classes, activation="softmax"))

modelo.summary()
modelo.compile(loss="categorical_crossentropy", optimizer="adadelta", metrics=["accuracy"])
#Fin de la red

modelo.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, verbose=1, validation_data=(X_test, Y_test))
score = modelo.evaluate(X_test, Y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
import pandas
import sys

from Utils.Logger import Logger
from Utils.DataExtractor import dataExtraction
from Utils.utils import generarCarpeta
from keras.layers import ZeroPadding2D, Convolution2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
import keras.models as models
from keras.utils import np_utils
from Utils.utils import particionar_train_test


#########GENERAR CARPETA Y OBTENER DATOS##############
# Se genera una carpeta nueva por cada compilacion
# En esa carpeta se guardan los datos recolectados
carpeta = generarCarpeta()
archivo_generado = carpeta+"/datosBrutos.log"
sys.stdout = Logger(archivo_generado)
######################################################

n_classes = 10
n_epoch = 1
batch_size = 128
# input image dimensions
img_rows, img_cols = 28, 28
# number of convolutional filters to use
n_filters = 32
# size of pooling area for max pooling
n_pool = 2
# convolution kernel size
n_conv = 3

n_filters_1 = 64
n_filters_2 = 128
n_filters_3 = 256

print("Cargando set de datos.")

valeTrain = '/home/val/mnist/train.csv'
valeTest  = '/home/val/mnist/test.csv'
dariusTrain = "/home/darius/workspace/train.csv"
dariusTest  = "/home/darius/workspace/test.csv"

set_train = pandas.read_csv(dariusTrain).values
set_test = pandas.read_csv(dariusTest).values

set_train_particion, set_validacion = particionar_train_test(set_train, 0.70)

#Separamos los datos (la primer columna contiene la clase de cada imagen).
Y_train = set_train_particion[:, 0]
X_train = set_train_particion[:, 1:]
X_validacion = set_validacion[:, 1:]
Y_validacion = set_validacion[:, 0]

#X_test es el set que debemos clasificar y submittear en kaggle.
X_test = set_test

X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
X_validacion = X_validacion.reshape(X_validacion.shape[0], 1, img_rows, img_cols)

X_train = X_train.astype('float32')
X_validacion = X_validacion.astype('float32')

#Normalizacion
X_train /= 255.0
X_validacion /= 255.0

Y_train = np_utils.to_categorical(Y_train)
Y_validacion = np_utils.to_categorical(Y_validacion)
cnn = Sequential()
cnn.add(ZeroPadding2D((1,1), input_shape=(1, 28, 28),))
cnn.add(Convolution2D(n_filters_1, n_conv, n_conv,  activation="relu"))
cnn.add(MaxPooling2D(strides=(2,2)))
cnn.add(Flatten())

cnn.add(Dense(128, activation="relu"))
cnn.add(Dense(n_classes, activation="softmax"))

cnn.summary()
cnn.compile(loss="categorical_crossentropy", optimizer="adadelta", metrics=["accuracy"])

cnn.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=n_epoch, verbose=1, validation_data=(X_validacion, Y_validacion))
score = cnn.evaluate(X_validacion, Y_validacion, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])

############PLOTEO############
'''archivo generado da el path de los datos'''
dataExtraction(carpeta)



##############################

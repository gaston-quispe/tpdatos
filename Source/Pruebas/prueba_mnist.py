import pandas
import sys

from Utils.DataExtractor import dataExtraction
from Utils.Logger import Logger
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
from keras.utils import np_utils
from Utils.utils import generarCarpeta
import numpy as np


#########GENERAR CARPETA Y OBTENER DATOS##############
# Se genera una carpeta nueva por cada compilacion
# En esa carpeta se guardan los datos recolectados
carpeta = generarCarpeta()
archivo_generado = carpeta+"/datosBrutos.log"
sys.stdout = Logger(archivo_generado)
######################################################

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

print("Cargando set de datos.")
set_train = pandas.read_csv("/home/darius/workspace/train.csv").values
set_test = pandas.read_csv("/home/darius/workspace/test.csv").values

#Separamos los datos (la primer columna contiene la clase de cada imagen).
Y_train = set_train[:, 0]
X_train = set_train[:, 1:]

X_train = X_train.reshape(set_train.shape[0], 1, img_rows, img_cols)
X_test = set_test.reshape(set_test.shape[0], 1, img_rows, img_cols)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

#Normalizacion
X_train /= 255.0
X_test /= 255.0

Y_train = np_utils.to_categorical(Y_train)

modelo = Sequential()

#Aqui va la red de confianza

modelo.compile(loss="categorical_crossentropy", optimizer="adadelta", metrics=["accuracy"])

modelo.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, verbose=1)

#Este es con un ejemplo en el que se predice Y
Y_prediccion = modelo.predict_classes(X_test)

np.savetxt('mnist_resultados.csv', np.c_[range(1,len(Y_prediccion)+1),Y_prediccion], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

############PLOTEO############
'''archivo generado da el path de los datos'''
dataExtraction(carpeta)



##############################
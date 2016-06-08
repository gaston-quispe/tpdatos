import numpy as np
import pandas

print("Cargando set de datos.")

set_train = pandas.read_csv('/home/val/mnist/train.csv').values
set_test = pandas.read_csv('/home/val/mnist/test.csv').values

#Separamos los labels (la primer columna contiene la clase de cada imagen).
Y_train = set_train.ix[1:,0]
X_train = set_train.ix[1:,1:]


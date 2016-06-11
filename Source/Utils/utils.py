# particiona el vector 'vec_in' en dos vectores
# porcentaje_train: 0 a 1 . Porcentaje de muestras
# que se van a vec_out_train
import os
import time

def particionar_train_test(vec_in, porcentaje_train):
    vec_out_train = vec_in[:porcentaje_train*len(vec_in),:]
    vec_out_test  = vec_in[porcentaje_train*len(vec_in):,:]

    return vec_out_train, vec_out_test


###########################

# getMomento()
# esta boludez es para darle nombre distinto a las carpetas que se van a ir generando
# a medida que hacemos pruebas
# formado: dia_HoraMinutosSegundos 24 hs
def getMomento():
    return time.strftime("%d_%H%M%S")

def generarCarpeta():
    momento = getMomento()
    carpeta_archivos = "/home/darius/workspace/RESULTADOSTP/"+momento
    if not os.path.exists(carpeta_archivos):
        os.makedirs(carpeta_archivos)
    return carpeta_archivos

############################
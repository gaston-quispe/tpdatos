
import matplotlib.pyplot as plt
import numpy as np

# plotear
# Usar Parser primero, el archivo pasado por parametro tiene que estar previamente procesado
# archivoDeDatos = ruta del archivo ya procesado
def plotear(archivoDeDatos,savingFolder):
    
    datos = ['loss','accuracy']
    data = np.genfromtxt(archivoDeDatos,delimiter = ',',skip_header = 1,skip_footer = 1,names = datos)
    
    for i in datos:
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.plot(data[i],color='r', label=i)
        #plt.show()
        direccion = savingFolder+"/"+i+".png"
        plt.savefig(direccion)
        plt.close()

if __name__ == '__main__':
    pass
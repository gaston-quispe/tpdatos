'''
Created on 10 de jun. de 2016

@author: darius
'''

from Utils.Parser import parsear
from Utils.Ploteo import plotear

def dataExtraction(folderPath):
    
    archivoSinProcesar = folderPath + '/datosBrutos.log'
    archivoProcesado   = folderPath + '/datosProcesados.csv'
    
    parsear(archivoSinProcesar,archivoProcesado)
    plotear(archivoProcesado,folderPath)
    

'''
Created on 10 de jun. de 2016

@author: darius
'''
import unittest
from Utils.Parser import parsear

class TestParser(unittest.TestCase):
    

    def testParser(self):
        inputFile  = '/home/darius/workspace/RESULTADOSTP/11_012317/datosBrutos.log'
        outputFile = '/home/darius/workspace/RESULTADOSTP/11_012317/datosProcesados.csv'
        parsear(inputFile,outputFile)
        
        
if __name__ == "__main__":

    unittest.main()
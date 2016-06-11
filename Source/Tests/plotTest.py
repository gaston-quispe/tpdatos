'''
Created on 10 de jun. de 2016

@author: darius
'''
import unittest
from Utils import Ploteo


class TestPlot(unittest.TestCase):


    def testPloteo(self):
        Ploteo.plotear('/home/darius/workspace/RESULTADOSTP/probando.csv')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
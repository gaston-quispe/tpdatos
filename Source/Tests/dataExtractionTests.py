'''
Created on 10 de jun. de 2016

@author: darius
'''
import unittest
from Utils.DataExtractor import dataExtraction

class Test(unittest.TestCase):

    def setUp(self):
        self.folderPath = "/home/darius/workspace/RESULTADOSTP/11_001059"
        
    def testDataExtraction(self):
        dataExtraction(self.folderPath)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
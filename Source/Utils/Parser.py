'''
Created on 10 de jun. de 2016

@author: darius
'''
import csv

def parsear(inputFilePath,outputFilePath):
    harcode = open(inputFilePath)
    harcode.close()
    with open(inputFilePath) as f:
        f = f.readlines()
    
        with open(outputFilePath,'wb') as csvfile:
            outputFile = csv.writer(csvfile,delimiter = ',')
            outputFile.writerow(['loss','accuracy'])
        
            for linea in f:
                if linea.find('ETA: ')!=-1:
                    accPosition = linea.index("acc")+5
                    lossPosition = linea.index("loss")+6
                    outputFile.writerow([linea[lossPosition:lossPosition+6],linea[accPosition:accPosition+6]])

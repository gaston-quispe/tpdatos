'''
Created on 9 de jun. de 2016

@author: darius
'''
import sys
import os

class Logger(object):
    def __init__(self,nombre):
        self.terminal = sys.stdout
        self.log = open(nombre, "wb")

    def write(self, message):
        #Sorry por el harcodeo animal
        message = message.replace('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b','\n')
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()
        os.fsync(self.log)
    
    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass
    
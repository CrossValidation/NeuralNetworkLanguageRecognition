'''
Created on 20/mag/2016

@author: lorenzo
'''

class wordAndValue(object):
    '''
    classdocs
    '''


    def __init__(self, word, value):
        '''
        Constructor
        '''
        self.word = word
        self.value = value
        self.result = -1
        
    def getWord(self):
        return self.word
    def getValue(self):
        return self.value
    
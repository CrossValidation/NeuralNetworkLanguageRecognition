'''
Created on 09/giu/2016

@author: lorenzo
'''
from CodeWarrior.CodeWarrior_suite import target

class performances(object):
    '''
    classdocs
    '''
    

    def __init__(self, params):
        '''
        Constructor
        '''
        #0 is Italian
        self.trueItalian = 0
        self.falseItalian = 0
        #1 is English
        self.trueEnglish = 0
        self.falseEnglish = 0
       
        
    def updatePerformance(self,computeObjectList):
        
        for computeObject in computeObjectList:
            target = computeObject.value
            result = computeObject.result
            result = round(result)
            if target == 1: #is  English word
                if  result == 1:
                    self.trueEnglish = self.trueEnglish + 1
                else:
                    self.falseItalian = self.falseItalian + 1
            else:#is Italian word
                if result == 0:
                    self.trueItalian = self.trueItalian + 1
                else:
                    self.falseEnglish = self.falseEnglish + 1
    
    
    def italianCorrectnessRate(self):
        return (self.trueItalian/(self.trueItalian + self.falseEnglish))     
    def englishCorrectnessRate(self):
        return (self.trueEnglish/(self.trueEnglish + self.falseItalian))
    def totalCorrectnessRate(self):
        return ((self.trueItalian + self.trueItalian) / (self.falseItalian + self.falseEnglish))
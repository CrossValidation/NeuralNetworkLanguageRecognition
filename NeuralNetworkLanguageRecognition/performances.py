class Performances(object):  

    def __init__(self):
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
            if result <= 0.6:
                result = 0
            else:
                result = 1
            
            if int(target) == 1: #is  English word
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
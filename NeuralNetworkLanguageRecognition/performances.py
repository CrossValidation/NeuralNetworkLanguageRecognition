from datetime import datetime

class Performances(object):  

    def __init__(self,k):
        #0 is Italian
        self.trueItalians = []
        self.falseItalians = []
        #1 is English
        self.trueEnglishs = []
        self.falseEnglishs = []
        self.k = k
        UNIQUE_ID = str(datetime.now().time()).replace(":","_")
        self.nameFile = UNIQUE_ID + "_performances.txt" 
       
        
    def updatePerformance(self,computeObjectList,numIter,numNet):
        self.trueItalian = 0
        self.falseItalian = 0
        self.trueEnglish = 0
        self.falseEnglish = 0
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
        self.trueItalians.append(self.trueItalian)
        self.falseItalians.append(self.falseItalian)
        self.trueEnglishs.append(self.trueEnglish)
        self.falseEnglishs.append(self.falseEnglish)
        out_file = open(self.nameFile,"a")
        out_file.write("Iterazione: {} ".format(numIter))
        out_file.write("Network: {} ".format(numNet))
        out_file.write("trueItalian: {}\n".format(self.trueItalian))
        out_file.write("falseItalian: {}\n".format(self.falseItalian))
        out_file.write("trueEnglish: {}\n".format(self.trueEnglish))
        out_file.write("falseEnglish: {}\n".format(self.falseEnglish))
        out_file.write("-------------------------------------------------\n")
        if numIter == self.k:
            out_file.write("Mean\n")
            out_file.write("Iterazione: {} ".format(numIter))
            out_file.write("Network: {} ".format(numNet))
            out_file.write("trueItalian: {}\n".format(self.meanTrueItalian()))
            out_file.write("falseItalian: {}\n".format(self.meanFalseItalian()))
            out_file.write("trueEnglish: {}\n".format(self.meanTrueEnglish()))
            out_file.write("falseEnglish: {}\n".format(self.meanFalseEnglish()))
            out_file.write("ItalianCorrectnessRate: {}\n".format(self.italianCorrectnessRate()))
            out_file.write("EnglishCorrectnessRate: {}\n".format(self.englishCorrectnessRate()))
            out_file.write("TotalCorrectnessRate: {}\n".format(self.totalCorrectnessRate()))
        out_file.close()
    
        
        
    def meanTrueItalian(self):   
        return sum(self.trueItalians)/len(self.trueItalians)
    def meanFalseItalian(self):
        return sum(self.falseItalians)/len(self.falseItalians)
    def meanTrueEnglish(self):
        return sum(self.trueEnglishs)/len(self.trueEnglishs)
    def meanFalseEnglish(self):
        return sum(self.falseEnglishs)/len(self.falseEnglishs)
    
    
    def italianCorrectnessRate(self):
        return (sum(self.trueItalians)/(sum(self.trueItalians) + sum(self.falseEnglishs)))     
    def englishCorrectnessRate(self):
        return (sum(self.trueEnglishs)/(sum(self.trueEnglishs) + sum(self.falseItalians)))
    def totalCorrectnessRate(self):
        return ((sum(self.trueItalians) + sum(self.trueEnglishs)) / (sum(self.falseItalians) + sum(self.falseEnglishs)))
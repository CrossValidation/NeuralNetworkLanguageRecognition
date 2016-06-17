from datetime import datetime

class Performances(object):  

    def __init__(self, k):
        # 0 is Italian
        self.trueItalians = []
        self.falseItalians = []
        # 1 is English
        self.trueEnglishs = []
        self.falseEnglishs = []
        self.k = k
        UNIQUE_ID = str(datetime.now().time()).replace(":", "_")
        self.nameFile = UNIQUE_ID + "_performances.txt" 
       
        
    def updatePerformance(self, computeObjectList, numIter, numNet, network, printNetworkShape = False):
        self.trueItalian = 0
        self.falseItalian = 0
        self.trueEnglish = 0
        self.falseEnglish = 0
        
        #threshold computation
        threshold = 0
        for computeObject in computeObjectList:
            threshold += computeObject.result
        threshold = threshold/len(computeObjectList)
            
        for computeObject in computeObjectList:
            target = computeObject.value
            result = computeObject.result
            if result <= threshold:
                result = 0
            else:
                result = 1
            
            if int(target) == 1:  # is  English word
                if  result == 1:
                    self.trueEnglish = self.trueEnglish + 1
                else:
                    self.falseItalian = self.falseItalian + 1
            else:  # is Italian word
                if result == 0:
                    self.trueItalian = self.trueItalian + 1
                else:
                    self.falseEnglish = self.falseEnglish + 1
        self.trueItalians.append(self.trueItalian)
        self.falseItalians.append(self.falseItalian)
        self.trueEnglishs.append(self.trueEnglish)
        self.falseEnglishs.append(self.falseEnglish)
        out_file = open(self.nameFile, "a")
        out_file.write("Iteration: {} ".format(numIter))
        out_file.write("Network: {} \n".format(numNet))
        if (printNetworkShape == True):
            out_file.write("---- Start Network shape ----\n")
            out_file.write(network.toString())
            out_file.write("---- End Network shape ----\n")
        out_file.write("trueItalian: {}\n".format(self.trueItalian))
        out_file.write("falseItalian: {}\n".format(self.falseItalian))
        out_file.write("trueEnglish: {}\n".format(self.trueEnglish))
        out_file.write("falseEnglish: {}\n".format(self.falseEnglish))
        out_file.write("-------------------------------------------------\n")
        if numIter == self.k:
            out_file.write("Confusion matrix\n")
            out_file.write("trueItalian: {}\n".format(sum(self.trueItalians)))
            out_file.write("falseItalian: {}\n".format(sum(self.falseItalians)))
            out_file.write("trueEnglish: {}\n".format(sum(self.trueEnglishs)))
            out_file.write("falseEnglish: {}\n".format(sum(self.falseEnglishs)))
            out_file.write("ItalianCorrectnessRate: {}\n".format(self.italianCorrectnessRate()))
            out_file.write("EnglishCorrectnessRate: {}\n".format(self.englishCorrectnessRate()))
            out_file.write("TotalCorrectnessRate: {}\n".format(self.totalCorrectnessRate()))
            out_file.write("\n\n")
            # 0 is Italian
            self.trueItalians = []
            self.falseItalians = []
            # 1 is English
            self.trueEnglishs = []
            self.falseEnglishs = []
        out_file.close()
 
    def italianCorrectnessRate(self):
        return sum(self.trueItalians) / float((sum(self.trueItalians) + sum(self.falseEnglishs))) * 100     
    def englishCorrectnessRate(self):
        return sum(self.trueEnglishs) / float((sum(self.trueEnglishs) + sum(self.falseItalians))) * 100
    def totalCorrectnessRate(self):
        return (sum(self.trueItalians) + sum(self.trueEnglishs)) / float(sum(self.falseItalians) + sum(self.falseEnglishs) + sum(self.trueEnglishs) + sum(self.trueItalians)) * 100

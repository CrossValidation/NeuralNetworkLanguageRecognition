import random
import math

TO_STRING_OFFSET = 28

class Element(object):
    def fi(self):
        pass
    
    def toString(self, levels=[{'level' :0, 'last': False}]):
        pass

class Input(Element):
    
    def __init__(self, value=0):
        self.value = value
    
    def fi(self):
        return self.value
    
    def toString(self, levels=[{'level' :0, 'last': False}]):
        return str(self.value)

class Perceptron(Element):
    
    def __init__(self, inputs, weights=[]):
        self.inputs = []
        if len(weights) == 0:
            randomWeigths = True
        else :
            assert len(inputs) == len(weights)
            randomWeigths = False
        for index, perceptronInput in enumerate(inputs):
            dictionary = {"input": perceptronInput}
            if randomWeigths is True:
                dictionary["weight"] = random.uniform(-0.5, 0.5)
            else:
                dictionary["weight"] = weights[index]
            self.inputs.append(dictionary)  

    def fi(self):
        return 1 / (1 + math.exp(-self.entryPoint()))
    
    def entryPoint(self):
        summatory = 0
        for perceptronInput in self.inputs:
            summatory += perceptronInput["input"].fi() * perceptronInput["weight"]
        return summatory
    
    def toString(self, levels=[{'level' :0, 'last': False}]):
        level = levels[-1]['level']
        last = levels[-1]['last']
        string = "Perceptron\n"
        for index, perceptronInput in enumerate(self.inputs):
            spaces = ""
            for levelInfo in levels[1 : len (levels)]:
                if levelInfo['last'] == True:
                    spaces = spaces + " "
                else:
                    spaces = spaces + "|"
                spaces = spaces + " "* TO_STRING_OFFSET
            if (index < (len(self.inputs) - 1)):
                last = False
            else:
                last = True
            string = string + spaces
            string = string + "|---[{}]---".format(perceptronInput["weight"])
            newLevels = levels[:]
            newLevels.append({'level' :level+TO_STRING_OFFSET, 'last': last})
            string = string + perceptronInput["input"].toString(levels=newLevels)
            if (index < (len(self.inputs) - 1)):
                string = string + "\n"
            else:
                string = string + "\n" + spaces
        return string

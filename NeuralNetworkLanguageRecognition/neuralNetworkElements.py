import random
import math

class Element(object):
    def fi(self):
        pass
    
    def toString(self, level=0):
        pass

class Input(Element):
    
    def __init__(self, value=0):
        self.value = value
    
    def fi(self):
        return self.value
    
    def toString(self, level=0):
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
        try:
            for perceptronInput in self.inputs:
                summatory += perceptronInput["input"].fi() * perceptronInput["weight"]
        except Exception as e:
            print (e)
        return summatory
    
    def toString(self, level=0):
        str = "Perceptron\n"
        for perceptronInput in self.inputs: 
            spaces = " "* level
            str = str + spaces
            str = str + "|---[{}]---".format(perceptronInput["weight"])
            str = str + perceptronInput["input"].toString(level=level + 30)
            str = str + "\n"
        return str

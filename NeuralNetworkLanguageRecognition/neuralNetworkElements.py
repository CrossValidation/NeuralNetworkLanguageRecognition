import random
import math

class Element(object):
    def fi(self):
        pass

class Input(Element):
    
    def __init__(self, value=0):
        self.value = value
    
    def fi(self):
        return self.value

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

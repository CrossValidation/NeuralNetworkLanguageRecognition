import random


class Element(object):
    def activated(self):
        pass

class Input(Element):
    
    def __init__(self, activate=0):
        self.isActivate = activate
    
    def activated(self):
        return self.isActivate

class Perceptron(Element):
    
    def __init__(self, inputs, treshold=0, weights=[]):
        self.treshold = 0
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
        
    def weightsUpdate(self):
        # todo
        pass
        
    def activated(self):
        summatory = 0
        for perceptronInput in self.inputs:
            summatory += perceptronInput["input"].activated() * perceptronInput["weight"]
        if summatory > self.treshold:
            return 1
        else:
            return 0
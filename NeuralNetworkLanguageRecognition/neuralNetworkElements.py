import random


class Element(object):
    def activeted(self):
        pass

class Input(Element):
    
    def __init__(self, activate=0):
        self.isActivate = activate
    
    def activeted(self):
        return self.isActivate

class Perceptron(Element):
    
    def __init__(self, inputs, treshold=0):
        self.treshold = 0
        self.inputs = []
        for perceptronInput in inputs:
            self.inputs.append({"input": perceptronInput,
                                "weight" : random.uniform(-0.5, 0.5)})
        
    def weightsUpdate(self):
        # todo
        pass
        
    def activeted(self):
        summatory = 0
        for perceptronInput in self.inputs:
            summatory += perceptronInput["input"].activeted() * perceptronInput["weight"]
        if summatory > self.treshold:
            return 1
        else:
            return 0
    

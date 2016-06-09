import unittest

from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input
from NeuralNetworkLanguageRecognition import backPropagation

class Test(unittest.TestCase):

    def testPerceptron(self):
        inputs = [ Input(1), Input(0), Input(1)]
        weights = [0.5, 0, -0.6]
        perceptron = Perceptron(inputs=inputs, weights=weights)
        assert (perceptron.fi() > 0.475 and perceptron.fi() < 0.476)

    def testPerceptronsNetwork(self):
        inputsPerceptron1 = [Input(1), Input(0), Input(1)]
        weightsPerceptron1 = [0.7, -0.3, 1]
        inputsPerceptron2 = [Input(1), Input(0)]
        weightsPerceptron2 = [-0.4, -0.5]
        perceptron1 = Perceptron(inputs=inputsPerceptron1, weights=weightsPerceptron1)
        perceptron2 = Perceptron(inputs=inputsPerceptron2, weights=weightsPerceptron2)
        perceptron3 = Perceptron(inputs=[perceptron1, perceptron2], weights=[0.7, 0.3])
        assert (perceptron3.fi() > 0.6709 and perceptron3.fi() < 0.671)
        
    def testOneHidden(self):
        inputsPerceptron1 = [Input(1), Input(0), Input(1)]
        weightsPerceptron1 = [0.7, -0.3, 1]
        inputsPerceptron2 = [Input(1), Input(0)]
        weightsPerceptron2 = [-0.4, -0.5]
        perceptron1 = Perceptron(inputs=inputsPerceptron1, weights=weightsPerceptron1)
        perceptron2 = Perceptron(inputs=inputsPerceptron2, weights=weightsPerceptron2)        
        perceptron3 = Perceptron(inputs=[perceptron1, perceptron2], weights=[0.7, 0.3])
        
        print("\n")
        print(perceptron3.fi())
        backPropagation.computeFormula(perceptron3, expected=1, n=1)
        print(perceptron3.fi())
        
    def testTwoHidden(self):
        inputsPerceptron1 = [Input(1), Input(0), Input(1)]
        weightsPerceptron1 = [0.7, -0.3, 1]
        inputsPerceptron2 = [Input(1), Input(0)]
        weightsPerceptron2 = [-0.4, -0.5]
        
        perceptron1 = Perceptron(inputs=inputsPerceptron1, weights=weightsPerceptron1)
        perceptron2 = Perceptron(inputs=inputsPerceptron2, weights=weightsPerceptron2) 
        perceptron3 = Perceptron(inputs=[perceptron1], weights=[0.2])
        perceptron4 = Perceptron(inputs=[perceptron2], weights=[0.1])
        perceptron5 = Perceptron(inputs=[perceptron3, perceptron4], weights=[0.7, 0.3])
        
        print("\n")
        print(perceptron5.fi())
        backPropagation.computeFormula(perceptron5, expected=1, n=0.5)
        print(perceptron5.fi())
       
    def testNoHidden(self):
        inputsPerceptron1 = [Input(1), Input(0), Input(1)]
        weightsPerceptron1 = [0.7, -0.3, 1]
        
        perceptron1 = Perceptron(inputs=inputsPerceptron1, weights=weightsPerceptron1)
        print("\n")
        print(perceptron1.fi())
        backPropagation.computeFormula(perceptron1, expected=1, n=0.5)
        print(perceptron1.fi())
        
if __name__ == "__main__":
    unittest.main()

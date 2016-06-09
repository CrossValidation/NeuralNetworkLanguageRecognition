import unittest

from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input

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

if __name__ == "__main__":
    unittest.main()

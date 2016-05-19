import unittest

from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input

class Test(unittest.TestCase):

    def testPerceptron(self):
        inputs = [ Input(1), Input(0), Input(1)]
        weights = [0.5, 0, -0.6]
        perceptron = Perceptron(inputs=inputs, weights=weights)
        assert (perceptron.activated() == 0)

    def testPerceptronsNetwork(self):
        inputsPerceptron1 = [Input(1), Input(0), Input(1)]
        weightsPerceptron1 = [0.7, -0.3, 1]
        inputsPerceptron2 = [Input(1), Input(0)]
        weightsPerceptron2 = [-0.4, -0.5]
        perceptron1 = Perceptron(inputs=inputsPerceptron1, weights=weightsPerceptron1)
        assert (perceptron1.activated() == 1)
        perceptron2 = Perceptron(inputs=inputsPerceptron2, weights=weightsPerceptron2)
        assert (perceptron2.activated() == 0)
        perceptron3 = Perceptron(inputs=[perceptron1, perceptron2], weights=[0.7, 0.3])
        assert (perceptron3.activated() == 1)

if __name__ == "__main__":
    unittest.main()

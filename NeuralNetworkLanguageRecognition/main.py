from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input
from NeuralNetworkLanguageRecognition.encoder import Encoder
from NeuralNetworkLanguageRecognition import backPropagation
import numpy as np

if __name__ == '__main__':
    
    #creation of neural network
    firstLayer = []
    for index in range(0, 50, 5):
            firstLayer.append(Perceptron(inputs=[Input(),Input(),Input(),Input(),Input()]))
    secondLayer = []
    for index in range(0, len(firstLayer), 2):
        secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                              firstLayer[index+1]]))
    output = Perceptron(inputs=secondLayer)
    
    #get training examples
    encoder = Encoder()
    trainingExamples = encoder.getWord(0, 0, 500)
      
    #training
    for wordAndValue in trainingExamples:
        word = wordAndValue.word
        assert (len(word) == 50)
        #update neural network input
        for index, perceptron in enumerate(firstLayer):
            for indexInput, inputPerceptron in enumerate(perceptron.inputs):
                inputPerceptron["input"].value = int(word[(index*5+ indexInput)])
        #learning
        backPropagation.computeFormula(output, expected=float(wordAndValue.value), n=0.5)
    
    #get testing examples
    encoder = Encoder()
    testingExamples = encoder.getWord(1, 0, 100)
      
    #testing
    for wordAndValue in testingExamples:
        word = wordAndValue.word
        assert (len(word) == 50)
        #update neural network input
        for index, perceptron in enumerate(firstLayer):
            for indexInput, inputPerceptron in enumerate(perceptron.inputs):
                inputPerceptron["input"].value = int(word[(index*5+ indexInput)])
        wordAndValue.result = output.fi()
        
    for example in testingExamples:
        print ("word:{} value:{} result:{}".format(example.word, example.value, example.result))
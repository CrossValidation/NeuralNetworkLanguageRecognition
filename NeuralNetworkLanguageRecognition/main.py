from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input
from NeuralNetworkLanguageRecognition.encoder import Encoder
from NeuralNetworkLanguageRecognition import backPropagation
from NeuralNetworkLanguageRecognition.performances import Performances

def crossValidation(output, inputLayer, numberIteration, learning=True):
    # get examples
    if (learning == True):
        examples = encoder.getTraining(numberIteration)
    else:
        examples = encoder.getTesting(numberIteration)
    
    for wordAndValue in examples:
        word = wordAndValue.word
        #print wordAndValue.originalWord
        assert (len(word) == 50)
        # update neural network input
        for index, inputObj in enumerate(inputLayer):
                inputObj.value = int(word[index])
        if (learning == True):
            # learning
            backPropagation.computeFormula(output, expected=float(wordAndValue.value), n=0.5)
        else:
            wordAndValue.result = output.fi()
    
    if learning == False:
        return examples

def createNeuralNetwork ():
    # creation of neural network
    inputLayer = []
    for index in range(0, 50):
        inputLayer.append(Input())
    firstLayer = []
    for index in range(0, 50, 5):
        firstLayer.append(Perceptron(inputs=inputLayer[index : index + 5]))
    secondLayer = []
    for index in range(0, len(firstLayer), 2):
        secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                              firstLayer[index + 1]]))
    output = Perceptron(inputs=secondLayer)
    return output, inputLayer 

if __name__ == '__main__':
    encoder = Encoder(10)
    performances = []
    for index in range(1, 11):
        output, inputLayer = createNeuralNetwork()
        crossValidation(output, inputLayer, index, learning=True)
        testingExamples = crossValidation(output, inputLayer, index, learning=False)
        performancesObj = Performances()
        performances.append(performancesObj.updatePerformance(testingExamples))
        print("Iterazione {}".format(index))
        print("trueItalian: {}".format(performancesObj.trueItalian))
        print("falseItalian: {}".format(performancesObj.falseItalian))
        print("trueEnglish: {}".format(performancesObj.trueEnglish))
        print("falseEnglish: {}".format(performancesObj.falseEnglish))
        print("-------------------------------------------------")

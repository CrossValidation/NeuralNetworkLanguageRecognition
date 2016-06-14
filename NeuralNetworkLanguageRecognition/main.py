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

def createNeuralNetwork (numberOfNetwork = 0):
    # creation of neural network
    inputLayer = []
    for index in range(0, 50):
        inputLayer.append(Input())
    firstLayer = []
    for index in range(0, 50, 5):
        firstLayer.append(Perceptron(inputs=inputLayer[index : index + 5]))
    secondLayer = []
    thirdLayer = []
    if (numberOfNetwork == 0): 
        for index in range(0, len(firstLayer), 2):
            secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                                  firstLayer[index + 1]]))
        output = Perceptron(inputs=secondLayer)
    elif(numberOfNetwork == 1):  
        for index in (0, 2, 4):
            secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                                  firstLayer[index + 1]]))
        secondLayer.append(Perceptron(inputs=[firstLayer[6],
                                       firstLayer[7],
                                       firstLayer[8],
                                       firstLayer[9]]))
        
        output = Perceptron(inputs=secondLayer)
    elif(numberOfNetwork == 2):
        for index in (0, 3):
            secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                                  firstLayer[index + 1],
                                                  firstLayer[index + 2]]))
        secondLayer.append(Perceptron(inputs=[firstLayer[6],
                                       firstLayer[7],
                                       firstLayer[8],
                                       firstLayer[9]]))
        output = Perceptron(inputs=secondLayer)
    elif(numberOfNetwork == 3):
        for index in  range(0, len(firstLayer), 2):
            secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                                  firstLayer[index + 1]]))
        thirdLayer.append(Perceptron(inputs=[secondLayer[0],
                                              secondLayer[1]]))
        thirdLayer.append(Perceptron(inputs=[secondLayer[2],
                                              secondLayer[3],
                                              secondLayer[4]]))
        output = Perceptron(inputs=thirdLayer)
    else:
        for index in range(0, len(firstLayer), 5):
            secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                                  firstLayer[index + 1],
                                                  firstLayer[index + 2],
                                                  firstLayer[index + 3],
                                                  firstLayer[index + 4]]))
        output = Perceptron(inputs=secondLayer)
    return output, inputLayer 

if __name__ == '__main__':
    encoder = Encoder(10)
    performancesObj = Performances(10)
    for numberOfNetwork in range(0,5):
        output, inputLayer = createNeuralNetwork(numberOfNetwork)
        performances = []
        for index in range(1, 11):
            crossValidation(output, inputLayer, index, learning=True)
            testingExamples = crossValidation(output, inputLayer, index, learning=False)
            performances.append(performancesObj.updatePerformance(testingExamples, index, numberOfNetwork, output))
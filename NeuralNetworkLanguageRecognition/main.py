from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input
from NeuralNetworkLanguageRecognition.encoder import Encoder
from NeuralNetworkLanguageRecognition import backPropagation

def crossValidation(learning = True, _from=0, _to=100):
    #get examples
    encoder = Encoder()
    if (learning == True):
        examples = encoder.getWord(0, _from, _to)
    else:
        examples = encoder.getWord(1, _from, _to)
        
    for wordAndValue in examples:
        word = wordAndValue.word
        assert (len(word) == 50)
        #update neural network input
        for index, perceptron in enumerate(firstLayer):
            for indexInput, inputPerceptron in enumerate(perceptron.inputs):
                inputPerceptron["input"].value = int(word[(index*5+ indexInput)])
        if (learning == True):
            #learning
            backPropagation.computeFormula(output, expected=float(wordAndValue.value), n=0.5)
        else:
            wordAndValue.result = output.fi()
    if learning == False:
        return examples
    
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
    crossValidation(True, 0, 100)
    testingExamples = crossValidation(False, 0, 100)
    
    for example in testingExamples:
        print ("word:{} value:{} result:{}".format(example.word, example.value, example.result))

    
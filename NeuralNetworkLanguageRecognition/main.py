from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input
from NeuralNetworkLanguageRecognition.encoder import Encoder
from NeuralNetworkLanguageRecognition import backPropagation

if __name__ == '__main__':
    encoder = Encoder()
    wordsAndValues = encoder.getWord(0, 0, 100)
    for wordAndValue in wordsAndValues:
        word = wordAndValue.word
        assert (len(word) == 50)
        firstLayer = []
        for index in range(0, len(word), 5):
            firstLayer.append(Perceptron(inputs=[Input(int(word[index])),
                               Input(int(word[index + 1])),
                               Input(int(word[index + 2])),
                               Input(int(word[index + 3])),
                               Input(int(word[index + 4]))]))
        secondLayer = []
        for index in range(0, len(firstLayer), 2):
            secondLayer.append(Perceptron(inputs=[firstLayer[index],
                                                  firstLayer[index+1]]))
        output = Perceptron(inputs=secondLayer)
        print "-----------------------------------"
        before = output.fi()
        print "Before back: %s " % before
        backPropagation.computeFormula(output, expected=float(wordAndValue.value), n=0.1)
        print "Expected: %s " % wordAndValue.value
        after = output.fi()
        print "After back: %s" % after 
        if after > before:
            print "Result: 1 "
        else:
            print "Result: 0 "
        
        
        
            
            
            
            

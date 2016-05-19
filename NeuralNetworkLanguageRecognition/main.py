from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron, Input
def onePerceptron():
    inputs = [ Input(1), Input(1), Input()]
    perceptron = Perceptron(inputs=inputs)
    print (perceptron.inputs)
    print (perceptron.activeted())
    
def perceptronNetwork():
    input1 = Input(1)
    input2 = Input(1)
    input3 = Input(1)
    input4 = Input(1)
    perceptron1 = Perceptron(inputs=[input1, input2])
    perceptron2 = Perceptron(inputs=[input3, input4])
    perceptron3 = Perceptron(inputs=[perceptron1, perceptron2])
    print (perceptron1.inputs)
    print (perceptron2.inputs)
    print (perceptron3.inputs)
    print (perceptron3.activeted())
    
    
if __name__ == '__main__':
    # onePerceptron()
    perceptronNetwork()
   
    

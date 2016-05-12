from neuralNetworkElements  import Perceptron, Input

if __name__ == '__main__':
    inputs = [ Input(1), Input(1), Input()]
    perceptron = Perceptron(inputs=inputs)
    print perceptron.inputs
    print perceptron.activeted()
    

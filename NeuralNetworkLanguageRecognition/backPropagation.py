from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron


def computeFormula(network):
    d=[]
    fiprimo=[]
    j=0
    
    #NOT really like THIS: we need the neurons in the OUTPUT LEVEL in this "for" loop!
    for perceptron in network:
        yj=perceptron.fi()
        
        #ej = dj - yj: compute error at neuron j as difference between what I expected and the obtained output (yj)
        ej=perceptron.expected-yj
        
        #fiprimo = yj[1-yj]
        fiprimo[j]=yj*(1-yj)
       
        #dj = ej * fiprimo (see formula [A]): compute delta_j as product of error at j and derivative applied to output
        d[j]=ej*fiprimo[j]
        j = j+1
        
        
    #until now we have computed the deltas for the output layer: from here, we have to back-propagate them
    n=0.5
    deltaw=[]   
    
    #L = # of layers in network
    L = network.layers
    
    i=0
    #we have to reach the input level: is it 0 or 1?
    for l in range(L-1,0):
        #in the following "for", I'm trying to extract nodes in level "l" of the network
        for nodes in network.layers(l):
            j=0
            for yi in perceptron.inputs:
                sum = perceptron.inputs[yi]["weights"]*d[j]
                j = j+1            
            #compute the delta_i
            d[i] = fiprimo[i] * sum
            i = i+1
            
            
    #delta_wij = n * dj * yi (see formula [A])
    j=0
    for yi in perceptron.inputs:
        deltaw=n*d[j]*yi
        perceptron.inputs[yi]["weights"]+=deltaw;
        j = j+1
    
    
   
    
        



    
        

        
        
    
        
        
        
                
    
    
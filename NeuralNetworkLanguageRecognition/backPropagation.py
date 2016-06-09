from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron
    

def computeFormula(perceptronOutput, n = 0.5, expected = 1):
    d=[]
    fiprimo=[]
    
    #we're assuming that there's just ONE output perceptron    
    yj=perceptronOutput.fi()    
    #ej = dj - yj: compute error at neuron j as difference between what I expected and the obtained output (yj)
    ej=expected-yj    
    #fiprimo = yj[1-yj]
    fiprimoj=yj*(1-yj)   
    #dj = ej * fiprimo (see formula [A]): compute delta_j as product of error at j and derivative applied to output
    dj=ej*fiprimoj
        
    #until now we have computed the deltas for the output layer: from here, we have to back-propagate them
    deltaw=[]    
    i=0    
    currentPerceptron = perceptronOutput
    if(currentPerceptron.inputs):
        layer = currentPerceptron.inputs  
        #in the following "for" I iterate over the perceptrons in input to the current perceptron
        for p in layer:
            if(p.isclass(Perceptron)):
                j=0
                for yi in p.inputs:
                    pseudosum = p.inputs[yi]["weights"]*dj
                    j = j+1            
                #compute the delta_i
                d[i] = fiprimo[i] * pseudosum
                i = i+1            
            
    #delta_wij = n * dj * yi (see formula [A])
    j=0
    currentPerceptron = perceptronOutput
    if(currentPerceptron.inputs):
        layer = currentPerceptron.inputs
        for yi in layer:
            deltaw=n*d[j]*yi
            layer[yi]["weights"]+=deltaw;
            j = j+1
   
    
        



    
        

        
        
    
        
        
        
                
    
    
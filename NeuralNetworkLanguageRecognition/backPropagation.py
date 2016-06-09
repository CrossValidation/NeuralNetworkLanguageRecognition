from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron
import math
    
def fiprimo(x):
    return math.exp(x)/(math.pow((math.exp(x)+1), 2))

def computeFormula(perceptronOutput, n = 0.5, expected = 1):
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
    d=[]
    nextl=[]  
    nextl.append(perceptronOutput)  
    
    for currentPerceptron in nextl:
        if(currentPerceptron.inputs):
            layer = currentPerceptron.inputs  
            #in the following "for" I iterate over the perceptrons in input to the current perceptron
            for inputP in layer:
                if(isinstance(inputP["input"], Perceptron)):
                    #for p in inputP["input"]:
                    p = inputP["input"]
                    pseudosum = inputP["weight"]*dj
                    #compute the delta_i
                    d.append(fiprimo(p.entryPoint()) * pseudosum)
                    nextl.append(p)
        
            
    #delta_wij = n * dj * yi (see formula [A])
    for currentPerceptron in nextl:
        if(currentPerceptron.inputs):
            layer = currentPerceptron.inputs  
            #in the following "for" I iterate over the perceptrons in input to the current perceptron
            for yi in layer:
                deltaw=n*dj*yi["input"].fi()
                yi["weight"]+=deltaw;
   
    
        



    
        

        
        
    
        
        
        
                
    
    
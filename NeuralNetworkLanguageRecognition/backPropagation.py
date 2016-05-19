from NeuralNetworkLanguageRecognition.neuralNetworkElements import Perceptron


def computeFormula(perceptron):
    yj=perceptron.fi();
    
    #ej = dj - yj
    ej=perceptron.expected-yj;
    
    #fiprimo = yj[1-yj]
    fiprimo=yj*(1-yj)
   
    #dj = ej * fiprimo (vedi formula [A])
    dj=ej*fiprimo
    
    n=0.5
    deltaw=[]   
    
    #delta_wij = n * dj * yi (vedi formula [A])
    for yi in perceptron.inputs:
        deltaw=n*dj*yi
        perceptron.inputs[yi]["weights"]+=deltaw;
    
    
   
    
        



    
        

        
        
    
        
        
        
                
    
    
import numpy as np

def sigmoid(x): # activation function
    return 1/(1+np.exp(-x)) # sigmoid function
    
class Neuron:
    def __init__(self , weight , bais):
        self.weight = weight
        self.bais = bais
        
    def Neuron_Output(self , input):
        self.input = input
        total = np.dot(self.input , weight) + bais
        return sigmoid(total)
        
input = np.array([1,2]) 
weight = np.array([1,1])
bais = 2

Neuron_1 = Neuron(weight , bais)
Neuron_1.Neuron_Output(input)



import numpy as np                                                              # import module numpy as np
import matplotlib.pyplot as plt                                                 # import matplotlib.pyplot as plt for drawing graph     															

inputData = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])                         # define inputData
referenceOutput1 = np.array([[0,1,1,0]]).T                                      # define referenceOutput1
referenceOutput2= np.array([[0,0,1,1]]).T                                       # define referenceOutput2
TN = 900                                                                        # define the TN as 900

np.random.seed(42)                                                              # setting a seed of 42 for the random function to get a consistent values for weights01, 
                                                                                # because we are using Numpy's random generator

X = np.zeros(TN)                                                                # define X as a array sets of number TN of zeros
Y = np.arange(0, TN)                                                            # define Y as a array from 0 to TN-1 in total of TN numbers


def sigmoid(x):                                                                 # Sigmoid function coded with Numpy                           
    return 1 / (1+np.exp(-x))                   

def sigmoidSlope(x):                                                            # Calculate the slope by useing the derivative of the sigmoid function                                      
    return x * (1-x)

def SL(TN,referenceOutput):                                                     # A function SL taking TN and referencOutput as input
    weights01 = 2*np.random.random((3,1)) - 1                                   # Weights of the synapses connection input and outputPerceptronLayer are randomly selected made into 3by1 matrix
    for i in range(TN):                                                         # A for loop in range of TN
        inputLayer = inputData                                                  # Set the input data for simple forward propagation                        				
        outputPerceptronLayer = sigmoid(np.dot(inputLayer,weights01))           # Apply Sigmoid Function to the dot product of two arrays   
        outputError = referenceOutput - outputPerceptronLayer                   # The difference between the output perceptron Layer and the reference output 
        X[i] = np.mean(np.abs(outputError))                                     # Changing the components of array X
        outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)         # The difference between reference (outputError) output multiplied by the slope of the sigmoid function at value of the output perceptron layer    
        weights01 += np.dot(inputLayer.T,outputDelta)                           # update the weights


def ML(TN,referenceOutput):                                                     # A function WL taking TN and referenceOutput as input
    weights02 = 2*np.random.random((3,4)) - 1                                   # Weights of the synapses connection input and hiddenLayer are randomly selected made into 3by4 matrix                
    weights03 = 2*np.random.random((4,1)) - 1                                   # Weights of the synapses connection hiddenLayer and outputPerceptronLayer are randomly selected made into 4by1 matrix               
    for i in range(TN):                                                         # A for loop in range of TN         
        inputLayer = inputData                                                  # Set the input data for simple forward propagation                
        hiddenLayer = sigmoid(np.dot(inputLayer, weights02))                    # Apply Sigmoid Function to the dot product of two arrays (inputLayer and weights02)
        outputPerceptronLayer = sigmoid(np.dot(hiddenLayer,weights03))          # Apply Sigmoid Function to the dot product of two arrays (hiddenLayer and weights03)    
        outputError = referenceOutput - outputPerceptronLayer                   # The difference between the output perceptron Layer and the reference output
        X[i] = np.mean(np.abs(outputError))                                     # Changing the components of array X
        outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)         # The difference between reference (outputError) output multiplied by the slope of the sigmoid function at value of the output perceptron layer     
        hiddenLayerError = outputDelta.dot(weights03.T)                         # implementation of backpropagation
        hiddenLayerDelta = hiddenLayerError * sigmoidSlope(hiddenLayer)         # The error contributed by the hidden layer multiplied by the slope of the sigmoid function at value of the hidden layer   
        weights03 += hiddenLayer.T.dot(outputDelta)                             # update the weights
        weights02 += inputData.T.dot(hiddenLayerDelta)                          # update the weights

    
plt.xlabel("training iteration")                                                # set xlabel of the graph as "training iteration"
plt.ylabel("outputError mean")                                                  # set ylabel of the graph as "outputError mean"
plt.title("Week12 Graph")                                                       # set title of the graph as "Week12  Graph"

SL(TN,referenceOutput1)                                                         # Run function SL(TN,referenceOutput1)
plt.plot(Y,X,label = "SingleLayer / referenceOutput1")                          # plot the graph and label as "SingleLayer / referenceOutput1"

ML(TN,referenceOutput1)                                                         # Run function ML(TN,referenceOutput1)
plt.plot(Y,X,label = "MultiLayer / referenceOutput1")                           # plot the graph and label as "MultiLayer / referenceOutput1"

SL(TN,referenceOutput2)                                                         # Run function SL(TN,referenceOutput2)
plt.plot(Y,X,label = "SingleLayer / referenceOutput2")                          # plot the graph and label as "SingleLayer / referenceOutput2"

ML(TN,referenceOutput2)                                                         # Run function ML(TN,referenceOutput2)
plt.plot(Y,X, label = "MultiLayer / referenceOutput2")                          # plot the graph and label as "MultiLayer / referenceOutput2"

plt.legend()                                                                    # show legend
plt.show()                                                                      # show the graph
plt.savefig("Week12BioPic.png")                                                 # save the graph in the name of "Week12BioPic" in png format




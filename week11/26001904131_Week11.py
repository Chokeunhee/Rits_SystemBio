#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:31:43 2019

@author: Chokeunhee
"""

# Question 1 Complete Python code for the simple neural network(one Neuron) and propagation mechanism (Exercise 1, 2, 3)


import numpy as np                                                              # import module numpy as np

inputData = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])                         # Exercise 1 setting the inputdata, define inputdata as an array 

# process of defining referenceOutput
print("[a,b,c,d] : input a, b, c, d,")                                          # print String
a = int(input("a : "))                                                          # input a string and change it as a data type integer and define as a
b = int(input("b : "))                                                          # input a string and change it as a data type integer and define as b
c = int(input("c : "))                                                          # input a string and change it as a data type integer and define as c
d = int(input("d : "))                                                          # input a string and change it as a data type integer and define as d

#referenceOutput = np.array([[0,0,1,1]]).T                                      #Exercise 1 setting referenceOutput as [[0][0][1][1]]

referenceOutput = np.array([[a,b,c,d]]).T                                       # define referenceOutput based on the data inputed make it as a tranformation matrix of [a,b,c,d]
Y = referenceOutput                                                             # define referenceOutput as Y
print("The referenceOutput is : ")                                              # print string
print(Y)                                                                        #print Y

np.random.seed(1)                                                               # Exercise 2 - setting a seed of 1 for the random function to get a consistent values for weights01, because we are using Numpy's random generator

def sigmoid(x):                                                                 # Sigmoid function coded with Numpy
	return 1/(1+np.exp(-x))                                                     

def sigmoidSlope(x):                                                            # Calculate the slope by useing the derivative of the sigmoid function
	return x * (1-x)                                                            

weights01 = 2*np.random.random((3,1))-1                                         # Weights of the synapses connection input and outputPerceptronLayer are randomly selected made into 3by1 matrix
#print(weights01)

i = 0                                                                           # define i as 0 (training number)

                                                                                # Exercise 3 - making a while loop to find the training iteration
while True:                                                                     # Start a while loop
    inputLayer = inputData                                                      # Set the input data for simple forward propagation
    outputPerceptronLayer = sigmoid(np.dot(inputLayer,weights01))               # Apply Sigmoid Function to the dot product of two arrays
    outputError = referenceOutput - outputPerceptronLayer                       # The difference between the output perceptron Layer and the reference output
    outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)             # The difference between reference (outputError) output multiplied by the slope of the sigmoid function at value of the output perceptron layer
    X = np.round(outputPerceptronLayer, decimals = 2)                           # round the outputPerceptronLayer for two decimal points
    
    if X[0] == Y[0] and X[1] == Y[1] and X[2] == Y[2] and X[3] == Y[3] :        # if the each compoments of X and Y is same
        print("Training iteration found : " , i)                                # print string and training number
        break                                                                   # break loop
 
    weights01 += np.dot(inputLayer.T, outputDelta)                              # update the weights
    i += 1                                                                      # define i as i + 1 (training number)


print("Output values after " + str(i) + " training iterations: ")               # print string / training number as string / and string
print(np.round(outputPerceptronLayer,decimals =2))                              # print the rounded outputPerceptronLayer

print(outputPerceptronLayer)                                                    # print the outputPerceptronLayer



# Question 2
#
# How can you change the slope of the Sigmoid function to reduce the number of steps in trainingNumber to get to the result satisfying condition in Exercise 3?
# Refer to Figure 3 and please indicate the chosen Sigmoid function in the comments of source code.
#
# From the figure 3, the the purple slope is x -> 2x and blue slope is x -> x/2 
# 
# So when coefficient of x is doubled(purple slope), the speed of changing throughout training iterations is faster. 
# It is because update of weights01 is influenced by outputDelta, which is the multiplied of outputError and sigmoidSlope(outputPerceptronLayer)
# sigmoidSlope and outputPerceptrinLayer are both influenced by sigmoid function proportionately.
#
# Therefore, in order to reduce the number of steps in trainingNumber to get to the result satisfying, use the purple slope.
# 
# for the purple slope 

#def sigmoid(x):
#    return 1/(1+np.exp(-2*x))

#def sigmoidSlope(x):
#    return 2*(np.exp(2*x)) / (np.exp(2*x)+1)**2 

#However if both is changed it is influenced twice. However according to the comment given of function sigmoidSlope it need to be changed
#










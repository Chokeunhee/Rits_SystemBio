#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:27:20 2019

@author: Chokeunhee
"""

import random #import module random
import string #import module string
import numpy as np #import numpy as the name np
import math

target = "Cho_keun_hee" # define a variable target as "CHO_KEUN_HEE"
                        # this is the goal of the genetic algorithm if the fitnessfunction is defined the output will be similar with this target
dnaLength = len(target) # define dnaLength as length of target
populationSize = 20 # set populationSize as 20
generations = 5000 # set generations as 5000
mutationChance = 100 # set mutationChance as 100

def randomGene(): # Define a function randomGene
    return random.choice(string.printable) # choose a random string and return the function as it

def initialPopulation(): # Define initialPopulation (this function is a set of 20(populationSize) strings)
    initPop = [] # Make a set named initPop
    for i in range(populationSize): # make a for loop in range of populationSize
        initPop.append(''.join(random.choice(string.printable) for i in range(dnaLength))) #make random string based on repeating random choice dnaLength times and append to the set
    return initPop # return initPop

#----------------------------------------------- fitness function -----------------------------------
# for all the equation function ord() is used in order to enable the calculation
# it is because the data type of DNAs are string. However it digits are needed in order to allow calculation
# therefore function ord() is used which convert them.


# Ex 1  from the bio lecture class
def fitnessFunction(competingDNA):                                  # define a function name fitnessFunction
    fitness = 0                                                     # define fitness as 0
    for i in range(dnaLength):                                      # make a for loop
        X = np.abs(ord(competingDNA[i])-ord(target[i]))             # X is defined as | xi -ti |  // xi is the number i component of competingdata, ti is the number i component of target data
        fitness += X                                                # fitness is defined as fitness + X ,which is (| xi -ti |) //and this step can be considered as Sigma
    return fitness                                                  # return the value fitness


#Ex 2 from the bio lecture class    
#def fitnessFunction(competingDNA):                                 # define a function name fitnessFunction
#    fitness = 0                                                    # define fitness as 0
#    for i in range(dnaLength):                                     # make a for loop
#        Y = math.pow((ord(competingDNA[i])-ord(target[i])),2)      # Y is defined as power of (xi-ti) // xi is the number i component of competingdata, ti is the number i component of target data
#        fitness += Y                                               # fitness is defined as fintness + Y
#    return fitness                                                 # return the value fitness


#Ex 3 from the bio lecture class
#def fitnessFunction(competingDNA):                                 # define a function name fitnessFunction
#    fitness = 0                                                    # define fitness as 0
#    for i in range(dnaLength):                                     # make a for loop
#        if competingDNA[i] != target[i]:                            # if xi and ti is not the same
#            fitness += 1                                           # add 1 to the the variable fitness
#    return fitness                                                 # return the value fitness
        
#------------------------------------------------------------------------------------------------------
 
def mutation(competingDNA,mutationRatio):                           # mutation function
    mut = ""                                                        # define mut as an empty string
    
    for i in competingDNA:                                          # make a for loop 
        if random.randint(1,mutationRatio) == mutationRatio:        # if the random number selected is mutationRatio(100) , which is 1/100 
            mut = mut + random.choice(string.printable)             # define mut as mut + a random string chosen
        else:                                                       # if not , which is 99/100
            mut = mut + i                                           # mut is defined as mut + i (the i components of competingDNA)
    return mut                                                      # return mut

def recombination(competingDNA1, competingDNA2):                    # define a function recombination
    a = random.randint(1,dnaLength - 1)                             # define a as a random number  between 1 and dnaLength-1
    DNAout1 = competingDNA1[:a] + competingDNA2[a:]                 # define DNAout1 as sum of first to a-1 part competingDNA1 and a to last part competingDNA2
    DNAout2 = competingDNA2[:a] + competingDNA1[a:]                 # define DNAout2 as sum of first to a-1 part competingDNA2 and a to last part competingDNA1
    return(DNAout1,DNAout2)                                         # return DNAout1 and DNAout2
    
def weightedDNAchoice(competingDNAfitnessPairs):                                                        # weight selection of DNA for Next Generation
    probs = [competingDNAfitnessPairs[i][1] for i in range(len(competingDNAfitnessPairs))]              # make a set consists of len(competingDNAfitnessPairs) number of competingDNAfitnessPairs[i][1] and define as probs
    probs = np.array(probs)                                                                             # make the probs into a form of np.array (until now the number are in the form of fitness value)
    probs /= probs.sum()                                                                                # use /= probs.sum() to change each of the fitness value into a respective ratio (if added up adds up to 1)
    return competingDNAfitnessPairs[np.random.choice(len(competingDNAfitnessPairs),1,p = probs)[0]][0]  # randomly chose one of the consisting competingDNAfitnessPairs based on the fitness value which is converted into proportion

currentPopulation = initialPopulation()
for i in range(generations):
    lastfitnessarray = []
    for k in currentPopulation:
        lastfitnessarray.append(fitnessFunction(k))
    
    # print the generation number and its current fittest DNA string
    print("The fittest DNA for generation", i, "is ---", currentPopulation[lastfitnessarray.index(min(lastfitnessarray))],"--- with penalty:",min(lastfitnessarray))
    
    #Returns a new population with their respective fitness in format
    populationWeighted = []
    for individual in currentPopulation:
        individualPenalty = fitnessFunction(individual)
        if individualPenalty == 0:
            DNAfitnessPair = (individual, 1.0)
        else:
            DNAfitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(DNAfitnessPair)
    
    #Reset population and repopulate with newly selected, recombined, and mmutated DNA
    currentPopulation = []
    for m in range(int(populationSize/2)):
        #Random selection, weighted by fitness
        fittestDNA1 = weightedDNAchoice(populationWeighted)
        fittestDNA2 = weightedDNAchoice(populationWeighted)
        #Recombination or crossover
        fittestDNA1, fittestDNA2 = recombination(fittestDNA1, fittestDNA2)
        #Mutation in 1/mutationChance chances
        fittestDNA1 = mutation(fittestDNA1, mutationChance)
        fittestDNA2 = mutation(fittestDNA2, mutationChance)
        #Combining the population for next iteraction
        currentPopulation.append(fittestDNA1)
        currentPopulation.append(fittestDNA2)
#Creates an array of penalty value for each DNA in population        
lastfitnessarray = []
for g in currentPopulation:
    lastfitnessarray.append(fitnessFunction(g))
# Prints fittest DNA out of the resulting popultation
print("Fittest String at" , generations, "is:", currentPopulation[lastfitnessarray.index(min(lastfitnessarray))])


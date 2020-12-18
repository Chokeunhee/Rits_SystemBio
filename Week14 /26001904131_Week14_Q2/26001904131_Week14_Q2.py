#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 23:14:44 2020

@author: Chokeunhee
"""

import random                                                                  # import module random
import string                                                                  # import module string
import numpy as np                                                             # import module numpy as np

################################################################################
################################################################################

with open("AISdiseases_4.txt","r") as loadDiseases:                              # Read "AISdiseases.txt" file and define as loadDiseases
    listOfDiseases = loadDiseases.read().split(",");                           # define listOfDiseases as list in loadDisease(AISdiseases.txt)

with open("AISmemoryCell.txt","r") as loadMemoryCell:                          # Read "AISmemoryCell.txt" file and define as loadMemoryCell
    memoryCell = loadMemoryCell.read().split(",")                              # define memoryCell as list in loadMemoryCell(AISmemoryCell.txt) which is blank for now

with open("AISvaccines.txt",'r') as loadVaccines:                              # Read "AISmemoryCell.txt" file and define as loadMemoryCell
    listOfVaccines = loadVaccines.read().split(",")                            # define memoryCell as list in loadMemoryCell(AISmemoryCell.txt) which is blank for now


#######################        Exercise 4     #################################

# Due to the vaccines when selected ones with vaccines the penalty goes to 0 therefore the diseses with vaccines is immuned  
    
memoryCell[:len(listOfVaccines)]= listOfVaccines[:]                            # add listOfVaccines at the begining of the memoryCell list

################################################################################

                                                                               # Set global variables    
antigen = random.choice(listOfDiseases)                                        # define antigen as a random choice from listofDiseases
print (antigen)                                        
antigenLength = len(antigen)                                                   # define antigenLength as length as antigen
#print (antigenLength)                                                  
antibodyNumber = 200                                                           # set antibodyNumber as 200
generations = 20                                                               # set generations as 20
mutationChance = 10                                                            # set mutationChance as 10
selectPenalty = 2                                                              # set selectPenalty as 2
MemoryCellFraction = 10                                                        # set MemoryCellFraction as 10

################################################################################
################################################################################

def randomGene():                                                              # Generates a random gene out of all printable ASCII characters
    return random.choice(string.printable)                                     # return as a random printavle ASCII character

def initialAntibodyPopulation():                                               # Creates antibodyNumber - number of antibodies with random genes
    initPop = []                                                               # define initPop as a empty set
    for i in range(antibodyNumber):
        initPop.append(''.join(random.choice(string.printable) for i in range(antigenLength))) 
                                                                               # make a set of antibodyNumber of random strings with each length of antigenLength
    return initPop 

##########################  Exercise 1    ######################################

def affinityPenaltyMetric(antibodyAttack): # define affinityPenaltyMetric function, which return fitness value which tells how well an antibody fits the antigen
    global antigen 
    penalty = 0                                                                # set fitness to 0                         
    for i in range(antigenLength):                                             # The fitness function      
        penalty += abs(ord(antibodyAttack[i]) - ord(antigen[i]))               # 
    return penalty                                                             # return fitness value as output

################################################################################
################################################################################

#Randomly selects an antibody, weighted by their respective probabilty
#higher the affinity means higher chance of bding selected similar concept as weightedDNAchoice function at GA
def weightedAntibodyChoice(listOfAntibodyAffinity): 
    probs = [listOfAntibodyAffinity[i][1] for i in range(len(listOfAntibodyAffinity))] # make a set consists of len(listOfAntibodyAffinity) number of listOfAntibodyAffinity[i][1] and define as probs
    probs = np.array(probs)                                                            # make the probs into a form of np.array (until now the number are in the form of fitness value)
    probs /= probs.sum()                                                               # use /= probs.sum() to change each of the fitness value into a respective ratio (if added up adds up to 1)
    return listOfAntibodyAffinity[np.random.choice(len(listOfAntibodyAffinity), 1, p = probs)[0]][0] # randomly chose one of the consisting listOfAntibodyAffinity based on the fitness value which is converted into proportion

#Mutation of single antibody in 1/mutationRatio chance
def mutation(antibodyMutate, mutationRatio): 
    mutatedDNA = ""                                                            # define mutatedDNA as a "" string 
    for gene in range(antigenLength):
        mutationCheck = random.randint(0,mutationRatio)                        # define a random number between 0 and mutationRatio as mutationCheck
        if mutationCheck == 1:                                                 # if mutationCheck equals to 1 (1/mutationRatio+1)
            mutatedDNA += randomGene()                                         # add randomGene to mutatedDNA
        else:                                                                  # if not
            mutatedDNA += antibodyMutate[gene]                                 # add the orignal character(antibodyMutate[gene])
    return mutatedDNA                                                          # return mutaedDNA as output

################################################################################
################################################################################

currentAntibodyPopulation = initialAntibodyPopulation()                        # define currentAntibodyPopulation as initialAntibodyPopulation

for ik in memoryCell:                                                          
    if len(ik) == len(currentAntibodyPopulation[memoryCell.index(ik)]):
        currentAntibodyPopulation[memoryCell.index(ik)] = ik

#############################  Exercise 2   ####################################
     
if (len(memoryCell) > antibodyNumber / MemoryCellFraction):                    # if the length of memoryCell is larger than antibodyNumber divided by MemoryCellFraction
   with open("AISmemoryCell.txt", "w") as loadMemoryCell:                      # Read "AISmemoryCell.txt" file and define as loadMemoryCell
        while (len(memoryCell) > antibodyNumber / MemoryCellFraction):         # while length of memoryCell is larger than antibodyNumber divided by MemoryCellFraction
            del memoryCell[0]                                                  # delete the first component of memoryCell
        for i in range(memoryCell):                                            # for range of memoryCell
            loadMemoryCell.write(memoryCell[i])                                # 
            if(i != len(memoryCell) - 1):                                      # if i not equal to length of memoryCell - 1
                loadMemoryCell.write(',')                                      # loadMemoryCell and write a ','

################################################################################
################################################################################
    
for i in range(generations):
    lastAffinityArray = []
    for k in currentAntibodyPopulation:
        lastAffinityArray.append(affinityPenaltyMetric(k))
    
    #print the antibody mutation closest to an antigen    
    print("The antibody closest to the antigen at interation", i,"is ---", 
          currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))], "--- with penalty:", min(lastAffinityArray))
    # Returns a antibody list with their respective affinity in format
    # [["antibody1",affinity],["antibody2",affinity],["antibody3",affinity], ...]
    populationWeighted = []
    for individual in currentAntibodyPopulation:
        individualPenalty = affinityPenaltyMetric(individual)
        if individualPenalty == 0:
            antibodyFitnessPair = (individual, 1.0)
        else:
            antibodyFitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(antibodyFitnessPair)
    
    #New set, repopulated with newly selected and mutated antibodies
    currentAntibodyPopulation = []
    for m in range(int(antibodyNumber/2)):
        # Random selection, weighted
        bestAntibody1 = weightedAntibodyChoice(populationWeighted)
        bestAntibody2 = weightedAntibodyChoice(populationWeighted)
        #Mutation in 1/mutationCance chance (similar concept with mutation in GA)
        bestAntibody1 = mutation(bestAntibody1, mutationChance)
        bestAntibody2 = mutation(bestAntibody2, mutationChance)
        #Combining the list of antibodies for next iteration (similar concept with recombination in GA)
        currentAntibodyPopulation.append(bestAntibody1)
        currentAntibodyPopulation.append(bestAntibody2)

################################################################################
################################################################################

        
lastAffinityArray = []                                                         # set lastAffinityArray as empty set
for g in currentAntibodyPopulation:
    lastAffinityArray.append(affinityPenaltyMetric(g))                         # add affinityPenaltyMetric() to list lastAffinityArray
    
with open("AISmemoryCell.txt", "r") as loadMemoryCell:                         # Read "AISmemoryCell.txt" file and define as loadMemoryCell
    newMemoryCell = loadMemoryCell.read()                                      # define memoryCell as list in loadMemoryCell(AISmemoryCell.txt) which is blank for now
    
if min(lastAffinityArray) < 50:                                                # if lastAffineArray is under 50 (if the penalty of lastone is under 50)
    putIntoMemory = currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))]
    #print fittest antibody out of the resulting list
    print("Fittest String at", generations, "is:", putIntoMemory)
    newMemoryCell += "," + putIntoMemory
    with open("AISmemoryCell.txt","w") as writeMemoryCell:                     # Open "AISmemoryCell.txt" file and define as WriteMemoryCell
        writeMemoryCell.write(newMemoryCell)                                   # write newMemoryCell in the list
else:                                                                          # if not 
    putIntoMemory = ""                                                         # define putInMemory as ""
    print("No antibody to put into memory")                                    # print "No antibody to put into memory"
    
del memoryCell
del listOfDiseases

################################################################################
################################################################################

 



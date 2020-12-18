#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:09:27 2020

@author: Chokeunhee
"""

import random
import string
import numpy as np

with open("AISdiseases.txt","r") as loadDiseases:
    listOfDiseases = loadDiseases.read().split(",");
    
with open("AISmemoryCell.txt","r") as loadMemoryCell:
    memoryCell = loadMemoryCell.read().split(",")
    
antigen = random.choice(listOfDiseases)
antigenLength = len(antigen)
antibodyNumber = 200
generations = 20
mutationChance = 10
selectPenalty = 2
MemoryCellFraction = 10

def randomGene():
    return random.choice(string.printable)

def initialAntibodyPopulation():
    initPop = []
    for i in range(antibodyNumber):
        initPop.append(''.join(random.choice(string.printable) for i in range(antigenLength)))
    return initPop

def affinityPenaltyMetric(antibodyAttack):
    global antigen
    fitness = 0                             
    for i in range(antigenLength):          
        fitness += abs(ord(antibodyAttack[i]) - ord(antigen[i])) 
    return fitness

def weightedAntibodyChoice(listOfAntibodyAffinity):
    probs = [listOfAntibodyAffinity[i][1] for i in range(len(listOfAntibodyAffinity))]
    probs = np.array(probs)
    probs /= probs.sum()
    return listOfAntibodyAffinity[np.random.choice(len(listOfAntibodyAffinity), 1, p = probs)[0]][0]

def mutation(antibodyMutate, mutationRatio):
    mutatedDNA = ""
    for gene in range(antigenLength):
        mutationCheck = random.randint(0,mutationRatio)
        if mutationCheck == 1:
            mutatedDNA += randomGene()
        else:
            mutatedDNA += antibodyMutate[gene]
    return mutatedDNA

currentAntibodyPopulation = initialAntibodyPopulation()

for ik in memoryCell:
    if len(ik) == len(currentAntibodyPopulation[memoryCell.index(ik)]):
        currentAntibodyPopulation[memoryCell.index(ik)] = ik
     
if (len(memoryCell) > antibodyNumber / MemoryCellFraction):
   with open("AISmemoryCell.txt", "w") as loadMemoryCell:
        while (len(memoryCell) > int(antibodyNumber / MemoryCellFraction)):
            del memoryCell[0]
        for i in range(memoryCell):
            loadMemoryCell.write(memoryCell[i])
            if(i != len(memoryCell) - 1):
                loadMemoryCell.write(',')        
        
for i in range(generations):
    lastAffinityArray = []
    for k in currentAntibodyPopulation:
        lastAffinityArray.append(affinityPenaltyMetric(k))
        
    print("The antibody closest to the antigen at interation", i,"is ---", 
          currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))], "--- with penalty:", min(lastAffinityArray))
    
    populationWeighted = []
    for individual in currentAntibodyPopulation:
        individualPenalty = affinityPenaltyMetric(individual)
        if individualPenalty == 0:
            antibodyFitnessPair = (individual, 1.0)
        else:
            antibodyFitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(antibodyFitnessPair)
    
    currentAntibodyPopulation = []
    for m in range(int(antibodyNumber/2)):
        bestAntibody1 = weightedAntibodyChoice(populationWeighted)
        bestAntibody2 = weightedAntibodyChoice(populationWeighted)
        
        bestAntibody1 = mutation(bestAntibody1, mutationChance)
        bestAntibody2 = mutation(bestAntibody2, mutationChance)
        
        currentAntibodyPopulation.append(bestAntibody1)
        currentAntibodyPopulation.append(bestAntibody2)
        
lastAffinityArray = []
for g in currentAntibodyPopulation:
    lastAffinityArray.append(affinityPenaltyMetric(g))
    
with open("AISmemoryCell.txt", "r") as loadMemoryCell:
    newMemoryCell = loadMemoryCell.read()
    
if min(lastAffinityArray) < 50:
    putIntoMemory = currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))]
    
    print("Fittest String at", generations, "is:", putIntoMemory)
    newMemoryCell += "," + putIntoMemory
    with open("AISmemoryCell.txt","w") as writeMemoryCell:
        writeMemoryCell.write(newMemoryCell)
else:
    putIntoMemory = ""
    print("No antibody to put into memory")
    
del memoryCell
del listOfDiseases
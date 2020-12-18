'''
Created on Dec 30, 2018
AIS Ex 1, 2, and 3
@author: ranthawonmas
'''
import random
import string
import numpy as np

#These read "AISdiseases.txt" and "AISmemoryCell.txt"

#The list contains 100 names of diseases. 
with open("AISdiseases.txt", "r") as loadDiseases:
    listOfDiseases = loadDiseases.read().split(",")
    
#The result (antibody) after running the codes above.
with open("AISmemoryCell.txt", "r") as loadMemoryCell:
    memoryCell = loadMemoryCell.read().split(",")
    
#These are global variables, which can be used anywhere.
#print(listOfDiseases)
antigen = random.choice(listOfDiseases)
antigenLength = len(antigen)
print(antigen)
#print(antigenLength)
antibodyNumber = 200
generations = 20
mutationChance = 10
selectPenalty = 2
memoryCellFraction = 10

#It creates "printable" ASCII characters, including letters, numbers, punctuation, and even whitespace.
def randomGene():
    return random.choice(string.printable)

#It generates the number (population) of antibodies, which is initially set as an empty list.
def initialAntibodyPopulation():
    initPop = []
    for i in range(antibodyNumber):
        initPop.append(''.join(random.choice(string.printable) for i in range(antigenLength)))
    return initPop

# It determines the similarity between antibodies and antigens.
def affinityPenaltyMetric(antibodyAttack):
    #Ex. 1
    count = 0
    for i in range(antigenLength):
        count += abs(ord(antibodyAttack[i]) - ord(antigen[i]))
    if count != 0:
        count += 1
    affinity = count #This is the penalty (the lower the fitter). 
    return affinity
        
#It randomly selects an antibody, where an antibody with higher probability is more likely to be selected..
def weightedAntibodyChoice(listOfAntibodyAffinity):
    probs = [listOfAntibodyAffinity[i][1] for i in range(len(listOfAntibodyAffinity))]
    probs = np.array(probs)
    probs /= probs.sum()
    return listOfAntibodyAffinity[np.random.choice(len(listOfAntibodyAffinity), 1, p = probs) [0]] [0]

# It mutates single antibody in 1/mutationRatio chance.
def mutation(antibodyMutate, mutationRatio):
    mutatedDNA = ""
    for gene in range(antigenLength):
        mutationCheck = random.randint(0, mutationRatio)
        if mutationCheck == 1:
            mutatedDNA += randomGene()
        else:
            mutatedDNA += antibodyMutate[gene]
    return mutatedDNA

currentAntibodyPopulation = initialAntibodyPopulation()

#Ex. 2 (If the length of population is equal to the remainder of the length of population divided by  memory cell, the population will be equal to that remainder. 
for ik in range(len(currentAntibodyPopulation)):
    if len(currentAntibodyPopulation[ik]) == len(memoryCell[ik % len(memoryCell)]):
        currentAntibodyPopulation[ik] = memoryCell[ik % len(memoryCell)]

#It concatenates an affinity value to the empty list set in line 80. 
for i in range(generations):
    lastAffinityArray = []
    for k in currentAntibodyPopulation:
        lastAffinityArray.append(affinityPenaltyMetric(k))
    
    #It prints an antibody-mutation which is closest, or fittest, to its antigen.
    print("The antibody closest to the antigen at iteration", i, "is___", currentAntibodyPopulation[
        lastAffinityArray.index(min(lastAffinityArray))], "---with penalty:", min(lastAffinityArray))
    
    #It returns an antibody list in [ ["antibody", affinity1], ["antibody2", affinity2] [...]...] format.
    populationWeighted = []
    for individual in currentAntibodyPopulation:
        individualPenalty = affinityPenaltyMetric(individual)
        if individualPenalty == 0:
            antibodyFitnessPair = (individual, 1.0)
        else:
            antibodyFitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(antibodyFitnessPair)
        
        #It generates a new list of antibodies.
        currentAntibodyPopulation = []
        for m in range(int(antibodyNumber/2)):
            #It randomly selects an affinity value, where those with higher probability are more likely to be selected.
            bestAntibody1 = weightedAntibodyChoice(populationWeighted)
            bestAntibody2 = weightedAntibodyChoice(populationWeighted)
            
            #It mutates antibodies in 1/mutationChance chance.
            bestAntibody1 = mutation(bestAntibody1, mutationChance)
            bestAntibody2 = mutation(bestAntibody2, mutationChance)
            
            #It combines the list of antibodies for the next generations, which is similar to GA's crossover.
            currentAntibodyPopulation.append(bestAntibody1)
            currentAntibodyPopulation.append(bestAntibody2)
            
lastAffinityArray = []
for g in currentAntibodyPopulation:
    lastAffinityArray.append(affinityPenaltyMetric(g))
    
with open("AISmemoryCell.txt", "r") as loadMemoryCell:
    newMemoryCell = loadMemoryCell.read()
    #Ex.2 cont'd
    if len(newMemoryCell) == memoryCellFraction/100 * len(currentAntibodyPopulation):
        newMemoryCell.pop(0) #It "pops" or removes the leftmost, which is the oldest, element.
    
if min(lastAffinityArray) < 50:
    putIntoMemory = currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))]
    #It prints the fittest antibody out of the resulting list
    print("Fittest String at", generations, "is: ", putIntoMemory)
    newMemoryCell += " , " + putIntoMemory
    with open("AISmemoryCell.txt", "w") as writeMemoryCell:
        writeMemoryCell.write(newMemoryCell)
else:
    putIntoMemory = ""
    print("No antibody to put into memory") 
    
#For Exericse 3, I got the list from https://en.wikipedia.org/wiki/List_of_virus_species.
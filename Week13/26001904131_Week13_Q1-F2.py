#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:49:31 2019

@author: Chokeunhee
"""

import random #import module random                                           
import math #import module math

def errorFunction(x): # defining errorFunction (which is used as costFunction at function particleSwarmOptimization)                                  
    return sum([50 * math.sin(x[i]) + (x[i])**2 + 100 for i in range(len(x))])  #define as sum([50 * math.sin(x[i]) + x[i] ** 2 + 100 for i in range(len(x))])  
   
class individualParticle:     # A class of a computer agent, here also called particle                                   
    def __init__(self, x0):                                     
        self.individualPosition = []       #define individualPosition as an empty list
        # Exercise1 #########################################################################                 
        self.individualVelocity = []       #define individualVelocity as an empty list                     
        self.individualBestPosition = []   #define individualBestPosition as an empty list                  
        self.individualBestError = -1      #define individualBestError as -1                     
        self.individualError = -1          #define individualError as -1
        #####################################################################################                    
    
        for i in range(0, numStartingLocation):                     # for loop for range 0 to numStartingLocation           
            self.individualVelocity.append(random.uniform(-1,1))    # add a random number between -1 and 1 to list individualVelocity
            self.individualPosition.append(x0[i])                   # add number i of array x0 to list individualPosition       
     
        
    def evaluate(self, costFunction):            #Evaluate the current fitness of the computer agents             
        self.individualError = costFunction(self.individualPosition) #define individualError as costFunction(ErrorFunction) with individualPosition as input
        # the current position of the agent is compared with the individual best and updated if necessary        
        if self.individualError < self.individualBestError or self.individualBestError == -1: # if individualError is smaller than individualBestError of if individualBestError is -1
            self.individualBestPosition = self.individualPosition  #define individualBestPosition as indicidualPosition
            self.individualBestError = self.individualError         # define individualBestError as individualError
    
    def update_velocity(self, groupsBestPosition):    #Calculate the new agent's velocity
        # Exercise 3 ##########################################################################
        # Particle with low velocity have difficulties finding the global minimum even after an increased number of iterations
        # because velocity is sort of like the learning rate, so for example for f(x) there is only one only one local min so it does not
        # give much influence. However for g(x) there exist various local minimum. So if the celocity is too small they wont be able to get out
        # from a certain local minimum and consider that local minimum as the global minimum.
        # 
        # in order to give a better solution it is need to change the value of velocity.
        # velocity is consider with 3 factors, vector of previous velocity vector of individual best position and vector of groupbestposition
        # w is the weight of previous velocity, c1 is the factor of individual and c2 for group.
        # therefore by changing these 3 factors we can change the value of the velocity.
        # For my code I can changed c1 to 1.4 and c2 to 2.8, making the error smaller, which is giving a better solution.
        #
        w = 0.5         # define w {Inertia weight of previous velocity} as 0.5                                              
        c1 = 1.4        # define c1 {Cognitive constant(distance from the individual's known best position)} as 1.4                                            
        c2 = 2.8        # define c2 {Social constant(distance from the group's known best position)} as 2.8                                              
                
        for i in range(0, numStartingLocation):     # Do a for loop for 0 to numStartingLocation                    
            r1 = random.random()                    # define r1 as a random number between 0 to 1                          
            r2 = random.random()                    # define r1 as a random number between 0 to 1                         
            #updating cognitive velocity and social velocity
            cognitiveVelocity = c1 * r1 * (self.individualBestPosition[i] - self.individualPosition[i])          #update cognitiveVelocity
            socialVelocity = c2 * r2 * (groupsBestPosition[i] - self.individualPosition[i])                      # update socialVelocity         
            self.individualVelocity[i] = w * self.individualVelocity[i] + cognitiveVelocity + socialVelocity     #update individualVelocity
            
    def positionUpdate(self, bounds):           #Update the position of each agent based on the new velocity updates                            
        for i in range(0, numStartingLocation):                             
            self.individualPosition[i] = self.individualPosition[i] + self.individualVelocity[i] 
            # Compesate maximum position
            if self.individualPosition[i] > bounds[i][1]:                   
                self.individualPosition[i] = bounds[i][1]                   
            # Compesate minimum position
            if self.individualPosition[i] < bounds[i][0]:                   
                self.individualPosition[1] = bounds[i][0]                   
                
def particleSwarmOptimization(costFunction, x0, bounds, num_particles, maxiter):   #define particleSwarmOptimization function
    # initialize the swarm
    global numStartingLocation      # use numStartingLocation using global                                         
    numStartingLocation = len(x0)   #define numStartingLocation as len of x0                                     
    print(numStartingLocation)                                              
    bestGroupError = -1             #define bestGroupError as -1                                         
    groupsBestPosition = []         #define groupsBestPosition as a empty list                                            
    swarm = []                      #define swarm as a empty list                                                         
        
    for i in range(0, num_particles):                                       
        swarm.append(individualParticle(x0))                                

    # Loop to start the optimization process            
    for i in range(0, maxiter):                                            
        #Evaluate each agent's fitness    
        for j in range(0, num_particles):                                   
            swarm[j].evaluate(costFunction)                                  
            #Which agent has the best position(minimum error) in the swarm?    
            if swarm[j].individualError < bestGroupError or bestGroupError == -1: 
                groupsBestPosition = list(swarm[j].individualPosition)       
                bestGroupError = float(swarm[j].individualError)              
        #Update velocities and positions inside the swarm            
        for j in range(0, num_particles):                                  
            swarm[j].update_velocity(groupsBestPosition)                     
            swarm[j].positionUpdate(bounds)                                 
    #Print the final results with error            
    print('After running the swarm of computer agents, the group\'s best position is ' + str(groupsBestPosition) + " with an error of " + str(bestGroupError))  

initialStartingPosition = [-15, 15]     # define initialStartingPosition as [-15,15]                                    
minMaxBounds = [(-30,30),(-30,30)]
#minMaxBounds = [(-100, 100), (-100, 100)]    # define minMaxBounds                               
particleSwarmOptimization(errorFunction, initialStartingPosition, minMaxBounds, num_particles = 150, maxiter = 30) # Run function particleSwarmOptimization with selected argument
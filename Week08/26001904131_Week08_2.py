#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:20:22 2019

@author: Chokeunhee
"""

import numpy as np # import module numpy and name it as np
import matplotlib.pyplot as plt # import matplotlib.pyplot and name as plt
import matplotlib.animation as animation # import matplotlib.animation and name as animation

N = 200                                                                         # define N as 100
A = 1                                                                           # define A as 1 (alive)
D = 0                                                                           # define D as 0 (Dead)
vals=[A,D]                                                                      #define vals as a set of A and D

grid1 = np.zeros((N,N))                                                         # define grid1 as set of zeros N by N
gridmaze = np.random.choice(vals,20*20,p=[0.5,0.5]).reshape(20,20)              # define gridmaze as 30 by 30 matrix, which components are randomly selected from val with percentage of p 
grid1[90:110,90:110] = gridmaze                                                   # change the selected section(60:90,60:90) of grid1 to gridmaze

grid2 = np.random.choice(vals,N*N,p=[0.9,0.1]).reshape(N,N)                     # define grid2 as N by N matrix, which components are randomly selected from val with percentage of p


def animated_Maze(framenumber, *arg, **kwargs):                                 # define a function name animated_Maze
    global grid1                                                                # use global to allow the use of variable grid1 which is outside of the current scope
    global animatedcount                                                        # use global to allow the use of variable animatedcount which is outside of the current scope
    newGrid1 = grid1.copy()                                                     # define newGrid1 as copy of grid1
    for i in range(N):                                                          # for i which in the range of N 
        for j in range(N):                                                      # for j which in the range of N 
            T = (grid1[i,(j-1)%N] + grid1[i,(j+1)%N] +                          # Define variable T as number A which are neighboring the cell [i,j]
                      grid1[(i-1)%N,j] + grid1[(i+1)%N,j] + 
                      grid1[(i-1)%N,(j-1)%N] + grid1[(i+1)%N,(j-1)%N] + 
                      grid1[(i-1)%N,(j+1)%N] + grid1[(i+1)%N,(j+1)%N])/A            
            if grid1[i,j] == A:                                                 # if the cell[i,j] is A
                if (T < 1) or (T > 5):                                          # if T is 0 6 7 8
                    newGrid1[i,j] = D                                           # for newGrid1 cell[i,j] is defined as D          
            else:                                                               # if not; if the cell[i,j] at grid1 is D 
                if (T == 3):                                                    # if T equals to 3
                    newGrid1[i,j] = A                                           # for newGrid1[i,j] is defined as A
    grid1 = newGrid1.copy()                                                     # define grid as copy of newGrid
    mat.set_data(grid1) 
    return mat                                                                  # return the values as variable mat for function animated_Maze

def animated_Move(framenumber, *arg, **kwargs):
    global grid2
    global animatedcount
    newGrid2 = grid2.copy()
    for i in range(N):
        for j in range(N):
            T = (grid2[i,(j-1)%N] + grid2[i,(j+1)%N] + 
                      grid2[(i-1)%N,j] + grid2[(i+1)%N,j] + 
                      grid2[(i-1)%N,(j-1)%N] + grid2[(i+1)%N,(j-1)%N] + 
                      grid2[(i-1)%N,(j+1)%N] + grid2[(i+1)%N,(j+1)%N])/A            
            if grid2[i,j] == A:                                                 # if grid[i,j] is defined as A
                if (T < 2) or (T == 3) or (T > 5):                              # if T is 0 1 3 6 7 8 
                    newGrid2[i,j] = D                                           # for newGrid2[i,j] is define as D
            else:                                                               # if not; grid[i,j] is defined as D
                if (T == 3) or (T == 6) or (T == 8):                            # if T equals to 3 6 8
                    newGrid2[i,j] = A                                           # for newGrid2[i,j] is define as A
    grid2 = newGrid2.copy()
    mat.set_data(grid2)
    return mat

print ("To show maze input 1")                                                  # print string 
print ("To show move input 2")                                                  # print string 

while True:                                                                     # run while loop
    X = input("please inout [1/2] : ")                                          # define X as input
    if (X == "1"):                                                              # if X equals to "1"
        y = grid1                                                               # y is defined as grid1
        z = animated_Maze                                                       # z is defined as animated_Maze
        break                                                                   # break loop
    if (X == "2"):                                                              # if X equals to "2"
        y = grid2                                                               # y is defind as grid2
        z = animated_Move                                                       # z is defind as ainmated_Move
        break                                                                   # break loop
    else:                                                                       # if not
        print("invalid input")                                                  # print string
    
fig, ax = plt.subplots()                                                        # define fig and ax as subplots
mat = ax.matshow(y)                                                             # define the variable mat as ax.matshow(y)
ani = animation.FuncAnimation(fig, z, interval = 30)                            # define ani of a function animation.FuncAnimation(fig, z, interval = 30) 
plt.show()                                                                      # run the function plt.show() which display the defined figure


# For Maze the rule was B3/S12345 (born on 3 survive at 1,2,3,4,5)
# I defined the function for maze so that it start somewhere in the middle(randomly) and spreads out.
#
# For Move the rule was B368/S245
#
# For random grid population p[n,1-n] is the percentage for initial status state of the cells
# we were told to change it to emphasize the dynamics of Maze and Move
# 
# It was hard to define the number, because it hard to define which result is emphasized 
# Therefore I have tried various numbers by myself and made the decitions
#
# For Maze I chose [0.5,0.5] ([0.005,0.995])
# It was because if the grid is small and number of living cell is very few there is a low chance of not being able to make the maze
# One the other hand if the number of living cell is too much compare to the grid size than the process of making the maze will be too quick
# Therefore it seems like a number which was not too big not too small will be the best if it is done on a regular grid
# However due to specialty of my grid, [0.5,0.5] is actually [0.005,0.995] but focused in the middle which show the maze successfully
#  
#
# For Move I chose [0.9,0.1]
# For Move random string pattern tend to stabilize into a much lower density than in Game of life.
# Therfore I thought it will be good to emphasize by starting with a very high density
# Moreover I thought using a bigger grid will give us a higher chance to see jellyfish, jason's bow and puffer
#


   
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:08:45 2019

@author: Chokeunhee
"""
import numpy as np                                                                           # import module numpy and name it as np
import matplotlib.pyplot as plt                                                              # import matplotlib.pyplot and name it as plt
import matplotlib.animation as animation                                                     # import matplotlib.animation and name it as animation


universe = 50                                                                                # Size of the grid (universe) 50 by 50
alive = 1                                                                                    # Alive cells = "on"
dead = 0                                                                                     # Dead cells = "off"
vals = [alive, dead]                                                                         # list of values "on" and "off" used to populate the initial universe                                                                  

grid = np.zeros((50,50))                                                                     # Poputlate the universe with sets of zeros(dead cells) using function np.zeros() 50 by 50

Octagon_2 = [[0,0,0,1,1,0,0,0],                                                              # One of the oscillator(Octagon_2)
             [0,0,1,0,0,1,0,0],
             [0,1,0,0,0,0,1,0],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [0,1,0,0,0,0,1,0],
             [0,0,1,0,0,1,0,0],
             [0,0,0,1,1,0,0,0]]

grid[3:11,3:11] = Octagon_2                                                                  # Define the [3:11,3:11],[10:18,10:18],[17:25,17:25] and more of the grid to Octagon_2 
grid[10:18,10:18] = Octagon_2
grid[17:25,17:25] = Octagon_2
grid[24:32,24:32] = Octagon_2
grid[31:39,31:39] = Octagon_2
grid[38:46,38:46] = Octagon_2

def animated_universe(framenumber, *arg, **kwargs) :                                         # Create a function name animated_universe
    global grid                                                                              # use global to allow the use of variable grid(line 18) which is outside of the current scope
    global animatedcount                                                                     # use global to allow the use of variable animatedcount which is outside of the current scope
    newGrid = grid.copy()                                                                    # define newGrid as copy of grid
    for i in range(universe):                                                                # for i which in the range of universe which is 50 
        for j in range(universe):                                                            # for j which in the range of universe which is 50
            total = (grid[i, (j-1)%universe] +                                               # 
                          grid[i, (j+1)%universe] +                                          #
                          grid[(i-1)%universe, j] + grid[(i+1)%universe, j] +                # Define variable total as number alive cells which are neighboring the cell [i,j]
            grid[(i-1)%universe,(j-1)%universe] + grid[(i-1)%universe,(j+1)%universe] +      #
            grid[(i+1)%universe,(j-1)%universe] + grid[(i+1)%universe,(j+1)%universe])/alive #
            if grid[i, j]  == alive:                                                         # if the cell[i,j] is alive
                if (total < 2) or (total > 3):                                               # if the variable total is smaller than 2 or bigger than 3
                    newGrid[i, j] = dead                                                     # for newGrid cell[i,j] is defined dead which is 0
            else:                                                                            # if not
                if total ==3:                                                                # if variable total equals to 3
                    newGrid[i, j] = alive                                                    # for newGrid cell[i,j] is defined alive which is 1
    grid = newGrid.copy()                                                                    # define grid as copy of newGrid
    mat.set_data(grid)                                                                       
    return mat                                                                               # return the values as variable mat for function animated_universe

fig, ax = plt.subplots()                                                                     # define fig and ax as subplots
mat = ax.matshow(grid)                                                                       # define the variable mat as ax.matshow(grid)

ani = animation.FuncAnimation(fig, animated_universe, interval = 300)                        # define ani of a function animation.FuncAnimation(fig, animated_universe, interval = 500)
                                                                                             # interval means the delay between frames the bigger the delay goes longer
plt.show()                                                                                   # run the function plt.show() which display the defined figure

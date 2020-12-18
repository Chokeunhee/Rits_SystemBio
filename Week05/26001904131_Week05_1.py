#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:30:18 2019

@author: Chokeunhee
"""

import numpy as np                    # Import module numpy and name it as np
import matplotlib.pyplot as plt       # Import matplotlib.pyplot and name it as plt

universe = np.zeros((10,10))          # Define universe as a set of 0s, 10 by 10 matrix

Octagon_2 = [[0,0,0,1,1,0,0,0],       # One of the oscillator(Octagon_2)
             [0,0,1,0,0,1,0,0],
             [0,1,0,0,0,0,1,0],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [0,1,0,0,0,0,1,0],
             [0,0,1,0,0,1,0,0],
             [0,0,0,1,1,0,0,0]]


universe[1:9, 1:9] = Octagon_2        # Define cells at [1:9,1:9] as Octagon_2

plt.imshow(universe, cmap='Reds')     # set the display setting as universe(10,10) and color based on colormap 'Reds'
#plt.imshow(universe, cmap='binary')  # The original code with colormap 'binary' 

plt.show()                            # Run the function plt.show() which display the defined figure

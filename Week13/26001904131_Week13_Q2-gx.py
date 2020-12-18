#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:20:11 2019

@author: Chokeunhee
"""

from matplotlib import pyplot as plt                                           # import pyplot from matplotlib as the name plt
import numpy as np                                                             # import module numpy as the name np

def g(x):                                                                      # define function g(x) as (50 * np.sin(x) + x ** 2 + 100)
    return (50 * np.sin(x) + x ** 2 + 100) 

x = np.arange(-30, 30, 0.1)                                                    # define x as from -30 to 30 with interval of 0.1

plt.grid()                                                                     # put grid for the graph
plt.xlabel("x")                                                                # label xlabel as "x"                                     
plt.ylabel("y")                                                                # label ylabel as "y"
plt.title("g(x)", fontsize=20, fontweight='bold')                              # graph title as g(x) with font size 20 and bold

plt.plot(x, g(x))                                                              # draw the graph x = x , y = g(x)

plt.savefig("26001904131_Week13_Q2-gx.png")                                    # save the figure as 26001904131_Week13_Q2-gx.png



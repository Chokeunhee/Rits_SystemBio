#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:20:12 2019

@author: Chokeunhee
"""

from matplotlib import pyplot as plt                                           # import pyplot from matplotlib as the name plt
import numpy as np                                                             # import module numpy as the name np

def h(x):                                                                      # define function h(x) as ((15 * np.sin(x / 5) ** 2) * 75 * np.cos(x / 13) * 3 * np.sin(x / 7) + x ** 2 + 300)
    return ((15 * np.sin(x / 5) ** 2) * 75 * np.cos(x / 13) * 3 * np.sin(x / 7) + x ** 2 + 300)

x = np.arange(-100, 100, 0.1)                                                  # define x as from -100 to 100 with interval of 0.1

plt.grid()                                                                     # put grid for the graph
plt.xlabel("x")                                                                # label xlabel as "x"                                     
plt.ylabel("y")                                                                # label ylabel as "y"
plt.title("h(x)", fontsize=20, fontweight='bold')                              # graph title as h(x) with font size 20 and bold

plt.plot(x, h(x))                                                              # draw the graph x = x , y = h(x)

plt.savefig("26001904131_Week13_Q2-hx.png")                                    # save the figure as 26001904131_Week13_Q2-gx.png
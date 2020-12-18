#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:14:27 2019

@author: Chokeunhee
"""

from matplotlib import pyplot as plt                                           # import pyplot from matplotlib as the name plt
import numpy as np                                                             # import module numpy as the name np

def f(x):                                                                      # define function f(x) as (5 * (x - 20) ** 2)
    return (5 * (x - 20) ** 2) 

x = np.arange(-100, 100)                                                       # define x as from -100 to 100

plt.grid()                                                                     # put grid for the graph
plt.xlabel("x")                                                                # label xlabel as "x"                                              
plt.ylabel("y")                                                                # label ylabel as "y"
plt.title("f(x)", fontsize=20, fontweight='bold')                              # graph title as f(x) with font size 20 and bold

plt.plot(x, f(x))                                                              # draw the graph x = x , y = f(x)

plt.savefig("26001904131_Week13_Q2-fx.png")                                    # save the figure as 26001904131_Week13_Q2-fx.png
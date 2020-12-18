#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:40:45 2019

@author: Chokeunhee
"""
import matplotlib.pyplot as plt                                                 # import module matplotlib.pyplot and name it as plt
import numpy as np                                                              # import module numpy and name it as np


def Question_1(n, iteration_number, x1,x2,y1,y2):                               # create a function name Question_1 with the variable n, iteration_number, x1, x2, y1, y2
    M = np.zeros([n,n], int)                                                    # create a array of 0 in the shape of n by n and data type is integer
    xvalues = np.linspace(x1,x2,n)                                              # defining the X-axis from x1 to x2 (region spanning)
    yvalues = np.linspace(y1,y2,n)                                              # defining the Y-axis from y1 to y2 (region spanning)
    for u,x in enumerate(xvalues):                                               
        for v,y in enumerate(yvalues):                                           
            z = 0 + 0j                                                          # define z as a complex number 0 + 0j / initialization
            C = complex(x,y)                                                    # C is a complex number x + yj
            for i in range(iteration_number):                                   # for i in the range of defined number of interation
                z = z*z + C                                                     # z = z*z + C / due to this cumulative absolute value of z goes to infinity
                if abs(z) > 2.0:                                                # if the absolute value z is bigger than 2.0
                    M[v,u] = 1                                                  # define all the [v,u] point of the array M as 1 so it can be distinguished (if not the whole scale will turn out as black)
                    break                                                       # and end the loop
    plt.imshow(M,origin="lower", extent=(x1,x2,y1,y2))                          # creating the image with axes label defined above
    plt.gray()                                                                  # set the image as grayscale image
    plt.show()                                                                  # image output which show the image


A = int(input("Please input line resolution : "))                               # Define A as an integer (data type of line resolution(n) is integer is Question_1 (line13)) which the user input / print string
B = int(input("Please input number of iterations : "))                          # Define B as an  integer (data type of  number of iterations is integer because of range() in Question_1 (line20)) which the user input / print string
C = float(input("Please input left  boundary : "))                              # Define C as an real number ( if use int(input()) it can get an error if user input numbers like 0.5 ) which the user input / print string
D = float(input("Please input right boundary : "))                              # Define D as an real number which the user input / print string
E = float(input("Please input lower boundary : "))                              # Define E as an real number which the user input / print string
F = float(input("Please input upper boundary : "))                              # Define F as an real number which the user input / print string
                                                                                # int(input()) and float(input()) is used instead of input(), it is because input() can only read string

print("Please wait")                                                            # print string

Question_1(A,B,C,D,E,F)                                                         # Run function Question_1 with the variable A B C D E F
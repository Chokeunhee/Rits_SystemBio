#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:40:47 2019

@author: Chokeunhee
"""
import matplotlib.pyplot as plt                                                 # import module matplotlib.pyplot and name it as plt
import numpy as np                                                              # import module numpy and name it as np

n = int(input("Please input line resolution : "))                               # define n as the integer which the user input
iteration_number = int(input("Please input number of iterations : "))           # define iteration_number as the integer which the user input

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


def Question_2():                                                               # create a function Question_2 for choosing which set to show
    
    print ("To show Original Mandelbrot set          input 1")                  # print string
    print ("To show Elephant valley Mandelbrot set   input 2")                  # print string
    print ("To show Sea horse valley Mandelbrot set  input 3")                  # print string
    X = input("please input [1/2/3] : ")                                        # define a as the "string" which the user input / and print string
    if X == "1":                                                                # if the user input "1"
        print("Original Mandelbrot set")                                        # print string
        print("line resolution :",n )                                           # print string and n
        print("number of iterations :",iteration_number)                        # print string and iteration_number
        Question_1(n,iteration_number , -2, 0.5, -1, 1)                         # run Question_1 with variable defined as following (1000,100,-2,0.5,-1,1)
    elif X == "2":                                                              # if the user input "2"
        print("Elephant valley Mandelbrot set")                                 # print string
        print("line resolution :",n )                                           # print string and n
        print("number of iterations :",iteration_number)                        # print string and iteration_number
        Question_1(n,iteration_number , 0.2, 0.4, -0.1, 0.1)                    # run Question_1 with variable defined as following (1000,100,0.2,0.4,-0.1,0.1)
    elif X == "3":                                                              # if the user input "3"
        print("Sea horse valley Mandelbrot set")                                # print string
        print("line resolution :",n )                                           # print string and n
        print("number of iterations :",iteration_number)                        # print string and iteration_number
        Question_1(n,iteration_number , -0.85, -0.65, 0, 0.2)                   # run Question_1 with variable defined as following (1000,100,-0.85,-0.65,0,0.2)
    else:                                                                       # if user input any string other than "1" "2" "3"
        print("wrong input Please run again")                                   # print string


Question_2()                                                                    # run function Question_2
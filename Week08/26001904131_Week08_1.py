#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:34:32 2019

@author: Chokeunhee
"""

import random #import module random
import math #import module math


while True:                                                                         # make a while loop
    X = int(input ("input rule number [0:255] : "))                                 # input X as an the form of int
    if 0 <= X <= 255:                                                               # if the X is between 0 and 255 break the loop
       break
    else:                                                                           # if not print string "invalid input, Please input again"
        print("invalid input, Please input again")

  
Y = int(input ("input size number : "))                                             # input Y as int
        

while True:                                                                         # make a while loop
    Z = input ("input 1 for single 1 state / 2 for random initial state [1/2] : ")  # input Z as an string
    if (Z == "1") or (Z == "2"):                                                    # if Z is "1" or "2" break the loop
        break
    else:                                                                           # if not print string "invalid input, Please input again"
        print("invalid input, Please input again")

G = int(input("input generation number : "))


wolfram_rule_string ="{0:{fill}8b}".format(X, fill="0")                             # 8 bit binary integer number X(number inputed above) as a string

wolfram_rule_dict = {"111":wolfram_rule_string[0], "110":wolfram_rule_string[1],    # apply the 8-bit binary number to the Wolfram rule
                     "101":wolfram_rule_string[2],"100":wolfram_rule_string[3],
                     "011":wolfram_rule_string[4],"010":wolfram_rule_string[5],
                     "001":wolfram_rule_string[6],"000":wolfram_rule_string[7]}

if (Z == "1"):                                                                      # if Z equals to "1" which is to run single 1 initial state(non-random)
    iterstr = "0"*math.floor(Y/2) + "1" + "0"*math.floor(Y/2)                       # the initial state(generation0) is string 000..00100..000  
                                                                                    # the number of 0 each side is half of Y
elif (Z == "2"):                                                                    # if Z equals to "2" which is to run random initial state(random)
    z = ["0","1"]                                                                   # set z is consists of "0" and "1"                                                                 # define iterstr as z[r] // z[0] = "0" and z[1] = "1"
    if (len(iterstr) < Y):                                                          # if length of iterstr is smaller than Y
        r = random.randint(0,1)                                                     # randomly pick a int between 0 and 1 and define as r
        iterstr = iterstr + z[r]                                                    # define iterstr as iterstr + z[r] // z[0] = "0" and z[1] = "1"
    
    
def wolfram_generater(iterstr):                                                     # define a function wolfram_generater which returns next generation
    x = ""                                                                          # define x as ""
    for i in range(len(iterstr) - 2):                                               # for loop of i in the range of (length of iterstr-2)   
        x += wolfram_rule_dict[iterstr[i:i+3]]                                      # x = x + value based on wolfram_rule_string   
    return x                                                                        # return value x

def replace(string):                                                                # define a function replace which replace string
    string = string.replace('0',' ').replace('1','A')                               # define string as the string which "0" and "1" is replaced by " " and "A"
    return string                                                                   # return the value string

def wolfram():                                                                      # define a function wolfram which prints the result
    global iterstr                                                                  # use variable iterstr from above
    print(replace(iterstr))                                                         # print iterstr but base on the method function replace   
    for _ in range(G):                                                              # do the process in range of G (how much generation to show)
        line = wolfram_generater(iterstr)                                           # line is defined as the function wolframe_generater(iterstr)
        line = '0{}0'.format(line)                                                  # the format of line is define as 0{}0               
        print(replace(line))                                                        # print line in the method of function replace
        iterstr = line                                                              # define iterstr as line

wolfram()                                                                           # run function wolfram   
     



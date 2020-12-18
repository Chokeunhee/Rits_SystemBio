#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:20:55 2019

@author: Chokeunhee
"""

import random # Importing the module random
import string # Importing the module string 

def Question_1(length): # Define the function Question_1
    sett = string.digits  # Providing a Set (string.digits)
    r = random.randint(0,len(sett)-1) # Create a random integer number r within the range of provided Set
    number = sett[r] # Creat a variable number define it as sett[r]
    while len(number) < length: # If the length of the defined number is smaller than length of function Question_1 proceed the following loop
        r = random.randint(0,len(sett)-1) # Select a character out of the provided set
        number += sett[r] # Attach the new r to the previous number
    return number # If the function is really, cause the function to exit and hand back the caller a value.


print(Question_1(100)) # Print the random number which is define as Question_1
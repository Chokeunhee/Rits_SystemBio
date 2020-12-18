#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:47:09 2019

@author: Chokeunhee
"""

import random # Importing the module random
import string # Importing the module string

def Question_2(length): # Define the function Question_2
    set = string.ascii_lowercase # Provinding a set of lowercased alphabet(string.ascii_lowercase)
    word = "" # Create a variable word    
    while len(word) < length: # If the length of the defined word is smaller than length of function Question_2 proceed the following loop
        if random.randint(1,3) > 2: # use random.randint to pick a number between 1, 2, and 3. If the number is bigger than 2 (33.33%)
            r = random.randrange(1,len(set),2) # define r randomly from [1,3,5,7,9, ..23,25] which will becomes even alphabet ("b","d","f" ...) if in the form of set[r]
        else: # If not which is (66.67%)
            r = random.randrange(0,len(set),2) # define r randomly from [0,2,4,6,8, ..22,24] which will becomes odd alphabet ("a","c","e" ...) if in the form of set[r] 
        word += set[r] # Attach the new set[r] to the previous defined word
    return word # If the function is really, cause the function to exit and hand back the caller the value.

print(Question_2(100)) # Print the random set of alphabet which is define as Question_2
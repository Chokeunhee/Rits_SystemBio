#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:34:22 2020

@author: Chokeunhee
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


###############################################################################
INFECTED = int(input("set I0 : "))
x = int(input("day : ")) 

###############################################################################
N = 100000
I0 = INFECTED # 초기 병든 인간 값
R0 = 0
S0 = N - I0 - R0
###############################################################################

###############################################################################
beta = 0.7 # 전염확률
###############################################################################
gamma = float(1/7) # Remove 하는 비율
###############################################################################
t = np.linspace(0,x,num=24*x) # 날짜 설정
###############################################################################

def SIRmodel (compartmentValues, t ,N, beta, gamma):
    S, I, R = compartmentValues
    dSdt = -beta * S * I/N
    dIdt = beta * S * I/N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

compartmentValues0 = S0, I0, R0

SIRmodelNumSolve = odeint(SIRmodel, compartmentValues0, t, args=(N,beta,gamma))
S,I,R = SIRmodelNumSolve.T

fig = plt.figure(facecolor="w")

ax = fig.add_subplot(1,1,1,facecolor="#eeeeee",axisbelow=True)

ax.plot(t, S/N, "b" ,alpha=0.2, lw=1,label="Susceptible")
ax.plot(t, I/N, "r" ,lw=2,label="Infected")
ax.plot(t, R/N, "g" ,alpha=0.2, lw=1,label="Removed")

#day = t[np.argmax(I)]
#print(np.around(day))
#hours = day * 24
#print(np.around(hours))
peak = np.max(I)
print("The peak is ", np.around(peak))

ax.set_xlabel("Time in days")
ax.set_ylabel("Individuals (in " + str(N) + "s)")

ax.legend()
plt.show()
    
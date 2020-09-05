# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:46:11 2020

@author: cdm18
"""

import matplotlib.pyplot as plt
import numpy as np

def capacitorChargeGraph(epsilon, resistance, capacitance):
    
    time = np.array(np.linspace(0,6,100))
    diffeqSol = np.exp(-time/(resistance * capacitance))
    charge = epsilon * (1 - diffeqSol)
    current = epsilon - charge
    
    plt.title('Capacitor Charge')
    plt.xlabel('Time in Seconds')
    plt.ylabel('Charge in Volts')
    plt.plot(time, charge, color = 'blue')
    plt.plot(time, [epsilon for i in range(100)], color = 'red')
    plt.plot(time, current, linestyle = 'dotted', color = 'black')
    plt.grid() #Add a grid to the plot
    plt.show() #Show the plot
    
def capacitorDischargeGraph(epsilon, resistance, capacitance):
    
    time = np.array(np.linspace(0,6,100))
    diffeqSol = np.exp(-time/(resistance * capacitance))
    charge = epsilon * diffeqSol
    current = epsilon - charge
    
    plt.title('Capacitor Discharge')
    plt.xlabel('Time in Seconds')
    plt.ylabel('Charge in Volts')
    plt.plot(time, charge, color = 'blue')
    plt.plot(time, [0 for i in range(100)], color = 'red')
    plt.plot(time, current, linestyle = 'dotted', color = 'black')
    plt.grid() #Add a grid to the plot
    plt.show() #Show the plot
    
capacitorDischargeGraph(9, 1000, 0.001)
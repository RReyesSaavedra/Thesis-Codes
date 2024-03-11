#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:16:50 2024

@author: Rudy
"""

import numpy as np
import matplotlib.pyplot as plt

V_recip = 22.28
VH2O = 15.43
VO2 = V_recip - VH2O

pCO2_measured = (1/1.013)*np.array([0.15,0.21,0.25,0.30,0.335,0.36])

pulsos = np.size(pCO2_measured)
V_CO2 = np.zeros(pulsos+1)

for i in range(pulsos):
    V_CO2[i+1] = pCO2_measured[i]*VO2
    print(f"El vol de CO2 inyectado en el pulso {i+1} es: ", V_CO2[i+1]-V_CO2[i])
    

print("\n\n RESULTADOS CUBETA\n")
V_recip = 4
VH2O = 1
VO2 = V_recip - VH2O

"""pCO2_measured = (1/1.013)*np.array([0,0,0.14,0.19,0.24,0.30,0.35,0.41,0.47,0.53,0.59,0.66,
                                    0.74,0.81,0.88,0.96,1.03,1.10,1.20,1.29,1.38,1.48,
                                    1.58,1.68,1.79,1.91,2.02,2.14])
"""
    
pCO2_measured = (1/1.013)*np.array([0,0.15,0.26,0.36,0.48,0.60,0.74,0.88,1.03,1.22,1.40,1.59,1.80,2.03,2.25,2.50,2.69,2.75,2.76,2.76])

pulsos = np.size(pCO2_measured)
V_CO2 = np.zeros(pulsos+1)

for i in range(pulsos):
    V_CO2[i+1] = pCO2_measured[i]*VO2
    print(f"Vol de CO2 inyectado en pulso {i+1}: %.4f cc" %(V_CO2[i+1]-V_CO2[i]))
    
plt.scatter(range(21),V_CO2)
plt.title('Volumen de CO2 inyectado en cubeta')
plt.xlabel('pulsos')
plt.ylabel('VCO2 (cc)')
plt.show()

    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:25:46 2024

@author: Rudy
"""

import numpy as np
import matplotlib.pyplot as plt

kh = 1.7e-3
ka1 = 2.5e-4
kH = 29.76

VH2O = 0.002
VO2 = 0.002
V_T = VH2O + VO2
pulso = 0.0008

pCO2_measured = (1/1.013)*np.array([0,0,0.14,0.19,0.24,0.30,0.35,0.41,0.47,0.53,0.59,0.66,
                                    0.74,0.81,0.88,0.96,1.03,1.10,1.20,1.29,1.38,1.48,
                                    1.58,1.68,1.79,1.91,2.02,2.14])

pulsos = np.size(pCO2_measured)
print("Pulsos: ",pulsos)
pCO2_t = np.zeros(pulsos)

for i in range(pulsos):
    pCO2_t[i] = (i*pulso)/V_T

plt.plot(pCO2_t, label="pCO2 teórica")
plt.plot(pCO2_measured, label="pCO2 medida")
plt.title("pCO2 vs pulsos")
plt.xlabel('pulsos')
plt.ylabel('pCO2 (atm)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

pCO2_porc = (pCO2_measured[1:]/pCO2_t[1:])*100
plt.plot(pCO2_porc)
plt.title("porcentaje de pCO2 teórico")
plt.xlabel('pulsos')
plt.ylabel('porcentaje')
plt.grid()
plt.show()

#pCO2_t = np.empty(pulsos)
#pCO2_t[0] = 0
pHi = 8.579
exp = pHi*2

def components(h,p):
    c1 = p/kH
    c2 = kh*c1
    c3 = h-(10**(-exp))/h
    return c1,c2,c3 

for i in range(1,pulsos):
    H_t2 = np.sqrt((10**(-exp))+kh*ka1/kH*pCO2_measured)
    pH_t2 = -np.log10(H_t2)

H_t2 = np.sqrt((10**(-exp))+kh*ka1/kH*pCO2_measured)
pH_t2 = -np.log10(H_t2)

CO2,H2CO3,HCO3 = components(H_t2,pCO2_measured)

print('pCO2 alcanzada es: %.2f' % pCO2_t[-1])
print('pH: %.2f' % pH_t2[-1])
print('CO2: %.2e M' % CO2[-1])
print('H2CO3: %.2e M' % H2CO3[-1])
print('HCO3: %.2e M' % HCO3[-1])

plt.plot(pCO2_measured, CO2, label="CO2")
plt.plot(pCO2_measured, H2CO3, label="H2CO3")
plt.plot(pCO2_measured, HCO3, label="HCO3")
plt.title("pCO2 vs Concentraciones")
plt.xlabel('pCO2 (atm)')
plt.ylabel('Concentraciones (mol/L)')
plt.yscale('log')
plt.legend(loc='upper left')
plt.grid()
plt.show()

#plt.plot(range(pulsos), pH_t, label="pH")
plt.plot(range(pulsos), pH_t2, label="pH")
plt.xlim([0,pulsos])
plt.title("pH teóricos")
plt.xlabel('Pulsos')
plt.ylabel('pH')
plt.grid()
plt.show()

plt.plot(range(pulsos), pCO2_measured)
plt.xlim([0,pulsos])
plt.title("presión alcanzada")
plt.xlabel('Pulsos')
plt.ylabel('pCO2')
plt.grid()
plt.show()

#plt.plot(pCO2_measured, pH_t, label="pH")
plt.plot(pCO2_measured, pH_t2, label="pH")
plt.title("pH vs pCO2")
plt.xlabel('pCO2 atm')
plt.ylabel('pH')
plt.grid()
plt.show()


plt.scatter(range(pulsos)         , CO2)
plt.title("pulsos vs Molaridad CO2")
plt.xlabel('pulsos')
plt.ylabel('M (mol/L)')
plt.grid()
plt.show()


print('CO2: %.4f M' % CO2[5])
print('CO2: %.4f M' % CO2[10])
print('CO2: %.4f M' % CO2[15])
print('CO2: %.4f M' % CO2[19])
print('CO2: %.4f M' % CO2[-1])




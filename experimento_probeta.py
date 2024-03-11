#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:55:38 2024

@author: Rudy
"""
import numpy as np
import matplotlib.pyplot as plt

g = 9.8 #m/s2
po_h2o = 997 #kg/m3

"""
#probeta chiquitita
20cc, 1min
"""
h_ml = np.array([2,3.2,4.5,5.95,7.45,9])
h = 0.01*h_ml*0.65 #pasamos a metros
h_aguja = 10*0.01*0.65

n = np.size(h)
a = np.zeros(n-1)
P = np.zeros(n-1)
dh_ml = np.zeros(n-1)

for i in range(n-1):
    a[i] = h_aguja - h[i]
    P[i] = g*po_h2o*a[i]
    dh_ml[i] = h_ml[i+1]-h_ml[i]
    
P_atm = P/101327 
    
"""
#probeta grande
20cc, 1 min
"""

H_ml = np.array([64.9,65.9,67,68,69,70,71.1,72.2,73.3,74.6])
H = 0.01*H_ml*0.1889 #pasamos a metros
H_aguja = 104*0.01*0.1889

n2 = np.size(H)
a2 = np.zeros(n2-1)
P2 = np.zeros(n2-1)
dH_ml = np.zeros(n2-1)

for i in range(n2-1):
    a2[i] = H_aguja - H[i]
    P2[i] = g*po_h2o*a2[i]
    dH_ml[i] = H_ml[i+1]-H_ml[i]
    

P_atm2 = P2/101327 
plt.scatter(P_atm,dh_ml)
plt.scatter(P_atm2,dH_ml)

plt.title('Presión atm  vs volumen pulso')
plt.xlabel('Presion atm')
plt.ylabel('ml_desplazados')
plt.show()

def d_h(array_h):
    n = np.size(array_h)
    d_h = np.zeros(n-1)
    for i in range(n-1):
        d_h[i] = array_h[i+1]-array_h[i]
    print(d_h)

#above surface

dh_aire = [1.85,1.8,1.8,1.7,1.7]

"""
10cc 1 min
80-86
6cm 
"""

"""
10cc 1 min
doble de tiempo (solo 5 pulsos)
3cm
dh_pip_grande_pdoble = [89.7,91.2,93,94.5,96]

d_h(dh_pip_grande_pdoble)
"""

"""
cuando pensaste, ahv ya quedó
dh_f = [63.3,64.9,65.9,67,68,69,70,71.1,72.2,73.3,74.6]
aguja en 105

"""



"""  vectores juntados"""





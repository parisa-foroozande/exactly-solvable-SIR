# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 00:11:09 2021

@author: ROZHIN
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#_______________________________________________________________________
#Arranging actual data in lists

#importing actual data
data = pd.read_excel (r'C:\Users\ROZHIN\Desktop\Raw.xlsx') 
df = pd.DataFrame(data, columns= ['time','Acc'])

#parameters derived from curve fitting
K=[5037802, 5077658,4660157 , 5074263, 4611069,5039739 , 4609520, 4649150]
a=[0.000601, -0.00063, -0.00066 , -0.00053, 0.000634,0.00055 , 0.000671, -0.00067]
r=[32.75163, -30.9463, -30.0542 , -37.027, 31.69486, 35.78211 , 29.94901, -29.6931]
names=['AZ+', 'AZ-', 'BZ+', 'BZ-', 'AY+', 'AY-', 'BY+', 'BY-']

#_____________________________________________________________________
#plotting all data sets

def model(y, t, r, K, a ):
    A=y
    dAdt= r*A*(1-((A/K)**a))
    return dAdt

y0=1
ret=[]
t=np.arange(0,188,0.1)


#integrating the 8 curves
for i in range(0,8):
    ret.append(odeint(model,y0,t, args=(r[i],K[i],a[i],)))
    i += 1


for i in range(0,8):
    plt.plot(t,ret[i], label= names[i])
    i += 1

plt.plot(df['time'].tolist(), df['Acc'].tolist(), label='Actual Data', marker='o', markersize=6, color='k', markerfacecolor='r')

plt.plot([134,134],[-250000,4500000],'r--')
plt.text(138,100000,'Last day used\n for fitting', size=13)
plt.ylim(bottom=-200000, top= 4100000)
plt.title('COVID-19 in Brazil Accumulated Infection Plot ')
plt.xlabel('Time (in days) - Starting from Feb 14th, 2020')
plt.ylabel('Accumulated Infection')
plt.grid()
plt.legend()
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:22:29 2021

@author: ROZHIN
"""

import numpy as np
import matplotlib.pyplot as plt

def Apeak(a,r,K):
    Ap = K*((r/(a+1))**(1/a))
    return Ap

def F(a,r,K,A):
    f=r*A*(1-((A/K)**(a)))
    return f


A =np.arange(0.0000001,10,0.01)
alpha= np.arange(.01,10,0.01)


#__________________________________________________________________________________________
"""Part 1: Negative values for a""" 
"""To Run this part: activate the following lines and mark Part 2 as comments"""
#r=-1
#K=10
#aval=[-0.5,-0.1,-0.3,-0.7,-0.9,-1,-1.2,-1.4]  
#colors=['blue','orange','green','red','olive','pink','cyan']

#______________________________________________________________________________________
"""Part 2: Positive values for a""" 
"""To Run this part: activate the following lines and mark Part 2 as comments"""

r=1
K=10
aval=[0.2,0.1,0.3,0.7,1,1.5,3,6] #different values of a
colors=['blue','orange','green','red','olive','pink','cyan']

#________________________________________________________________________________

#Plot Iteration
n=0
for n in range(0,len(aval)-1):
    a=aval[n]
    Fgrowth = F(a,r,K,A)
    plt.plot(A,Fgrowth,color=colors[n],label= aval[n]) #the curve
    Fmax= max(Fgrowth)
    Amax = np.argmax(Fgrowth)
    plt.plot(Amax/100,Fmax, marker='D', markerfacecolor='blue') #marker for maximum point of the curve
    plt.text(Amax/100-0.1,Fmax+0.1,round(Fmax,2))
    n+=1

#marker for limit of the maximum's A value as "a" approches zero     
plt.plot(K/np.exp(1),0, marker='X', markerfacecolor= 'red', markersize=30)
plt.text(K/np.exp(1)-0.5,-0.4, 'K/e', color='r',size=15)



plt.ylim(bottom=0, top=5)
plt.title('F-A plot of various values of positive a and their peaks, r=+1, K=10')
plt.ylabel('F')
plt.xlabel('A')
plt.legend()
plt.grid()
plt.show()
    
    
    
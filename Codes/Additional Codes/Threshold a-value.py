# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:09:20 2021

@author: ROZHIN
"""

import numpy as np
import matplotlib.pyplot as plt

#Ratio of H(y_c) to y_e
def H(a): 
    res= ((2*((2**(1/a))/((1+a)**(1/a))))-((2)/(1+a))**((a+1)/(a)))/(2**(1/a))
    return res

#plot of the ratio vs. 'a'
a=np.arange(-0.999,5,0.01)
results=H(a)
plt.plot(a,results, 'b')

#axes and line y=1
plt.plot([-1,5],[0,0], color='k')
plt.plot([0,0],[-2,2],color='k')
plt.plot([-1,5],[1,1], color='r')

#marker for cross point of the curves
plt.plot(3.4034978,1,marker='D')
plt.text(3.034978,1.4,'a=3.4034978,1')

plt.xlim(left=-1,right=5)
plt.ylim(top=2,bottom=-2)
plt.title('H(yc)-y1 ratio')
plt.xlabel('a')
plt.ylabel('Ratio')

plt.grid()
plt.show()
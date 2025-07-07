import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#curve data
r=[77.3681, -0.1460, 68.1746, -0.0866, 103.54, -0.131129, 53.8848, -0.086317]
k=[633787, 1313370, 699919, 1614580, 742090, 1419160, 815251, 1620450]
a=[0.000258, -0.08728, 0.000279, -0.12713, 0.000185, -0.09335, 0.000338, -0.127318]
curvelabels = ['I+','I-','II+','II-','III+','III-','IV+','IV-']
A0=1

#making the differential funciton
def model(y, t, r, k, a ):
    A=y
    dAdt= r*A*(1-((A/k)**a))
    return dAdt
  

y0 = A0

# time points
t = np.linspace(0,600,10000)

ret=[]

#integrating the 8 curves
for i in range(0,8):
    ret.append(odeint(model,y0,t, args=(r[i],k[i],a[i],)))
    i += 1

# plotting fig6
for i in range(0,8):
    plt.plot(t,ret[i]/100000, label= curvelabels[i])
    i += 1
    

plt.xlabel('time ( in days)')
plt.ylabel('A(t) x10^5')
plt.grid()
plt.title('Figure 6')
plt.legend()
plt.show()
#plt.savefig('fig6.png', dpi=800)
plt.figure()

#plotting fig7
for i in range(0,8):
    plt.plot(t,ret[i]/100000, label= curvelabels[i])
    i += 1
    
plt.xlim(right=200)
plt.ylim(top=9)
plt.xlabel('time ( in days)')
plt.ylabel('A(t) x10^5')
plt.grid()
plt.title('Figure 7')
plt.legend()
plt.show()


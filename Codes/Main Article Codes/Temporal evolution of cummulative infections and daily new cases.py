import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


alpha=0.1

beta=1
t = np.linspace(0, 120 , 1000000)
dy=np.zeros(120)
t_for_dy=np.arange(120)

def deriv(y, t, alpha, beta):
    
    dydt = beta*y*(1-(y**alpha))
    print(dydt)
    return dydt

# Initial conditions vector
y0 = 0.00001

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(alpha,beta))
y = ret.T


tau=0
y_for_dy=0.00001
for i in range(120):
    dy[i]=deriv(y_for_dy,tau,alpha,beta)
    y_for_dy=y_for_dy+dy[i]

y=np.reshape(y,(1000000,1))

plt.plot(t,y,'b',label='$y_n$')
plt.plot(t_for_dy,10*dy,'o',color='b',ms=1,label='$\Delta y_n$')
plt.xlabel('n')
plt.ylabel('$y_n$ and $\Delta y_n$')
plt.legend()
plt.show()


alphaa=0.2
beta=1
t = np.linspace(0, 120 , 1000000)
dy=np.zeros(120)
t_for_dy=np.arange(120)

def deriv(y, t, alpha, beta):
    
    dydt = beta*y*(1-(y**alphaa))
    print(dydt)
    return dydt

# Initial conditions vector
y0 = 0.00001

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(alpha,beta))
y = ret.T


tau=0
y_for_dy=0.00001
for i in range(120):
    dy[i]=deriv(y_for_dy,tau,alpha,beta)
    y_for_dy=y_for_dy+dy[i]

y=np.reshape(y,(1000000,1))

plt.plot(t,y,'k',label='$y_n$')
plt.plot(t_for_dy,10*dy,'o',color='k',ms=1,label='$\Delta y_n$')
plt.xlabel('n')
plt.ylabel('$y_n$ and $\Delta y_n$')
plt.legend()
plt.show()
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initial number of I0 and R0 , beta , gamma.
S0 = 10**3
I0 = 10
R0 = 0

kappa = 1/0.004

# Total population
N = I0 + R0 + S0

#time(days)
tau = np.linspace(0, 60 , 1000)

#SIR model differential equations
def A(y, tau, N):
   
    S, I, R = y
    dSdtau = - S * I / N
    dIdtau = ( S - kappa ) * I / N
    dRdtau = kappa * I / N
    return dSdtau, dIdtau, dRdtau

# Initial conditions
y0 = S0, I0, R0

# Integrate the SIR equations over time
SIR = odeint(A, y0, tau, args=(N,))
S, I, R = SIR.T

# Plot SIR
plt.ylabel('Population')
plt.xlabel('Time')

plt.plot(tau/2, S, 'b',label="S")
plt.plot(tau/2, I, 'r',label="I")
plt.plot(tau/2, R, 'g',label="R") 
plt.legend()
plt.figure()

#----------------------
kappa1 = 1/0.002

# Total population
N = I0 + R0 + S0

#time(days)
tau = np.linspace(0, 20 , 1000)

#SIR model differential equations
def A(y, tau, N):
   
    S, I, R = y
    dSdtau = - S * I / N
    dIdtau = ( S - kappa1 ) * I / N
    dRdtau = kappa1 * I / N
    return dSdtau, dIdtau, dRdtau

# Initial conditions
y0 = S0, I0, R0

# Integrate the SIR equations over time
SIR = odeint(A, y0, tau, args=(N,))
S, I, R = SIR.T

# Plot SIR
plt.ylabel('Population')
plt.xlabel('Time')

plt.plot(tau, S, 'b',label="S")
plt.plot(tau, I, 'r',label="I")
plt.plot(tau, R, 'g',label="R") 
plt.legend()
plt.figure()
#---------------------------

kappa2 = 1/0.0013

# Total population
N = I0 + R0 + S0

#time(days)
tau = np.linspace(0, 50 , 1000)

#SIR model differential equations
def A(y, tau, N):
   
    S, I, R = y
    dSdtau = - S * I / N
    dIdtau = ( S - kappa2 ) * I / N
    dRdtau = kappa2 * I / N
    return dSdtau, dIdtau, dRdtau

# Initial conditions
y0 = S0, I0, R0

# Integrate the SIR equations over time
SIR = odeint(A, y0, tau, args=(N,))
S, I, R = SIR.T

# Plot SIR
plt.ylabel('Population')
plt.xlabel('Time')

plt.plot(tau, S, 'b',label="S")
plt.plot(tau, I, 'r',label="I")
plt.plot(tau, R, 'g',label="R") 
plt.legend()
plt.figure()

#---------------------------

for i in np.arange (1.1,2,0.1):
    kappa3 = 1000/i

    #time(days)
    tau = np.linspace(0, 50 , 1000)
    
    #SIR model differential equations
    def A(y, tau, N):
       
        S, I, R = y
        dSdtau = - S * I / N
        dIdtau = ( S - kappa3 ) * I / N
        dRdtau = kappa3 * I / N
        return dSdtau, dIdtau, dRdtau
    
    # Initial conditions
    y0 = S0, I0, R0
    
    # Integrate the SIR equations over time
    SIR = odeint(A, y0, tau, args=(N,))
    S, I, R = SIR.T
    
    # Plot SIR
    plt.ylabel('Population')
    plt.xlabel('Time')
    plt.plot(tau, R, 'g') 
    
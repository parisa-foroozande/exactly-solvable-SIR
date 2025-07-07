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
plt.title('10^3/Kappa = 4 , 1 , 4')
plt.axvline(x=2)
plt.axvline(x=5)
plt.plot(tau/2, S, 'b--',label="S(kappa=1/0.004)")
plt.plot(tau/2, I, 'r--',label="I(kappa=1/0.004)")
plt.plot(tau/2, R, 'g--',label="R(kappa=1/0.004)") 
plt.legend()
plt.show()

#SIR model differential equations
def A(y, tau, N):
    if tau<4:
        kappa = 1/0.004
    if 4<=tau<10:
        kappa = 1/0.001
    if tau>=10:
        kappa = 1/0.004
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
plt.title('10^3/Kappa = 4 , 1 , 4')
plt.axvline(x=2)
plt.axvline(x=5)
plt.plot(tau/2, S, 'b',label="S")
plt.plot(tau/2, I, 'r',label="I")
plt.plot(tau/2, R, 'g',label="R") 
plt.legend()
plt.show()
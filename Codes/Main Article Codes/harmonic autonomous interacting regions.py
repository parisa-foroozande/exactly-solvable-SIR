import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Initial numbers.
S0 , I0 , R0 = 10**3 , 2*10**1 , 0
S00 , I00 , R00 = 10**3 , 2*10**1 , 0

# Total population, N.
N = S0 + I0 + R0

# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.0021 , 0.1
w = 1/3
W = 1/3
a = 40*w/3
A = 2*W/3 
l = 9*10**-4
L = 1
sigma = 20000
Sigma = 0

# A grid of time points (in days)
t = np.linspace(0, 0.05 , 1000)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):

    S1, I1, R1 , S2 , I2 , R2 = y

    #F = w*np.sign((S1-sigma)*(S2-sigma))*((np.absolute(S1-sigma))*np.absolute(S2-sigma))**0.5*np.heaviside(S1*S2,0)
    #J = W*np.sign((I1-Sigma)*(I2-Sigma))*((np.absolute(I1-Sigma))*np.absolute(I2-Sigma))**0.5*np.heaviside(I1*I2,0)
    F = a/w * np.cos(w*t) 
    J = A/W * np.cos(W*t) 
    #F =l*(S1-sigma)*(S2-sigma)*np.heaviside(S1*S2,0)
    #J=0
   
    dS1dt = (-S1 * I1 + F )
    dI1dt = ((S1-gamma/beta) * I1 + J)
    dR1dt = (gamma/beta * I1)
    
    dS2dt = (-S2 * I2 -F)
    dI2dt = ((S2-gamma/beta) * I2  -J)
    dR2dt = (gamma/beta* I2 )
    return dS1dt, dI1dt, dR1dt , dS2dt , dI2dt , dR2dt

# Initial conditions vector
y0 = S0, I0, R0 , S00, I00, R00

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S1, I1, R1 , S2 , I2 , R2 = ret.T
tt = np.linspace(0,0.5/0.0007,1000)
f1 = np.zeros((1000,))
f2 = np.zeros((1000,))
f1 =0.1* np.exp(-0.3j/15*tt)
f2 =0.1* np.exp(-0.2j/15*tt)
P=10
T=0.0007
# Plot the data on three separate curves for S(t), I(t) and R(t)

plt.plot(t/T, (1*S1/P+20), 'blue',linewidth=1,label='$S_1$')
plt.plot(t/T, (0.7*I1/P+20), 'black',linewidth=1,label='$I_1$')
plt.plot(t/T,0.7* R1/P, 'red',linewidth=1,label='$R_1$')

plt.plot(t/T, (0.4*S2/P+80), 'blue',linewidth=1.8,label='$S_2$')
plt.plot(t/T, (0.5*I2/P+20), 'black',linewidth=1.8,label='$I_2$')
plt.plot(t/T, 0.9*R2/P, 'red',linewidth=1.8,label='$R_2$')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title("$S_1(0)=S_2(0)=10^3 , I_1(0)=I_2(0)=20 , R_1(0)=R_2(0)=0$")
plt.legend()
plt.show()
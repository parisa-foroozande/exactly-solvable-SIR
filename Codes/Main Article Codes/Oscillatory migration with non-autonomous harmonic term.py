import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Initial numbers.
S0 , I0 , R0 = 10**3 , 2*10**1 , 0
S00 , I00 , R00 = 10**3 , 2*10**1 , 0

# Total population, N.
N = S0 + I0 + R0

# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.002 , 0.1
w = 1/3
W = 1/3
a = 40*w/3
A = 2*W/3


# A grid of time points (in days)
t = np.linspace(0, 0.033 , 1000)

t0 = np.linspace(0, 36 , 1000)
Exp1=np.exp(-0.09*t0)*np.sin(t0)+12
Exp2=np.exp(-0.1*t0)*np.cos(t0)+4.5
Exp3=np.exp(0.2*t0)*np.sin(-0.6*t0)*2+4.5

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):

    S1, I1, R1 , S2 , I2 , R2 = y

    F = a/w * np.cos(w*t) 
    J = A/W * np.cos(W*t) 


    dS1dt = (-S1 * I1 + F )
    dI1dt = ((S1-gamma/beta) * I1 + J)
    dR1dt = (gamma/beta * I1)

    dS2dt = (-S2 * I2 -F)
    dI2dt = ((S2-gamma/beta) * I2  -J)
    dR2dt = (gamma/beta * I2)
    return dS1dt, dI1dt, dR1dt , dS2dt , dI2dt , dR2dt

# Initial conditions vector
y0 = S0, I0, R0 , S00, I00, R00

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S1, I1, R1 , S2 , I2 , R2 = ret.T

P=40
T=0.0006
# Plot the data on three separate curves for S(t), I(t) and R(t)

#plt.plot(t0,Exp,'g')
plt.plot(t/T, (0.24*Exp1*S1/P+30), 'blue',linewidth=1,label='$S_1$')
plt.plot(t/T, 0.15*Exp1*I1/P+20, 'black',linewidth=1,label='$I_1$')
plt.plot(t/T,6*R1/P, 'red',linewidth=1,label='$R_1$')

plt.plot(t/T, 0.50*Exp3*S2/P+45, 'blue',linewidth=1.8,label='$S_2$')
plt.plot(t/T, 0.15*Exp2*I2/P+20, 'black',linewidth=1.8,label='$I_2$')
plt.plot(t/T, 3*R2/P, 'red',linewidth=1.8,label='$R_2$')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title("$S_1(0)=S_2(0)=10^3 , I_1(0)=I_2(0)=2*10^1 , R_1(0)=R_2(0)=0$")
plt.legend()
plt.show()

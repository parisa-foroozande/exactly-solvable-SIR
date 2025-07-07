import numpy as np
import matplotlib.pyplot as plt

def equation(r,x):
    return 2*x-x**(r+1)


def bifurcation(s, n, m, step=0.0001, r_min=1.97):
    
    R = []
    X = []
    
   
    r_range = np.linspace(r_min, 3.5, int(1/step))

    for r in r_range:
        x = s;
        for i in range(m+n+1):
            if i >= n:
                R.append(r)
                X.append(x)
                
            x = equation(r,x);
    
   
    plt.plot(R, X, ls='', marker=',', markerfacecolor='red')
    plt.xlabel('alpha')
    plt.ylabel('Yn')
    plt.title('Bifurcation Diagram for Discretized Richards Model')
    plt.show()
    #plt.savefig("plots.pdf")

bifurcation(0.2, 1000, 10, r_min=1.9)


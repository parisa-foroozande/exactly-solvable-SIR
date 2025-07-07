
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

"""Cobweb for a greater than a_threshold: diverges to -infinity""" 

rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
dpi = 72


def plot_cobweb(f, r, x0, nmax=40):
   
    x = np.linspace(0, 1.5, 500)
    fig = plt.figure(figsize=(600/dpi, 450/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    # Plot y = f(x) and y = x
    ax.plot(x, f(x, r), c='#444444', lw=2)
    ax.plot(x, x, c='#444444', lw=2)

    # Iterate x = f(x) for nmax steps, starting at (x0, 0).
    px, py = np.empty((2,nmax+1,2))
    px[0], py[0] = x0, 0
    for n in range(1, nmax, 2):
        px[n] = px[n-1]
        py[n] = f(px[n-1], r)
        px[n+1] = py[n]
        py[n+1] = py[n]

    # Plot the path traced out by the iteration.
    ax.plot(px, py, c='b', alpha=0.7)

    # Annotate and tidy the plot.
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('${y_ n}$')
    ax.set_ylabel(f.latex_label)
    ax.set_title('$y_0 = {:.1}, a = {:.2}$'.format(x0, r))
    plt.plot([-1,5],[0,0], color='k')
    plt.plot([0,0],[-2,2],color='k')

    plt.savefig('cobweb_{:.1}_{:.2}.png'.format(x0, r), dpi=dpi)

class AnnotatedFunction:
   
    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# The logistic map, f(x) = rx(1-x).
func = AnnotatedFunction(lambda x,r: 2*x-x**(r+1), r'$H({y_ c})$')


plot_cobweb(func, 3.5, 0.2, 200)


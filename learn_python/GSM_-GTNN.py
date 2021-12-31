from __future__ import division, print_function, unicode_literals
import math
import numpy as np 
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings('ignore')
def grad(x):
     return 2*(np.exp(-x)-4/(np.exp(2*x)))*(-np.exp(-x)+8/(np.exp(2*x)))

def cost(x):
    return (np.exp(x)-(2/np.exp(x)))**2
    #return (np.exp(-x)-4/np.exp(2*x))**2

def myGD1(eta,x0):
    x = [x0]
    for it in range(1000):
        x_new = x[-1] - eta*grad(x[-1])
        print("test %f"%x_new);
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)
    
(x1, it1) = myGD1(0.1,0.5)
print('Solution x1 = %f, cost = %.12f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))

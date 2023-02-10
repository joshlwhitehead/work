from scipy.stats import chi2,norm
import numpy as np
import matplotlib.pyplot as plt
import math

a = .7992
b = -4.5558
c = 1.2018
d = 6.772
z = 1.96
s = .1
yL = 93.5
yU = 96.5


def findNwS(a,b,c,d,z,s,yu,yl,n):
    top = (yu-yl)**2*(a*c*n**2+n*(a*d+b*c)+b*d)
    bottom = z**2*s**2*(n*(a+c)+b+d+np.sqrt(a*c*n**2+n*(a*d+b*c)+b*d))

    return -top/bottom+(n**2-1)/n


n = np.arange(1,100)

def findNwM(a,b,c,d,ybar,yl,yu):
    k = (ybar-yl)/(yu-ybar)

    N = (d-k*b)/(k*a-c)
    return N+1

ybar = np.linspace(90,100)

plt.plot(ybar,findNwM(a,b,c,d,ybar,yL,yU))
# plt.plot(n,findNwS(a,b,c,d,z,s,yU,yL,n))
plt.grid()
plt.show()
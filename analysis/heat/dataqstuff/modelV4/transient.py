import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import fsolve
from scipy.interpolate import interp1d

data = pd.read_csv('test.csv')
therm = data['therm']
time = data['time']
samp = data['samp']
# plt.figure()
# plt.plot(time,samp)
# plt.grid()
# plt.show()


def interpBasic(y1,y2,x,x1,x2):
    y = y1+(x-x1)*(y2-y1)/(x2-x1)
    return y


Tinf = 96
Ti = 55
k = .648
h = 500
L = .0011
ro = 982.36
cp = 4190
alpha = k/ro/cp
Bi = h*L/k
x = np.linspace(0,L,5)
t = np.linspace(0,10,10)
def eigen(x):
    
    return x*np.tan(x)-Bi
si = []
for i in np.arange(1,100*np.pi,np.pi):
    root = fsolve(eigen,i)
    si.append(root[0])
# print(si)



def theta(si,F0,xStar):
    ans = 0
    for i in si:
        Cn = 4*np.sin(i)/(2*i+np.sin(2*i))
        ans += Cn*np.exp(-i**2*F0)*np.cos(i*xStar)

    return ans*(Ti-Tinf)+Tinf


# plt.figure()
for i in x:
    plt.plot(t,theta(si,alpha*t/L**2,i/L))
plt.grid()
plt.show()
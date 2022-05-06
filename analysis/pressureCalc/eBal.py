import getDataPress as gd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from antoine import antoine
watProp = pd.read_csv('waterProp.csv')
temp = watProp['Temperature (C)'].tolist()

U = watProp['Internal Energy (l, kJ/kg)'].tolist()

UInterp = interp1d(temp,U,'cubic')
tempInterp = interp1d(U,temp,'cubic')



samp = gd.getData('lid001Cons2.csv')[2]
therm = gd.getData('lid001Cons2.csv')[1]
for i in samp:
    if str(i) == 'nan':
        samp.remove(i)
for i in therm:
    if str(i) == 'nan':
        therm.remove(i)




h = 10                                          #w/m2/c
r = 8                                           # mm
h = 6
A = np.pi*r**2+2*np.pi*r*h
Tinf = 30


Qconv = h*A*(samp-Tinf)



def dU(T0,T1):
    U0 = UInterp(T0)/1000
    U1 = UInterp(T1)/1000
    return U1-U0


intPV = Qconv - dU(samp[0],samp)
def wEC(T):
    return h*A*(T-Tinf) - dU(T[0],T)

a = 8.07131
b = 1730.63

c = 233.426
temp = np.linspace(25,90)
def V2(T):
    return wEC(T)/antoine(a,b,c,T)

plt.plot(temp,V2(temp))
plt.show()






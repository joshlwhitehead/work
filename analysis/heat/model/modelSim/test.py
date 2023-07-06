from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

x = [100,10000,1000000,100000000]
y = [.6,2,172,16283]

def fun(x,a,b,c,d):
    return a*np.exp(x+b)**c+d

popt,popc = curve_fit(fun,x,y)

plt.plot(x,y,'o')
xx = np.linspace(10,10000)
# plt.plot(xx,fun(xx,*popt))
plt.show()
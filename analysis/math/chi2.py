from scipy.stats import chi2,norm
import numpy as np
import matplotlib.pyplot as plt
import math

a = .7992
b = -4.5558
c = 1.2018
d = 6.772
z = 1.645
s = .1
yL = 93.5
yU = 96.5



def TIlow(ybar,s,z,x2,n):
    x2 = a*(n-1)+b
    k = z*np.sqrt((n-1)*(1+1/n)/x2)
    return ybar-k*s
def TIHigh(ybar,s,z,x2,n):
    x2 = c*(n-1)+d
    k = z*np.sqrt((n-1)*(1+1/n)/x2)
    return ybar+k*s

def TIlowForN(ybar,yL,s,z):
    alpha = ((ybar-yL)/z/s)**2
    return n*(1-alpha*a)-1/n-alpha*(b-a)

def TIhighForN(ybar,yU,s,z):
    alpha = ((yU-ybar)/z/s)**2
    return n*(1-alpha*c)-1/n-alpha*(d-c)

n = np.linspace(3,20)

# plt.plot(n,TIhighForN(3.55e-149,.5,1e-148,z))
# plt.plot(n,TIhighForN(3.55e-149,.03,1e-148,z))
# plt.plot(n,TIlowForN(3.55e-149,.001,1e-148,z))
s = .33
plt.plot(n,TIlow(88.8,s,z,3,n))
plt.plot(n,TIHigh(88.8,s,z,3,n))
# plt.plot(n,TIlow(56.5,s,z,3,n))
# plt.plot(n,TIlow(53.5,s,z,3,n))
# plt.hlines(0,1,20)
plt.grid()
plt.legend()
plt.show()

# print(TIHigh(3.55e-149,1e-148,z,2.733,9))

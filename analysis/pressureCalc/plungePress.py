import numpy as np
from antoine import antoine
import matplotlib.pyplot as plt
a = 8.07131
b = 1730.63
V1 = .116

c = 233.426
def vPlunge(r,l):
    return np.pi*r**2*l/1000

# T = np.linspace(25,90)
T = [25,60,80,90]
L = np.linspace(0,6)
V2 = V1-vPlunge(4.9/2,L)
for i in T:

    P1 = antoine(a,b,c,i)



    P2 = P1*V1/V2
    plt.plot(L,P2,label=''.join([str(i),'c']))
    
    plt.ylabel('Pressure (psig)')
    plt.xlabel('length of plunge (mm)')
    plt.ylim(0,50)
plt.legend()
plt.grid()
plt.show()

# print(vPlunge(4.9/2,L))
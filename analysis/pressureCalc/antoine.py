import numpy as np
import matplotlib.pyplot as plt

def antoine(a,b,c,T):
    return (10**(a-b/(c+T)))/760*14.6959


temp = np.linspace(20,120)

a = 8.07131
b = 1730.63

c = 233.426


plt.plot(temp,antoine(a,b,c,temp),label='water')
plt.xlabel('temp c')
plt.ylabel('psig')
plt.grid()
plt.yticks(np.arange(0,31,1))
plt.xticks(np.arange(20,121,5))
plt.show()
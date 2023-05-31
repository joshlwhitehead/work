from scipy.stats import chi2,norm
import numpy as np
import matplotlib.pyplot as plt


a = .8427
b = -3.9455
c = 1.2018
d = 6.772
z = 1.645
s = 1.982
yl = 19
yb = 23





def n(a,b,x):
    return (x**2-1)/(a*x**2-a*x+b*x) - ((yb-yl)/s/z)**2


nnn = np.linspace(0,10,99)
print(n(a,b,nnn),nnn)
plt.plot(nnn,n(a,b,nnn))
plt.grid()
plt.show()
plt.savefig('test.png')

    





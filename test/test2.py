import numpy as np
import matplotlib.pyplot as plt



xa = np.linspace(np.pi,2*np.pi)
y = np.sin(xa)
y2 = (xa-3*np.pi/2)**2-1


a,b,c,d,e = np.polyfit(xa,y,4)

y2 = a*xa**4+b*xa**3+c*xa**2+d*xa+e


def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2

print(r2(y,y2))


plt.plot(xa,y)
plt.plot(xa,y2)
plt.grid()
plt.show()



x = np.linspace(2*np.pi,3*np.pi)
y = np.sin(x)


y2 = -(a*(xa)**4+b*xa**3+c*xa*2+d*xa+e)


# plt.plot(x,y)
plt.plot(xa,y2)
plt.grid()
plt.show()
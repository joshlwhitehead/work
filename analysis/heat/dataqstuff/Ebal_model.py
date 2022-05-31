import numpy as np
import dataToVar as dat
import matplotlib.pyplot as plt

Tinf = dat.h90_inf[2]
tempSlug = dat.h90_c[3][:len(Tinf)]
tempSamp = dat.h90_c[2][:len(Tinf)]
time = dat.h90_c[0][:len(Tinf)]
k1 = .2
k2 = .2
l1 = .00013
l2 = .0006

ro = 997
cp = 4.2
dx = .006

def dTdt(T1,T2):
    return (T2*(-k1/l1-k2/l2)+k1/l1*T1+k2/l2*Tinf)/ro/cp/dx

plt.figure()
plt.plot(dTdt(tempSlug,tempSamp))
plt.grid()
plt.show()

plt.figure()
# plt.plot(time,tempSlug)
plt.plot(time,-tempSamp)
# plt.plot(time,Tinf)
plt.grid()
plt.show()


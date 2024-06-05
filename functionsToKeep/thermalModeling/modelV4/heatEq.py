import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv('test.csv')
# plt.plot(file['time'],file['therm'])
# plt.plot(file['time'],file['samp'])
# plt.show()


l = 5.5
n = 10
T0 = 20
Ta = 90
Tb = 30
dt = 1
tf = 100
k = 0.648/1000
ro = 982.36/1e9
cp = 4190
alpha = k/ro/cp
# print(k/ro/cp)
dz = l/n
print(dz**2)
z = np.linspace(dz/2,l-dz/2,n)
T = np.ones(n)*T0
dTdt = np.empty(n)

t = np.arange(0,tf,dt)

# for i in range(1,len(t)):
#     plt.clf()
#     for u in range(1,n-1):
#         dTdt[u] = alpha*(-(T[u]-T[u-1])/dz**2+(T[u+1]-T[u])/dz**2)
#     dTdt[0] = alpha*(-(T[0]-Ta)/dz**2+(T[1]-T[0])/dz**2)
#     dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dz**2+(Tb-T[n-1])/dz**2)
#     T += dTdt*dt
#     # print(T)
#     plt.figure(1)
#     plt.plot(z,T)
#     plt.text(.09,T[0],t[i])
#     # plt.savefig('test.png')
#     # plt.show()
#     plt.pause(.01)
    


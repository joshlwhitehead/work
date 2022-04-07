import numpy as np
import matplotlib.pyplot as plt


L = .00448
r = 0.007225                 #m
n = 10


cp = 4180               #J/kg/K
ro = 1000               #kg/m3

T_in = 100              #K inlet
T_out = 23
T0 = 23                #initial


t_fin = 200                 #sec
dt = 1                  

dx = L/n
h = 845

x = np.linspace(dx/2,L-dx/2,n)          #using center of node so /2



T = np.ones(n)*T0
dTdt = np.zeros(n)

t = np.arange(0,t_fin,dt)

for i in range(1,len(t)):
    for j in range(1,n-1):
        dTdt[j] = h*(T[j+1]-2*T[j]+T[j-1])/ro/cp/dx
    dTdt[0] = h*(T_in-2*T[0]+T[1])/ro/cp/dx
    dTdt[n-1] = h*(T_out-2*T[n-1]+T[n-2])/ro/cp/dx
    


    T = T + dTdt*dt

    plt.cla()

    plt.plot(x,T)
    plt.ylim(23,100)
    plt.legend()
    plt.pause(.05)
plt.show()











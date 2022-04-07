import numpy as np
import matplotlib.pyplot as plt
import time

L = 0.0005                     #m


ro = 2770                   #kg/m3
cp = 875                    #J/kg/k
k = 170                     #w/m/k
tfin = 2000                   #sec

n = 10
                      #number of nodes
dx = L/n                    #
alpha = k/ro/cp             #
dt = 1
x = np.linspace(dx/2,L-dx/2,n)

Ts1 = 75         #c
T0 = 23                    #c
Ts2 = 23

Ts11 = 95





T = np.ones(n)*T0
dTdt = np.empty(n)
t = np.arange(0,tfin,dt)
for i in range(len(t)):
    
    for j in range(1,n-1):
        dTdt[j] = alpha*(T[j+1]-2*T[j]+T[j-1])/dx**2

    dTdt[0] = alpha*(T[1]-2*T[0]+Ts1)/dx**2
    dTdt[n-1] = alpha*(Ts2-2*T[n-1]+T[n-2])/dx**2
    if T[-1] <= 65:
        startTimer = i
    if i == startTimer + 30:
        Ts1 = 95
        one = i
        print(i)
    if T[-1] <=90:
        startTimer2 = i
    if i == startTimer2 +30:
        print(i-one)
        break
        

        



    plt.cla()

    plt.plot(x,T)
    T = T+dTdt*dt
    plt.text(.0035,95,''.join(['time=',str(i),' sec']))

    plt.xlabel('Distance (m)')
    plt.ylabel('Temperature (C)')
    plt.ylim(20,100)

    plt.pause(0.0001)
    plt.title('T(x) at '+str(tfin)+' sec')
    plt.grid()
    
# plt.savefig('600sec.png')
plt.show()





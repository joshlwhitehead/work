import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
Ts2_data = pd.read_csv('cham1tempDataQ.csv')['dataQLiquidStg1']
Ts2 = []
for i in Ts2_data:
    if i !=0:
        Ts2.append(i)


L = 0.00448                     #m


ro = 1000                   #kg/m3
cp = 4180                    #J/kg/k
k = .598                     #w/m/k
tfin = 2000                   #sec

n = 8

                      #number of nodes
dx = L/n                    #
alpha = k/ro/cp             #
dt = 1
x = np.linspace(dx/2,L-dx/2,n)

Ts1 = 90         #c
T0 = 23                    #c

hold1 = 90
hold2 = 120
hold3 = 90
hold4 = 180
hold5 = 30
hold6 = 60

mid = []
mi = []
plt.figure(1)
# plt.pause(3)
T = np.ones(n)*T0
dTdt = np.empty(n)
t = np.arange(0,tfin,dt)
for i in range(len(t)):
    
    for j in range(1,n-1):
        dTdt[j] = alpha*(T[j+1]-2*T[j]+T[j-1])/dx**2
    
    
    dTdt[0] = alpha*(T[1]-2*T[0]+Ts1)/dx**2
    dTdt[n-1] = alpha*(Ts2[i]-2*T[n-1]+T[n-2])/dx**2
    



    # if i < hold1: #and Ts2<Ts1:
    #     Ts2 += tim
    # elif i >= hold1 and i <hold1+hold2: #and Ts2>Ts1:
    #     Ts2 -=tim
    # elif i >=hold1+hold2 and i < hold1+hold2+hold3: #and Ts2<Ts1:
    #     Ts2+=tim
    # elif i >= hold1+hold2+hold3 and i < hold1+hold2+hold3+hold4: #and Ts2>Ts1:
    #     Ts2-=tim
    # elif i >= hold1+hold2+hold3+hold4 and i < hold1+hold2+hold3+hold4+hold5: #and Ts2>Ts1:
    #     Ts2-=tim


    
    if i == hold1:                                       #transition
        
        Ts1 = 90   
        x1 = x
        T1 = T       
    elif i == hold1+hold2:
        Ts1 = 75
    elif i == hold1+hold2+hold3:                              #transition
        Ts1 = 115
        x2 = x
        T2 = T
    elif i == hold1+hold2+hold3+hold4:
        Ts1 = 105
    elif i == hold1+hold2+hold3+hold4+hold5:                         #transition
        Ts1 = 45
        x3 = x
        T3 = T




        # print(i)
    
        break
    
    

    plt.cla()

    # plt.plot(x,T,label=   'Transient')
    mid.append(np.average(T[:]))
    mi.append(i)
    T = T+dTdt*dt
    plt.plot(mi,mid)
    plt.text(.0035,95,''.join(['time=',str(i),' sec']))

    plt.xlabel('Distance (m)')
    plt.ylabel('Temperature (C)')
    plt.ylim(20,120)

    plt.pause(0.0001)
    plt.title('Stage 1 Temperature Profile')
    plt.grid()
    
# plt.savefig('600sec.png')
plt.plot(x1,T1,label='65')
plt.plot(x2,T2,label='95')
plt.plot(x3,T3,label='end (~50)')
plt.legend()
plt.show()





import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
data = pd.read_csv('test.csv')
therm = data['therm']
time = data['time']
samp = data['samp']
plt.figure()
plt.plot(time,samp)
plt.grid()
# plt.show()

def TConstantTS(Ts,Ti,x,a,t):
    return (Ti-Ts)*math.erf(x/2/np.sqrt(a*t))+Ts

def TConstantQ(Ta,Tb,k,Ts,Ti,alpha,t,x):
    q2 = k*(Tb-Ta)/np.sqrt(np.pi*alpha*t)
    # q2 = k*(Tb-Ta)/x
    return Ti + 2*q2*np.sqrt(alpha*t/np.pi)/k*np.exp(-x**2/4/alpha/t) - q2*x/k*math.erfc(x/2/np.sqrt(alpha*t))

k = .68
ro = 958.35
cp = 4184
Ti = 25
Ts = 115
Ta = 25
Tb = 90
alpha = k/ro/cp
L = .005



x = np.linspace(0,L,10)
# t = np.arange(1,300,20)
t = time[5:]

temps = []
for i in x:
    temp = []
    count = 0
    for u in t:
        temp.append(TConstantTS(therm[len(therm)-1],Ti,i,alpha,u))
        # temp.append(TConstantQ(Ta,Tb,k,Ts,Ti,alpha,u,i))
        count += 1
    temps.append(temp)

for i in temps:
    plt.plot(t,i)


tempsTranspose = np.array(temps).T
meanTemp = []
for i in tempsTranspose:
    meanTemp.append(np.mean(i))

plt.plot(t,meanTemp,'k')
plt.savefig('test.png')


import numpy as np
import matplotlib.pyplot as plt
import clausis
temp = [90,95,100,105,110,115,120]
temp = np.array(temp)
p = [.0702,.0846,.1014,.1209,.1434,.1692,.1987]
p = np.array(p)


tStart = 23
pStart = 10.88



R = 1205.84

def Pig(T):
    return 8.63e-7*R*T/.02

def pSimp(T1,T2,P1):
    
    return T2*P1/T1





xSimp = np.linspace(273.15+tStart,393.15)
mair = (pSimp(273.15+tStart,xSimp,pStart)[39] -pSimp(273.15+tStart,xSimp,pStart)[38])/ (xSimp[39] - xSimp[38])

def delP(T):
    if T < 97.5:
        return pSimp(tStart,T,pStart) - pStart
    else:
        return clausis.P(T+273.15)*145 - pStart
print(delP(115))

plt.plot(xSimp-273.15,pSimp(273.15+tStart,xSimp,pStart),lw=2,label='Air')
# plt.plot(temp,p*145,lw=2,label='Water')
# plt.plot(clausis.T(p)-273.15,p*145)
plt.plot(temp,clausis.P(temp+273.15)*145,lw=2,label='Water')
plt.title('Water Vapor Pressure')
plt.grid()
plt.xlabel('Temperature (C)')
plt.ylabel('Pressure')
# plt.legend()
# plt.yticks(np.arange(.6,2.1,.1))
plt.xticks(np.arange(20,121,5))
plt.savefig('Stage1Press.png')

plt.show()







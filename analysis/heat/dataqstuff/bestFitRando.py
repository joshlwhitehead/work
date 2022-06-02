
import matplotlib.pyplot as plt
import numpy as np
import dataToVar as dat







data = dat.h100_insertA






samp = -data[2]+max(data[2])
sampRaw = data[2]
time = data[0][:len(samp)]
Tset = np.array(data[1][:len(samp)])
for i in range(len(Tset)):
    if str(Tset[i]) == 'nan':
        Tset[i] = Tset[i-1]
offset = 0.0004947486312725369*Tset**2+ 0.013852650591628062*Tset+ 1.6253000693004136

# print(offset)







def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2

def decay(lam):
    return (max(data[2])-min(data[2]))*np.exp(-lam*time)
def T(lam):
    return (-Tset+offset+30)*np.exp(-lam*time)+Tset-offset

tries = np.arange(0,.1,.0001)

fits = {}
fitsa = {}
for i in tries:
   
    r = r2(samp,decay(i))
    if r >=.9 and r <=1:
        fits[r] = i
    ra = r2(sampRaw,T(i))
    if ra >=.1 and ra <=1:
        
        fitsa[ra] = i  
lamb = fits[max(fits.keys())]
lamba = fitsa[max(fitsa.keys())]
print(lamb)
print(lamba)
print()


plt.plot(-samp+max(data[2]),label='data')
plt.plot(-decay(lamb)+max(data[2]),label='setTemp')
plt.plot(T(lamba),label='tempTherm')
plt.grid()
plt.legend()
plt.show()
print(max(fits.keys()))
print()
print(max(fitsa.keys()))






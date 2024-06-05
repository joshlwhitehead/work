import SiblingDir
import matplotlib.pyplot as plt
import numpy as np
import dataCollect.dataToVar as dat

# a = dat.h50
# b = dat.h70
# c = dat.h90
# d = dat.h100

# a = dat.h50_noInsert
# b = dat.h70_noInsert
# c = dat.h90_noInsert
# d = dat.h100_noInsert

a = dat.h50
b = dat.h70
c = dat.h90
d = dat.h100


# a = dat.h50_insertA
# b = dat.h70_insertA
# c = dat.h90_insertA
# d = dat.h100_insertA    len(a[1]),len(a[2]),len(b[1]),len(b[2])

shortest = min(len(a[1]),len(a[2]),len(b[1]),len(b[2]),len(c[1]),len(c[2]),len(d[1]),len(d[2]))
# shortest = len(c[2])

totalDat = [a,b,c,d]

samp = []
sampRaw = []
time = []
Ttherm = []
for i in totalDat:
    samp.append(-i[2][119:shortest]+max(i[2]))
    sampRaw.append(i[2][119:shortest])
    time.append(i[0][119:shortest])
    Ttherm.append(np.array(i[1][119:shortest]))


for i in Ttherm:
    for j in range(len(i)):
        if str(i[j]) == 'nan':
            i[j] = i[j-1]


for i in range(4):
    print(sampRaw[i][0])


offFif = 50 - 44#np.average(a[2][-50:])

offSev = 70 - 62#np.average(b[2][-50:])
offNin = 90 - 81#np.average(c[2][-50:])
offOne = 100 - 91#np.average(d[2][-50:])         #offFif,
print(offFif,offSev,offNin,offOne)
xx = np.array([50,70,90,100])
yy = np.array([offFif,offSev,offNin,offOne])

aa,bb,cc = np.polyfit(xx,yy,2)                              #offset coeffs
plt.plot(xx,yy,'o')
plt.plot(xx,aa*xx**2+bb*xx+cc)
plt.grid()
print(aa,bb,cc)




def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2

# def decay(lam):
#     return (max(totalDat[i][2])-min(totalDat[i][2]))*np.exp(-lam*time[i])

# def T(lam,Tset,time):
#     offset = aa*Tset**2+bb*Tset+cc
#     return (-Tset+offset+30)*np.exp(-lam*time)+Tset-offset
def T(lam,Tset,time,sampa):
    offset = aa*Tset**2+bb*Tset+cc
    # print(sampa[0])
    return (-Tset[-1]+offset+sampa[0])*np.exp(-lam*time)+Tset[-1]-offset

        



zlist = []
for i in sampRaw:
    for j in i:
        zlist.append(j)
zlist = np.array(zlist)
###############################################################################################################################################################################################


tries = np.arange(0,.1,.0001)

rr = {}
for i in tries:
    zlistFit = []
    for j in range(len(sampRaw)):
        zlistFit.append(T(i,Ttherm[j],time[j],sampRaw[j]))
  
    zlistFitShape = []
    for k in zlistFit:
        for l in k:
            zlistFitShape.append(l)
    zlistFitShape = np.array(zlistFitShape)
    

    r = r2(zlist,zlistFitShape)

    if r >= 0 and r <= 1:
        rr[r] = i
print(max(rr.keys()))
print(rr[max(rr.keys())])
    
    

plt.figure(figsize=(16,9))
for i in range(len(sampRaw)):
    plt.plot(time[i],sampRaw[i])
for i in range(len(totalDat)):
    plt.plot(time[i],T(rr[max(rr.keys())],Ttherm[i],time[i],sampRaw[i]))
    # plt.plot(time[i],T(.025,Ttherm[i],time[i]))
plt.grid()
plt.yticks(np.arange(25,95,5))
# plt.xticks(np.arange(0,500,50))



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.optimize as opt
import dataToVar as dat


################# returns list until 5% max ###############
def percFit(list):
    err = []
    ratioBot = np.average(list[-100:])/list
    for i in ratioBot:
        if i>1.04:
            err.append(i)
    percy = list[100:len(err)]
    percx = np.arange(0,len(percy))
    
    return list[100:len(err)]

fif = dat.newCup50
sev = dat.newCup70
nin = dat.newCup90
one = dat.newCup100




#################### makes a csv ############################
def makeCsv():
    ninFit = percFit(nin[0])
    sevFit = sev[0][100:len(ninFit)+100]
    fifFit = fif[0][100:len(ninFit)+100]
    oneFit = one[0][100:len(ninFit)+100]
    sevsev = dat.newCup70b[0][100:len(ninFit)+100]
    ninThermFit = nin[1][100:len(ninFit)+100]
    fifThermFit = fif[1][100:len(ninFit)+100]
    sevThermFit = sev[1][100:len(sevFit)+100]
    oneThermFit = one[1][100:len(oneFit)+100]

    # ninFit = nin[100:].tolist()
    # sevFit = sev[100:len(ninFit)+100]
    # fifFit = fif[100:len(ninFit)+100]
    # onetFit = onet[100:len(ninFit)+100]
    # print(ninFit)
    
    import pandas as pd
    dF = pd.DataFrame({'time':np.arange(0,len(ninFit)),
                        20:fifFit,
                        40:sevFit,
                        60:ninFit,
                        80:oneFit,
                        999:sevsev,
                        '20therm':fifThermFit,
                        '40therm':sevThermFit,
                        '60therm':ninThermFit,
                        '80therm':oneThermFit})
    dF.to_csv('percData4.csv')
# makeCsv()

data = 'percData2.csv'
Ttherm = ['20therm','40therm','60therm','80therm']
time = pd.read_csv(data)['time']
Tset = [20,40,60,80]
T = time.tolist()
TIME,TSET = np.meshgrid(T,Tset)
# print(len(TIME))

x = []
y = []
z = []

for i in Tset:
    for u in T:
        y.append(i)





def fun(a):
    c = []
    for i in a:
        c.append(np.array(pd.read_csv(data)[str(i)]-np.min(pd.read_csv(data)[str(i)]).tolist()))
    return np.array(c)

TempMat = fun(Tset)
thermMat = fun(Ttherm)
# print(TempMat)
# for i in range(len(TempMat)):
#     plt.plot(TempMat[i],thermMat[i])


for i in TempMat:
    for u in i:
        z.append(u)
for i in thermMat:
    for u in i:
        x.append(u)


def fitFun(xy,a,b,c,d,e,f,g,h):
    x=xy[0]
    y=xy[1]
    return (a*(x+f)**e+d)+(b*y+c)                                        ####################################################################################################


param2d,xxx = opt.curve_fit(fitFun,[x,y],z)

# print(*param2d)

def r2(temp):
    st = sum((TempMat[temp]-np.average(TempMat[temp]))**2)
    sr = sum((TempMat[temp]-fitFun([TIME,TSET],*param2d)[temp])**2)
    r2 = 1-sr/st
    return round(r2,3)

def r2surf():
    zlist = []
    for i in TempMat:
        for u in i:
            zlist.append(u)


    zlistfit = []
    for i in fitFun([TIME,TSET],*param2d):
        for u in i:
            zlistfit.append(u)
    zlist = np.array(zlist)
    zlistfit = np.array(zlistfit)

    st = sum((zlist-np.average(zlist))**2)
    sr = sum((zlist-zlistfit)**2)
    r2 = 1-sr/st
    return round(r2,3)

def r2(temp):

    st = sum((TempMat[temp]-np.average(TempMat[temp]))**2)
    sr = sum((TempMat[temp]-fitFun([TIME,TSET],*param2d)[temp])**2)
    r2 = 1-sr/st
    return round(r2,3)

# print('50: ',r2(0))
# print('70: ',r2(1))
# print('90: ',r2(2))
# print('110: ',r2(3)) 
# print('surf: ',r2surf())
# print(len(Tset[0]))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(TempMat,TSET,thermMat,label='data')
# ax.plot_wireframe(thermMat*TempMat-np.min(thermMat*TempMat),TSET,TempMat,label='data')
# ax.plot_wireframe(thermMat*TempMat-np.min(thermMat*TempMat),TSET,fitFun([thermMat,TSET],*param2d),color='orange')

ax.set_xlabel('Thermister')
ax.set_ylabel('Set')
ax.set_zlabel('Sample')

# ax.plot_wireframe(TIME,TSET,fitFun([TIME,TSET],*param2d),color='orange',label='fit')
ax.legend()
# plt.savefig('ddd')
plt.show()


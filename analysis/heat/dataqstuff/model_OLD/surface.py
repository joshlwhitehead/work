import matplotlib.pyplot as plt
# from plotAvgTemp import sev, nin, fiff,onet
import pandas as pd
import numpy as np
import scipy.optimize as opt

data = 'percData.csv'


time = pd.read_csv(data)['time']
# print(len(time)*2)
Tset = [20,40,60,80]
T = time.tolist()
TIME,TSET = np.meshgrid(T,Tset)
# print(len(TIME[0]),len(TSET[0]))
xdata = [T,Tset]
x = []
y = []
z = []
for i in Tset:
    for u in T:
        y.append(i)
for i in Tset:
    for u in T:
        x.append(u)



def fitFun(xy,a,b,c,d,e,f,g,h):
    x=xy[0]
    y=xy[1]
    # return a*np.arctan(x**e+d)*np.log(x)+(b*y**g+c)

    return (a*np.log(x**b+c)+d)*(e*y**f+g)+h


def fun(a):
    c = []
    for i in a:
        c.append(np.array(pd.read_csv(data)[str(i)].tolist()))
    return np.array(c)
hal = fun(Tset)
for i in hal:
    for u in i:
        z.append(u)
# print(x)
# print(len(time))

param2d,xxx = opt.curve_fit(fitFun,[x,y],z)
print(param2d)
def r2(temp):

    st = sum((hal[temp]-np.average(hal[temp]))**2)
    sr = sum((hal[temp]-fitFun([TIME,TSET],*param2d)[temp])**2)
    r2 = 1-sr/st
    return round(r2,3)


def makeCsv():
    dF = pd.DataFrame({20:fitFun([TIME,TSET],*param2d)[0],
    40:fitFun([TIME,TSET],*param2d)[1],
    60:fitFun([TIME,TSET],*param2d)[2],
    80:fitFun([TIME,TSET],*param2d)[3]})
    dF.to_csv('fitData3d.csv')
# makeCsv()



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(TIME,TSET,hal,label='data')
ax.plot_wireframe(TIME,TSET,fitFun([TIME,TSET],*param2d),color='orange',label='fit')
ax.legend()
plt.show()

plt.plot(fitFun([TIME,TSET],*param2d)[0],label='50fit')
plt.plot(hal[0],label='50data')
plt.plot(fitFun([TIME,TSET],*param2d)[1],label='70fit')
plt.plot(hal[1],label='70data')
plt.plot(fitFun([TIME,TSET],*param2d)[2],label='90fit')
plt.plot(hal[2],label='90data')
plt.plot(fitFun([TIME,TSET],*param2d)[3],label='110fit')



plt.plot(hal[3],label='110data')

plt.text(150,30,''.join(['r2_50: ',str(r2(0)),'\n','r2_70: ',str(r2(1)),'\n','r2_90: ',str(r2(2)),'\n','r2_110: ',str(r2(3))]))
plt.grid()
plt.legend()

plt.savefig('comp3dFit.png')

def r2surf():
    zlist = []
    for i in hal:
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

    st = sum((hal[temp]-np.average(hal[temp]))**2)
    sr = sum((hal[temp]-fitFun([TIME,TSET],*param2d)[temp])**2)
    r2 = 1-sr/st
    return round(r2,3)

print('50: ',r2(0))
print('70: ',r2(1))
print('90: ',r2(2))
print('110: ',r2(3)) 
print('surf: ',r2surf())
import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np
import scipy.optimize as opt
import dataToVar as dat

tset = [50,80,100]
###################### normalize therm by set and fit that by sample #########################
nin = dat.h90
fif = dat.h50
sev = dat.h70
one = dat.h100

fifSamp = np.array(fif[0][100:])-np.min(fif[0])
sevSamp = np.array(sev[0][100:])-np.min(sev[0])
ninThermNorm = np.array(nin[1][100:])/90
ninSamp = np.array(nin[0][100:])-np.min(nin[0])
oneSamp = np.array(one[0][100:])-np.min(one[0])
# print(np.min(fif[0]))
# print(np.min(sev[0]))
# print(np.min(nin[0]))
# plt.plot(ninThermNorm[100:],ninSamp[100:])
# plt.show()
# print(ninThermNorm[:10])
lessOne = []
for i in ninThermNorm:
    if i <= 1:
        # print(i)
        lessOne.append(i)
    else:
        break
lessOne = np.array(lessOne)
a,b = np.polyfit(ninThermNorm,ninSamp,1)

def fit(x,a,b,c,d):
    return a*np.exp(x+b)**c+d
# print(len(lessOne),len(ninSamp))
param,xxx = opt.curve_fit(fit,lessOne,ninSamp[:len(lessOne)])
# coef = *param
def r2(y,fun):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fun)**2)
    r2 = 1-sr/st
    return round(r2,3)
# print(r2(ninSamp[:len(lessOne)],fit(lessOne,*param)))

# print(*param)
# plt.figure()
# plt.plot(lessOne,ninSamp[:len(lessOne)])
# plt.plot(lessOne,fit(lessOne,*param))
# # plt.plot(lessOne,a*lessOne+b)
# plt.grid()
# plt.savefig('fitToOne')




"""                        sample as function of # of data points since maxTherm               """



def percFit(list):
    err = []
    ratioBot = np.average(list[-100:])/list
    for i in ratioBot:
        if i>1.05:
            err.append(i)
    # percy = list[100:len(err)]
    # percx = np.arange(0,len(percy))
    
    return np.array(list[100:len(err)])

ninSamp2 = percFit(ninSamp[len(lessOne):])-percFit(ninSamp[len(lessOne):])[0]
ninNumDat = np.arange(0,len(ninSamp2))
sevSamp2 = sevSamp[len(lessOne):len(ninSamp2)+len(lessOne)]-sevSamp[len(lessOne):len(ninSamp2)+len(lessOne)][0]
# sevNumDat = np.arange(0,len(sevSamp2))
fifSamp2 = fifSamp[len(lessOne):len(ninSamp2)+len(lessOne)]-fifSamp[len(lessOne):len(ninSamp2)+len(lessOne)][0]

# fifNumDat = np.arange(0,len(fifSamp2))
oneSamp2 = oneSamp[len(lessOne):len(ninSamp2)+len(lessOne)]-oneSamp[len(lessOne):len(ninSamp2)+len(lessOne)][0]
# oneNumDat = np.arange(0,len(oneSamp2))

NUM,TSET = np.meshgrid(ninNumDat,tset)
SAMP = np.array([fifSamp2,ninSamp2,oneSamp2])
# print(NUM)
x = []
y = []
z = []
for i in tset:
    for u in ninNumDat:
        y.append(i)
        x.append(u)
for i in SAMP:
    for u in i:
        z.append(u)

def fitSurf(xy,a,b,c,d,e,f):
    x = xy[0]
    y = xy[1]
    return (a*x**b+c) * (d*y**e+f)                      #############################################################################################################

# plt.plot(ninSamp2)
# plt.plot(sevSamp2)
# plt.plot(oneSamp2)
# plt.plot(fifSamp2)
# plt.savefig('x')
# print(z)
coef3d,xxx = opt.curve_fit(fitSurf,[x,y],z)
# print(coef3d)
def r2surf():
    zlist = []
    for i in SAMP:
        for u in i:
            zlist.append(u)
    zlistfit = []
    for i in fitSurf([NUM,TSET],*coef3d):
        for u in i:
            zlistfit.append(u)
    zlist = np.array(zlist)
    zlistfit = np.array(zlistfit)

    st = sum((zlist-np.average(zlist))**2)
    sr = sum((zlist-zlistfit)**2)
    r2 = 1-sr/st
    return round(r2,3)
# print(r2surf())
# print(type(SAMP))
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_wireframe(NUM,TSET,SAMP)
# ax.plot_wireframe(NUM,TSET,fitSurf([NUM,TSET],*coef3d),color='orange')
# plt.show()








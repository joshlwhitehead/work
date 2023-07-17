import matplotlib.pyplot as plt
import numpy as np
from parseTxt import modelTune
from scipy.interpolate import interp1d
from timeit import default_timer as timer
import random
from itertools import chain



start = timer()
def listToListList(li):
    return np.array(list(map(lambda item:[item],li)))
def calculation(T0,offset,someTemp,lam,time):                               #someTemp is either thermistor temp or set temp

    return (-someTemp+offset+T0)*np.exp(-lam*(time))+someTemp-offset
def randomGenExclude(toExclude,minim,maxim,popSize):
    toExclude = list(chain.from_iterable(toExclude))
    randList = []
    while len(randList) < popSize:
        randNum = random.uniform(minim,maxim)
        if randNum not in toExclude:
            randList.append(randNum)
    return randList
    
def off(someTemp,a,b):
    return a*someTemp+b
# a = -0.0013693467336683212
# b = 0.2659547738693443
# c = -3.881909547738627
def kalman(someTemp,old,kal,a,b):
    # print(len(old),len(kal),len(off(someTemp,a,b)))
    # old=24
    kalFull = [old]
    for i in someTemp:
        old = old*kal+(i-off(someTemp,a,b))*(1-kal)
        
        kalFull.append(old)
    
    return np.array(old)

def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2

file = 'justKalman_4.txt'
fullData = modelTune(file)
therm = [np.array(fullData[i][1][0]) for i in range(len(fullData))]
samp = [np.array(fullData[i][0][0]) for i in range(len(fullData))]
mod = [np.array(fullData[i][1][1]) for i in range(len(fullData))]
sampTime = [np.array(fullData[i][0][1]) for i in range(len(fullData))]
time = [np.array(fullData[i][1][2]) for i in range(len(fullData))]
# print(sampTime[4])
T0 = samp[0][0]
mod.append([T0])



popSize = 10         #DONT GO UP TO 100000!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# lamHeatL = 0
# lamHeatH = .1
# lamCoolL = 0
# lamCoolH = .01
# off1L = -5
# off1H = 5
# off2L = -5
# off2H = 5
# kalHeatL = .99
# kalHeatH = 1
# kalCoolL = .999
# kalCoolH = 1
# lamHeatEx = []
# lamCoolEx = []
# kalHeatEx = []
# kalCoolEx = []
# off1Ex = []
# off2Ex = []
# monteHeat = listToListList(np.random.uniform(lamHeatL,lamHeatH,popSize))
# monteCool = listToListList(np.random.uniform(lamCoolL,lamCoolH,popSize))
# monteOff1 = listToListList(np.random.uniform(off1L,off1H,popSize))
# monteOff2 = listToListList(np.random.uniform(off2L,off2H,popSize))
# # monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
# kalHeat = listToListList(np.random.uniform(kalHeatL,kalHeatH,popSize))
# kalCool = listToListList(np.random.uniform(kalCoolL,kalCoolH,popSize))
monteHeat = listToListList(np.zeros(popSize))
monteCool = monteHeat
kalHeat = listToListList(np.ones(popSize)*0.9988)
kalCool = listToListList(np.ones(popSize)*.9995)
monteOff1 = listToListList(np.ones(popSize)*.4613)
monteOff2 = listToListList(np.ones(popSize)*-12.603)
# arangeDx = .0001
# monteOff1 = listToListList(np.linspace(off1L,off1H,popSize))
# monteOff2 = listToListList(np.linspace(off2L,off2H,popSize))
# # monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
# kalHeat = listToListList(np.linspace(kalHeatL,kalHeatH,popSize))
# kalCool = listToListList(np.linspace(kalCoolL,kalCoolH,popSize))
rrrr = 0
# popSize = len(kalHeat)
# print(len(kalHeat))
# print(len(monteOff1))

while round(rrrr,2) < 0.1:
    
    # monteHeat = listToListList(np.random.uniform(lamHeatL,lamHeatH,popSize))
    # monteCool = listToListList(np.random.uniform(lamCoolL,lamCoolH,popSize))
    # monteOff1 = listToListList(np.random.uniform(off1L,off1H,popSize))
    # monteOff2 = listToListList(np.random.uniform(off2L,off2H,popSize))
    # # monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
    # kalHeat = listToListList(np.random.uniform(kalHeatL,kalHeatH,popSize))
    # kalCool = listToListList(np.random.uniform(kalCoolL,kalCoolH,popSize))
    

    # print(type(monteHeat))
    section = [0,1,2,3,4,5]
    rr = {}
    fullSamp = []
    fullTime = []
    fullTherm = []
    fullThermTime = []
    fullMod = []
    for sec in section:
        fullSamp += list(samp[sec])
        fullTime += list(sampTime[sec])
        fullTherm += list(therm[sec])
        fullThermTime += list(time[sec])
        fullMod += list(mod[sec])
    fullSamp = np.array(fullSamp)
    fullTime = np.array(fullTime)
    fullTherm = np.array(fullTherm)
    fullThermTime = np.array(fullThermTime)
    fullMod = np.array(fullMod)


    # print(listToListList(monteHeat))
    totInterp = []
    for sec in section:
        if sec == 0:
            T0New = listToListList(np.ones(popSize)*24)
            # print(popSize)
            test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2)
            testInterp = interp1d(time[sec],test)(sampTime[sec])
            totInterp += list(testInterp)
        elif sec == 1:
            totInterpTranspose = np.array(totInterp).T
            T0New = listToListList(totInterpTranspose[-1])
            
            test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2)
            testInterp = interp1d(time[sec],test)(sampTime[sec])
            totInterp += list(testInterp) 
        elif sec == 2:
            totInterpTranspose = np.array(totInterp[-popSize:]).T
            T0New = listToListList(totInterpTranspose[-1])
            test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2)
            testInterp = interp1d(time[sec],test)(sampTime[sec])
            totInterp += list(testInterp)
        elif sec == 3:
            totInterpTranspose = np.array(totInterp[-popSize:]).T
            T0New = listToListList(totInterpTranspose[-1])
            test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2)
            # test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
            testInterp = interp1d(time[sec],test)(sampTime[sec])
            totInterp += list(testInterp) 
        elif sec == 4:
            totInterpTranspose = np.array(totInterp[-popSize:]).T
            T0New = listToListList(totInterpTranspose[-1])
            test = kalman(therm[sec],T0New,kalCool,monteOff1,monteOff2)
            testInterp = interp1d(time[sec],test)(sampTime[sec])
            totInterp += list(testInterp)
        elif sec == 5:
            totInterpTranspose = np.array(totInterp[-popSize:]).T
            T0New = listToListList(totInterpTranspose[-1])
            test = kalman(therm[sec],T0New,kalCool,monteOff1,monteOff2)
            # test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
            testInterp = interp1d(time[sec],test)(sampTime[sec])
            totInterp += list(testInterp) 

    totInterpNew = []
    for indx,val in enumerate(totInterp[:popSize]):
        # totInterpNew.append(list(val))
        # for i in range(1,6):
        #     totInterpNew += list(totInterp[indx+popSize*i])
        totInterpNew.append(list(val)+list(totInterp[indx+popSize])+list(totInterp[indx+popSize*2])+list(totInterp[indx+popSize*3])+list(totInterp[indx+popSize*4])+list(totInterp[indx+popSize*5]))
    # 
    for indx,val in enumerate(totInterpNew):
        rr[r2(fullSamp,val)] = [monteHeat[indx],monteCool[indx],kalHeat[indx],kalCool[indx],monteOff1[indx],monteOff2[indx],val]
        # totIn

    rrrr = max(rr.keys())
    print(rrrr)

    lamHeatEx.append(list(chain.from_iterable(monteHeat)))
   
    lamCoolEx.append(list(chain.from_iterable(monteCool)))
    kalHeatEx.append(list(chain.from_iterable(kalHeat)))
    kalCoolEx.append(list(chain.from_iterable(kalCool)))
    off1Ex.append(list(chain.from_iterable(monteOff1)))
    off2Ex.append(list(chain.from_iterable(monteOff2)))


    monteHeat = listToListList(randomGenExclude(lamHeatEx,lamHeatL,lamHeatH,popSize))
    monteCool = listToListList(randomGenExclude(lamCoolEx,lamCoolL,lamCoolH,popSize))
    monteOff1 = listToListList(randomGenExclude(off1Ex,off1L,off1H,popSize))
    monteOff2 = listToListList(randomGenExclude(off2Ex,off2L,off2H,popSize))
    # monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
    kalHeat = listToListList(randomGenExclude(kalHeatEx,kalHeatL,kalHeatH,popSize))
    kalCool = listToListList(randomGenExclude(kalCoolEx,kalCoolL,kalCoolH,popSize))
 

# print(list(chain.from_iterable(lamHeatEx)))
# print(max(rr.keys()))
print(rr[max(rr.keys())][:-1])
# print(rr[max(rr.keys())])
# section = 4
# testCool = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],0.00525,time[section]-time[section][0]-5)
# testCoolInterp = interp1d(time[section],testCool)(sampTime[section])

end = timer()

print(end-start)
plt.plot(fullTime,fullSamp,label='sample')
plt.plot(fullTime,rr[max(rr.keys())][-1],label='new model')
plt.plot(fullThermTime,fullTherm,label='thermistor')
plt.plot(fullThermTime,fullMod,label='old model')
plt.legend()
plt.grid()
plt.show()

# heatLambda()

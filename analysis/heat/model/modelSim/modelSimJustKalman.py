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
    

def off(someTemp,a,b,c):
    return a*someTemp**2+b*someTemp+c
# a = -0.0013693467336683212
# b = 0.2659547738693443
# c = -3.881909547738627


def kalman(someTemp,old,kal,a,b,c):
    # print(len(old),len(kal),len(off(someTemp,a,b)),len(someTemp))
    kalFull = []
    for i in someTemp:
        offset = off(i,a,b,c)
        old = old*kal+(i-offset)*(1-kal)
        kalFull.append(old)
    # print(len(kalFull),len(someTemp))
    return np.array(kalFull)


def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2
def interpolate(x,x1,x2,y1,y2):
    return y1 + (x-x1)*(y2-y1)/(x2-x1)


def doubleData(data,dataTime):
    print(len(data[0]))
    print(len(dataTime[0]))
    newData = []
    newDataTime = []
    for i in range(len(data)):
        newDataSec = []
        newDataTimeSec = []
        
        for indx,val in enumerate(data[i]):
            if val != (data[i][0] and data[i][-1]):
                x1 = dataTime[i][indx]
                x2 = dataTime[i][indx+1]
                x = (x1+x2)*0.5
                y1 = val
                y2 = data[i][indx+1]

                newDataSec.append(y1)
                newDataSec.append(interpolate(x,x1,x2,y1,y2))
                newDataTimeSec.append(x1)
                newDataTimeSec.append(x)
        newData.append(newDataSec)
        newDataTime.append(newDataTimeSec)

    return newData,newDataTime

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

therm1 = doubleData(therm,time)[0]
time1 = doubleData(therm,time)[1]
print(len(therm[0]))


popSize = 100         #DONT GO UP TO 100000!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

off1L = -1
off1H = 1
off2L = -1
off2H = 1
kalHeatL = .9
kalHeatH = 1
kalCoolL = .9
kalCoolH = 1
lamHeatEx = []
lamCoolEx = []
kalHeatEx = []
kalCoolEx = []
off1Ex = []
off2Ex = []

# monteOff1 = listToListList(np.random.uniform(off1L,off1H,popSize))
# monteOff2 = listToListList(np.random.uniform(off2L,off2H,popSize))
# # monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
# kalHeat = listToListList(np.random.uniform(kalHeatL,kalHeatH,popSize))
# kalCool = listToListList(np.random.uniform(kalCoolL,kalCoolH,popSize))

emptyOnes = np.ones(popSize)

monteOff1 = -0.0027263
monteOff2 = .4613
monteOff3 = -12.603
kalHeat = .9988
kalCool = .9995


rrrr = -4

        

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
print(len(fullTherm))


# print(listToListList(monteHeat))
totInterp = []
for sec in section:
    if sec == 0:
        T0New = 24
        
        test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2,monteOff3)
        # print(test)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp)
    elif sec == 1:
        totInterpTranspose = np.array(totInterp).T
        T0New = totInterpTranspose[-1]
        # print(T0New)
        test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2,monteOff3)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp) 
    elif sec == 2:
        totInterpTranspose = np.array(totInterp[-popSize:]).T
        T0New = totInterpTranspose[-1]
        test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2,monteOff3)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp)
    elif sec == 3:
        totInterpTranspose = np.array(totInterp[-popSize:]).T
        T0New = totInterpTranspose[-1]
        test = kalman(therm[sec],T0New,kalHeat,monteOff1,monteOff2,monteOff3)
        # test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp) 
    elif sec == 4:
        totInterpTranspose = np.array(totInterp[-popSize:]).T
        T0New = totInterpTranspose[-1]
        test = kalman(therm[sec],T0New,kalCool,monteOff1,monteOff2,monteOff3)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp)
    elif sec == 5:
        totInterpTranspose = np.array(totInterp[-popSize:]).T
        T0New = totInterpTranspose[-1]
        test = kalman(therm[sec],T0New,kalCool,monteOff1,monteOff2,monteOff3)
        # test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp) 

totInterpNew = []
# for indx,val in enumerate(totInterp[:popSize]):
    # totInterpNew.append(list(val))
    # for i in range(1,6):
    #     totInterpNew += list(totInterp[indx+popSize*i])
    # print(val)

# totInterpNew.append(list(val)+list(totInterp[indx+popSize])+list(totInterp[indx+popSize*2])+list(totInterp[indx+popSize*3])+list(totInterp[indx+popSize*4])+list(totInterp[indx+popSize*5]))
# 
# for indx,val in enumerate(totInterpNew):
rr[r2(fullSamp,totInterp)] = [kalHeat,kalCool,monteOff1,monteOff2,monteOff3,totInterp]
    # totIn

rrrr = max(rr.keys())
print(rrrr)


# kalHeatEx.append(list(chain.from_iterable(kalHeat)))
# kalCoolEx.append(list(chain.from_iterable(kalCool)))
# off1Ex.append(list(chain.from_iterable(monteOff1)))
# off2Ex.append(list(chain.from_iterable(monteOff2)))



# monteOff1 = listToListList(randomGenExclude(off1Ex,off1L,off1H,popSize))
# monteOff2 = listToListList(randomGenExclude(off2Ex,off2L,off2H,popSize))
# # monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
# kalHeat = listToListList(randomGenExclude(kalHeatEx,kalHeatL,kalHeatH,popSize))
# kalCool = listToListList(randomGenExclude(kalCoolEx,kalCoolL,kalCoolH,popSize))
 

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
plt.savefig('test.png')

# heatLambda()

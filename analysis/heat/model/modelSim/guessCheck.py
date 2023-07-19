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
    # toExclude = list(chain.from_iterable(toExclude))
    randList = []
    while len(randList) < popSize:
        randNum = random.uniform(minim,maxim)
        if randNum not in toExclude:
            randList.append(randNum)
    return np.array(randList)
    

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
        # print(offset)
        old = old*kal+(i-offset)*(1-kal)
        kalFull.append(old)
    # print(len(kalFull),len(someTemp))
    return np.array(kalFull)


def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2



def doubleData(data,dataTime):
    newData = []
    newDataTime = []
    for i in range(len(data)):
        newT = np.linspace(dataTime[i][0],dataTime[i][-1],len(dataTime[i])*3)
        newD = interp1d(dataTime[i],data[i])(newT)
        newData.append(newD)
        newDataTime.append(newT)
    return newData,newDataTime

file = 'kalmanOnlyMorePrints1.txt'
fullData = modelTune(file)
therm = [np.array(fullData[i][1][0]) for i in range(len(fullData))]
samp = [np.array(fullData[i][0][0]) for i in range(len(fullData))]
mod = [np.array(fullData[i][1][1]) for i in range(len(fullData))]
sampTime = [np.array(fullData[i][0][1]) for i in range(len(fullData))]
time = [np.array(fullData[i][1][2]) for i in range(len(fullData))]
# print(sampTime[4])
T0 = samp[0][0]
mod.append([T0])

# therm1 = doubleData(therm,time)[0]
# time1 = doubleData(therm,time)[1]
# print(len(therm1[0]))


popSize = 10         #DONT GO UP TO 100000!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

off1L = -.1
off1H = .1
off2L = -1
off2H = 1
off3L = -100
off3H = 100
kalHeatL = 0
kalHeatH = 1
kalCoolL = 0
kalCoolH = 1

kalHeatEx = []
kalCoolEx = []
off1Ex = []
off2Ex = []
off3Ex = []

# monteOff1 = np.random.uniform(off1L,off1H,popSize)
# monteOff2 = np.random.uniform(off2L,off2H,popSize)
# monteOff3 = np.random.uniform(off3L,off3H,popSize)
# kalHeat = np.random.uniform(kalHeatL,kalHeatH,popSize)
# kalCool = np.random.uniform(kalCoolL,kalCoolH,popSize)

# print(monteOff1)
# print(randomGenExclude(monteOff1,off1L,off1H,popSize))
emptyOnes = np.ones(popSize)

gOff1 = -0.0027263
gOff2 = .4653
gOff3 = -10.603
gkalHeat = .9984
gkalCool = .9996

gOff1 = 0
gOff2 = -4.006835899048015e-14
gOff3 = 6.5316881644389095
gkalHeat = 0.9984199262731229
gkalCool = 0.9997104153556947

        

# print(type(monteHeat))
section = [0,1,2,3,4,5]

fullSamp = []
fullTime = []
fullTherm = []
fullThermTime = []
fullThermTime1 = []
fullMod = []
for sec in section:
    fullSamp += list(samp[sec])
    fullTime += list(sampTime[sec])
    fullTherm += list(therm[sec])
    fullThermTime += list(time[sec])
    fullThermTime1 += list(time[sec])
    fullMod += list(mod[sec])
fullSamp = np.array(fullSamp)
fullTime = np.array(fullTime)
fullTherm = np.array(fullTherm)
fullThermTime = np.array(fullThermTime)
fullThermTime1 = np.array(fullThermTime1)
fullMod = np.array(fullMod)
# print(len(fullTherm))

rrrr = 0
def buildModel(kalHeat1,kalCool1,monteOff11,monteOff21,monteOff31):
    rr = {}
    # print(listToListList(monteHeat))
    newInterp = []
    for sec in section:
        if sec == 0:
            T0New = 24
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21,monteOff31).T
            
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
            
        elif sec == 1:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21,monteOff31).T
            
        
                
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))


        elif sec == 2:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21,monteOff31).T
            
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
        elif sec == 3:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21,monteOff31).T
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
        elif sec == 4:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalCool1,monteOff11,monteOff21,monteOff31).T
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
        elif sec == 5:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalCool1,monteOff11,monteOff21,monteOff31).T
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))



    rr[r2(fullSamp,newInterp)] = [kalHeat1,kalCool1,monteOff11,monteOff21,monteOff31,newInterp]
    return rr
rr  = buildModel(gkalHeat,gkalCool,gOff1,gOff2,gOff3)
# print(buildModel(.9,gkalCool,gOff1,gOff2,gOff3))
numCoeffs = 5
increasing = 0

r2Current = list(rr.keys())[0]
print(r2Current)

end = timer()

print(end-start)
plt.plot(fullTime,fullSamp,label='sample')
plt.plot(fullTime,rr[max(rr.keys())][-1],label='new model')
plt.plot(fullThermTime,fullTherm,label='thermistor')
plt.plot(fullThermTime1,fullMod,label='old model')
plt.legend()
plt.grid()
# plt.show()
plt.savefig('test.png')

# heatLambda()

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

file = 'revertModel4.txt'
fullData = modelTune(file)
therm = [np.array(fullData[i][1][0]) for i in range(len(fullData))]
samp = [np.array(fullData[i][0][0]) for i in range(len(fullData))]
mod = [np.array(fullData[i][1][1]) for i in range(len(fullData))]
sampTime = [np.array(fullData[i][0][1]) for i in range(len(fullData))]
time = [np.array(fullData[i][1][2]) for i in range(len(fullData))]
# print(sampTime[4])
T0 = samp[0][0]
mod.append([T0])



popSize = 1000         #DONT GO UP TO 100000!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
lamHeatL = 0
lamHeatH = .1
lamCoolL = 0
lamCoolH = .05
off1L = -1
off1H = 1
off2L = -100
off2H = 100
kalHeatL = -1
kalHeatH = 1
kalCoolL = -1
kalCoolH = 1
lamHeatEx = []
lamCoolEx = []
kalHeatEx = []
kalCoolEx = []
off1Ex = []
off2Ex = []
monteHeat = listToListList(np.random.uniform(lamHeatL,lamHeatH,popSize))
monteCool = listToListList(np.random.uniform(lamCoolL,lamCoolH,popSize))
monteOff1 = listToListList(np.random.uniform(off1L,off1H,popSize))
monteOff2 = listToListList(np.random.uniform(off2L,off2H,popSize))
# monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
kalHeat = listToListList(np.random.uniform(kalHeatL,kalHeatH,popSize))
kalCool = listToListList(np.random.uniform(kalCoolL,kalCoolH,popSize))

rrrr = 0
emptyOnes = np.ones(popSize)
guessLamHeat = listToListList(emptyOnes*0.1)
guessLamCool = listToListList(emptyOnes*0.02)
guessKalHeat = listToListList(emptyOnes*-0.1)
guessKalCool = listToListList(emptyOnes*0.3)
guessOff1 = listToListList(emptyOnes*1)
guessOff2 = listToListList(emptyOnes*-78)

numCoeffs = 6


# print(type(monteHeat))
section = [0,1,2,3,4,5]

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


def buildModel(monteHeat,monteCool,kalHeat,kalCool,monteOff1,monteOff2):
    rr = {}
    totInterp = []
    for sec in section:
        if sec == 0:
            test = calculation(mod[sec-1][-1],off(therm[sec],monteOff1,monteOff2),therm[sec],monteHeat,time[sec]-time[sec][0]-5)
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
            test = calculation(T0New,off(therm[sec],monteOff1,monteOff2),therm[sec],monteHeat,time[sec]-time[sec][0]-5)
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
            test = calculation(T0New,off(therm[sec],monteOff1,monteOff2),therm[sec],monteCool,time[sec]-time[sec][0]-5)
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
    
    return rr

rrReal = 0
while rrReal < 0.9:
    for i in range(numCoeffs):
        if i == 0:
            lamHeat = buildModel(monteHeat,guessLamCool,guessKalHeat,guessKalCool,guessOff1,guessOff2)
            
            guessLamHeat = listToListList(emptyOnes*(lamHeat[max(lamHeat.keys())][i]))
            
        elif i == 1:
            lamCool = buildModel(guessLamHeat,monteCool,guessKalHeat,guessKalCool,guessOff1,guessOff2)
            guessLamCool = listToListList(emptyOnes*(lamCool[max(lamCool.keys())][i]))
            
        elif i == 2:
            akalHeat = buildModel(guessLamHeat,guessLamCool,kalHeat,guessKalCool,guessOff1,guessOff2)
            guessKalHeat = listToListList(emptyOnes*(akalHeat[max(akalHeat.keys())][i]))
        elif i == 3:
            akalCool = buildModel(guessLamHeat,guessLamCool,guessKalHeat,kalCool,guessOff1,guessOff2)
            guessKalCool = listToListList(emptyOnes*(akalCool[max(akalCool.keys())][i]))
        elif i == 4:
            aoff1 = buildModel(guessLamHeat,guessLamCool,guessKalHeat,guessKalCool,monteOff1,guessOff2)
            guessOff1 = listToListList(emptyOnes*(aoff1[max(aoff1.keys())][i]))
        elif i == 5:
            aoff2 = buildModel(guessLamHeat,guessLamCool,guessKalHeat,guessKalCool,guessOff1,monteOff2)
            guessOff2 = listToListList(emptyOnes*(aoff2[max(aoff2.keys())][i]))
    rrReal = max(buildModel(guessLamHeat,guessLamCool,guessKalHeat,guessKalCool,guessOff1,guessOff2).keys())
    print(rrReal)




rr = buildModel(guessLamHeat,guessLamCool,guessKalHeat,guessKalCool,guessOff1,guessOff2)

rrrr = max(rr.keys())
print(rrrr)
x = list(rr.keys())
x.sort()

# test = []
# rstuff = []
# for i in range(1,popSize):
#     test.append(list(chain.from_iterable(rr[x[-i]][:-1])))
#     rstuff.append(x[-i])
# test = np.array(test).T
print(rrrr)
# print(rstuff)
print(rr[rrrr][:-1])

plt.plot(fullTime,fullSamp,label='sample')
plt.plot(fullTime,rr[max(rr.keys())][-1],label='new model')
plt.plot(fullThermTime,fullTherm,label='thermistor')
plt.plot(fullThermTime,fullMod,label='old model')
plt.legend()
plt.grid()
plt.show()

# left = []
# right = []
# for i in rr.keys():
#     x = list(chain.from_iterable(rr[i][:-1]))
#     best = list(chain.from_iterable(rr[i][:-1]))
#     if x[0] < best[0] and x[1] < best[1] and x[2] < best[2] and x[3] < best[3] and x[4] < best[4] and x[5] < best[5]:
#         left.append(i)
#     elif x[0] > best[0] and x[1] > best[1] and x[2] > best[2] and x[3] > best[3] and x[4] > best[4] and x[5] > best[5]:
#         right.append(i)

# print(left,right)





# for i in range(1,7):
#     plt.subplot(2,3,i)
#     plt.plot(test[i-1],rstuff,'o')
#     plt.ylim(.6,1)
# plt.show()



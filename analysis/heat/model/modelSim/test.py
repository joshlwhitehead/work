import matplotlib.pyplot as plt
import numpy as np
from parseTxt import modelTune
from scipy.interpolate import interp1d
from timeit import default_timer as timer
T0 = 24
start = timer()
def listToListList(li):
    return np.array(list(map(lambda item:[item],li)))
def calculation(T0,offset,someTemp,lam,time):                               #someTemp is either thermistor temp or set temp

    return (-someTemp+offset+T0)*np.exp(-lam*(time))+someTemp-offset

def off(someTemp,a,b):
    return a*someTemp+b
a = -0.0013693467336683212
b = 0.2659547738693443
c = -3.881909547738627
def kalman(someTemp,old,kal,a,b):
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

file = 'revertModel1.txt'
fullData = modelTune(file)
therm = [np.array(fullData[i][1][0]) for i in range(len(fullData))]
samp = [np.array(fullData[i][0][0]) for i in range(len(fullData))]
mod = [np.array(fullData[i][1][1]) for i in range(len(fullData))]
sampTime = [np.array(fullData[i][0][1]) for i in range(len(fullData))]
time = [np.array(fullData[i][1][2]) for i in range(len(fullData))]

mod.append([T0])
section = 0
test = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],0.0259,time[section]-time[section][0]-5)
testInterp = interp1d(time[section],test)(sampTime[section])






# plt.plot(time[section],test)
# plt.plot(sampTime[section],samp[section])
# plt.plot(time[section],mod[section])
# plt.plot(time[section],therm[section])
# plt.show()


# print(testInterp(sampTime[section]))
# testInterp = testInterp(sampTime[section])


monteCarlo = np.random.uniform(0,1,10000)
# print(r2(samp[section],testInterp))
rr = {}
for i in monteCarlo:
    test3 = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],i,time[section]-time[section][0]-5)
    testInterp = interp1d(time[section],test3)(sampTime[section])
    rr[r2(samp[section],testInterp)] = i

test2 = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],rr[max(rr.keys())],time[section]-time[section][0]-5)
# print(max(rr.keys()))
# print(rr[max(rr.keys())])



# # plt.plot(time[section],therm[section])
# # plt.plot(time[section],mod[section])
# plt.plot(sampTime[section],samp[section])
# plt.plot(time[section],test)
# plt.plot(time[section],test2)
# # plt.plot(sampTime[section],testInterp(sampTime[section]))
# plt.show()


def heatLambda():
    section = 0
    fullHeat = [i for i in samp[section]]
    fullTest1 = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],0.0259,time[section]-time[section][0]-5)
    fullTestInterp1 = interp1d(time[section],fullTest1)(sampTime[section])
    fullTestInterp = [i for i in fullTestInterp1]
    section = 2
    for i in samp[section]:
        fullHeat.append(i)
    fullTest2 = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],0.0259,time[section]-time[section][0]-5)
    fullTestInterp2 = interp1d(time[section],fullTest2)(sampTime[section])
    for i in fullTestInterp2:
        fullTestInterp.append(i)
    fullHeat = np.array(fullHeat)
    fullTestInterp = np.array(fullTestInterp)

    print(r2(fullHeat,fullTestInterp))


    rr = {}
    for i in monteCarlo:
        section = 0
        test3 = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],i,time[section]-time[section][0]-5)
        testInterp3 = interp1d(time[section],test3)(sampTime[section])
        section = 2
        test4 = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],i,time[section]-time[section][0]-5)
        testInterp4 = interp1d(time[section],test4)(sampTime[section])

        fullTest = [u for u in testInterp3]
        for u in testInterp4:
            fullTest.append(u)
        fullTest = np.array(fullTest)
        rr[r2(fullHeat,fullTest)] = i
    print(max(rr.keys()))
    section = 0
    a = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],rr[max(rr.keys())],time[section]-time[section][0]-5)
    aInterp = interp1d(time[section],a)(sampTime[section])
    section = 2
    b = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],rr[max(rr.keys())],time[section]-time[section][0]-5)
    bInterp = interp1d(time[section],b)(sampTime[section])

    oldInterp = [i for i in aInterp]
    for i in bInterp:
        oldInterp.append(i)

    plt.plot(fullHeat)
    plt.plot(fullTestInterp)
    plt.plot(oldInterp)


    plt.show()





popSize = 50000         #DONT GO UP TO 100000!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
monteHeat = listToListList(np.random.uniform(0,.1,popSize))
monteCool = listToListList(np.random.uniform(0,.1,popSize))
monteOff1 = listToListList(np.random.uniform(-1,1,popSize))
monteOff2 = listToListList(np.random.uniform(-1,1,popSize))
# monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
kalHeat = listToListList(np.random.uniform(.9,1,popSize))
kalCool = listToListList(np.random.uniform(.9,1,popSize))

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
    if sec == 0 or sec == 2:
        test = calculation(mod[sec-1][-1],off(therm[sec],monteOff1,monteOff2),therm[sec],monteHeat,time[sec]-time[sec][0]-5)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp)
    elif sec == 1:
        test = kalman(therm[sec],mod[sec-1][-1],kalHeat,monteOff1,monteOff2)
        # test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp) 
    elif sec == 3:
        test = kalman(therm[sec],mod[sec-1][-1],kalHeat,monteOff1,monteOff2)
        # test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp) 
    elif sec == 4:
        test = calculation(mod[sec-1][-1],off(therm[sec],monteOff1,monteOff2),therm[sec],monteCool,time[sec]-time[sec][0]-5)
        testInterp = interp1d(time[sec],test)(sampTime[sec])
        totInterp += list(testInterp)
    elif sec == 5:
        test = kalman(therm[sec],mod[sec-1][-1],kalCool,monteOff1,monteOff2)
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
    rr[r2(fullSamp,val)] = [monteHeat[indx],monteCool[indx],monteOff1[indx],monteOff2[indx],val]
    # totInterp = np.array(totInterp)
    # rr[r2(fullSamp,totInterp)] = [lamHeat,lamCool,a,b,c,totInterp]

# for (lamHeat,lamCool,off1,off2,off3) in zip(monteHeat,monteCool,monteOff1,monteOff2,monteOff3):
#     totInterp = []
# for lamHeat in monteHeat:
#     for lamCool in monteCool:
#         for a in monteOff1:
#             for b in monteOff2:
#                 for c in monteOff3:
#                     for kal in kalHeat:
#                         totInterp = []
#                         for sec in section:
#                             if sec == 0 or sec == 2:
#                                 test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
#                                 testInterp = interp1d(time[sec],test)(sampTime[sec])
#                                 totInterp += list(testInterp)
#                             elif sec == 1:
#                                 test = kalman(therm[sec],mod[sec-1][-1],kal,a,b,c)
#                                 # test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
#                                 testInterp = interp1d(time[sec],test)(sampTime[sec])
#                                 totInterp += list(testInterp)
#                             # elif sec == 3:
#                             #     test = calculation(mod[sec-1][-1],off2,therm[sec],lamHeat,time[sec]-time[sec][0]-5)
#                             #     testInterp = interp1d(time[sec],test)(sampTime[sec])
#                             #     totInterp += list(testInterp)
#                             elif sec == 4:
#                                 test = calculation(mod[sec-1][-1],off(therm[sec],a,b,c),therm[sec],lamCool,time[sec]-time[sec][0]-5)
#                                 testInterp = interp1d(time[sec],test)(sampTime[sec])
#                                 totInterp += list(testInterp)
#                             # else:
#                             #     test = calculation(mod[sec-1][-1],off3,therm[sec],lamCool,time[sec]-time[sec][0]-5)
#                             #     testInterp = interp1d(time[sec],test)(sampTime[sec])
#                             #     totInterp += list(testInterp)


    
print(max(rr.keys()))
print(rr[max(rr.keys())][:-1])
# print(rr[max(rr.keys())])
section = 4
testCool = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],0.00525,time[section]-time[section][0]-5)
testCoolInterp = interp1d(time[section],testCool)(sampTime[section])

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

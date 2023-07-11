import matplotlib.pyplot as plt
import numpy as np
from parseTxt import modelTune
from scipy.interpolate import interp1d
from timeit import default_timer as timer

start = timer()

def calculation(T0,offset,someTemp,lam,time):                               #someTemp is either thermistor temp or set temp

    return (-someTemp+offset+T0)*np.exp(-lam*(time))+someTemp-offset

def off(someTemp):
    
    a = -0.0013693467336683212
    b = 0.2659547738693443
    c = -3.881909547738627
    return a*someTemp**2+b*someTemp+c

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

mod.append([24])
section = 0
test = calculation(mod[section-1][-1],off(therm[section]),therm[section],0.0259,time[section]-time[section][0]-5)
testInterp = interp1d(time[section],test)(sampTime[section])



# print(testInterp(sampTime[section]))
# testInterp = testInterp(sampTime[section])


monteCarlo = np.random.uniform(0,1,10000)
# print(r2(samp[section],testInterp))
rr = {}
for i in monteCarlo:
    test3 = calculation(mod[section-1][-1],off(therm[section]),therm[section],i,time[section]-time[section][0]-5)
    testInterp = interp1d(time[section],test3)(sampTime[section])
    rr[r2(samp[section],testInterp)] = i

test2 = calculation(mod[section-1][-1],off(therm[section]),therm[section],rr[max(rr.keys())],time[section]-time[section][0]-5)
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
    fullTest1 = calculation(mod[section-1][-1],off(therm[section]),therm[section],0.0259,time[section]-time[section][0]-5)
    fullTestInterp1 = interp1d(time[section],fullTest1)(sampTime[section])
    fullTestInterp = [i for i in fullTestInterp1]
    section = 2
    for i in samp[section]:
        fullHeat.append(i)
    fullTest2 = calculation(mod[section-1][-1],off(therm[section]),therm[section],0.0259,time[section]-time[section][0]-5)
    fullTestInterp2 = interp1d(time[section],fullTest2)(sampTime[section])
    for i in fullTestInterp2:
        fullTestInterp.append(i)
    fullHeat = np.array(fullHeat)
    fullTestInterp = np.array(fullTestInterp)

    print(r2(fullHeat,fullTestInterp))


    rr = {}
    for i in monteCarlo:
        section = 0
        test3 = calculation(mod[section-1][-1],off(therm[section]),therm[section],i,time[section]-time[section][0]-5)
        testInterp3 = interp1d(time[section],test3)(sampTime[section])
        section = 2
        test4 = calculation(mod[section-1][-1],off(therm[section]),therm[section],i,time[section]-time[section][0]-5)
        testInterp4 = interp1d(time[section],test4)(sampTime[section])

        fullTest = [u for u in testInterp3]
        for u in testInterp4:
            fullTest.append(u)
        fullTest = np.array(fullTest)
        rr[r2(fullHeat,fullTest)] = i
    print(max(rr.keys()))
    section = 0
    a = calculation(mod[section-1][-1],off(therm[section]),therm[section],rr[max(rr.keys())],time[section]-time[section][0]-5)
    aInterp = interp1d(time[section],a)(sampTime[section])
    section = 2
    b = calculation(mod[section-1][-1],off(therm[section]),therm[section],rr[max(rr.keys())],time[section]-time[section][0]-5)
    bInterp = interp1d(time[section],b)(sampTime[section])

    oldInterp = [i for i in aInterp]
    for i in bInterp:
        oldInterp.append(i)

    plt.plot(fullHeat)
    plt.plot(fullTestInterp)
    plt.plot(oldInterp)


    plt.show()





popSize = 100
monteHeat = np.random.uniform(0,1,popSize)
monteCool = np.random.uniform(0.006,.007,popSize)
monteOff1 = np.random.uniform(0,10,popSize)
monteOff2 = np.random.uniform(0,10,popSize)
monteOff3 = np.random.uniform(0,10,popSize)


section = [0,1,2,4]
rr = {}
fullSamp = []
fullTime = []
for sec in section:
    fullSamp += list(samp[sec])
    fullTime += list(sampTime[sec])
fullSamp = np.array(fullSamp)
fullTime = np.array(fullTime)

# for (lamHeat,lamCool,off1,off2,off3) in zip(monteHeat,monteCool,monteOff1,monteOff2,monteOff3):
#     totInterp = []
for lamHeat in monteHeat:
    for lamCool in monteCool:
        totInterp = []
        for sec in section:
            if sec == 0 or sec == 2:
                test = calculation(mod[sec-1][-1],off(therm[sec]),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
                testInterp = interp1d(time[sec],test)(sampTime[sec])
                totInterp += list(testInterp)
            elif sec == 1:
                test = calculation(mod[sec-1][-1],off(therm[sec]),therm[sec],lamHeat,time[sec]-time[sec][0]-5)
                testInterp = interp1d(time[sec],test)(sampTime[sec])
                totInterp += list(testInterp)
            # elif sec == 3:
            #     test = calculation(mod[sec-1][-1],off2,therm[sec],lamHeat,time[sec]-time[sec][0]-5)
            #     testInterp = interp1d(time[sec],test)(sampTime[sec])
            #     totInterp += list(testInterp)
            elif sec == 4:
                test = calculation(mod[sec-1][-1],off(therm[sec]),therm[sec],lamCool,time[sec]-time[sec][0]-5)
                testInterp = interp1d(time[sec],test)(sampTime[sec])
                totInterp += list(testInterp)
            # else:
            #     test = calculation(mod[sec-1][-1],off3,therm[sec],lamCool,time[sec]-time[sec][0]-5)
            #     testInterp = interp1d(time[sec],test)(sampTime[sec])
            #     totInterp += list(testInterp)


    totInterp = np.array(totInterp)
    rr[r2(fullSamp,totInterp)] = [lamHeat,lamCool,totInterp]
print(max(rr.keys()))
print(rr[max(rr.keys())][:-1])
# print(rr[max(rr.keys())])
section = 4
testCool = calculation(mod[section-1][-1],off(therm[section]),therm[section],0.00525,time[section]-time[section][0]-5)
testCoolInterp = interp1d(time[section],testCool)(sampTime[section])

end= timer()

print(end-start)
plt.plot(fullSamp)
plt.plot(rr[max(rr.keys())][2])
plt.plot(np.arange(138,138+len(testCoolInterp)),testCoolInterp)
plt.grid()
plt.show()

# heatLambda()

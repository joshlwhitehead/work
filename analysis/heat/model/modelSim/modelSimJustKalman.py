import matplotlib.pyplot as plt
import numpy as np
from parseTxt import modelTune
from scipy.interpolate import interp1d
from timeit import default_timer as timer
import random
# from sklearn.metrics import r2_score



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
    fit = np.array(fit)
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

file = 'newCoeffs1.txt'
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

off1L = -1
off1H = 1
off2L = -5
off2H = 5
off3L = -20
off3H = 20
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
gOff2 = .4613
gOff3 = -12.603
gkalHeat = .9988
gkalCool = .9995


        

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

# print(buildModel(.9,gkalCool,gOff1,gOff2,gOff3))
numCoeffs = 5
increasing = 0

r2Current = 0#list(buildModel(gkalHeat,gkalCool,gOff1,gOff2,gOff3).keys())[0]
r2Orig = list(buildModel(gkalHeat,gkalCool,gOff1,gOff2,gOff3).keys())[0]
print(r2Orig)
print(r2Current)
while round(r2Current,2) < 0.99:
    for i in range(numCoeffs):
        if i == 0:
            r2New = .1
            r2Old = 0
            while r2New - r2Old > .000001:
                r2Old = r2New

                if gkalHeat > (kalHeatH+kalHeatL)*0.5:
                    rando = np.random.uniform(0,kalHeatH-gkalHeat)
                else:
                    rando = np.random.uniform(0,gkalHeat)

                gUp = gkalHeat + rando
                resUp = buildModel(gUp,gkalCool,gOff1,gOff2,gOff3)

                r2Up = list(resUp.keys())[0]  

                gDown = gkalHeat - rando
                resDown = buildModel(gDown,gkalCool,gOff1,gOff2,gOff3)
                r2Down = list(resDown.keys())[0]  
                
                if r2Up > r2Down:
                    gkalHeat = gUp
                    r2New = r2Up
                else:
                    gkalHeat = gDown
                    r2New = r2Down

                
        elif i == 1:
            r2New = .1
            r2Old = 0
            while r2New - r2Old > .000001:
                r2Old = r2New

                if gkalCool > (kalCoolH+kalCoolL)*0.5:
                    rando = np.random.uniform(0,kalCoolH-gkalCool)
                else:
                    rando = np.random.uniform(0,gkalCool)

                gUp = gkalCool + rando
                resUp = buildModel(gkalHeat,gUp,gOff1,gOff2,gOff3)

                r2Up = list(resUp.keys())[0]  

                gDown = gkalCool - rando
                resDown = buildModel(gkalHeat,gDown,gOff1,gOff2,gOff3)
                r2Down = list(resDown.keys())[0]  
                
                if r2Up > r2Down:
                    gkalCool = gUp
                    r2New = r2Up
                else:
                    gkalCool = gDown
                    r2New = r2Down
        elif i == 2:
            r2New = .1
            r2Old = 0
            while r2New - r2Old > .000001:
                r2Old = r2New

                if gOff1 > (off1H+off1L)*0.5:
                    rando = np.random.uniform(0,off1H-gOff1)
                else:
                    rando = np.random.uniform(0,gOff1)

                gUp = gOff1 + rando
                resUp = buildModel(gkalHeat,gkalCool,gUp,gOff2,gOff3)

                r2Up = list(resUp.keys())[0]  

                gDown = gOff1 - rando
                resDown = buildModel(gkalHeat,gkalCool,gDown,gOff2,gOff3)
                r2Down = list(resDown.keys())[0]  
                
                if r2Up > r2Down:
                    gOff1 = gUp
                    r2New = r2Up
                else:
                    gOff1 = gDown
                    r2New = r2Down
        elif i == 3:
            r2New = .1
            r2Old = 0
            while r2New - r2Old > .000001:
                r2Old = r2New

                if gOff2 > (off2H+off2L)*0.5:
                    rando = np.random.uniform(0,off2H-gOff2)
                else:
                    rando = np.random.uniform(0,gOff2)

                gUp = gOff2 + rando
                resUp = buildModel(gkalHeat,gkalCool,gOff1,gUp,gOff3)

                r2Up = list(resUp.keys())[0]  

                gDown = gOff2 - rando
                resDown = buildModel(gkalHeat,gkalCool,gOff1,gDown,gOff3)
                r2Down = list(resDown.keys())[0]  
                
                if r2Up > r2Down:
                    gOff2 = gUp
                    r2New = r2Up
                else:
                    gOff2 = gDown
                    r2New = r2Down
        elif i == 4:
            r2New = .1
            r2Old = 0
            while r2New - r2Old > .000001:
                r2Old = r2New

                if gOff3 > (off3H+off3L)*0.5:
                    rando = np.random.uniform(0,off3H-gOff3)
                else:
                    rando = np.random.uniform(0,gOff3)

                gUp = gOff3 + rando
                resUp = buildModel(gkalHeat,gkalCool,gOff1,gOff2,gUp)

                r2Up = list(resUp.keys())[0]  

                gDown = gOff3 - rando
                resDown = buildModel(gkalHeat,gkalCool,gOff1,gOff2,gDown)
                r2Down = list(resDown.keys())[0]  
                
                if r2Up > r2Down:
                    gOff3 = gUp
                    r2New = r2Up
                else:
                    gOff3 = gDown
                    r2New = r2Down
    r2Current = r2New        
    result = buildModel(gkalHeat,gkalCool,gOff1,gOff2,gOff3)
    rrrr = list(result.keys())[0]
    plt.clf()
    # plt.figure(1)
    plt.plot(fullTime,fullSamp,label='sample')
    plt.plot(fullThermTime,fullTherm,label='thermistor')
    plt.plot(fullThermTime1,fullMod,label='old model')
    plt.plot(fullTime,result[rrrr][-1],label='new model')
    plt.title(''.join([str(rrrr)]))
    plt.legend()
    plt.grid()
    plt.savefig('test.png')
    plt.pause(.000001)
    with open('possible3Results.txt','a') as file:
        if rrrr >= r2Orig:
            file.write(''.join([str(rrrr),' ',str(result[rrrr][:-1]),'\n']))
print(rrrr)
print(result[rrrr][:-1])
# print(monteOff1)





# kalHeatEx += list(kalHeat)
# kalCoolEx += list(kalCool)
# off1Ex += list(monteOff1)
# off2Ex += list(monteOff2)
# off3Ex += list(monteOff3)



# monteOff1 = randomGenExclude(off1Ex,off1L,off1H,popSize)
# # print('\n')
# # print(monteOff1)
# monteOff2 = randomGenExclude(off2Ex,off2L,off2H,popSize)
# monteOff3 = randomGenExclude(off3Ex,off3L,off3H,popSize)
# # monteOff3 = listToListList(np.random.uniform(-5,5,popSize))
# kalHeat = randomGenExclude(kalHeatEx,kalHeatL,kalHeatH,popSize)
# kalCool = randomGenExclude(kalCoolEx,kalCoolL,kalCoolH,popSize)

    
    



# print(list(chain.from_iterable(lamHeatEx)))
# print(max(rr.keys()))
# print(rr[max(rr.keys())][:-1])
# print(rr[max(rr.keys())])
# section = 4
# testCool = calculation(mod[section-1][-1],off(therm[section],a,b),therm[section],0.00525,time[section]-time[section][0]-5)
# testCoolInterp = interp1d(time[section],testCool)(sampTime[section])

end = timer()

print(end-start)
# plt.plot(fullTime,fullSamp,label='sample')
# plt.plot(fullTime,rr[max(rr.keys())][-1],label='new model')
# plt.plot(fullThermTime,fullTherm,label='thermistor')
# plt.plot(fullThermTime1,fullMod,label='old model')
# plt.legend()
# plt.grid()
# plt.show()
# plt.savefig('test.png')

# heatLambda()

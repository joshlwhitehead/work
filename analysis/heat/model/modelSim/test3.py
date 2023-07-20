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
    

def off(someTemp,a,b):
    a = -0.0027263
    b = .4653
    c = -10.603
    return a*someTemp**2+b*someTemp+c
# a = -0.0013693467336683212
# b = 0.2659547738693443
# c = -3.881909547738627


def kalman(someTemp,old,kal,a,b):
    # print(len(old),len(kal),len(off(someTemp,a,b)),len(someTemp))
    kalFull = []
    for i in someTemp:
        offset = off(i,a,b)
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

file = 'newCoeffsgoodish15.txt'
fullData = modelTune(file)
therm1 = [np.array(fullData[i][1][0]) for i in range(len(fullData))]
samp = [np.array(fullData[i][0][0]) for i in range(len(fullData))]
mod = [np.array(fullData[i][1][1]) for i in range(len(fullData))]
sampTime = [np.array(fullData[i][0][1]) for i in range(len(fullData))]
time1 = [np.array(fullData[i][1][2]) for i in range(len(fullData))]
# print(sampTime[4])


x1 = therm1[1][-1]
x2 = therm1[3][-1]
s1 = samp[1][-1]
s2 = samp[3][-1]
gOff1,gOff2 = np.polyfit([x1,x2],[x1-s1,x2-s2],1)


T0 = samp[0][0]
mod.append([T0])

therm = doubleData(therm1,time1)[0]
time = doubleData(therm1,time1)[1]
# print(len(therm1[0]))


popSize = 10         #DONT GO UP TO 100000!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

off1L = -5
off1H = 5
off2L = -20
off2H = 20

kalHeatL = 0
kalHeatH = 1
kalCoolL = 0
kalCoolH = 1

kalHeatEx = []
kalCoolEx = []
off1Ex = []
off2Ex = []
off3Ex = []



gkalHeat = 0.9
gkalCool = 0.9


        

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
    fullThermTime1 += list(time1[sec])
    fullMod += list(mod[sec])
fullSamp = np.array(fullSamp)
fullTime = np.array(fullTime)
fullTherm = np.array(fullTherm)
fullThermTime = np.array(fullThermTime)
fullThermTime1 = np.array(fullThermTime1)
fullMod = np.array(fullMod)

rrrr = 0
def buildModel(kalHeat1,kalCool1,monteOff11,monteOff21,whichOne):
    rr = {}
    
    # print(listToListList(monteHeat))
    newInterp = []
    for sec in section:
        if sec == 0:
            T0New = 24
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21).T
            
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
            
        elif sec == 1:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21).T
            
        
                
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))


        elif sec == 2:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21).T
            
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
        elif sec == 3:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalHeat1,monteOff11,monteOff21).T
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
        elif sec == 4:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalCool1,monteOff11,monteOff21).T
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))
        elif sec == 5:
            totInterpTranspose = test.T
            T0New = totInterpTranspose[-1]
            test = kalman(therm[sec],T0New,kalCool1,monteOff11,monteOff21).T
            
            newInterp += list(interp1d(time[sec],test)(sampTime[sec]))


    if whichOne == 2:
        rr[r2(fullSamp,newInterp)] = [kalHeat1,kalCool1,monteOff11,monteOff21,newInterp]
        
    elif whichOne == 0:
        print(len(newInterp),len(fullSamp))
        rr[r2(fullSamp[:-(len(samp[4])+len(samp[5]))],newInterp[:-(len(samp[4])+len(samp[5]))])] = [kalHeat1,kalCool1,monteOff11,monteOff21,newInterp]
        # plt.plot(rr[r2(fullSamp,newInterp)][-1])
        # plt.show()
    elif whichOne == 1:
        rr[r2(fullSamp[-(len(samp[4])+len(samp[5])):],newInterp[-(len(samp[4])+len(samp[5])):])] = [kalHeat1,kalCool1,monteOff11,monteOff21,newInterp]
    return rr


# print(buildModel(.9,gkalCool,gOff1,gOff2,gOff3))
numCoeffs = 2
increasing = 0

r2Current = 0
r2Orig = list(buildModel(gkalHeat,gkalCool,gOff1,gOff2,2).keys())[0]
print(r2Orig)
print(r2Current)
conditionToMove = .0000000001
# while round(r2Current,2) < 0.99:
for i in range(numCoeffs):
    if i == 0:
        r2New = .1
        r2Old = 0
        while round(r2New,2)< 0.99:
            r2Old = r2New

            if gkalHeat > (kalHeatH+kalHeatL)*0.5:
                rando = np.random.uniform(0,kalHeatH-gkalHeat)
            else:
                rando = np.random.uniform(0,gkalHeat)

            gUp = gkalHeat + rando
            resUp = buildModel(gUp,gkalCool,gOff1,gOff2,0)

            r2Up = list(resUp.keys())[0]  

            gDown = gkalHeat - rando
            resDown = buildModel(gDown,gkalCool,gOff1,gOff2,0)
            r2Down = list(resDown.keys())[0]  
            
            if r2Up > r2Down:
                gkalHeat = gUp
                r2New = r2Up
                plt.clf()
                plt.plot(fullTime,fullSamp,label='sample')
                plt.plot(fullThermTime,fullTherm,label='thermistor')
                plt.plot(fullThermTime1,fullMod,label='old model')
                plt.plot(fullTime,resUp[r2New][-1],label='new model')
                plt.title(''.join([str(r2New)]))
                plt.legend()
                plt.grid()
                plt.savefig('test.png')
                plt.pause(.000001)
                print(r2New)
            else:
                gkalHeat = gDown
                r2New = r2Down
                plt.clf()
                plt.plot(fullTime,fullSamp,label='sample')
                plt.plot(fullThermTime,fullTherm,label='thermistor')
                plt.plot(fullThermTime1,fullMod,label='old model')
                plt.plot(fullTime,resDown[r2New][-1],label='new model')
                plt.title(''.join([str(r2New)]))
                plt.legend()
                plt.grid()
                plt.savefig('test.png')
                plt.pause(.000001)
                print(r2New)
            # plt.clf()
            # # plt.figure(1)
            
            # plt.plot(fullTime,fullSamp,label='sample')
            # plt.plot(fullThermTime,fullTherm,label='thermistor')
            # plt.plot(fullThermTime1,fullMod,label='old model')
            # plt.plot(fullTime,result[rrrr][-1],label='new model')
            # plt.title(''.join([str(rrrr)]))
            # plt.legend()
            # plt.grid()
            # plt.savefig('test.png')
            # plt.pause(.000001)

            
    elif i == 1:
        r2New = .1
        r2Old = 0
        while round(r2New,2) < 0.99:
            r2Old = r2New

            if gkalCool > (kalCoolH+kalCoolL)*0.5:
                rando = np.random.uniform(0,kalCoolH-gkalCool)
            else:
                rando = np.random.uniform(0,gkalCool)

            gUp = gkalCool + rando
            resUp = buildModel(gkalHeat,gUp,gOff1,gOff2,1)

            r2Up = list(resUp.keys())[0]  

            gDown = gkalCool - rando
            resDown = buildModel(gkalHeat,gDown,gOff1,gOff2,1)
            r2Down = list(resDown.keys())[0]  
            
            if r2Up > r2Down:
                gkalCool = gUp
                r2New = r2Up
                plt.clf()
                plt.plot(fullTime,fullSamp,label='sample')
                plt.plot(fullThermTime,fullTherm,label='thermistor')
                plt.plot(fullThermTime1,fullMod,label='old model')
                plt.plot(fullTime,resUp[r2New][-1],label='new model')
                plt.title(''.join([str(r2New)]))
                plt.legend()
                plt.grid()
                plt.savefig('test.png')
                plt.pause(.000001)
            else:
                gkalCool = gDown
                r2New = r2Down
                plt.clf()
                plt.plot(fullTime,fullSamp,label='sample')
                plt.plot(fullThermTime,fullTherm,label='thermistor')
                plt.plot(fullThermTime1,fullMod,label='old model')
                plt.plot(fullTime,resDown[r2New][-1],label='new model')
                plt.title(''.join([str(r2New)]))
                plt.legend()
                plt.grid()
                plt.savefig('test.png')
                plt.pause(.000001)
                print(r2New)

       
    r2Current = r2New        
    result = buildModel(gkalHeat,gkalCool,gOff1,gOff2,2)
    rrrr = list(result.keys())[0]
    # plt.clf()
    # # plt.figure(1)

    # plt.plot(fullTime,fullSamp,label='sample')
    # plt.plot(fullThermTime,fullTherm,label='thermistor')
    # plt.plot(fullThermTime1,fullMod,label='old model')
    # plt.plot(fullTime,result[rrrr][-1],label='new model')
    # plt.title(''.join([str(rrrr)]))
    # plt.legend()
    # plt.grid()
    # plt.savefig('test.png')
    # plt.pause(.000001)
    with open('possibleModelCoeffs.txt','a') as file:
        if rrrr >= 0.97:
            file.write(''.join([str(rrrr),' ',str(result[rrrr][:-1]),'\n']))
print(rrrr)
print(result[rrrr][:-1])
# print(monteOff1)






end = timer()

print(round(end-start,2),'sec')

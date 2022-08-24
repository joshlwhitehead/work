import numpy as np
from scipy import interpolate as interp
import dataToVar as dat
import matplotlib.pyplot as plt


def interppp(dataInd,dataDep):
    dataInterpAll = []
    timeLen = []
    for i in range(len(dataInd)):
        timeLen.append(dataInd[i][:len(dataDep[i])][-1])
    x = min(timeLen)-1
        
    for i in range(len(dataInd)):
        
        dataInterp = interp.interp1d(dataInd[i][:len(dataDep[i])],dataDep[i])
        # print(dataInd[i])
        time = np.arange(0,x)
        # print(time[-1])
        # time = np.arange(0,400)
        # print(int(round(dataInd[i][-1],0)))
        dataInterpAll.append(dataInterp(time))
    # print(dataInterpAll)
    return dataInterpAll

def listAvg(dataInd,dataDep):                              #all data should be same size
    avgData = []
   
    for i in np.array(interppp(dataInd,dataDep)).transpose():
        avgData.append(np.average(i))
       
    return avgData



def listStd(dataInd,dataDep):                    
    stdev = []
    
    for i in np.array(interppp(dataInd,dataDep)).transpose():
        stdev.append(np.std(i))
    return stdev






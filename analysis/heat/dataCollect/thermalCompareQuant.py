import numpy as np
from scipy import interpolate as interp



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
       
    return np.array(avgData)



def listStd(dataInd,dataDep):                    
    stdev = []
    
    for i in np.array(interppp(dataInd,dataDep)).transpose():
        stdev.append(np.std(i))
    return np.array(stdev)

def listRms(dataInd,dataDep):
    interpData = np.array(interppp(dataInd,dataDep)).transpose()

    rmsData = np.sqrt(1/len(interpData)*sum(interpData**2))       
    # print(interpData)
    return rmsData

def listGrad(dataInd,dataDep1,dataDep2):
    interp1 = np.array(interppp(dataInd,dataDep1))
    interp2 = np.array(interppp(dataInd,dataDep2))
    final = []
    grad = interp1-interp2
    for i in range(len(grad)):
        
        mag = max(grad[i])-min(grad[i])
        magNorm = mag/np.average(grad[i])
        final.append(magNorm)
        # print((len(grad)))
    return final






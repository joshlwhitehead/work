import pandas as pd
import numpy as np
import scipy.interpolate as interp


def getData(filename,date):
    fullSheet = pd.read_csv(''.join(['data/',date,'/',filename]))

    time = np.array(fullSheet['timeSinceBoot']) - fullSheet['timeSinceBoot'][0]
    thermRaw = fullSheet['Stage1 TempC'].tolist()
    if 'Stage1 Thermocouple TempC' in fullSheet:
        sampRaw = fullSheet['Stage1 Thermocouple TempC'].tolist()
    elif 'dataQLiquidStg1' in fullSheet:
        sampRaw = fullSheet['dataQLiquidStg1'].tolist()
    modelRaw = fullSheet['Stage1 Modeled TempC'].tolist()
    wav3 = []
    wavTime = []
    if '515nm' in fullSheet.columns:
        nm515 = fullSheet['515nm'].tolist()
        
        for i in range(len(nm515)):
            if str(nm515[i]) !='nan':
                wav3.append(nm515[i])
                wavTime.append(time[i])
    if 'Stage1 Thermocouple TempC 2' in fullSheet.columns:
        samp2Raw = fullSheet['Stage1 Thermocouple TempC 2'].tolist()
    elif 'liquid2' in fullSheet.columns:
        samp2Raw = fullSheet['liquid2']
    elif 'Stage1 Alternate1 Thermocouple TempC' in fullSheet.columns:
        samp2Raw = fullSheet['Stage1 Alternate1 Thermocouple TempC']
    else:
        samp2Raw = np.ones(len(sampRaw))
    
    if 'liquid3' in fullSheet.columns:
        samp3Raw = fullSheet['liquid3']
    else:
        samp3Raw = np.ones(len(sampRaw))

 

   
    # setRaw = fullSheet['stage1SetTempC'].tolist()
   
    thermMod = []
    for i in range(len(time)):
        if i == 0:
            if str(thermRaw[i]) == 'nan':
                thermMod.append(thermRaw[i+1])
            else:
                thermMod.append(thermRaw[i])

        else:
            if str(thermRaw[i]) == 'nan':
                thermMod.append(thermRaw[i-1])
            else:
                thermMod.append(thermRaw[i])

    

    sampMod = []
    timeMod = []
    samp2Mod = []
    samp3Mod = []
    modelMod = []
    
    for i in range(len(sampRaw)):
        if str(sampRaw[i]) != 'nan':
            sampMod.append(sampRaw[i])
            timeMod.append(time[i])
            samp2Mod.append(samp2Raw[i])
            samp3Mod.append(samp3Raw[i])
            modelMod.append(modelRaw[i])
    # print(sampMod[:5])
    if len(sampMod) != 0:
        sampInterp = interp.interp1d(timeMod,sampMod)
        sampMod = sampInterp(time[:-4])
        samp2Interp = interp.interp1d(timeMod,samp2Mod)
        samp3Interp = interp.interp1d(timeMod,samp3Mod)
        samp2Mod = samp2Interp(time[:-4])
        samp3Mod = samp3Interp(time[:-4])
    
    return time,thermMod,sampMod,samp2Mod,modelRaw,samp3Mod,wav3,wavTime


def getPcrData(filename,date):
    fullSheet = pd.read_csv(''.join(['../data/',date,'/',filename]))
    modelRaw = fullSheet['PCR Modeled TempC'].tolist()
    time = np.array(fullSheet['timeSinceBoot']) - fullSheet['timeSinceBoot'][0]
    if 'PCR Thermocouple TempC' in fullSheet:
        sampRaw = fullSheet['PCR Thermocouple TempC'].tolist()

    sampMod = []
    modelMod = []
    timeMod = []

    for i in range(len(sampRaw)):
        if str(sampRaw[i]) != 'nan':
            sampMod.append(sampRaw[i])
            modelMod.append(modelRaw[i])
            timeMod.append(time[i])
    
    if len(sampMod) != 0:
        sampInterp = interp.interp1d(timeMod,sampMod)
        sampMod = sampInterp(time)
    return time,1,sampMod,3,modelRaw

def test(filename,date):
    fullSheet = pd.read_csv(''.join(['../data/',date,'/',filename]))
    timeRaw = np.array(fullSheet['timeSinceBoot'])
    if 'PCR Temp' in fullSheet:
        thermRaw = fullSheet['PCR Temp'].tolist()
    if 'PCR Thermocouple TempC' in fullSheet:
        sampRaw = fullSheet['PCR Thermocouple TempC'].tolist()
        samp = []
        time = []
        for i in sampRaw:
            if str(i) != 'nan' and i not in samp:
                samp.append(i)
                time.append(timeRaw[sampRaw.index(i)])
    return time,samp


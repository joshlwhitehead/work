import pandas as pd
import numpy as np
import scipy.interpolate as interp


def getData(filename,date):
    fullSheet = pd.read_csv(''.join(['../data/',date,'/',filename]))

    time = np.array(fullSheet['timeSinceBoot']) - fullSheet['timeSinceBoot'][0]
    thermRaw = fullSheet['Stage1 TempC'].tolist()
    if 'Stage1 Thermocouple TempC' in fullSheet:
        sampRaw = fullSheet['Stage1 Thermocouple TempC'].tolist()
    elif 'dataQLiquidStg1' in fullSheet:
        sampRaw = fullSheet['dataQLiquidStg1'].tolist()
      
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
    else:
        samp2Raw = np.ones(len(sampRaw))

   
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
    for i in range(len(sampRaw)):
        if str(sampRaw[i]) != 'nan':
            sampMod.append(sampRaw[i])
            timeMod.append(time[i])
            samp2Mod.append(samp2Raw[i])
    # print(sampMod[:5])
    if len(sampMod) != 0:
        sampInterp = interp.interp1d(timeMod,sampMod)
        sampMod = sampInterp(time[:-4])
        samp2Interp = interp.interp1d(timeMod,samp2Mod)
        samp2Mod = samp2Interp(time[:-4])
    
    return time,thermMod,sampMod,samp2Mod,wav3,wavTime



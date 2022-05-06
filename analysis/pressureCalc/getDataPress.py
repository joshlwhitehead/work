import pandas as pd
import numpy as np
import scipy.interpolate as interp


def getData(filename):
    fullSheet = pd.read_csv(''.join([filename]))

    time = np.array(fullSheet['timeSinceBootSeconds']) - fullSheet['timeSinceBootSeconds'][0]
    thermRaw = fullSheet['stage1TempC'].tolist()
    sampRaw = fullSheet['dataQLiquidStg1'].tolist()
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
    for i in range(len(sampRaw)):
        if str(sampRaw[i]) != 'nan':
            sampMod.append(sampRaw[i])
            timeMod.append(time[i])
    # print(sampMod[:5])

    sampInterp = interp.interp1d(timeMod,sampMod)
    sampMod = sampInterp(time[:-4])
    return time,thermMod,sampMod
   




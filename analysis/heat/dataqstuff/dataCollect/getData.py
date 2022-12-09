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
    if 'Stage1 Expected TempC' in fullSheet:
        expectRaw = fullSheet['Stage1 Expected TempC'].tolist()
    else:
        expectRaw = np.ones(len(sampRaw))
    if 'Stage1 Target TempC' in fullSheet:
        targetRaw = fullSheet['Stage1 Target TempC'].tolist()
    else:
        targetRaw = np.ones(len(sampRaw))

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

    thermMod = []
    modelMod = []
    targetMod = []
    expectMod = []
    for i in range(len(thermRaw)):
        if str(thermRaw[i]) == 'nan' and i == 0:
            thermMod.append(thermMod[i+1])
            modelMod.append(modelMod[i+1])
            targetMod.append(targetMod[i+1])
            expectMod.append(expectMod[i+1])
        elif str(thermRaw[i]) == 'nan' and i != 0:
            thermMod.append(thermMod[i-1])
            modelMod.append(modelMod[i-1])
            targetMod.append(targetMod[i-1])
            expectMod.append(expectMod[i-1])
        else:
            thermMod.append(thermRaw[i])
            modelMod.append(modelRaw[i])
            targetMod.append(targetRaw[i])
            expectMod.append(expectRaw[i])

    sampMod = []
    samp2Mod = []
    thermModTrue = []
    timeTrue = []
    modelModTrue = []
    targetModTrue = []
    expectModTrue = []
    for i in range(len(sampRaw)):
        if str(sampRaw[i]) != 'nan' and thermMod[i] != thermMod[-1]:#and thermRaw[i:]*len(thermRaw[i:]) != thermRaw[i:] and str(thermRaw[i] != 'nan'):
                                                                                                                                                            # and thermRaw[i] != 'nan' and thermRaw[i+1] != 'nan' and thermRaw[i+2] != 'nan' and thermRaw[i+3] != 'nan' and thermRaw[i+4] != 'nan' and thermRaw[i+5] != 'nan' and thermRaw[i+6] != 'nan' and thermRaw[i+7] != 'nan' and thermRaw[i+8] != 'nan' and thermRaw[i+9] != 'nan' and thermRaw[i+10] != 'nan' and thermRaw[i+11] != 'nan' and thermRaw[i+12] != 'nan' and thermRaw[i+13] != 'nan' and thermRaw[i+14] != 'nan' and thermRaw[i+15] != 'nan' and thermRaw[i+16] != 'nan' and thermRaw[i+17] != 'nan' and thermRaw[i+18] != 'nan' and thermRaw[i+19] != 'nan':
            sampMod.append(sampRaw[i])
            thermModTrue.append(thermMod[i])
            timeTrue.append(time[i])
            modelModTrue.append(modelMod[i])
            targetModTrue.append(targetMod[i])
            expectModTrue.append(expectMod[i])


    


    return timeTrue,thermModTrue,sampMod,samp2Mod,modelModTrue,targetModTrue,expectModTrue#,samp3Mod,wav3,wavTime

def getDataPCR(filename,date):
    fullSheet = pd.read_csv(''.join(['data/',date,'/',filename]))

    time = np.array(fullSheet['timeSinceBoot']) - fullSheet['timeSinceBoot'][0]
    thermRaw = fullSheet['PCR Temp'].tolist()
    

    if 'PCR Thermocouple TempC' in fullSheet:
        sampRaw = fullSheet['PCR Thermocouple TempC'].tolist()

    modelRaw = fullSheet['PCR Modeled TempC'].tolist()
    if 'PCR Expected TempC' in fullSheet:
        expectRaw = fullSheet['PCR Expected TempC'].tolist()
    else:
        expectRaw = np.ones(len(sampRaw))
    if 'PCR Target TempC' in fullSheet:
        targetRaw = fullSheet['PCR Target TempC'].tolist()
    else:
        targetRaw = np.ones(len(sampRaw))

   
    thermMod = []
    modelMod = []
    targetMod = []
    expectMod = []
    for i in range(len(thermRaw)):
        if str(thermRaw[i]) == 'nan' and i == 0:
            thermMod.append(thermMod[i+1])
            modelMod.append(modelMod[i+1])
            targetMod.append(targetMod[i+1])
            expectMod.append(expectMod[i+1])
        elif str(thermRaw[i]) == 'nan' and i != 0:
            thermMod.append(thermMod[i-1])
            modelMod.append(modelMod[i-1])
            targetMod.append(targetMod[i-1])
            expectMod.append(expectMod[i-1])
        else:
            thermMod.append(thermRaw[i])
            modelMod.append(modelRaw[i])
            targetMod.append(targetRaw[i])
            expectMod.append(expectRaw[i])

    sampMod = []
    samp2Mod = []
    thermModTrue = []
    timeTrue = []
    modelModTrue = []
    targetModTrue = []
    expectModTrue = []
    for i in range(len(sampRaw)):
        if str(sampRaw[i]) != 'nan' and thermMod[i] != thermMod[-1]:#and thermRaw[i:]*len(thermRaw[i:]) != thermRaw[i:] and str(thermRaw[i] != 'nan'):
                                                                                                                                                            # and thermRaw[i] != 'nan' and thermRaw[i+1] != 'nan' and thermRaw[i+2] != 'nan' and thermRaw[i+3] != 'nan' and thermRaw[i+4] != 'nan' and thermRaw[i+5] != 'nan' and thermRaw[i+6] != 'nan' and thermRaw[i+7] != 'nan' and thermRaw[i+8] != 'nan' and thermRaw[i+9] != 'nan' and thermRaw[i+10] != 'nan' and thermRaw[i+11] != 'nan' and thermRaw[i+12] != 'nan' and thermRaw[i+13] != 'nan' and thermRaw[i+14] != 'nan' and thermRaw[i+15] != 'nan' and thermRaw[i+16] != 'nan' and thermRaw[i+17] != 'nan' and thermRaw[i+18] != 'nan' and thermRaw[i+19] != 'nan':
            sampMod.append(sampRaw[i])
            thermModTrue.append(thermMod[i])
            timeTrue.append(time[i])
            modelModTrue.append(modelMod[i])
            targetModTrue.append(targetMod[i])
            expectModTrue.append(expectMod[i])


    


    return timeTrue,thermModTrue,sampMod,samp2Mod,modelModTrue,targetModTrue,expectModTrue#,samp3Mod,wav3,wavTime


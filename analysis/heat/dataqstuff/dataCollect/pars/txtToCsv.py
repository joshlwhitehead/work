import pandas as pd



# Stage1TempC = []
# Stage1ModeledTempC = []
# Stage1ExpectedTempC = []
# Stage1TargetTempC = []
# dataQStg1Heatsink = []



def mkCsv(txt,csv):
    full = []

    
    timeSinceBoot = []
    PCRTemp = []
    PCRModeledTempC = []
    PCRTargetTempC = []
    PCRThermocoupleTempC = []
    PCRHeatSinkTempC = []
    timeSinceBootThermocouple = []
    # try:
    f = open(''.join(['fileToUse/',txt]),'r')
    for i in f:
        if '(' in i or 'DATAQ:' in i or 'TC:' in i:
            full.append(i)
    f.close()

    count = 0

    for i in full:
        
        i = i.split()
        if 'TC:' in i:
            timeSinceBoot.append(float(i[0][1:-1])/1000)
            PCRTemp.append(float(i[4][:-1]))
            PCRModeledTempC.append(float(i[7][:-1]))
            PCRTargetTempC.append(float(i[10][:-1]))
            PCRHeatSinkTempC.append(float(i[13][:-1]))
        elif 'DATAQ:' in i and count >0:
            PCRThermocoupleTempC.append(float(i[4]))
            # if float(full[count-1].split()[0][1:-1]) == :
            try:
                if full[count-1].split()[0][1:-1] != 'ATAQ':
                    timeSinceBootThermocouple.append(float(full[count-1].split()[0][1:-1])/1000)
                else:
                    timeSinceBootThermocouple.append(float(full[count-2].split()[0][1:-1])/1000)
            except:
                if full[count+1].split()[0][1:-1] != 'ATAQ':
                    timeSinceBootThermocouple.append(float(full[count+1].split()[0][1:-1])/1000)
                else:
                    timeSinceBootThermocouple.append(float(full[count+2].split()[0][1:-1])/1000)
               
                
        
            
        count += 1
    count = 0
    for i in timeSinceBootThermocouple:
        if i not in timeSinceBoot:
            timeSinceBoot.insert(count,i)
            PCRTemp.insert(count,'nan')
            PCRModeledTempC.insert(count,'nan')
            PCRTargetTempC.insert(count,'nan')
            PCRHeatSinkTempC.insert(count,'nan')
        count +=1
    count = 0
    for i in timeSinceBoot:
        if i not in timeSinceBootThermocouple:
            PCRThermocoupleTempC.insert(count,'nan')
        count +=1
    
    print(len(timeSinceBoot),len(PCRThermocoupleTempC),len(PCRTemp))

    dF = pd.DataFrame({'timeSineBoot':timeSinceBoot,
        'PCR Temp':PCRTemp,
        'PCR Modeled TempC':PCRModeledTempC,
        'PCR Target TempC':PCRTargetTempC,
        'PCR Thermocouple TempC':PCRThermocoupleTempC,
        'PCR HeatSink TempC':PCRHeatSinkTempC})

    dF.to_csv(''.join(['fileMade/',str(csv),'.csv']))
    # except:
    #     print(txt)


import os

mkCsv('Adv01_DV03_220907_Run1.txt','d')
# for i in os.listdir('fileToUse'):
#     mkCsv(i,i[:-4])



import pandas as pd



# Stage1TempC = []
# Stage1ModeledTempC = []
# Stage1ExpectedTempC = []
# Stage1TargetTempC = []
# dataQStg1Heatsink = []



def mkCsv(txt,csv):
    full = []
    use = []

    
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
        full.append(i)
        if '(' in i or 'DATAQ:' in i:# or 'TC:' in i:
            use.append(i)
    f.close()
    basic = []
    count = 0

    for i in use:
        if i[0] == '(':
            basic.append(i)
        else:
            if count == 0:
                if i[0] == 'D' and use[count+1][0] != 'D':
                    basic.append(i)
            else:
                if i[0] == 'D' and use[count-1][0] != 'D':
                    basic.append(i)
        count +=1

    
        
        

    count = 0

    for i in basic:
        
        i = i.split()
        if 'TC:' in i:
            timeSinceBoot.append(float(i[0][1:-1])/1000)
            PCRTemp.append(float(i[4][:-1]))
            PCRModeledTempC.append(float(i[7][:-1]))
            PCRTargetTempC.append(float(i[10][:-1]))
            PCRHeatSinkTempC.append(float(i[13][:-1]))

        elif 'DATAQ:' in i:# and count > 0:
            PCRThermocoupleTempC.append(float(i[4]))

            if count == 0:
                timeSinceBootThermocouple.append(float(basic[count+1].split()[0][1:-1])/1000)
            else:
                timeSinceBootThermocouple.append(float(basic[count-1].split()[0][1:-1])/1000)

            
        count += 1



    count = 0
    for i in timeSinceBootThermocouple:
        if i not in timeSinceBoot:
            timeSinceBoot.insert(count,i)
            PCRTemp.insert(count,None)
            PCRModeledTempC.insert(count,None)
            PCRTargetTempC.insert(count,None)
            PCRHeatSinkTempC.insert(count,None)
        count +=1
    count = 0
    for i in timeSinceBoot:
        if i not in timeSinceBootThermocouple:
            PCRThermocoupleTempC.insert(count,None)
        count +=1
    

    # print(len(PCRThermocoupleTempC),len(timeSinceBoot))
    if len(PCRThermocoupleTempC) > len(timeSinceBoot):
        PCRThermocoupleTempC.pop(-1)
    dF = pd.DataFrame({'timeSinceBoot':timeSinceBoot,
        'PCR Temp':PCRTemp,
        'PCR Modeled TempC':PCRModeledTempC,
        'PCR Target TempC':PCRTargetTempC,
        'PCR Thermocouple TempC':PCRThermocoupleTempC,
        'PCR HeatSink TempC':PCRHeatSinkTempC})

    dF.to_csv(''.join(['fileMade/',str(csv),'.csv']))
    # except:
    #     print(txt)
    
    # import matplotlib.pyplot as plt
    # plt.plot(timeSinceBoot,PCRModeledTempC)
    # # plt.plot(timeSinceBoot,PCRThermocoupleTempC)
    # plt.show()

import os

# mkCsv('Adv13_DV05_221018_Run 2.txt','d')
for i in os.listdir('fileToUse'):
    mkCsv(i,i[:-4])



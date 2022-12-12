import pandas as pd
import os



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
   


    f = open(''.join(['fileToUse/',txt]),'r')
    for i in f:
        full.append(i)
        if '(' in i or 'DATAQ:' in i:
            use.append(i)
    f.close()


    tc = []
    useAdjust = []
    for i in use:
        if 'TC:' in i:
            tc.append(i)
    
    for i in use:
        if use.index(i) >= use.index(tc[0]) and use.index(i) <= use.index(tc[-1]):
            useAdjust.append(i)
    count = 0
    for i in useAdjust:
        i = i.split()
        
        if 'TC:' in i:
            timeSinceBoot.append(float(i[0][1:-1]))
            PCRTemp.append(float(i[4][:-1]))
            PCRModeledTempC.append(float(i[7][:-1]))
            PCRTargetTempC.append(float(i[10][:-1]))
            PCRHeatSinkTempC.append(float(i[13][:-1]))
            PCRThermocoupleTempC.append(None)
        elif 'DATAQ:' in i:

            if 'DATAQ' not in useAdjust[count-1]:
                x = useAdjust[count-1].split()
                timeSinceBoot.append(float(x[0][1:-1])/1000)
            else:
                timeSinceBoot.append(timeSinceBoot[-1])



            # if 'DATAQ:' not in useAdjust[count-1]:
            #     timeSinceBoot.append(float(useAdjust[count-1][1:7]))
            # elif 'DATAQ:' not in useAdjust[count-2]:
            #     timeSinceBoot.append(float(useAdjust[count-2][1:7]))
            # elif 'DATAQ:' not in useAdjust[count-3]:
            #     timeSinceBoot.append(float(useAdjust[count-3][1:7]))
            



            # try:
            #     x = useAdjust[count-1].split()
            #     timeSinceBoot.append(float(x[0][1:-1])/1000)
            # except:
            #     x = useAdjust[count+1].split()
            #     timeSinceBoot.append(float(x[0][1:-1])/1000)
            PCRTemp.append(None)
            PCRModeledTempC.append(None)
            PCRTargetTempC.append(None)
            PCRHeatSinkTempC.append(None)
            PCRThermocoupleTempC.append(float(i[4]))
            
        count += 1
    # print(len(timeSinceBoot))
    # print(len(PCRThermocoupleTempC))
    dF = pd.DataFrame({'timeSinceBoot':timeSinceBoot,
        'PCR Temp':PCRTemp,
        'PCR Modeled TempC':PCRModeledTempC,
        'PCR Target TempC':PCRTargetTempC,
        'PCR Thermocouple TempC':PCRThermocoupleTempC,
        'PCR HeatSink TempC':PCRHeatSinkTempC})
    
    dF.to_csv(''.join(['fileMade/',csv,'.csv']))
    

for i in os.listdir('fileToUse'):
    mkCsv(i,i[:-4])





# mkCsv('Adv01_DV03_220907_Run1.txt','d')





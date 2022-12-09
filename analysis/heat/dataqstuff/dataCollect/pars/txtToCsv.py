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
   


    f = open(''.join(['fileToUse/',txt]),'r')
    for i in f:
        full.append(i)
        if '(' in i or 'DATAQ:' in i:
            use.append(i)
    f.close()

    tc = []
    dataq = []
    for i in full:
        if 'TC:' in i:
            tc.append(i)
        # elif 'DATAQ:' in full:
        #     dataq.append(i)
    print(full[0])
    for i in full:
        if i != tc[0]:
            full.remove(i)
        else:
            break
    print(full[0])
    print(tc[0])





mkCsv('Adv13_DV05_221018_Run 2.txt','d')





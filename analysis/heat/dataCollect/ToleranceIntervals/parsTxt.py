"""This script reads a .txt file generated from the DAVE tool during thermal runs. The script then parses out the thermocouple data.
The first function returns lists of temps while heating and lists of temps while cooling during the PCR stage. The lists are embedded within
another list, clumped by cycle number (ie. each cycle has a seperate list of heating/cooling temps).
The second function returns a single list of heat kill temperatures and a single list of activation temperatures during the Treatment stage.
Both functions also return the set temps used."""

def parsPCRTxt(file):                                                                                                       #read PCR data

    with open(file,'r') as readFile:                                                                                        #convert lines in file to list
        file = readFile.readlines()


    heat = [[]]                      #temp (c) while PCR is heating
    timeH = [[]]                     #time (sec) while PCR is heating
    cool = [[]]                      #temp (c) while PCR is cooling
    timeC = [[]]                     #time (sec) while PCR is cooling
    totalTemp = []
    totalTime = []
    heatCollect = False                                                                                                 #key to start collecting temps while heating
    coolCollect = False                                                                                                 #key to start collecting temps while cooling
    start = False  
    stopTotal = False                                                                                                     #key to know when to start collecting temps
    countLines = 0
    countH = 0
    countC = 0
    heatTherm = [[]]
    timeHeatTherm = [[]]
    coolTherm = [[]]
    timeCoolTherm = [[]]
    countHTherm = 0
    countCTherm = 0
    heatSink = []
    timeHeatSink = []

    for u in file:
        # if 'FINISH -> IDLE' in u:
        #     break
        # if 'DATAQ:' in u:
        #     # if stopTotal == False:
        #     totalTemp.append(float(u.split()[4].strip(',')))
        #     try:
        #         totalTime.append(float(file[countLines-1].split()[0].strip('()'))/1000)
        #     except:
        #         # print(u)
        #         totalTime.append(float(file[countLines+1].split()[0].strip('()'))/1000)
        if 'Start PCR' in u:
            start = True                                                                                                #start looking for temps
        if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) > 85:                                         #only look for temps under these conditions for heating
            denatTemp = float(u.split()[-1])
            heatCollect = True
            coolCollect = False
            # heat.append([])
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 65 and float(u.split()[-1]) >= 40:        #look for temps under these conditions for cooling
            annealTemp = float(u.split()[-1])
            heatCollect = False
            coolCollect = True
        elif 'MELT' in u:                                                                                               #start looking for temps
            start = False

        if start and 'DATAQ:' in u or start and 'CHUBE:' in u:                                                                                     #only collect temps in these lines

            try:
                if heatCollect and len(heat[countH]) != 0 and heat[countH][-1]-float(u.split()[4].strip(',')) > 10:     #if criteria met make a new index in heating lists
                    heat.append([])
                    timeH.append([])
                    countH+=1
                elif coolCollect and len(cool[countC]) != 0 and float(u.split()[4].strip(','))-cool[countC][-1] > 10:   #if criteria met make a new index in cooling lists
                    cool.append([])
                    timeC.append([])
                    countC+=1
            except:
                pass
            
            
            if heatCollect:                                                                                             #start collecting heating temps
                heat[countH].append(float(u.split()[4].strip(',')))
                # print(heat)
                # totalTemp.append(float(u.split()[4].strip(',')))
                try:
                    timeH[countH].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    
                    if file[countLines+1].split()[0] != 'CHUBE:':
                        # print(countLines)
                        timeH[countH].append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    else:
                        try:
                            timeH[countH].append(float(file[countLines-2].split()[0].strip('()'))/1000)
                        except:
                            try:
                                timeH[countH].append(float(file[countLines+2].split()[0].strip('()'))/1000)
                            except:
                                try:
                                    timeH[countH].append(float(file[countLines-3].split()[0].strip('()'))/1000)
                                except:
                                    timeH[countH].append(timeH[countH][-1])
                    # totalTime.append(float(file[countLines+1].split()[0].strip('()'))/1000)

            elif coolCollect:                                                                                          #start collecting cooling temps
                cool[countC].append(float(u.split()[4].strip(',')))
                # totalTemp.append(float(u.split()[4].strip(',')))

                try:
                    timeC[countC].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    if file[countLines+1].split()[0] != 'CHUBE:':
                        # print(countLines)
                        timeC[countC].append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    else:
                        try:
                            timeC[countC].append(float(file[countLines-2].split()[0].strip('()'))/1000)
                        except:
                            try:
                                
                                timeC[countC].append(float(file[countLines+2].split()[0].strip('()'))/1000)
                            except:
                                try:
                                    timeC[countC].append(float(file[countLines-3].split()[0].strip('()'))/1000)
                                except:
                                    timeC[countC].append(timeC[countC][-1])
        
        if start:
            try:
                if 'goto' in u and float(u.split()[-1]) > 85 and len(heatTherm[countHTherm]) != 0:
                    heatTherm.append([])
                    timeHeatTherm.append([])
                    countHTherm += 1
                elif 'goto' in u and float(u.split()[-1]) < 65 and float(u.split()[-1]) >45 and len(coolTherm[countCTherm]) != 0:
                    coolTherm.append([])
                    timeCoolTherm.append([])
                    countCTherm += 1
            except:
                pass
            if 'modeled' in u:
                if heatCollect:
                    heatTherm[countHTherm].append(float(u.split()[4].strip(',')))
                    timeHeatTherm[countHTherm].append(float(u.split()[0].strip('()'))/1000)
                    heatSink.append(float(u.split()[13].strip(',')))
                    timeHeatSink.append(float(u.split()[0].strip('()'))/1000)
                elif coolCollect:
                    coolTherm[countCTherm].append(float(u.split()[4].strip(',')))
                    timeCoolTherm[countCTherm].append(float(u.split()[0].strip('()'))/1000)
                    heatSink.append(float(u.split()[13].strip(',')))
                    timeHeatSink.append(float(u.split()[0].strip('()'))/1000)

        countLines += 1
    # print(heat)
    
    heat2 = []
    timeH2 = []
    for j in range(len(heat)):
        if len(heat[j]) > 2:
            heat2.append(heat[j])
            timeH2.append(timeH[j])
         
    # for i in heat2:
    #     print(i)
    cool2 = []
    timeC2 = []
    for j in range(len(cool)):
        if len(cool[j]) > 2:
            cool2.append(cool[j])
            timeC2.append(timeC[j])
    heatTherm2 = []
    timeHeatTherm2 = []
    for j in range(len(heatTherm)):
        if len(heatTherm[j]) > 2:
            heatTherm2.append(heatTherm[j])
            timeHeatTherm2.append(timeHeatTherm[j])
    coolTherm2 = []
    timeCoolTherm2 = []
    for j in range(len(coolTherm)):
        if len(coolTherm[j]) > 2:
            coolTherm2.append(coolTherm[j])
            timeCoolTherm2.append(timeCoolTherm[j])
            
    
    
    return (heat2[1:-1],timeH2[1:-1]),(cool2[1:-1],timeC2[1:-1]),(denatTemp,annealTemp),(totalTemp,totalTime),(heatTherm2[:-1],timeHeatTherm2[:-1]),(heatSink,timeHeatSink)             #return heating temps and times, cooling temps and times, and the set temps for denature and anneal



x = parsPCRTxt('data/Beta05-DV91-20230615-Run1.txt')
# # x = parsPCRTxt('data/PThermo_AdvBuild13_w87_230301_run1.txt')[1]
# print(x)
# # print(x)
# import matplotlib.pyplot as plt
# for i in range(len(x[0])):
#     plt.plot(x[1][i],x[0][i])
#     print(max(x[0][i]))
# plt.grid()
# plt.show()


# y = parsPCRTxt('dataC/adv22_pcr_w71_230519_run06.txt')[0][0]
# x = parsPCRTxt('dataC/adv22_pcr_w71_230519_run06.txt')[0][1]
# # print(y)
# # print(y)
# z = []
# for i in y:
#     z.append(max(i))
# # print(z)
# # print(len(z))
# # for i in y:
# #     print(i)
# import matplotlib.pyplot as plt
# for i in range(len(x)):
#     plt.plot(x[i],y[i],'o')
# plt.grid()
# plt.show()



# yy = []
# for i in y:
#     yy.append(max(i))
# plt.plot(yy,'o')
# plt.grid()
# plt.show()


# print(parsPCRTxt('cupA\PThermo_AdvBuild07_w86_230301_run1.txt')[3][0])
# import matplotlib.pyplot as plt
# import numpy as np
# y1 = parsPCRTxt('0217-DV0004-20230227-Run01.txt')[3][0]
# x1 = np.array(parsPCRTxt('0217-DV0004-20230227-Run01.txt')[3][1])
# y2 = parsPCRTxt('0217-DV0004-20230301-run-04.txt')[3][0]
# x2 = np.array(parsPCRTxt('0217-DV0004-20230301-run-04.txt')[3][1])
# plt.plot(x1-x1[0],y1,label='run1')
# plt.plot(x2-x2[0],y2,label='run4')
# plt.grid()
# plt.legend()

# plt.show()






def parsTCTxt(file):                                                                    #function that reads treatment chamber data

    

    with open(file,'r') as readFile:                                                    #read file into a list
        file = readFile.readlines()


    kill = []                              #temp (c) during heat kill step
    timeK = []                              #time (sec) for heat kill step
    act = []                                #temp (c) for activation step
    timeA = []                              #time (sec) for activation step
    killCollect = False                                                                 #keys to determine when to start/stop looking for the desired data
    actCollect = False
    start = True
    start2 = False
    countLines = 0
    start3 = True




    goto = []
    for u in file:
        if 'SWITCH to STEADY' in u:                                                     #this criteria indicates start of data
            start2 = True
        if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) >= 85:             #this criteria indicates start of kill temp collection
            killTemp = float(u.split()[-1])
            goto.append(float(u.split()[-1]))
            killCollect = True
            actCollect = False
            start2 = False
            start3 = False
            # heat.append([])
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 75 and float(u.split()[-1]) >= 35 and start3:        #this criteria indicates start of activation temp collect
            goto.append(float(u.split()[-1]))
            actTemp = float(u.split()[-1])
            killCollect = False
            actCollect = True
            start2 = False
        # elif 'Using Cooling Equations' in u:
        #     start = False

        if start2 and 'DATAQ:' in u or start2 and 'CHUBE:' in u:                                                  #start collecting data

            
            if killCollect:
                kill.append(float(u.split()[4].strip(',')))                                         #collect kill data
                try:
                    timeK.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    try:
                        print(file[countLines+1].split())
                        timeK.append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    except:
                        timeK.append(timeK[-1])

            elif actCollect:# and start3:                                                                            #collect activation data
                act.append(float(u.split()[4].strip(',')))
                try:
                    timeA.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    try:
                        timeA.append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    except:
                        timeA.append(timeA[-1])
        
        
        countLines += 1
        
            
    return (kill,timeK),(act,timeA),(killTemp,actTemp)                          #return kill temps and times, activation temps and times, and set temps for heat kill and activation step

# print(parsTCTxt('dataC/adv22_tc_tp002_230519_run05.txt')[0][0])
# print(parsTCTxt('TCRando/Beta13-TC91-20230622-run1 (1).txt'))

def TCramp(file):
    with open(file,'r') as readFile:                                                    #read file into a list
        file = readFile.readlines()
    heatRR1 = []
    timeH1 = []
    heatRR2 = []
    timeH2 = []
    coolRR = []
    timeC = []

    masterStop = False
    startHeat1 = False
    startHeat2 = False
    startCool = False
    startCool2 = False
    countLines = 0

    for u in file:
        if 'goto' in u and float(u.split()[-1]) > 85:
            startHeat2 = True
        elif 'goto' in u and float(u.split()[-1]) < 75 and float(u.split()[-1]) >= 35:
            startHeat1 = True
        elif 'Using Cooling Equations' in u:#'goto' in u and float(u.split()[-1]) < 55:
            startHeat1 = False
            startCool = True
        if 'Set Temp Reached' in u:
            startCool = False
            startHeat1 = False
            startHeat2 = False
        if 'Start Heating PCR' in u:
            masterStop = True
        
        if 'DATAQ:' in u and not masterStop or 'CHUBE:' in u and not masterStop:
            if startHeat1:
                heatRR1.append(float(u.split()[4].strip(',')))
                try:
                    timeH1.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeH1.append(float(file[countLines+1].split()[0].strip('()'))/1000)
            elif startHeat2:
                heatRR2.append(float(u.split()[4].strip(',')))
                try:
                    timeH2.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeH2.append(float(file[countLines+1].split()[0].strip('()'))/1000)
            elif startCool:
                coolRR.append(float(u.split()[4].strip(',')))
                try:
                    timeC.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeC.append(float(file[countLines+1].split()[0].strip('()'))/1000)


        countLines += 1

    return (heatRR1,timeH1),(heatRR2,timeH2),(coolRR,timeC)


# print(TCramp('dataC/adv22_tc_tp002_230519_run05.txt')[2][0])







def meltRamp(file):
    with open(file,'r') as readFile:                                                                                        #convert lines in file to list
        file = readFile.readlines()


    melt = []                      #temp (c) while PCR is heating
    timeM = []                     #time (sec) while PCR is heating
    meltCollect = False                                                                                                 #key to start collecting temps while heating                                                                                                 #key to start collecting temps while cooling
    start = False                                                                                                       #key to know when to start collecting temps
    countLines = 0
    countM = 0

    model = []
    timeMod = []
    

    for u in file:
        if 'Start Melt Acquisition' in u:
            start = True                                                                                                #start looking for temps
            meltCollect = True
        elif 'MELT -> FINISH' in u:
            start = False
        # if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) > 85:                                         #only look for temps under these conditions for heating
        #     denatTemp = float(u.split()[-1])
        #     heatCollect = True
        #     coolCollect = False
        #     # heat.append([])
        # elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 65 and float(u.split()[-1]) >= 45:        #look for temps under these conditions for cooling
        #     annealTemp = float(u.split()[-1])
        #     heatCollect = False
        #     coolCollect = True
        # elif 'MELT' in u:                                                                                               #start looking for temps
        #     start = False

        if start and 'DATAQ:' in u or start and 'CHUBE:' in u:                                                                                     #only collect temps in these lines

            # try:
            #     if meltCollect and len(melt) != 0 and melt[-1]-float(u.split()[4].strip(',')) > 10:     #if criteria met make a new index in heating lists
            #         # melt.append([])
            #         # timeM.append([])
            #         countH+=1
            #     # elif coolCollect and len(cool[countC]) != 0 and float(u.split()[4].strip(','))-cool[countC][-1] > 10:   #if criteria met make a new index in cooling lists
            #     #     cool.append([])
            #     #     timeC.append([])
            #     #     countC+=1
            # except:
            #     pass
            
            
            if meltCollect:                                                                                             #start collecting heating temps
                melt.append(float(u.split()[4].strip(',')))
                try:
                    timeM.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    try:
                        timeM.append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    except:
                        try:
                            timeM.append(float(file[countLines+2].split()[0].strip('()'))/1000)
                        except:
                            timeM.append(timeM[-1])

            # elif coolCollect:                                                                                          #start collecting cooling temps
            #     cool[countC].append(float(u.split()[4].strip(',')))
            #     try:
            #         timeC[countC].append(float(file[countLines-1].split()[0].strip('()'))/1000)
            #     except:
            #         timeC[countC].append(float(file[countLines+1].split()[0].strip('()'))/1000)
        
        elif start and 'modeled' in u:
            if meltCollect:
                model.append(float(u.split()[7].strip(',')))
                timeMod.append(float(u.split()[0].strip('()'))/1000)
        countLines += 1


    # count = 0
    # for j in range(len(heat)):                                         #remove heating arrays with too few values
    #     if len(heat[count]) <= 2:
    #         heat.remove(heat[count])
    #         timeH.remove(timeH[count])
    #         count += 1
    # count = 0      
    # for j in range(len(cool)):                                          #remove cooling arrays with too few values
    #     if len(cool[count]) <= 2:
    #         cool.remove(cool[count])
    #         timeC.remove(timeC[count])
    #         count += 1

            
    return (melt,timeM), (model,timeMod)





# print(meltRamp('dataPCR/Adv13_w85_230223_Run1.txt')[0][1])

# print(parsPCRTxt('V3_no-recess_102_Run7.txt')[0][0])
import pandas as pd
def saveDataUsingPCR():
    file = 'accept200_/0202-DV0001-20230210-Run-01.txt'
   

    fullDenat = parsPCRTxt(file)[0][0]
    fullAnneal = parsPCRTxt(file)[1][0]
    fullMelt = meltRamp(file)[0][0]

    Denat = []
    anneal = []
    for i in fullDenat:
        Denat.append(max(i))

    for i in fullAnneal:
        anneal.append(min(i))

    while len(anneal) < len(fullMelt):
        anneal.append(None)
    while len(Denat) < len(fullMelt):
        Denat.append(None)

    dF = pd.DataFrame({'Denature':Denat,'Anneal':anneal,'Melt':fullMelt})

    dF.to_csv('crToVerify/0202-DV0001-20230210-Run-01.csv')



def saveDataUsingTC():
    file = 'TCRando/Adv10_p12_bae517_221010_Run2.txt'
    

    fullActive = parsTCTxt(file)[1][0]
    fullKill = parsTCTxt(file)[0][0]
    fullRamp = TCramp(file)[1][0]

    while len(fullActive) <len(fullKill):
        fullActive.append(None)
    while len(fullRamp) < len(fullKill):
        fullRamp.append(None)

    dF = pd.DataFrame({'Activation':fullActive,'Heat Kill':fullKill,'Ramp Rate':fullRamp})

    dF.to_csv('crToVerify/Adv10_p12_bae517_221010_Run2.csv')

# saveDataUsingTC()
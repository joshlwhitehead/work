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
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 65 and float(u.split()[-1]) >= 45:        #look for temps under these conditions for cooling
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
                # totalTemp.append(float(u.split()[4].strip(',')))
                try:
                    timeH[countH].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeH[countH].append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines+1].split()[0].strip('()'))/1000)

            elif coolCollect:                                                                                          #start collecting cooling temps
                cool[countC].append(float(u.split()[4].strip(',')))
                # totalTemp.append(float(u.split()[4].strip(',')))
                try:
                    timeC[countC].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeC[countC].append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines+1].split()[0].strip('()'))/1000)
        
        
        countLines += 1


    count = 0
    for j in range(len(heat)):                                         #remove heating arrays with too few values
        if len(heat[count]) <= 2:
            heat.remove(heat[count])
            timeH.remove(timeH[count])
            count += 1
    count = 0      
    for j in range(len(cool)):                                          #remove cooling arrays with too few values
        if len(cool[count]) <= 2:
            cool.remove(cool[count])
            timeC.remove(timeC[count])
            count += 1

            
    return (heat,timeH),(cool,timeC),(denatTemp,annealTemp),(totalTemp,totalTime)             #return heating temps and times, cooling temps and times, and the set temps for denature and anneal








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





    for u in file:
        if 'Switching to steady' in u:                                                     #this criteria indicates start of data
            start2 = True
        if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) > 85:             #this criteria indicates start of kill temp collection
            killTemp = float(u.split()[-1])
            killCollect = True
            actCollect = False
            start2 = False
            # heat.append([])
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 75 and float(u.split()[-1]) >= 55:        #this criteria indicates start of activation temp collect
            actTemp = float(u.split()[-1])
            killCollect = False
            actCollect = True
        elif 'Using Cooling Equations' in u:
            start = False

        if start and start2 and 'DATAQ:' in u or start and start2 and 'CHUBE:' in u:                                                  #start collecting data

            
            if killCollect:
                kill.append(float(u.split()[4].strip(',')))                                         #collect kill data
                try:
                    timeK.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    print(file[countLines+1].split())
                    timeK.append(float(file[countLines+1].split()[0].strip('()'))/1000)

            elif actCollect:                                                                            #collect activation data
                act.append(float(u.split()[4].strip(',')))
                try:
                    timeA.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeA.append(float(file[countLines+1].split()[0].strip('()'))/1000)
        
        
        countLines += 1
        
            
    return (kill,timeK),(act,timeA),(killTemp,actTemp)                          #return kill temps and times, activation temps and times, and set temps for heat kill and activation step

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
    countLines = 0

    for u in file:
        if 'goto' in u and float(u.split()[-1]) > 85:
            startHeat2 = True
        elif 'goto' in u and float(u.split()[-1]) < 75 and float(u.split()[-1]) > 55:
            startHeat1 = True
        elif 'goto' in u and float(u.split()[-1]) <55:
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
# print(TCramp('dataTC/Adv02_P11_221215_Run2.txt')[0][0])









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
                    timeM.append(float(file[countLines+1].split()[0].strip('()'))/1000)

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

# print(parsPCRTxt('justin/V3_no-recess_102_Run7.txt')[0][0])
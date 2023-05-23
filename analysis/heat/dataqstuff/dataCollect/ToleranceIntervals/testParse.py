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
    heatTherm = [[]]
    timeHeatTherm = [[]]
    cool = [[]]                      #temp (c) while PCR is cooling
    timeC = [[]]                     #time (sec) while PCR is cooling
    coolTherm = [[]]
    timeCoolTherm = [[]]
    totalTemp = []
    totalTime = []
    heatCollect = False                                                                                                 #key to start collecting temps while heating
    coolCollect = False                                                                                                 #key to start collecting temps while cooling
    start = False  
    stopTotal = False                                                                                                     #key to know when to start collecting temps
    countLines = 0
    countH = 0
    countC = 0
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
                    print(u,countLines)
                    timeC[countC].append(float(file[countLines+1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines+1].split()[0].strip('()'))/1000)
        
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

    # print(heatTherm)
    heat2 = []
    timeH2 = []
    for j in range(len(heat)):
        if len(heat[j]) > 2:
            heat2.append(heat[j])
            timeH2.append(timeH[j])
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
   

            
    return (heat2[1:-1],timeH2[1:-1]),(cool2[1:-1],timeC2[1:-1]),(denatTemp,annealTemp),(totalTemp,totalTime),(heatTherm2[1:-1],timeHeatTherm2[1:-1]),(coolTherm2[1:-1],timeCoolTherm2[1:-1]),(heatSink,timeHeatSink)             #return heating temps and times, cooling temps and times, and the set temps for denature and anneal




import numpy as np
y = np.array(parsPCRTxt('data/PThermo_AdvBuild13_w86_230306_run1.txt')[6])




import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = y[1]

def test(x,a,b,c):
    return a*np.log(x+b)+c

popt, pcov = curve_fit(test, x,y[0])

a,b,c,d,e,f = np.polyfit(y[1],y[0],5)
plt.plot(y[1],y[0],'o')
plt.plot(x,test(x,*popt))
plt.show()


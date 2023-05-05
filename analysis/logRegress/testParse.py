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
                elif coolCollect:
                    coolTherm[countCTherm].append(float(u.split()[4].strip(',')))
                    timeCoolTherm[countCTherm].append(float(u.split()[0].strip('()'))/1000)
            
        countLines += 1

    # print(heatTherm)
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
    count = 0      
    for j in range(len(heatTherm)):                                          #remove cooling arrays with too few values
        if len(heatTherm[count]) <= 20:
            heatTherm.remove(heatTherm[count])
            timeHeatTherm.remove(timeHeatTherm[count])
            count += 1
    count = 0      
    for j in range(len(coolTherm)):                                          #remove cooling arrays with too few values
        if len(coolTherm[count]) <= 20:
            coolTherm.remove(coolTherm[count])
            timeCoolTherm.remove(timeCoolTherm[count])
            count += 1

            
    return (heat[1:-1],timeH[1:-1]),(cool[1:-1],timeC[1:-1]),(denatTemp,annealTemp),(totalTemp,totalTime),(heatTherm[1:-1],timeHeatTherm[1:-1]),(coolTherm[1:-1],timeCoolTherm[1:-1])             #return heating temps and times, cooling temps and times, and the set temps for denature and anneal





# x = parsPCRTxt('PThermo_AdvBuild13_w86_230306_run1.txt')[5]
# y = parsPCRTxt('PThermo_AdvBuild13_w86_230306_run1.txt')[1]




# import matplotlib.pyplot as plt

# for i in range(len(x[1])):
#     plt.plot(x[1][i],x[0][i],'o')

# for i in range(len(y[0])):
#     plt.plot(y[1][i],y[0][i],'o')
# plt.show()


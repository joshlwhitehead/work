def parsPCRTxt(file):

    

    with open(file,'r') as readFile:
        file = readFile.readlines()


    heat = [[]]
    timeH = [[]]
    cool = [[]]
    timeC = [[]]
    heatCollect = False
    coolCollect = False
    start = False
    countLines = 0
    countH = 0
    countC = 0




    for u in file:
        if 'Start PCR' in u:
            start = True
        if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) > 85:
            denatTemp = float(u.split()[-1])
            heatCollect = True
            coolCollect = False
            # heat.append([])
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 65 and float(u.split()[-1]) >= 45:
            annealTemp = float(u.split()[-1])
            heatCollect = False
            coolCollect = True
        elif 'MELT' in u:
            start = False

        if start and 'DATAQ:' in u:

            try:
                if heatCollect and len(heat[countH]) != 0 and heat[countH][-1]-float(u.split()[4].strip(',')) > 10:
                    heat.append([])
                    timeH.append([])
                    countH+=1
                elif coolCollect and len(cool[countC]) != 0 and float(u.split()[4].strip(','))-cool[countC][-1] > 10:
                    cool.append([])
                    timeC.append([])
                    countC+=1
            except:
                pass
            
            
            if heatCollect:
                heat[countH].append(float(u.split()[4].strip(',')))
                try:
                    timeH[countH].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeH[countH].append(float(file[countLines+1].split()[0].strip('()'))/1000)

            elif coolCollect:
                cool[countC].append(float(u.split()[4].strip(',')))
                try:
                    timeC[countC].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeC[countC].append(float(file[countLines+1].split()[0].strip('()'))/1000)
        
        
        countLines += 1


    count = 0
    for j in range(len(heat)):
        if len(heat[count]) <= 2:
            heat.remove(heat[count])
            timeH.remove(timeH[count])
            count += 1
    count = 0      
    for j in range(len(cool)):
        if len(cool[count]) <= 2:
            cool.remove(cool[count])
            timeC.remove(timeC[count])
            count += 1

            
    return (heat,timeH),(cool,timeC),(denatTemp,annealTemp)



# x = parsPCRTxt('data/27Jan2023/proposedModel_Adv15_wxx_120123_Run1.txt')


# heat = x[0][0][1:]
# timeH = x[0][1][1:]
# cool = x[1][0]
# timeC = x[1][1]
# import matplotlib.pyplot as plt

# for i in range(len(heat)):
#     plt.plot(timeH[i],heat[i],color='b')
#     plt.plot(timeC[i],cool[i],color='r')
# plt.show()



def parsTCTxt(file):

    

    with open(file,'r') as readFile:
        file = readFile.readlines()


    kill = []
    timeK = []
    act = []
    timeA = []
    killCollect = False
    actCollect = False
    start = True
    start2 = False
    countLines = 0





    for u in file:
        if 'Switching to steady' in u:
            start2 = True
        if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) > 85:
            killTemp = float(u.split()[-1])
            killCollect = True
            actCollect = False
            start2 = False
            # heat.append([])
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 75 and float(u.split()[-1]) >= 55:
            actTemp = float(u.split()[-1])
            killCollect = False
            actCollect = True
        elif 'Using Cooling Equations' in u:
            start = False

        if start and start2 and 'DATAQ:' in u:
            # try:
            #     if killCollect and kill[-1]-float(u.split()[4].strip(',')) > 10:
            #         countH+=1
            #     elif actCollect and float(u.split()[4].strip(','))-act[countC][-1] > 10:
            #         timeA.append([])
            #         countC+=1
            # except:
            #     pass
            
            
            if killCollect:
                kill.append(float(u.split()[4].strip(',')))
                try:
                    timeK.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    print(file[countLines+1].split())
                    timeK.append(float(file[countLines+1].split()[0].strip('()'))/1000)

            elif actCollect:
                act.append(float(u.split()[4].strip(',')))
                try:
                    timeA.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeA.append(float(file[countLines+1].split()[0].strip('()'))/1000)
        
        
        countLines += 1
        
            
    return (kill,timeK),(act,timeA),(killTemp,actTemp)



# x = parsTCTxt('data/10Feb2023_f09TC/Adv02_P11_221215_Run2.txt')


# import matplotlib.pyplot as plt


# plt.plot(x[0][1],x[0][0])
# plt.show()

















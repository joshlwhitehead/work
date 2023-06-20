import pandas as pd
import numpy as np

def fit(filename,date):
    fullSheet = pd.read_csv(''.join(['data/',date,'/',filename]))
    bot = fullSheet['dataQStage1Heatsink'].tolist()
    top = fullSheet['dataQLiquidStg1'].tolist()
    therm = fullSheet['stage1TempC'].tolist()
    # print(bot[9])
    # print(therm[9])


    newBot = []
    newTop = []
    newTherm = []
    
    for temp in bot:
        y = str(temp)
        # d.append(bot.index(temp))
        if y !='nan':
            y=float(temp)
            newBot.append(temp)
            newTop.append(top[bot.index(temp)])
            
            x = str(therm[bot.index(temp)])
            if x != 'nan':

                newTherm.append(therm[bot.index(temp)])
            else:
                newTherm.append(therm[bot.index(temp)+1])
                
                
            
    
    newBot = np.array(newBot)
    newTop = np.array(newTop)
    newTherm = np.array(newTherm)
    newTemp = []
    # print(newTherm[:14])
    for i in range(len(newBot)):
        newTemp.append((newBot[i]+newTop[i])/2)
    # newTemp = np.array(newTemp)
    
    
    return newTemp,newTherm


def single(filename,date):
    fullSheet = pd.read_csv(''.join(['data/',date,'/',filename]))
    # bot = fullSheet['dataQStage1Heatsink'].tolist()
    top = fullSheet['dataQLiquidStg1'].tolist()
    # print(top[:5])
    therm = fullSheet['stage1TempC'].tolist()
    newNum = np.arange(.00000001,.004,.00000001)
    count = 0
    top2 = []
    for i in top:
        top2.append(i+newNum[count])
        count +=1

    newBot = []
    newTherm = []
    newTop = []
    indexa = []
    fullTemp = []
    
    for temp in range(len(top2)):
        y = str(top2[temp])
        

        if y !='nan':
            
            newTop.append(top2[temp])
            # newBot.append(bot[top2.index(temp)])
            

        
            indexa.append(top2.index(top2[temp]))
            fullTemp.append(top2[temp])
        else:
            fullTemp.append(fullTemp[temp-1])
           

    for i in indexa:
        if str(therm[i]) != 'nan':
            newTherm.append(therm[i])
        else:
            newTherm.append(therm[i+1])
    newBot = np.array(newBot)
    newTop = np.array(newTop)
    newTherm = np.array(newTherm)
    newTemp = []
    for i in range(len(newTop)):
        
        newTemp.append(newTop[i])
    # newTemp = np.array(newTemp)
    fullTherm = therm
    
    return newTemp, newTherm, fullTherm, fullTemp
    
# x=fit('30_90_bothInside_a.csv','04Jan2022')
# y=fit('30_90_bothInside_b.csv','04Jan2022')
# z=fit('30_90_bothInside_c.csv','04Jan2022')
# x=fit('30_70_bothInsideBot_a.csv','05Jan2022')
# y=fit('30_70_bothInsideBot_b.csv','05Jan2022')
# z=fit('30_70_bothInsideBot_c.csv','05Jan2022')



def avgTrial(trial1,trial2,trial3):
    if len(trial1) <= len(trial2) and len(trial1) <= len(trial3):
        trial2 = np.array(trial2[:len(trial1)])
        trial3 = np.array(trial3[:len(trial1)])
    elif len(trial2) <= len(trial1) and len(trial2) <= len(trial3):
        trial1 = np.array(trial1[:len(trial2)])
        trial3 = np.array(trial3[:len(trial2)])
    else: #len(trial3) <= len(trial2) and len(trial3) <= len(trial1):
        trial2 = np.array(trial2[:len(trial3)])
        trial1 = np.array(trial1[:len(trial3)])
    # if len(trial1) < len(trial2):
    #     while len(trial1) < len(trial2):
    #         trial1.append(trial1[-1])
    # if len(trial2) < len(trial1):
    #     while len(trial2) < len(trial1):
    #         trial2.append(trial2[-1])
    # if len(trial3) < len(trial1):
    #     while len(trial3) < len(trial1):
    #         trial3.append(trial3[-1])
    # if len(trial1) < len(trial3):
    #     while len(trial1) < len(trial3):
    #         trial1.append(trial1[-1])
    #         trial2.append(trial2[-1])
    # trial1 = np.array(trial1)
    # trial2 = np.array(trial2)
    # trial3 = np.array(trial3)
    # # print(len(trial1),trial1,'\n',len(trial2),'\n',len(trial3))
    avgAvg = (trial1+trial2+trial3)/3
    
    


    return avgAvg

# avgTrial(x,y,z,70)
# print(avgTrial(x,y,z,70))

    
# print(single('lid0Cons0_90.csv','24Mar2022')[2][:])




































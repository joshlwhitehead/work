"""This script analyzes PCR thermal data parsed using parsPCRTxt. The data is then analyzed to determine it's tolerance interval
and its tolerance interval of the mean"""
from parsTxt import parsPCRTxt
import numpy as np
import os
from confidenceFun import CI



folder = 'capstoneGenThermals/'
instListShort = []
for i in os.listdir(folder):
    instListShort.append(i[:-4])

# instListShort = np.arange(0,len(os.listdir(folder)))

replicate = 1                                                                                   #how many runs of each instrument



##############              PROBABLY DONT CHANGE            #####################
deviationCrit = 1.5                                                                             #acceptance crit
alpha = 0.1                                                                                    #1-confidence level
p = 0.9                                                                                         #reliability




def findAvgValMin(data):
    peakSamp = []
    for peak in data:
        peakSamp.append(min(peak))
    return peakSamp

########                DONT CHANGE             ##################



def cycleTimeFun(folder,instListShort):                                                                               #function to analyze anneal temps
    # instListShort = inputtxt.get("1.0","end-1c").split()                                    #which instruments is the data from
    # replicate = int(inputtxt2.get("1.0","end-1c"))                                          #how many runs from each instrument
    instList = instListShort*replicate                                                      #list that has each instrument repeated as many times
                                                                                            #as replicates
    
    instListVar = []
    instList = instListShort*replicate                                                              #list of total runs
    if replicate > 1:
        instList.sort()                                                                                 #sort instrument list to match with order in directory

    instListVar = instListShort
    # for inst in instListShort:                                                                         
    #     for rep in range(replicate):
    #         instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates
  


    temp = []    
    means = []
    stdevs = []
    cycleTime = []
    tis = []
    count = 0
    for file in os.listdir(folder):
        peakSampOption = parsPCRTxt(''.join([folder,file]))
        heat,timeHeat = peakSampOption[7]
        cool,timeCool = peakSampOption[8]
        times = []
        if np.mean(findAvgValMin(cool)) > np.mean(findAvgValMin(heat)):
            peakSamp = findAvgValMin(cool)
            for indx,val in enumerate(peakSamp):
                # print(cool[indx].index(val))
                times.append(timeCool[indx][cool[indx].index(val)])
        else:
            peakSamp = findAvgValMin(heat)                                    #collect maximum (denature) temps for each cycle
            for indx,val in enumerate(peakSamp):
                times.append(timeHeat[indx][heat[indx].index(val)])
        cycleTimes = []
        for indx,val in enumerate(times[:-1]):
            cycleTimes.append(times[indx+1]-val)
        # print(cycleTimes)
        meanCycleTime = round(np.mean(cycleTimes),2)
        stdev = round(np.std(cycleTimes),2)
        ci = CI(cycleTimes,0.05)
        # print(file)
        # print(''.join([str(meanCycleTime),' +/- ',str(round(ci[1]-meanCycleTime,2))]))
        means.append(meanCycleTime)
        stdevs.append(stdev)
        # print(ci)
    return means,stdevs
# print(cycleTimeFun(folder,instListShort))
# print(cycleTimeFun(folder,instListShort)[0])
print(CI(cycleTimeFun(folder,instListShort)[0],.05)[1]-np.mean(cycleTimeFun(folder,instListShort)[0]))

# 
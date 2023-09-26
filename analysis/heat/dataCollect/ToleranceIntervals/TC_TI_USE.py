"""This script analyzes TC thermal data parsed using parsTCTxt. The data is then analyzed to determine it's tolerance interval
and its tolerance interval of the mean"""
from parsTxt import parsTCTxt
import numpy as np
import matplotlib.pyplot as plt
import toleranceinterval as ti
import os
from scipy import stats


folder = 'syd5/'
#############               CHANGE THESE                    ######################
instListShort = []
for i in os.listdir(folder):
    instListShort.append(i[:-4])
replicate = 1


########                PROBABLY DONT CHANGE                ##################
alpha = 0.10
p = 0.90
deviationCrit = 2.5

       
###############                  DONT CHANGE                    ##############
instList = instListShort*replicate
instList.sort()

def kill(folder,instListShort):
    instListVar = instListShort
    # for inst in instListShort:
    #     for rep in range(replicate):
    #         instListVar.append(''.join([str(inst),'.',str(rep)]))
    

    temp = []
    means = []
    stdev = []
    meansTherm = []
    stdevsTherm = []
    count = 0
    for file in os.listdir(folder):
        print(file)
        killTemps = parsTCTxt(''.join([folder,file]))[0][0]
        temp.append(killTemps)
        mean = np.mean(killTemps)
        means.append(mean)
        stdev.append(np.std(killTemps))
        killTemp = parsTCTxt(''.join([folder,file]))[2][0]

        killTherm = parsTCTxt(''.join([folder,file]))[3][0]
        meanTherm = np.mean(killTherm)
        stdevTherm = np.std(killTherm)
        meansTherm.append(meanTherm)
        stdevsTherm.append(stdevTherm)


        bound = ti.twoside.normal(killTemps,p,1-alpha)                                               #tolerance interval for each run                                                                        #list of TIs

        # plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        
        # if bound[0][0] < killTemp-deviationCrit or bound[0][1] > killTemp+deviationCrit:          #pass if TI within acceptance criteria
        #     print(instListVar[count],'TI:',bound,'FAIL')
        # else:
        #     print(instListVar[count],'TI:',bound,'PASS')
        count += 1
    return means,stdev,meansTherm,stdevsTherm

def act(folder,instListShort):
    instListVar = instListShort
    # for inst in instListShort:
    #     for rep in range(replicate):
    #         instListVar.append(''.join([str(inst),'.',str(rep)]))
    

    temp = []
    means = []
    stdev = []
    meansTherm = []
    stdevsTherm = []
    count = 0
    for file in os.listdir(folder):
        actTemps = parsTCTxt(''.join([folder,file]))[1][0]
        temp.append(actTemps)
        mean = np.mean(actTemps)
        means.append(mean)
        actTemp = parsTCTxt(''.join([folder,file]))[2][1]
        stdev.append(np.std(actTemps))
        actTherm = parsTCTxt(''.join([folder,file]))[4][0]
        meanTherm = np.mean(actTherm)
        stdevTherm = np.std(actTherm)
        meansTherm.append(meanTherm)
        stdevsTherm.append(stdevTherm)
    return means,stdev,meansTherm,stdevsTherm


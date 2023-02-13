"""analyze """
from parsTxt import parsTCTxt
import numpy as np
import matplotlib.pyplot as plt
import toleranceinterval as ti
import os


folder = 'dataTC/'
#############               CHANGE THESE                    ######################
instListShort = [2,6,9,10,13,15,18,25,27]
replicate = 1


########                PROBABLY DONT CHANGE                ##################
alpha = 0.05
p = 0.9
deviationCrit = 2.5

       
###############                  DONT CHANGE                    ##############
instList = instListShort*replicate
instList.sort()

def kill():
    instListVar = []
    for inst in instListShort:
        for rep in range(replicate):
            instListVar.append(''.join([str(inst),'.',str(rep)]))
    

    temp = []
    means = []
    count = 0
    for file in os.listdir(folder):
        killTemps = parsTCTxt(''.join([folder,file]))[0][0]
        temp.append(killTemps)
        mean = np.mean(killTemps)
        means.append(mean)
        killTemp = parsTCTxt(''.join([folder,file]))[2][0]


        bound = ti.twoside.normal(killTemps,p,1-alpha)                                               #tolerance interval for each run                                                                        #list of TIs

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        
        if bound[0][0] < killTemp-deviationCrit or bound[0][1] > killTemp+deviationCrit:          #pass if TI within acceptance criteria
            print(instListVar[count],bound,'FAIL')
        else:
            print(instListVar[count],bound,'PASS')
        count += 1
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.vlines(killTemp+deviationCrit,0,count,'k',lw=5)
    plt.vlines(killTemp-deviationCrit,0,count,'k',lw=5)
    plt.title('95% Tolerance Intervals (p=0.90)')
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()



kill()



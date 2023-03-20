"""This script analyzes TC thermal data parsed using parsTCTxt. It captures the ramp rates for heating and cooling the TC chamber."""
import numpy as np
import os
from parsTxt import meltRamp
import matplotlib.pyplot as plt




instListShort = [1,2,3,4,5]                                                                         #list of instruments. must be in order that they appear in folder
replicate = 1                                                                                  #how many runs of each instrument
alpha = 0.05                                                                                    #significance level (1-confidence level)
p = 0.9                                                                                         #reliability
meltLimitHigh = 1
meltLimitLow = 0.1
instList = instListShort*replicate                                                              #list of total runs
instList.sort()                                                                                 #sort instrument list to match with order in directory

instListVar = []
for inst in instListShort:                                                                         
    for rep in range(replicate):
        instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates





folder = 'accept/'                                                                       #folder to draw data from
def rr(temps,times):                                                                    #calculates derivative of 1 degree polynomial
                                                                    
    
    a,b = np.polyfit(times,temps,1)
    
    # plt.plot(times,temps,'o')
    # plt.plot(times,a*np.array(times)+b)
    # plt.show()
  
    return a

def melting():                                                                          #funtion to analyze heating data
    derivTotM = []                                                                  #list ramp rate for all cycles 
    derivTotNameM = []                                                              #list name of file
                                                              #clump ramp rates by run
    for i in os.listdir(folder):
        melt = meltRamp(''.join([folder,i]))[0]
        timeM = meltRamp(''.join([folder,i]))[1]

        derivTotM.append(rr(melt,timeM))
        derivTotNameM.append(i)

    count = 0
    for i in derivTotM:
        count += 1
        if i < meltLimitLow or i > meltLimitHigh:                                                         #fail 3 is included in ramp rate
            print(instListVar[count-1],'RR:',round(i,4),'FAIL')
        else:
            print(instListVar[count-1],'RR:',round(i,4),'PASS')




melting()
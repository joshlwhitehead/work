"""This script analyzes TC thermal data parsed using parsTCTxt. It captures the ramp rates for heating and cooling the TC chamber."""
import numpy as np
import os
from parsTxt import TCramp
import matplotlib.pyplot as plt


folder = 'dataMorgan/'                                                                       #folder to draw data from

instListShort = []
for i in os.listdir(folder):
    instListShort.append(i)                                                                     #list of instruments. must be in order that they appear in folder
replicate = 1                                                                                  #how many runs of each instrument
alpha = 0.05                                                                                    #significance level (1-confidence level)
p = 0.9                                                                                         #reliability
heatRRlimit = 0.5
coolRRlimit = -0.2
instList = instListShort*replicate                                                              #list of total runs
instList.sort()                                                                                 #sort instrument list to match with order in directory

instListVar = []
for inst in instListShort:                                                                         
    for rep in range(replicate):
        instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates






def rr(temps,times):                                                                    #calculates derivative of 1 degree polynomial
                                                                    
    
    a,b = np.polyfit(times,temps,1)
    
    # plt.plot(times,temps,'o')
    # plt.plot(times,a*np.array(times)+b)
    # plt.show()
  
    return a

def heating():                                                                          #funtion to analyze heating data
    derivTotH = []                                                                  #list ramp rate for all cycles 
    derivTotNameH = []                                                              #list name of file
                                                              #clump ramp rates by run
    for i in os.listdir(folder):
        heat = TCramp(''.join([folder,i]))[1][0]                                #call parsPCRTxt to parse txt file and return temp data
        timeH = TCramp(''.join([folder,i]))[1][1]                               #call parsPCRTxt to parse txt file and return time data


        derivTotH.append(rr(heat,timeH))
        derivTotNameH.append(i)

    count = 0
    for i in derivTotH:
        count += 1
        if i < heatRRlimit:                                                         #fail 3 is included in ramp rate
            print(instListVar[count-1],'RR:',round(i,4),'FAIL')
        else:
            print(instListVar[count-1],'RR:',round(i,4),'PASS')



def cooling():                                                  #function to analyze cooling data
    derivTotC = []                                                                  #list ramp rate for all cycles 
    derivTotNameC = []                                                              #list name of file
                                                              #clump ramp rates by run
    for i in os.listdir(folder):
        cool = TCramp(''.join([folder,i]))[2][0]                                #call parsPCRTxt to parse txt file and return temp data
        timeC = TCramp(''.join([folder,i]))[2][1]                               #call parsPCRTxt to parse txt file and return time data


        derivTotC.append(rr(cool,timeC))
        derivTotNameC.append(i)

    count = 0
    for i in derivTotC:
        count += 1
        if i > coolRRlimit:                                                         #fail 3 is included in ramp rate
            print(instListVar[count-1],'RR:',round(i,4),'FAIL')
        else:
            print(instListVar[count-1],'RR:',round(i,4),'PASS')



cooling()
"""This script analyzes PCR Melt data parsed using parsTCTxt. It captures the melting ramp rate and tolerance interval."""
import numpy as np
import os
from parsTxt import meltRamp
import toleranceinterval as ti



folder = 'data/'                                                                       #folder to draw data from
instListShort = [1]                                                                         #list of instruments. must be in order that they appear in folder

replicate = 1                                                                                  #how many runs of each instrument
instList = instListShort*replicate                                                              #list of total runs
instList.sort()                                                                                 #sort instrument list to match with order in directory

instListVar = []
for inst in instListShort:                                                                         
    for rep in range(replicate):
        instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates




def rr(temps,times):                                                                    #calculates derivative of 1 degree polynomial
    a,b = np.polyfit(times,temps,1)
    return a


def melting(alpha,p):                                                                          #funtion to analyze melting data
    for i in os.listdir(folder):
        melt = meltRamp(''.join([folder,i]))[0]                                                 #raw melt data
        timeM = meltRamp(''.join([folder,i]))[1]

        n = int(len(melt)/11)                                                                   #split melt into 11 chunks

        count0 = 0
        count1 = n
        rrChunks = []
        for u in range(11):
            rrChunks.append(rr(melt[count0:count1],timeM[count0:count1]))                       #find slope of each chunk in melt
            count0 += n
            count1 += n

        bound = ti.twoside.normal(rrChunks,p,1-alpha)                                           #find tolerance interval for each melt
        
        print(i,'Melt TI:',bound)


melting(.05,.9)
"""This script analyzes TC thermal data parsed using parsTCTxt. It captures the ramp rates for heating and cooling the TC chamber."""
import numpy as np
import os
from parsTxt import meltRamp
import matplotlib.pyplot as plt
import toleranceinterval as ti
from scipy.stats import t
from statsmodels.formula.api import ols
import pandas as pd
alpha = .1
p = .9


folder = 'rampStuff/'                                                                       #folder to draw data from
instListShort = [5,7,9,11,13,15,20,23,25,28]                                                                         #list of instruments. must be in order that they appear in folder
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


def melting(alpha,p):      
    count = 0  
    means = []                                                                  #funtion to analyze melting data
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
        
        print(bound)

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        means.append(np.mean(rrChunks))
        count += 1
    plt.plot(means,np.arange(0,len(instListVar)),'o',color='r')
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Interval (p=0.90)']))
    plt.ylabel('Instrument')
    plt.xlabel('Ramp Rate (C/sec)')
    plt.grid()
    plt.yticks(np.arange(0,len(os.listdir(folder))),instListVar)
    plt.show()
melting(alpha,p)


def meltCI(alpha):
    slopes = []
    cis = []
    cis2 = []
    for i in os.listdir(folder):
        
        melt = meltRamp(''.join([folder,i]))[0]                                                 #raw melt data
        timeM = meltRamp(''.join([folder,i]))[1]

        dfMelt = pd.DataFrame({'melt':melt,'time':timeM})
        model = ols('melt ~ time', dfMelt).fit()
        dof = len(melt)-1
        t_star = t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
        se = np.sqrt(model.mse_resid)
        n = len(melt)
        Sxx = np.var(dfMelt.time) * n # note - did not use ddof

        slope = rr(melt,timeM)

        ci = t_star*se/np.sqrt(Sxx)
        slopes.append(slope)
        cis.append([ci])
        # cis2.append([slope+ci])
    
    
    count = 0
    for i in range(len(cis)):
        plt.hlines(count,slopes[count]-cis[count],slopes[count]+cis[count],lw=5)
        count+= 1
    plt.plot(slopes,np.arange(0,len(instListVar)),'o',color='r')
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.ylabel('Instrument')
    plt.xlabel('Ramp Rate (C/sec)')
    plt.grid()
    plt.yticks(np.arange(0,len(os.listdir(folder))),instListVar)
    plt.show()

meltCI(alpha)


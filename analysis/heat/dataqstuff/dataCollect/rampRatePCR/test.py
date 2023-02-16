import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import os
from parsTxt import parsPCRTxt
import toleranceinterval as ti



instListShort = [15,25]                                                                         #list of instruments. must be in order that they appear in folder
replicate = 3                                                                                   #how many runs of each instrument
alpha = 0.05                                                                                    #significance level (1-confidence level)
p = 0.9                                                                                         #reliability
heatRRlimit = 3
coolRRlimit = -2
instList = instListShort*replicate                                                              #list of total runs
instList.sort()                                                                                 #sort instrument list to match with order in directory

instListVar = []
for inst in instListShort:                                                                         
    for rep in range(replicate):
        instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates





folder = 'data/'                                                                       #folder to draw data from
def rr(temps,times):                                                                    #calculates derivative of 1 degree polynomial
    derivs = []                                                                 
    for i in range(len(temps)):
        a,b = np.polyfit(times[i],temps[i],1)
        derivs.append(a)
    #     plt.plot(times[i],temps[i],'o')
    #     plt.plot(times[i],a*np.array(times[i])+b)
    # plt.show()
    return derivs

def heating():                                                                          #funtion to analyze heating data
    derivTotH = []                                                                  #list ramp rate for all cycles 
    derivTotNameH = []                                                              #list name of file
    derivClumpH = []                                                                #clump ramp rates by run
    for i in os.listdir(folder):
        heat = parsPCRTxt(''.join([folder,i]))[0][0]                                #call parsPCRTxt to parse txt file and return temp data
        timeH = parsPCRTxt(''.join([folder,i]))[0][1]                               #call parsPCRTxt to parse txt file and return time data
        for k in rr(heat,timeH):                                                    #add data to above lists
            derivTotH.append(k)
            derivTotNameH.append(i)
        derivClumpH.append(rr(heat,timeH))
    dfHeat = pd.DataFrame({'run':derivTotNameH,'rr':derivTotH})                     #create dataframe of ramp rate data for analysis


    m_compMM = pairwise_tukeyhsd(endog=dfHeat.rr, groups=dfHeat.run, alpha=alpha)   #print this to compare runs
    count = 0
    for i in derivClumpH:
        bound = ti.twoside.normal(i,p,1-alpha)                                      #calculate tolerance interval

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)                              #plot TI
        count += 1
        if bound[0][0] < heatRRlimit:                                                         #fail 3 is included in ramp rate
            print(instListVar[0],bound,'FAIL')
        else:
            print(instListVar[0],bound,'PASS')
    # plt.yticks(np.arange(0,len(os.listdir(folder))),instListVar)
    plt.vlines(3,0,count-1,'k',lw=5)
    plt.title('95% Tolerance Intervals (p=0.90)')
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()


    dfHeat.boxplot('rr',by='run')
    plt.show()



def cooling():                                                  #function to analyze cooling data

    derivTotC = []                                              #list of ramp rates while cooling
    derivTotNameC = []                                          #list of names of datafile

    derivClumpC = []                                            #clump ramp rates by run
    for i in os.listdir(folder):
        
        cool = parsPCRTxt(''.join([folder,i]))[1][0]            #call parsPCRTxt to parse txt file and return temp data
        timeC = parsPCRTxt(''.join([folder,i]))[1][1]           #call parsPCRTxt to parse txt file and return time data


        
        for k in rr(cool,timeC):                                #calculate ramp rate for each cycle
            derivTotC.append(k)
            derivTotNameC.append(i)
        
        derivClumpC.append(rr(cool,timeC))


     
    dfCool = pd.DataFrame({'run':derivTotNameC,'rr':derivTotC})                         #dataframe of ramp rates for analysis



    m_compMM = pairwise_tukeyhsd(endog=dfCool.rr, groups=dfCool.run, alpha=alpha)       #print this to compare runs


    count = 0
    for i in derivClumpC:                                                 #calculate tolerance interval
        bound = ti.twoside.normal(i,p,1-alpha)

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        count += 1
        if bound[0][0] > coolRRlimit:                                                #fail if TI contains -2
            print(instListVar[0],bound,'FAIL')
        else:
            print(instListVar[0],bound,'PASS')
    # plt.yticks(np.arange(0,len(os.listdir(folder))),instListVar)
    plt.vlines(-2,0,count-1,'k',lw=5)
    plt.title('95% Tolerance Intervals (p=0.90)')
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()




    dfCool.boxplot('rr',by='run')
    plt.show()
    # dF.boxplot('rr',by='type')
    # plt.show()






cooling()
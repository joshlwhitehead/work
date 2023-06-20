"""This script analyzes PCR thermal data parsed using parsPCRTxt. It captures the ramp rates for each cycle of a run
and calculates its tolerance interval along with the confidence interval of the mean."""
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import os
from parsTxt import parsPCRTxt
import toleranceinterval as ti
from scipy import stats



instListShort = [15,15.1,25]                                                                         #list of instruments. must be in order that they appear in folder
replicate = 1                                                                                  #how many runs of each instrument
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





folder = 'dataPCR/'                                                                       #folder to draw data from
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
            print(instListVar[count-1],bound,'FAIL')
        else:
            print(instListVar[count-1],bound,'PASS')
    # plt.yticks(np.arange(0,len(os.listdir(folder))),instListVar)
    plt.vlines(3,0,count-1,'k',lw=5)
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Interval (p=0.90)']))
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()


    # dfHeat.boxplot('rr',by='run')
    # plt.show()


    count=0
    for data in derivClumpH:
        mean_er = np.mean(data)                                                     #mean denature temp of run
        std_dev_er = np.std(data)                                                   #stdev of each run
        n = len(data)                                                               
        se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
        dof = n - 1                                                                 #degree of fredom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
        moe = t_star * se                                                           #margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
        print(instListVar[count],'CI:',round(mean_er,3),'+/-',round(moe,4))
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1

    plt.yticks(np.arange(0,len(derivClumpH)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Instrument')
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
            print(instListVar[count-1],bound,'FAIL')
        else:
            print(instListVar[count-1],bound,'PASS')
    # plt.yticks(np.arange(0,len(os.listdir(folder))),instListVar)
    plt.vlines(-2,0,count-1,'k',lw=5)
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Interval (p=0.90)']))
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()

    count=0
    for data in derivClumpC:
        mean_er = np.mean(data)                                                     #mean denature temp of run
        std_dev_er = np.std(data)                                                   #stdev of each run
        n = len(data)                                                               
        se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
        dof = n - 1                                                                 #degree of fredom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
        moe = t_star * se                                                           #margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
        print(instListVar[count],'CI:',round(mean_er,3),'+/-',round(moe,4))
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1

    plt.yticks(np.arange(0,len(derivClumpC)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Instrument')
    plt.show()


    # dfCool.boxplot('rr',by='run')
    # plt.show()
    # dF.boxplot('rr',by='type')
    # plt.show()






heating()
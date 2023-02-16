import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
import pandas as pd
import os
from parsTxt import parsPCRTxt
import toleranceinterval as ti



instListShort = [15,25]                                                                         #list of instruments. must be in order that they appear in folder
replicate = 3                                                                                   #how many runs of each instrument


instList = instListShort*replicate                                                              #list of total runs
instList.sort()                                                                                 #sort instrument list to match with order in directory

instListVar = []
for inst in instListShort:                                                                         
    for rep in range(replicate):
        instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates



alpha = 0.05
p = 0.9

folder = 'data/'
def rr(temps,times):
    derivs = []
    for i in range(len(temps)):
        a,b = np.polyfit(times[i],temps[i],1)
        derivs.append(a)
    #     plt.plot(times[i],temps[i],'o')
    #     plt.plot(times[i],a*np.array(times[i])+b)
    # plt.show()
    return derivs

def heating():
    derivTotH = []
    derivTotNameH = []
    derivClumpH = []
    for i in os.listdir(folder):
        heat = parsPCRTxt(''.join([folder,i]))[0][0]
        timeH = parsPCRTxt(''.join([folder,i]))[0][1]
        for k in rr(heat,timeH):
            derivTotH.append(k)
            derivTotNameH.append(i)
        derivClumpH.append(rr(heat,timeH))
    dfHeat = pd.DataFrame({'run':derivTotNameH,'rr':derivTotH})


    m_compMM = pairwise_tukeyhsd(endog=dfHeat.rr, groups=dfHeat.run, alpha=alpha)
    count = 0
    for i in derivClumpH:
        bound = ti.twoside.normal(i,p,1-alpha)

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        count += 1
        if bound[0][0] < 3:
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



def cooling():

    derivTotC = []
    derivTotNameC = []

    derivClumpC = []
    for i in os.listdir(folder):
        
        cool = parsPCRTxt(''.join([folder,i]))[1][0]
        timeC = parsPCRTxt(''.join([folder,i]))[1][1]


        
        for k in rr(cool,timeC):
            derivTotC.append(k)
            derivTotNameC.append(i)
        
        derivClumpC.append(rr(cool,timeC))


        
        # print(timeH[1])




    dfCool = pd.DataFrame({'run':derivTotNameC,'rr':derivTotC})



    m_compMM = pairwise_tukeyhsd(endog=dfCool.rr, groups=dfCool.run, alpha=alpha)


    count = 0
    for i in derivClumpC:
        bound = ti.twoside.normal(i,p,1-alpha)

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        count += 1
        if bound[0][0] > -2:
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
"""This script analyzes PCR thermal data parsed using parsPCRTxt. The data is then analyzed to determine it's tolerance interval
and its tolerance interval of the mean"""
from parsTxt import parsPCRTxt
import numpy as np
import matplotlib.pyplot as plt
import toleranceinterval as ti
import os
from scipy import stats
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols


folder = 'cupB/'                                                                      #folder where dave .txt files are kept

############                CHANGE THIS                                     ###################
# instListShort = ['p_a_7','p_b_7','p_a_9','p_b_9','p_a_11','p_b_13','p_a_15','p_b_15','g_a_5','g_b_23','g_a_25','g_b_25','g_a_28','g_b_28']                                                                         #list of instruments. must be in order that they appear in folder
instListShort = ['pb7','pb9','pb13','pb15','gb23','gb28']
replicate = 1                                                                                   #how many runs of each instrument



##############              PROBABLY DONT CHANGE            #####################
deviationCrit = 1.5                                                                             #acceptance crit
alpha = 0.05                                                                                    #1-confidence level
p = 0.9                                                                                         #reliability





########                DONT CHANGE             ##################
def denature():                                                                                     #create function to analyze denature temp
    instList = instListShort*replicate                                                              #list of total runs
    if replicate > 1:
        instList.sort()                                                                                 #sort instrument list to match with order in directory

    instListVar = []
    for inst in instListShort:                                                                         
        for rep in range(replicate):
            instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates

               
    temp = []    
    means = []
    tis = []
    count = 0
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[0][0]                                     #collect temperatures while heating
        peakSamp = []
        for peak in peakSampList:
            peakSamp.append(max(peak))                                                              #collect maximum (denature) temps for each cycle
        temp.append(peakSamp)                                                                       #matrix of denature temps for each run
        mean = np.mean(peakSamp)                                                                    #mean denature temp
        means.append(mean)                                                                          #list of mean denature temp
        denatTemp = parsPCRTxt(''.join([folder,file]))[2][0]


        bound = ti.twoside.normal(peakSamp,p,1-alpha)                                               #tolerance interval for each run
        tis.append(bound[0])                                                                        #list of TIs

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        
        if bound[0][0] < denatTemp-deviationCrit or bound[0][1] > denatTemp+deviationCrit:          #pass if TI within acceptance criteria
            print(instListVar[count],bound,'FAIL')
        else:
            print(instListVar[count],bound,'PASS')
        count += 1
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.vlines(denatTemp+deviationCrit,0,count-1,'k',lw=5)
    plt.vlines(denatTemp-deviationCrit,0,count-1,'k',lw=5)
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Interval (p=0.90)']))
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()
    # print(temp)
    instListLong = []
    tempLong=[]
    count = 0
    for inst in instListVar:
        for T in temp[count]:
            instListLong.append(inst)                                                                  #make long list of instruments
            tempLong.append(T)                                                                      #make total list of temps that correspond 
                                                                                                    #to long list of instruments
        count+= 1


    
    dfTemp = pd.DataFrame({'Temp':tempLong,'Instrument':instListLong})                              #make dataframe with list of instruemnts with denature temps
    dfTemp.boxplot('Temp',by='Instrument')
    plt.show()
    
    m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)      #use tukey method to compare runs
    print(m_compMult)
    formula = 'Temp ~ Instrument'
    model = ols(formula, dfTemp).fit()
    aov_table = anova_lm(model, typ=1)
    print(aov_table)
    count=0
    for data in temp:
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

    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Instrument')
    plt.show()

    

    




def anneal():                                                                               #function to analyze anneal temps
    # instListShort = inputtxt.get("1.0","end-1c").split()                                    #which instruments is the data from
    # replicate = int(inputtxt2.get("1.0","end-1c"))                                          #how many runs from each instrument
    instList = instListShort*replicate                                                      #list that has each instrument repeated as many times
                                                                                            #as replicates
    
    instListVar = []
    for inst in instListShort:
        for rep in range(replicate):
            instListVar.append(''.join([str(inst),'.',str(rep)]))                           #create list that distinguishes each run on an instrument
    instList.sort()


    temp = []    
    means = []
    tis = []
    count = 0
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[1][0]                                     #collect temperatures while heating
        peakSamp = []
        for peak in peakSampList:
            peakSamp.append(min(peak))                                                              #collect maximum (denature) temps for each cycle
        temp.append(peakSamp)                                                                       #matrix of denature temps for each run
        mean = np.mean(peakSamp)                                                                    #mean denature temp
        means.append(mean)                                                                          #list of mean denature temp
        annealTemp = parsPCRTxt(''.join([folder,file]))[2][1]


        bound = ti.twoside.normal(peakSamp,p,1-alpha)
        tis.append(bound[0])

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        if bound[0][0] < annealTemp-deviationCrit or bound[0][1] > annealTemp+deviationCrit:
            print(instListVar[count],'TI:',bound,'FAIL')
        else:
            print(instListVar[count],'TI:',bound,'PASS')
        count += 1
        
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.vlines(annealTemp+deviationCrit,0,count-1,'k',lw=5)
    plt.vlines(annealTemp-deviationCrit,0,count-1,'k',lw=5)
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Interval (p=0.90)']))
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()
    instListLong = []
    tempLong=[]
    count = 0
    for inst in instListVar:
        for T in temp[count]:
            instListLong.append(inst)                                                                  #make long list of instruments
            tempLong.append(T)                                                                      #make total list of temps that correspond 
                                                                                                    #to long list of instruments
        count+= 1


    
    dfTemp = pd.DataFrame({'Temp':tempLong,'Instrument':instListLong})                              #make dataframe with list of instruemnts with denature temps

    
    m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)      #use tukey method to compare runs
    print(m_compMult)
    formula = 'Temp ~ Instrument'
    model = ols(formula, dfTemp).fit()
    aov_table = anova_lm(model, typ=2)
    print(aov_table)
    count=0
    for data in temp:
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

    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Instrument')
    plt.show()



# denature()
anneal()
# 
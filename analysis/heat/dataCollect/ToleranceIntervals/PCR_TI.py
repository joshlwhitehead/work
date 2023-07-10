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


# folder = 'dataPCR/'                                                                      #folder where dave .txt files are kept
# instListShort = ['p_a_7','p_b_7','p_a_9','p_b_9','p_a_11','p_b_11','p_a_13','p_b_13','p_a_15','p_b_15','g_a_5','g_b_5','g_a_20','g_b_20','g_a_23','g_b_23','g_a_25','g_b_25','g_a_28','g_b_28']                                                                         #list of instruments. must be in order that they appear in folder
# totalInd = ['p','g']*10
# totalInd.sort(reverse=True)
# print(totalInd)
############                CHANGE THIS                                     ###################
# folder = 'RunA/'
# instListShort = ['pa7','pa9','pa11','pa13','pa15','ga5','ga20','ga23','ga25','ga28']
# totalInd = ['p','p','p','p','p','g','g','g','g','g']

# folder = 'RunB/'
# instListShort = ['pb7','pb9','pb11','pb13','pb15','gb5','gb20','gb23','gb25','gb28']
# totalInd = ['p','p','p','p','p','g','g','g','g','g']
# folder = 'justinTot/'
# instListShort = ['v102_c1','v102_c2','v102_c3','v109_c1','v109_c2','v109_c2','v118_c1','v118_c2','v118_c3','v102_1','v109_1','v118_1','v102_2','v109_2','v118_2']
folder = 'betaValphaModel/'
instListShort = []
for i in os.listdir(folder):
    instListShort.append(i[:-4])
print(instListShort)
# instListShort = np.arange(0,len(os.listdir(folder)))

replicate = 1                                                                                   #how many runs of each instrument



##############              PROBABLY DONT CHANGE            #####################
deviationCrit = 1.5                                                                             #acceptance crit
alpha = 0.1                                                                                    #1-confidence level
p = 0.9                                                                                         #reliability





########                DONT CHANGE             ##################
def denature(folder,instListShort):                                                                                     #create function to analyze denature temp
    # instListShort = inputtxt.get("1.0","end-1c").split()                                    #which instruments is the data from
    # replicate = int(inputtxt2.get("1.0","end-1c"))                                          #how many runs from each instrument
    instList = instListShort*replicate                                                      #list that has each instrument repeated as many times
                                                                                            #as replicates
    
    instListVar = []
    instList = instListShort*replicate                                                              #list of total runs
    if replicate > 1:
        instList.sort()                                                                                 #sort instrument list to match with order in directory

    instListVar = instListShort
    # for inst in instListShort:                                                                         
    #     for rep in range(replicate):
    #         instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates 
    temp = []    
    means = []
    tis = []
    total = []
    count = 0
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[0][0]                                     #collect temperatures while heating
        
        peakSamp = []
        for peak in peakSampList:
            # print(max(peak))
            peakSamp.append(max(peak))                                                              #collect maximum (denature) temps for each cycle
        temp.append(peakSamp)                                                                       #matrix of denature temps for each run
        mean = np.mean(peakSamp)                                                                    #mean denature temp
        means.append(mean)                                                                          #list of mean denature temp
        denatTemp = parsPCRTxt(''.join([folder,file]))[2][0]
        total.append(mean)


        bound = ti.twoside.normal(peakSamp,p,1-alpha)                                               #tolerance interval for each run
        tis.append(bound[0])                                                                        #list of TIs

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        
        if bound[0][0] < denatTemp-deviationCrit or bound[0][1] > denatTemp+deviationCrit:          #pass if TI within acceptance criteria
            print(instListVar[count],bound,'FAIL')
        else:
            print(instListVar[count],bound,'PASS')
        count += 1
    
    for i in range(len(means)):
        print(instListVar[i],'TI:',round(means[i],3),'+/-',round(means[i]-tis[i][0],4))
    plt.yticks(np.arange(0,len(temp)),instListVar,rotation=45)
    # plt.xlim(88.3,97)|
    plt.plot(means,np.arange(0,len(instListVar)),'o',color='r')
    plt.vlines(denatTemp+deviationCrit,0,count-1,'k',lw=5)
    plt.vlines(denatTemp-deviationCrit,0,count-1,'k',lw=5)
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Interval (p=0.90)',' denature']))
    plt.ylabel('Run')
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
    # dfTemp.boxplot('Temp',by='Instrument')
    # plt.show()
    # dfTot = pd.DataFrame({'Mean':total,'type':totalInd})
    
    # m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)      #use tukey method to compare runs
    # m_compMult = pairwise_tukeyhsd(endog=dfTot['Mean'],groups=dfTot['type'],alpha=alpha)
    # print(m_compMult)
    # formula = 'Mean ~ type'
    # model = ols(formula, dfTot).fit()
    # aov_table = anova_lm(model, typ=1)
    # print(aov_table)
    count=0
    cis = []
    for data in temp:
        mean_er = np.mean(data)                                                     #mean denature temp of run
        std_dev_er = np.std(data)                                                   #stdev of each run
        n = len(data)                                                               
        se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
        dof = n - 1                                                              #degree of fredom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
        moe = t_star * se                                                           #margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
        cis.append(ciMult)
        print(instListVar[count],'CI:',round(mean_er,3),'+/-',round(moe,4))
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1

    plt.yticks(np.arange(0,len(temp)),instListVar,rotation=45)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval',' denature']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Run')
    plt.show()

    # return cis
    

    




def anneal(folder,instListShort):                                                                               #function to analyze anneal temps
    # instListShort = inputtxt.get("1.0","end-1c").split()                                    #which instruments is the data from
    # replicate = int(inputtxt2.get("1.0","end-1c"))                                          #how many runs from each instrument
    instList = instListShort*replicate                                                      #list that has each instrument repeated as many times
                                                                                            #as replicates
    
    instListVar = []
    instList = instListShort*replicate                                                              #list of total runs
    if replicate > 1:
        instList.sort()                                                                                 #sort instrument list to match with order in directory

    instListVar = instListShort
    # for inst in instListShort:                                                                         
    #     for rep in range(replicate):
    #         instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates
  


    temp = []    
    means = []
    tis = []
    count = 0
    for file in os.listdir(folder):
        
        peakSampList = parsPCRTxt(''.join([folder,file]))[1][0]                                     #collect temperatures while heating
        peakSamp = []
        for peak in peakSampList:
            peakSamp.append(min(peak)) 
            # print(peakSamp) 
                                                                   #collect maximum (denature) temps for each cycle
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
    for i in range(len(means)):
        print(instListVar[i],'TI:',round(means[i],3),'+/-',round(means[i]-tis[i][0],4))
    plt.plot(means,np.arange(0,len(instListVar)),'o',color='r')
    plt.yticks(np.arange(0,len(temp)),instListVar,rotation=45)
    plt.vlines(annealTemp+deviationCrit,0,count-1,'k',lw=5)
    plt.vlines(annealTemp-deviationCrit,0,count-1,'k',lw=5)
    # plt.xlim(45,54)
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Interval (p=0.90)',' anneal']))
    plt.ylabel('Run')
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
    cis = []
    for data in temp:
        mean_er = np.mean(data)                                                     #mean denature temp of run
        std_dev_er = np.std(data)                                                   #stdev of each run
        n = len(data)                                                               
        se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
        dof = n - 1                                                               #degree of fredom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
        moe = t_star * se                                                           #margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
        cis.append(ciMult)
        print(instListVar[count],'CI:',round(mean_er,3),'+/-',round(moe,4))
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
        plt.plot(mean_er,count,'o',color='r',ms=7)
        
        count+=1

    plt.yticks(np.arange(0,len(temp)),instListVar,rotation=45)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval',' anneal']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Run')
    plt.show()
    
# folder = 'tape/'
# instlistshort = ['v1_102','v1_109','v1_118','v2_102','v2_109','v2_118']#,'v3_102_a','v3_102_b','v3_109','v3_118']
# instlistshort = [1.02,1.09,1.18,2.02,2.09,2.18,3.021,3.022,3.09,3.18]
# denature(folder,instListShort)
anneal(folder,instListShort)
denature(folder,instListShort)

# 
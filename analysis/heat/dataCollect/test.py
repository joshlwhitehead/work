"""analyze """
from parsTxt import parsTCTxt
import numpy as np
import dataToVar as dat
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
from statsmodels.graphics.factorplots import interaction_plot
import os


folder = 'data/10Feb2023_f09TC/'
deviationCrit = 2.5
instListShort = [2,6,9,10,13,15,18,25,27]
replicate = 1
instList = instListShort*replicate
instList.sort()
alpha = 0.05



colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']

        
def kill():
    
    
    

    instListVar = []
    for inst in instListShort:
        for rep in range(replicate):
            instListVar.append(''.join([str(inst),'.',str(rep)]))
    

    temp = []
    means = []
    for file in os.listdir(folder):
        killTemps = parsTCTxt(''.join([folder,file]))[0][0]
        temp.append(killTemps)
        mean = np.mean(killTemps)
        means.append(mean)
        killTemp = parsTCTxt(''.join([folder,file]))[2][0]
        plt.plot(killTemps,'o-',label=file)
    plt.legend()
    plt.show()
    

    instListLong = []
    tempLong = []
    count = 0
    for inst in instListVar:
        for T in temp[count]:
            instListLong.append(inst)
            tempLong.append(T)

        count += 1
    
    dfTemp = pd.DataFrame({'Temp':tempLong,'Instrument':instListLong})                              #make dataframe with list of instruemnts with denature temps

    
    m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)      #use tukey method to compare runs
    
    print(m_compMult)
    dfTemp.boxplot('Temp',by='Instrument')                                                              #create boxplot to compare runs
    plt.ylabel('Temp (c)')
    plt.hlines(killTemp,1,len(instList),'r')
    plt.hlines(killTemp-deviationCrit,1,len(instList),'k')
    plt.hlines(killTemp+deviationCrit,1,len(instList),'k')
    plt.show()
    count = 0
    for i in temp:
        if stats.anderson(i,dist='norm')[0] < stats.anderson(i,dist='norm')[1][2]:    #use anderson test to check if data follows normal distribution
            print('data are normal')
        else:
            print('data are not normal')
            print(stats.anderson(i,dist='norm'))
            plt.hist(i,density=True)
            x = np.linspace(min(i),max(i))
            plt.plot(x,stats.norm.pdf(x,loc=np.mean(i),scale=np.std(i)))
            plt.grid()
            plt.title(''.join(['Distribution of ',instListVar[count]]))
            plt.xlabel('Temperature (c)')
            plt.ylabel('Density')
            plt.show()
        count += 1

    ### this loop characterizes individual runs and 
    ### analyzes the diffrence between runs
    count=0
    limitLow = killTemp - deviationCrit                                                                   #define acceptance window
    limitHigh = killTemp + deviationCrit
    probs = []
    for data in temp:
        mean_er = np.mean(data)                                                     #mean denature temp of run
        std_dev_er = np.std(data)  
        print(std_dev_er)                                                 #stdev of each run
        n = len(data)                                                               
        se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
        dof = n - 1                                                                 #degree of fredom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
        moe = t_star * se                                                           #margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
        t_limitLow = (limitLow - mean_er) / se                                                              #set limit to find probability                                                     
        t_limitHigh = (limitHigh - mean_er) / se
        prLow = stats.t.cdf(t_limitLow, dof)                                                                #use cumulative distribution function of t-dist to find
                                                                                                            #probability of temperature being too low
        prHigh = 1 - stats.t.cdf(t_limitHigh, dof)                                                          #use cumulative distribution function of t-dist to find
                                                                                                            #probability of temperature being too low
        probs.append(prHigh+prLow) 
        
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1
    print(np.mean(probs),np.std(probs))
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Instrument')
    plt.show()



    ###ONLY DO THIS IF YOU WANT TO COMPARE INSTRUMENTS
    
    # dfAnova = pd.DataFrame({'Instrument':instList,'Mean':means,'Temp':temp})                        #make dataframe with list of instruments with mean denature temps
    # m_compMM = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], alpha=alpha)      #use tukey method to compare instruments w/ multiple runs
    # print(m_compMM)
    # if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:    #use anderson test to check if data follows normal distribution
    #     print('data are normal')
    # else:
    #     print('data are not normal')

    # dfAnova.boxplot('Mean',by='Instrument')                                                             #create boxplot to compare instruments
    # plt.ylabel('Temp (c)')
    # plt.hlines(killTemp,1,len(instListShort),'r')                                                             #draw line at upper and lower limit (+/- 3c)
    # plt.hlines(killTemp-deviationCrit,1,len(instListShort),'k')
    # plt.hlines(killTemp+deviationCrit,1,len(instListShort),'k')
    # plt.show()



    # clumpMeans = [means[i:i+replicate] for i in range(0,len(means),replicate)]                          #group lists of means for each instrument


    # ### this loop uses t-dist to characterize instruments
    # # and analyze differences between them
    # limitLow = killTemp - deviationCrit                                                                                   #establish upper and lower limit
    # limitHigh = killTemp + deviationCrit
    # count = 0
    # probs = []
    # for data in clumpMeans:                                         
    #     mean_er = np.mean(data)                                                     #mean of means on each instrument
    #     std_dev_er = np.std(data)                                                   #standard dev of means on each instrument
    #     n = len(data)
    #     se = std_dev_er / np.sqrt(n)                                                #standard error = stdev/sqrt(n)
    #     dof = n - 1                                                                 #degree of freedom for t-test = n-1
    #     t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from probability point function (ppf) for t-test
    #     moe = t_star * se                                                           #margin of error = t* x standard error
    #     ci = np.array([mean_er - moe, mean_er + moe])                               #confidence interval at 1-alpha
    #     t_limitLow = (limitLow - mean_er) / se                                      #set limit parameters for cumulative distribution function (cdf)
    #     t_limitHigh = (limitHigh - mean_er) / se
    #     prLow = stats.t.cdf(t_limitLow, dof)                                        #probability that temperature is lower than lower limit
    #     prHigh = 1 - stats.t.cdf(t_limitHigh, dof)                                  #probability that temp is higher than upper limit
    #     probs.append(prHigh+prLow)                                                  #total probability that temp is higher than upper or lower than lower limit
    #     plt.hlines(count,ci[0],ci[1],lw=5)
    #     plt.plot(mean_er,count,'o',color='r',ms=7)
    #     count+=1
    # plt.yticks(np.arange(0,len(clumpMeans)),instListShort)
    # plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))                #make plot to show 1-alpha confidence interval
    # plt.grid()
    # plt.xlabel('Mean Temp (c)')
    # plt.ylabel('Instrument')
    # plt.show()

    # plt.title('Probability of Deviation from Model')
    # plt.plot(np.array(probs)*100,'o')                                                             #plot probability that temperature is found outside of limits
    # plt.grid()
    # plt.xlabel('Instrument')
    # plt.ylabel('Probability of deviation (%)')
    # plt.xticks(np.arange(0,len(clumpMeans)),instListShort)
    # plt.show()

    








kill()



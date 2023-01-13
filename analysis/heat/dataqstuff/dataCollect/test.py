"""analyze """

import numpy as np
import dataToVar as dat
import matplotlib.pyplot as plt
import pandas as pd
# from thermalCompareQuant import listAvg, listStd, listRms, listGrad, interppp
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
from statsmodels.graphics.factorplots import interaction_plot
# import statsmodels.api as sm

alpha=0.05
total = dat.proposeMod
instListShort = [13,15,25]
instList = instListShort*3
instListVar = [13,13.1,13.2,15,15.1,15.2,25,25.1,25.2]
instList.sort()
# plt.plot(total[0][4])
# plt.plot(total[0][2])
# plt.grid()
# plt.show()
def denature():
    temp = []
    # colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']
    count = 0
    n=0
    means=[]
    percPassTot = []
    
    for i in total:
        time = i[0]
        model = i[4]
        samp = i[2]
        # plt.close('all')
        # plt.plot(samp,'o-')
        # plt.plot(model)
        # plt.hlines(90,0,max(time),'k')
        # # plt.hlines(94,0,max(time),'k')
        # plt.show()
        peakSamp = []
        peakModel = []
        countPass = 0
        percPass = []
        for i in range(len(samp)):
            if i > 590 and samp[i] >90 and samp[i]>samp[i-1] and samp[i]>samp[i+1]:
                peakSamp.append(samp[i])
            if model[i] >90 and model[i]>model[i-1] and model[i-1]>model[i-2] and model[i]>model[i+1] and model[i+1]>model[i+2]:
                peakModel.append(model[i])

        for i in peakSamp:
            if i <98 and i > 92:
                countPass +=1
        percPassTot.append(countPass/len(peakSamp))
        
        # plt.plot(peakSamp[:],label=instList[count])
        # plt.plot(peakModel[:len(peakSamp[:-3])],'k')
        
        count += 1
        # print(len(peakSamp[:-1]))
        temp.append(peakSamp)
        mean = np.mean(peakSamp[:])
        means.append(mean)
    
    # plt.grid()
    # plt.legend()
    # plt.show()
    # print(means)
    tempLong=[]
    instListLong = []
    count = 0
    
    for i in instListVar:
        for u in temp[count]:
            instListLong.append(i)
            tempLong.append(u)
        count+= 1
    # print(instListLong)
    # print(len(instList),len(means),len(tempLong),len(instListLong))
    # print(len(means),len(temp),len(instList))
    dfAnova = pd.DataFrame({'Instrument':instList,'Mean':means,'Temp':temp})
    dfTemp = pd.DataFrame({'Temp':tempLong,'Instrument':instListLong})

    
    if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:
        print('data are normal')
    else:
        print('data are not normal')

    # m_compMM = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], alpha=alpha)
    m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)
    # print(m_compMM)
    print(m_compMult)
    dfAnova.boxplot('Mean',by='Instrument')
    plt.ylabel('Temp (c)')
    plt.hlines(95,1,len(instListShort),'r')
    plt.hlines(92,1,len(instListShort),'k')
    plt.hlines(98,1,len(instListShort),'k')
    plt.show()

    dfTemp.boxplot('Temp',by='Instrument')
    plt.ylabel('Temp (c)')
    plt.hlines(95,1,len(instList),'r')
    plt.hlines(92,1,len(instList),'k')
    plt.hlines(98,1,len(instList),'k')
    plt.show()

    clumpMeans = [means[i:i+3] for i in range(0,len(means),3)]
    clumpInst = [instList[i:i+3] for i in range(0,len(instList),3)]
        
    # print(clumpMeans)

    # for i in dfAnova.Temp:
    #     dist = 'norm'
    #     x = np.linspace(min(i),max(i))
    
    #     if stats.anderson(np.array(i),dist=dist)[0] < stats.anderson(np.array(i),dist=dist)[1][2]:
    #         print('data are',dist)
    #     else:
    #         print('data are not',dist)
    #         print(stats.anderson(np.array(i),dist=dist))

    
    #     plt.hist(np.array(i),density=True)

    #     plt.show()




    limitLow = 95 - 3
    limitHigh = 95 + 3
    count = 0
    probs = []
    for i in clumpMeans:
        mean_er = np.mean(i) # sample mean
        std_dev_er = np.std(i, ddof=1) # sample standard devialtion
        se = std_dev_er / np.sqrt(len(i)) # standard error
        n = len(i) # sample size, n
        dof = n - 1 # degrees of freedom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
        moe = t_star * se # margin of error
        ci = np.array([mean_er - moe, mean_er + moe])
        t_limitLow = (limitLow - mean_er) / se
        t_limitHigh = (limitHigh - mean_er) / se
        prLow = stats.t.cdf(t_limitLow, dof)
        prHigh = 1 - stats.t.cdf(t_limitHigh, dof)
        probs.append(prHigh+prLow)
        

        plt.hlines(count,ci[0],ci[1],lw=5)
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1
    plt.yticks(np.arange(0,len(clumpMeans)),instListShort)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('AdvB')
    plt.show()
    count=0
    for i in temp:
        mean_er = np.mean(i)
        std_dev_er = np.std(i, ddof=1) # sample standard devialtion
        se = std_dev_er / np.sqrt(len(i)) # standard error
        n = len(i) # sample size, n
        dof = n - 1 # degrees of freedom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
        moe = t_star * se # margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1
    # print(clumpMeans)
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('AdvB')
    plt.show()

    plt.title('Probability of Deviation from Model')
    plt.plot(probs,'o')
    plt.grid()
    plt.xlabel('AdvB')
    plt.ylabel('Prob Mean < Model - 3c OR Mean > Model + 3c')
    plt.xticks(np.arange(0,len(clumpMeans)),instListShort)
    plt.show()
    
    print(percPassTot)


    


    plt.title('Pass Rate')
    plt.plot(np.array(percPassTot)*100,'o')
    plt.xticks(np.arange(0,len(percPassTot)),instListVar)
    plt.grid()
    plt.ylabel('%')
    plt.xlabel('AdvB')
    plt.show()













def anneal():
    temp = []
    # colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']
    count = 0
    n=0
    means=[]
    for i in total:
        time = i[0]
        model = i[4]
        samp = i[2]
        # plt.close('all')
        # plt.plot(samp,'o-')
        # plt.plot(model)
        # plt.hlines(90,0,max(time),'k')
        # # plt.hlines(94,0,max(time),'k')
        # plt.show()
        peakSamp = []
        peakModel = []
        # print(len(samp))
        for i in range(len(samp)):
            if i > 590 and i< 1865 and samp[i] < 60 and samp[i]<samp[i-1] and samp[i]<samp[i+1]:
                peakSamp.append(samp[i])
            # if model[i] <60 and model[i]<model[i-1] and model[i-1]<model[i-2] and model[i]<model[i+1] and model[i+1]<model[i+2]:
            #     peakModel.append(model[i])
    
        
        plt.plot(peakSamp[:],label=instList[count])
        # plt.plot(peakModel[:len(peakSamp[:-3])],'k')
        
        count += 1
        # print(len(peakSamp[:-1]))
        temp.append(peakSamp)
        mean = np.mean(peakSamp[:])
        means.append(mean)
    plt.grid()
    plt.legend()
    plt.show()
    # print(means)
    tempLong=[]
    instListLong = []
    count = 0
    # instListVar = [10,10.1,10.2,18,18.1,18.2]
    for i in instListVar:
        for u in temp[count]:
            instListLong.append(i)
            tempLong.append(u)
        count+= 1
    # print(instListLong)
    # print(len(instList),len(means),len(tempLong),len(instListLong))
    dfAnova = pd.DataFrame({'Instrument':instList,'Mean':means,'Temp':temp})
    dfTemp = pd.DataFrame({'Temp':tempLong,'Instrument':instListLong})


    if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:
        print('data are normal')
    else:
        print('data are not normal')

    m_compMM = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], alpha=alpha)
    m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)
    print(m_compMM)
    print(m_compMult)
    dfAnova.boxplot('Mean',by='Instrument')
    plt.ylabel('Temp (c)')
    plt.hlines(55,1,len(instListShort),'r')
    plt.hlines(52,1,len(instListShort),'k')
    plt.show()

    dfTemp.boxplot('Temp',by='Instrument')
    plt.ylabel('Temp (c)')
    plt.hlines(55,1,len(instList),'r')
    plt.hlines(52,1,len(instList),'k')
    plt.show()

    clumpMeans = [means[i:i+3] for i in range(0,len(means),3)]
    clumpInst = [instList[i:i+3] for i in range(0,len(instList),3)]
        


    # for i in dfAnova.Temp:
    #     dist = 'norm'
    #     x = np.linspace(min(i),max(i))
    
    #     if stats.anderson(np.array(i),dist=dist)[0] < stats.anderson(np.array(i),dist=dist)[1][2]:
    #         print('data are',dist)
    #     else:
    #         print('data are not',dist)
    #         print(stats.anderson(np.array(i),dist=dist))

    
    #     plt.hist(np.array(i),density=True)

    #     plt.show()




    limitLow = 55 - 3
    limitHigh = 55 + 3
    count = 0
    probs = []
    for i in clumpMeans:
        mean_er = np.mean(i) # sample mean
        std_dev_er = np.std(i, ddof=1) # sample standard devialtion
        se = std_dev_er / np.sqrt(len(i)) # standard error
        n = len(i) # sample size, n
        dof = n - 1 # degrees of freedom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
        moe = t_star * se # margin of error
        ci = np.array([mean_er - moe, mean_er + moe])
        t_limitLow = (limitLow - mean_er) / se
        t_limitHigh = (limitHigh - mean_er) / se
        prLow = stats.t.cdf(t_limitLow, dof)
        prHigh = 1 - stats.t.cdf(t_limitHigh, dof)
        probs.append(prHigh+prLow)
        

        plt.hlines(count,ci[0],ci[1],lw=5)
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1
    # print(clumpMeans)
    plt.yticks(np.arange(0,len(clumpMeans)),instListShort)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('AdvB')
    plt.show()
    count=0
    for i in temp:
        mean_er = np.mean(i)
        std_dev_er = np.std(i, ddof=1) # sample standard devialtion
        se = std_dev_er / np.sqrt(len(i)) # standard error
        n = len(i) # sample size, n
        dof = n - 1 # degrees of freedom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
        moe = t_star * se # margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1
    # print(clumpMeans)
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('AdvB')
    plt.show()

    plt.title('Probability of Deviation from Model')
    plt.plot(probs,'o')
    plt.grid()
    plt.xlabel('AdvB')
    plt.ylabel('Prob Mean < Model - 3c OR Mean > Model + 3c')
    plt.xticks(np.arange(0,len(clumpMeans)),instListShort)
    plt.show()
    # print(probs)

denature()

    
            
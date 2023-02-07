"""analyze """
from parsTxt import parsPCRTxt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
import os
from tkinter import *

alpha = 0.5
folder = 'data/27Jan2023/'

def denature():                                                                                     #create function to analyze denature temp
                                                                                #
    
    instListShort = inputtxt.get("1.0","end-1c").split()                                            #list of instruments in folder
    replicate = int(inputtxt2.get("1.0","end-1c"))                                                  #how many runs with each instrument
    instList = instListShort*replicate                                                              #list of total runs
    
    instListVar = []
    for i in instListShort:
        for u in range(replicate):
            instListVar.append(''.join([str(i),'.',str(u)]))
    # instListVar = ['15','15.1','15.2','25','25.1','25.2']
    print(instListVar)
    instList.sort()
    
    temp = []
    # colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']
    count = 0
    n=0
    means=[]
    for i in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,i]))[0][0]
        peakSamp = []
        for u in peakSampList:
            peakSamp.append(max(u))

        
        # plt.plot(peakSamp,'o')
        # plt.show()
        
        count += 1
        # print(len(peakSamp[:-1]))
        temp.append(peakSamp)
        mean = np.mean(peakSamp[:])
        means.append(mean)
   
    print(len(instList),len(means),len(temp))
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
    plt.hlines(95,1,len(instListShort),'r')
    plt.hlines(92,1,len(instListShort),'k')
    plt.show()

    dfTemp.boxplot('Temp',by='Instrument')
    plt.ylabel('Temp (c)')
    plt.hlines(95,1,len(instList),'r')
    plt.hlines(92,1,len(instList),'k')
    plt.show()

    clumpMeans = [means[i:i+replicate] for i in range(0,len(means),replicate)]
    clumpInst = [instList[i:i+replicate] for i in range(0,len(instList),replicate)]
        
    print(clumpMeans)




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
    # print(probs)




def anneal():


    instListShort = inputtxt.get("1.0","end-1c").split()
    replicate = int(inputtxt2.get("1.0","end-1c"))
    instList = instListShort*replicate
    

    instListVar = []
    for i in instListShort:
        for u in range(replicate):
            instListVar.append(''.join([str(i),'.',str(u)]))
    # instListVar = ['15','15.1','15.2','25','25.1','25.2']
    print(instListVar)
    instList.sort()


    temp = []
    # colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']
    count = 0
    n=0
    means=[]
    for i in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,i]))[1][0]
        peakSamp = []
        for u in peakSampList:
            peakSamp.append(min(u))

        
        plt.plot(peakSamp,'o')
        plt.show()
        
        count += 1
        # print(len(peakSamp[:-1]))
        temp.append(peakSamp)
        mean = np.mean(peakSamp[:])
        means.append(mean)
   
    
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

    clumpMeans = [means[i:i+replicate] for i in range(0,len(means),replicate)]
    clumpInst = [instList[i:i+replicate] for i in range(0,len(instList),replicate)]
        


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


root = Tk()                                                                                             #initialize user interface window
root.geometry("400x400")                                                                                #set size of window

root.title("Josh's Super-Duper Cool Stuff")                                                             #name ui window

inputtxt = Text(root, height = 8,width = 25)
lInst = Label(text='Instruments')
inputtxt2 = Text(root,height=2,width=25)
lRep = Label(text='Number of replicates for instruments')
inputtxt3 = Text(root,height=2,width=25)







run = Button(root,height=2,width=20,text='denature',command=lambda:denature())                            #create button that runs the above code when pushed
run2 = Button(root,height=2,width=20,text='anneal',command=lambda:anneal())#create button that runs the above code when pushed

lInst.pack()
inputtxt.pack()
lRep.pack()
inputtxt2.pack()
inputtxt3.pack()

run.pack()
run2.pack()
mainloop()


    
            
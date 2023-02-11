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

alpha = 0.05
folder = 'data/27Jan2023/'
deviationCrit = 1.5


def denature():                                                                                     #create function to analyze denature temp
                                                                                #
    
    instListShort = inputtxt.get("1.0","end-1c").split()                                            #list of instruments in folder
    replicate = int(inputtxt2.get("1.0","end-1c"))                                                  #how many runs with each instrument
    instList = instListShort*replicate                                                              #list of total runs
    instList.sort()                                                                                 #sort instrument list to match with order in directory

    instListVar = []
    for inst in instListShort:                                                                         
        for rep in range(replicate):
            instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates

               
    temp = []    
    means = []
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[0][0]                                     #collect temperatures while heating
        peakSamp = []
        for peak in peakSampList:
            peakSamp.append(max(peak))                                                              #collect maximum (denature) temps for each cycle
        temp.append(peakSamp)                                                                       #matrix of denature temps for each run
        mean = np.mean(peakSamp)                                                                    #mean denature temp
        means.append(mean)                                                                          #list of mean denature temp
        denatTemp = parsPCRTxt(''.join([folder,file]))[2][0]
    #     plt.plot(peakSamp,'o-')
    # plt.show()
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

    
    m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)      #use tukey method to compare runs
    
    print(m_compMult)
    dfTemp.boxplot('Temp',by='Instrument')                                                              #create boxplot to compare runs
    plt.ylabel('Temp (c)')
    plt.hlines(denatTemp,1,len(instList),'r')
    plt.hlines(denatTemp-deviationCrit,1,len(instList),'k')
    plt.hlines(denatTemp+deviationCrit,1,len(instList),'k')
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
    for data in temp:
        mean_er = np.mean(data)                                                     #mean denature temp of run
        std_dev_er = np.std(data)                                                   #stdev of each run
        n = len(data)                                                               
        se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
        dof = n - 1                                                                 #degree of fredom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
        moe = t_star * se                                                           #margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1

    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Instrument')
    plt.show()



    ###ONLY DO THIS IF YOU WANT TO COMPARE INSTRUMENTS
    if checkVar0.get() == 1:
        dfAnova = pd.DataFrame({'Instrument':instList,'Mean':means,'Temp':temp})                        #make dataframe with list of instruments with mean denature temps
        m_compMM = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], alpha=alpha)      #use tukey method to compare instruments w/ multiple runs
        print(m_compMM)
        if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:    #use anderson test to check if data follows normal distribution
            print('data are normal')
        else:
            print('data are not normal')

        dfAnova.boxplot('Mean',by='Instrument')                                                             #create boxplot to compare instruments
        plt.ylabel('Temp (c)')
        plt.hlines(denatTemp,1,len(instListShort),'r')                                                             #draw line at upper and lower limit (+/- 3c)
        plt.hlines(denatTemp-deviationCrit,1,len(instListShort),'k')
        plt.hlines(denatTemp+deviationCrit,1,len(instListShort),'k')
        plt.show()

    

        clumpMeans = [means[i:i+replicate] for i in range(0,len(means),replicate)]                          #group lists of means for each instrument


        ### this loop uses t-dist to characterize instruments
        # and analyze differences between them
        limitLow = denatTemp - deviationCrit                                                                                   #establish upper and lower limit
        limitHigh = denatTemp + deviationCrit
        count = 0
        probs = []
        for data in clumpMeans:                                         
            mean_er = np.mean(data)                                                     #mean of means on each instrument
            std_dev_er = np.std(data)                                                   #standard dev of means on each instrument
            n = len(data)
            se = std_dev_er / np.sqrt(n)                                                #standard error = stdev/sqrt(n)
            dof = n - 1                                                                 #degree of freedom for t-test = n-1
            t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from probability point function (ppf) for t-test
            moe = t_star * se                                                           #margin of error = t* x standard error
            ci = np.array([mean_er - moe, mean_er + moe])                               #confidence interval at 1-alpha
            t_limitLow = (limitLow - mean_er) / se                                      #set limit parameters for cumulative distribution function (cdf)
            t_limitHigh = (limitHigh - mean_er) / se
            prLow = stats.t.cdf(t_limitLow, dof)                                        #probability that temperature is lower than lower limit
            prHigh = 1 - stats.t.cdf(t_limitHigh, dof)                                  #probability that temp is higher than upper limit
            probs.append(prHigh+prLow)                                                  #total probability that temp is higher than upper or lower than lower limit
            plt.hlines(count,ci[0],ci[1],lw=5)
            plt.plot(mean_er,count,'o',color='r',ms=7)
            count+=1
        plt.yticks(np.arange(0,len(clumpMeans)),instListShort)
        plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))                #make plot to show 1-alpha confidence interval
        plt.grid()
        plt.xlabel('Mean Temp (c)')
        plt.ylabel('Instrument')
        plt.show()

        plt.title('Probability of Deviation from Model')
        plt.plot(np.array(probs)*100,'o')                                                             #plot probability that temperature is found outside of limits
        plt.grid()
        plt.xlabel('Instrument')
        plt.ylabel('Probability of deviation (%)')
        plt.xticks(np.arange(0,len(clumpMeans)),instListShort)
        plt.show()




    

    




def anneal():                                                                               #function to analyze anneal temps
    instListShort = inputtxt.get("1.0","end-1c").split()                                    #which instruments is the data from
    replicate = int(inputtxt2.get("1.0","end-1c"))                                          #how many runs from each instrument
    instList = instListShort*replicate                                                      #list that has each instrument repeated as many times
                                                                                            #as replicates
    
    instListVar = []
    for inst in instListShort:
        for rep in range(replicate):
            instListVar.append(''.join([str(inst),'.',str(rep)]))                           #create list that distinguishes each run on an instrument
    instList.sort()


    temp = []
    means=[]
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[1][0]                             #get data from anneal portion of file
        peakSamp = []
        for temps in peakSampList:
            peakSamp.append(min(temps))                                                     #select minimum temp (anneal)
        
        temp.append(peakSamp)                                                               #list of anneal temps
        mean = np.mean(peakSamp)                                                            #mean anneal temp for each run
        means.append(mean)                                                                  #list of means
        annealTemp = parsPCRTxt(''.join([folder,file]))[2][1]
        print(np.std(peakSamp))
        print(np.mean(peakSamp))
        plt.plot(peakSamp,'o-')
    plt.show()
    
    tempLong=[]
    instListLong = []
    count = 0
    for inst in instListVar:
        for temps in temp[count]:
            instListLong.append(inst)                                                       #one long list of instruments 
            tempLong.append(temps)                                                          #one long list of anneal temps that correlate with instrument list
        count+= 1

                                                                                         #than one run


    dfTemp = pd.DataFrame({'Temp':tempLong,'Instrument':instListLong})                                      #dataframe that has instrument/anneal temp data
              
    m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Instrument'], alpha=alpha)          #use tukey method to compare runs
    
    print(m_compMult)


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


    dfTemp.boxplot('Temp',by='Instrument')                                                                  #make boxplot to compare runs
    plt.ylabel('Temp (c)')
    plt.hlines(annealTemp,1,len(instList),'r')
    plt.hlines(annealTemp-deviationCrit,1,len(instList),'k')
    plt.hlines(annealTemp+deviationCrit,1,len(instList),'k')
    plt.show()

    count = 0
    limitLow = annealTemp - deviationCrit                                                                   #define acceptance window
    limitHigh = annealTemp + deviationCrit
    probs = []
    for data in temp:
        mean_er = np.mean(data)                                                                           #sample mean  
        std_dev_er = np.std(data)                                                                           # sample standard devialtion
        n = len(data)                                                                                       # sample size, n
        se = std_dev_er / np.sqrt(n)                                                                        # standard error
        dof = n - 1                                                                                         # degrees of freedom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                                        # using t-distribution
        moe = t_star * se                                                                                   #  margin of error
        ciMult = np.array([mean_er - moe, mean_er + moe])                                                       #1-alpha confidence interval for each run
        t_limitLow = (limitLow - mean_er) / se                                                              #set limit to find probability                                                     
        t_limitHigh = (limitHigh - mean_er) / se
        prLow = stats.t.cdf(t_limitLow, dof)                                                                #use cumulative distribution function of t-dist to find
                                                                                                            #probability of temperature being too low
        prHigh = 1 - stats.t.cdf(t_limitHigh, dof)                                                          #use cumulative distribution function of t-dist to find
                                                                                                            #probability of temperature being too low
        probs.append(prHigh+prLow)                                                                          #total probability of temp being outside defined window
                                                        
        plt.hlines(count,ciMult[0],ciMult[1],lw=5)
        plt.plot(mean_er,count,'o',color='r',ms=7)                                                          #plot confidence intervals
        count += 1
    print(probs)  
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))                                        
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('Instrument')
    plt.show()






    if checkVar0.get() == 1:
        dfAnova = pd.DataFrame({'Instrument':instList,'Mean':means,'Temp':temp})                                #dataframe that has instrument/mean anneal temp data
        m_compMM = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], alpha=alpha)          #use tukey method to compare instruments                                                                                                    #this is used for comparing instruments w/ more
        print(m_compMM)
        if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:        #run anderson test to check if data follows normal distribution
            print('data are normal')
        else:
            print('data are not normal') 
        dfAnova.boxplot('Mean',by='Instrument')                                                                 #make boxplot to compare instruments
        plt.ylabel('Temp (c)')
        plt.hlines(annealTemp+deviationCrit,1,len(instListShort),'k')
        plt.hlines(annealTemp,1,len(instListShort),'r')                                                                 #draw upper and lower limits +/-3c
        plt.hlines(annealTemp-deviationCrit,1,len(instListShort),'k')
        plt.show()    


        clumpMeans = [means[i:i+replicate] for i in range(0,len(means),replicate)]  
        
        
        
        count = 0
        probs = []
        for data in clumpMeans:
            mean_er = np.mean(data)                                                                                # sample mean
            std_dev_er = np.std(data)                                                                      # sample standard devialtion
            n = len(data)                                                                                          # sample size, n
            se = std_dev_er / np.sqrt(n)                                                                        # standard error
            dof = n - 1                                                                                         # degrees of freedom
            t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                                        # using t-distribution
            moe = t_star * se                                                                                   # margin of error
            ci = np.array([mean_er - moe, mean_er + moe])                                                       #1-alpha confidence interval
            t_limitLow = (limitLow - mean_er) / se                                                              #set limit to find probability                                                     
            t_limitHigh = (limitHigh - mean_er) / se
            prLow = stats.t.cdf(t_limitLow, dof)                                                                #use cumulative distribution function of t-dist to find
                                                                                                                #probability of temperature being too low
            prHigh = 1 - stats.t.cdf(t_limitHigh, dof)                                                          #use cumulative distribution function of t-dist to find
                                                                                                                #probability of temperature being too low
            probs.append(prHigh+prLow)                                                                          #total probability of temp being outside defined window
            print(probs)

            plt.hlines(count,ci[0],ci[1],lw=5)
            plt.plot(mean_er,count,'o',color='r',ms=7)                                                          #plot confidence interval for each instrument
            count+=1
        # print(clumpMeans)
        plt.yticks(np.arange(0,len(clumpMeans)),instListShort)
        plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
        plt.grid()
        plt.xlabel('Mean Temp (c)')
        plt.ylabel('Instrument')
        plt.show()       
        
        
        plt.title('Probability of Deviation from Model')
        plt.plot(probs,'o')                                                                                         #plot probability of deviation from defined window
        plt.grid()
        plt.xlabel('Instrument')
        plt.ylabel('Probability (%)')
        plt.xticks(np.arange(0,len(clumpMeans)),instListShort)
        plt.show()
        # print(probs) 
    


root = Tk()                                                                                             #initialize user interface window
root.geometry("400x400")                                                                                #set size of window

root.title("Josh's Super-Duper Cool Stuff")                                                             #name ui window

inputtxt = Text(root, height = 8,width = 25)                                                            #create window to input instrument list
lInst = Label(text='Instruments')
inputtxt2 = Text(root,height=4,width=25)                                                                #window to input number of replicates of each inst
lRep = Label(text='Number of replicates for instruments')
inputtxt3 = Text(root,height=2,width=25) 
inputtxt.insert(INSERT,'Which instruments/runs are you analyzing?')                                                               #window
inputtxt2.insert(INSERT,'Enter number of runs on \neach instrument. \nif no replicates, input \n"1"')
inputtxt3.insert(INSERT,'Are we having fun yet?')

checkVar0 = IntVar(value=0)
checkVar1 = IntVar(value=1)

checkRun = Checkbutton(root,text='Compare runs',variable=checkVar1,onvalue=1,offvalue=0)
checkInst = Checkbutton(root,text='Compare instrument',variable=checkVar0,onvalue=1,offvalue=0)





run = Button(root,height=2,width=20,text='denature',command=lambda:denature())                            #create button that runs the above code when pushed
run2 = Button(root,height=2,width=20,text='anneal',command=lambda:anneal())                                     #create button that runs the above code when pushed

lInst.pack()                                                                                            #add each thing to ui
inputtxt.pack()
checkInst.pack()
# checkRun.pack()
lRep.pack()

inputtxt2.pack()
inputtxt3.pack()

run.pack()
run2.pack()
mainloop()


    
            
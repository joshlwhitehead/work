"""This script analyzes TC thermal data parsed using parsTCTxt. The data is then analyzed to determine it's tolerance interval
and its tolerance interval of the mean"""
from parsTxt import parsTCTxt
import numpy as np
import matplotlib.pyplot as plt
import toleranceinterval as ti
import os
# from scipy import stats


folder = 'sydInf5/TOB Temp Discrepancy/'
#############               CHANGE THESE                    ######################
instListShort = []
for i in os.listdir(folder):
    instListShort.append(i[:-4])
replicate = 1


########                PROBABLY DONT CHANGE                ##################
alpha = 0.1
p = 0.9
deviationCrit = 2.5

       
###############                  DONT CHANGE                    ##############
instList = instListShort*replicate
instList.sort()
instListVar = []
for i in instListShort:
    instListVar.append(i[9:])
def kill():
    
    # for inst in instListShort:
    #     for rep in range(replicate):
    #         instListVar.append(''.join([str(inst),'.',str(rep)]))
    

    temp = []
    means = []
    therm = []
    meanTherm = []
    
    count = 0
    for file in os.listdir(folder):
        killTemps = parsTCTxt(''.join([folder,file]))[0][0]
        temp.append(killTemps)
        mean = np.mean(killTemps)
        means.append(mean)
        killTemp = parsTCTxt(''.join([folder,file]))[2][0]


        bound = ti.twoside.normal(killTemps,p,1-alpha)                                               #tolerance interval for each run                                                                        #list of TIs

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        
        # if bound[0][0] < killTemp-deviationCrit or bound[0][1] > killTemp+deviationCrit:          #pass if TI within acceptance criteria
        #     print(instListVar[count],'TI:',bound,'FAIL')
        # else:
        #     print(instListVar[count],'TI:',bound,'PASS')
        # killTherm = parsTCTxt(''.join([folder,file]))[3][0]
        # therm.append(killTherm)
        # mean = np.mean(killTherm)
        # meanTherm.append(mean)
        # bound = ti.twoside.normal(killTherm,p,1-alpha)
        # plt.hlines(count+10,bound[0][0],bound[0][1],lw=5)
        count += 1
    # plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.yticks(np.arange(0,len(temp)),instListVar,rotation=45)
    plt.plot(means,np.arange(0,len(means)),'o',color='r')
    # plt.vlines(killTemp+deviationCrit,0,count,'k',lw=5)
    # plt.vlines(killTemp-deviationCrit,0,count,'k',lw=5)
    # plt.plot(meanTherm,np.arange(len(means),len(instListVar)*2),'o',color='r')
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Intervals (p=',str(p),') (Heat Kill)']))
    plt.ylabel('Run')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()




    # count=0
    # for data in temp:
    #     mean_er = np.mean(data)                                                     #mean denature temp of run
    #     std_dev_er = np.std(data)                                                   #stdev of each run
    #     n = len(data)                                                               
    #     se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
    #     dof = n - 1                                                                 #degree of fredom
    #     t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
    #     moe = t_star * se                                                           #margin of error
    #     ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
    #     print(instListVar[count],'CI:',round(mean_er,3),'+/-',round(moe,4))
    #     plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
    #     plt.plot(mean_er,count,'o',color='r',ms=7)
    #     count+=1

    # plt.yticks(np.arange(0,len(temp)),instListVar)
    # plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    # plt.grid()
    # plt.xlabel('Mean Temp (c)')
    # plt.ylabel('Instrument')
    # plt.show()


def act():
    # for inst in instListShort:
    #     for rep in range(replicate):
    #         instListVar.append(''.join([str(inst),'.',str(rep)]))
    

    temp = []
    means = []
    therm = []
    meanTherm = []
    count = 0
    for file in os.listdir(folder):
        print(file)
        actTemps = parsTCTxt(''.join([folder,file]))[1][0]
        
        temp.append(actTemps)
        mean = np.mean(actTemps)
        means.append(mean)
        actTemp = parsTCTxt(''.join([folder,file]))[2][1]


        bound = ti.twoside.normal(actTemps,p,1-alpha)                                               #tolerance interval for each run                                                                        #list of TIs

        plt.hlines(count,bound[0][0],bound[0][1],lw=5)
        
        # actTherm = parsTCTxt(''.join([folder,file]))[3][0]
        # therm.append(actTherm)
        # mean = np.mean(actTherm)
        # meanTherm.append(mean)
        # bound = ti.twoside.normal(actTherm,p,1-alpha)
        # plt.hlines(count+10,bound[0][0],bound[0][1],lw=5)
        count += 1
    # plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.yticks(np.arange(0,len(temp)),instListVar,rotation=45)
    plt.plot(means,np.arange(0,len(means)),'o',color='r')
    # plt.vlines(killTemp+deviationCrit,0,count,'k',lw=5)
    # plt.vlines(killTemp-deviationCrit,0,count,'k',lw=5)
    # plt.plot(meanTherm,np.arange(len(means),len(instListVar)*2),'o',color='r')
    plt.title(''.join([str((1-alpha)*100),'% Tolerance Intervals (p=',str(p),') (Activation)']))
    plt.ylabel('Run')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()




    # count=0
    # for data in temp:
    #     mean_er = np.mean(data)                                                     #mean denature temp of run
    #     std_dev_er = np.std(data)                                                   #stdev of each run
    #     n = len(data)                                                               
    #     se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
    #     dof = n - 1                                                                 #degree of fredom
    #     t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
    #     moe = t_star * se                                                           #margin of error
    #     ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
    #     print(instListVar[count],'CI:',round(mean_er,3),'+/-',round(moe,4))
    #     plt.hlines(count,ciMult[0],ciMult[1],lw=5)                                  #plot confidence interval
    #     plt.plot(mean_er,count,'o',color='r',ms=7)
    #     count+=1

    # plt.yticks(np.arange(0,len(temp)),instListVar)
    # plt.title(''.join([str((1-alpha)*100),'% Confidence Interval']))
    # plt.grid()
    # plt.xlabel('Mean Temp (c)')
    # plt.ylabel('Instrument')
    # plt.show()


act()
kill()
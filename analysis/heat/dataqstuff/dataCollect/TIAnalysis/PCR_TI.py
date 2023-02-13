from parsTxt import parsPCRTxt
import numpy as np
import matplotlib.pyplot as plt
import toleranceinterval as ti
import os


folder = 'dataPCR/'                                                                      #folder where dave .txt files are kept

############                CHANGE THIS                                     ###################
instListShort = [15,25]                                                                         #list of instruments. must be in order that they appear in folder
replicate = 1                                                                                   #how many runs of each instrument



##############              PROBABLY DONT CHANGE            #####################
deviationCrit = 1.5                                                                             #acceptance crit
alpha = 0.05                                                                                    #1-confidence level
p = 0.9                                                                                         #reliability





########                DONT CHANGE             ##################
def denature():                                                                                     #create function to analyze denature temp
    instList = instListShort*replicate                                                              #list of total runs
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
        count += 1
        if bound[0][0] < denatTemp-deviationCrit or bound[0][1] > denatTemp+deviationCrit:          #pass if TI within acceptance criteria
            print(instListVar[0],bound,'FAIL')
        else:
            print(instListVar[0],bound,'PASS')
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.vlines(denatTemp+deviationCrit,0,count-1,'k',lw=5)
    plt.vlines(denatTemp-deviationCrit,0,count-1,'k',lw=5)
    plt.title('95% Tolerance Intervals (p=0.90)')
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
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
            print(instListVar[0],bound,'FAIL')
        else:
            print(instListVar[0],bound,'PASS')
        count += 1
        
    plt.yticks(np.arange(0,len(temp)),instListVar)
    plt.vlines(annealTemp+deviationCrit,0,count-1,'k',lw=5)
    plt.vlines(annealTemp-deviationCrit,0,count-1,'k',lw=5)
    plt.title('95% Tolerance Intervals (p=0.90)')
    plt.ylabel('Instrument')
    plt.xlabel('Temperature (c)')
    plt.grid()
    plt.show()



anneal()

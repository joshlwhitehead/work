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
import itertools


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
folder = 'tapeAdjust/'
instListShort = []
for i in os.listdir(folder):
    instListShort.append(i[:-4])
# print(instListShort)
# instListShort = np.arange(0,len(os.listdir(folder)))

replicate = 1                                                                                   #how many runs of each instrument



##############              PROBABLY DONT CHANGE            #####################
deviationCrit = 1.5                                                                             #acceptance crit
alpha = 0.1                                                                                    #1-confidence level
p = 0.9                                                                                         #reliability



def findAvgValMax(data):
    peakSamp = []
    for peak in data:
        peakSamp.append(max(peak))
    return peakSamp
def findAvgValMin(data):
    peakSamp = []
    for peak in data:
        peakSamp.append(min(peak))
    return peakSamp

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
    
    means = []
    tis = []
    total = []
    count = 0
    meanDiffs = []
    denat = []
    ann = []
    for file in os.listdir(folder):
        peakSampListHeat = parsPCRTxt(''.join([folder,file]))[0][0]                                     #collect temperatures while heating
        peakSampListCool = parsPCRTxt(''.join([folder,file]))[1][0]
        if np.mean(findAvgValMax(peakSampListCool)) > np.mean(findAvgValMax(peakSampListHeat)):
            peakSamp = findAvgValMax(peakSampListCool)
        else:
            peakSamp = findAvgValMax(peakSampListHeat)
        peakModListHeat = parsPCRTxt(''.join([folder,file]))[7][0]                                     #collect temperatures while heating
        peakModListCool = parsPCRTxt(''.join([folder,file]))[8][0]
        if np.mean(findAvgValMax(peakModListCool)) > np.mean(findAvgValMax(peakModListHeat)):
            peakMod = findAvgValMax(peakModListCool)
        else:
            peakMod = findAvgValMax(peakModListHeat)
        
        fullIndx = []
        temp = []    
        mod = []
        for peak in peakSamp:
            fullIndx.append('sample')                                                              #collect maximum (denature) temps for each cycle
        for peak in peakMod:
            fullIndx.append('model')
        temp.append(peakSamp)                                                                       #matrix of denature temps for each run
        mod.append(peakMod)
        tempLong = list(itertools.chain.from_iterable(temp))
        modLong = list(itertools.chain.from_iterable(mod))
        fullTemp = tempLong + modLong
        
        dF = pd.DataFrame({'type':fullIndx,'temp':fullTemp})
        
        try:
            # print(mod)
            m_compMult = pairwise_tukeyhsd(endog=dF['temp'], groups=dF['type'], alpha=alpha)      #use tukey method to compare runs
        except:
            print(file)
            print(mod)
            print('\n')
        # print(m_compMult.meandiffs)
        meanDiffs.append(m_compMult.meandiffs[0])
        denat.append(int(file[8:11]))
        ann.append(int(file[19:21]))
    test = {}
    for i in range(85,101,5):
        test[i] = []
    for indx,val in enumerate(denat):
        # test[val][0].append(ann[indx])
        test[val].append(meanDiffs[indx])

   
    return test
        




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
  


       
    means = []
    tis = []
    count = 0
    meanDiffs = []
    denat = []
    ann = []
    for file in os.listdir(folder):
        retVal = parsPCRTxt(''.join([folder,file]))
        peakSampList = retVal[1][0]                                     #collect temperatures while heating
        peakModList = retVal[8][0]
        peakSamp = []
        peakMod = []
        fullIndx = []
        temp = []    
        mod = [] 
        for peak in peakSampList:
            peakSamp.append(min(peak))
            fullIndx.append('sample') 
            # print(peakSamp) 
        for peak in peakModList:
            peakMod.append(min(peak))
            fullIndx.append('model')                                                           #collect maximum (denature) temps for each cycle
        temp.append(peakSamp)                                                                       #matrix of denature temps for each run
        mod.append(peakMod)
        tempLong = list(itertools.chain.from_iterable(temp))
        modLong = list(itertools.chain.from_iterable(mod))
        fullTemp = tempLong + modLong
        # print(modLong)
        dF = pd.DataFrame({'type':fullIndx,'temp':fullTemp})
        
       
        m_compMult = pairwise_tukeyhsd(endog=dF['temp'], groups=dF['type'], alpha=alpha)      #use tukey method to compare runs
        
        # print(m_compMult)
        meanDiffs.append(m_compMult.meandiffs[0])
        denat.append(int(file[8:11]))
        ann.append(int(file[19:21]))
    test = {}
    for i in range(85,101,5):
        test[i] = []
    for indx,val in enumerate(denat):
        # test[val].append(ann[indx])
        test[val].append(meanDiffs[indx])
    # for i in test.keys():
        # print(test[i])
    return test


annealVal = anneal(folder,instListShort)
denatVal = denature(folder,instListShort)



dFAnneal = pd.DataFrame(annealVal)
dFAnneal.to_csv('testAnneal.csv')
dFDenat = pd.DataFrame(denatVal)
dFDenat.to_csv('testDenat.csv')

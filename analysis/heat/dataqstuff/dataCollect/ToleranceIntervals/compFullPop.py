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


folder = 'dataPCR/'                                                                      #folder where dave .txt files are kept
instListShort = ['p_a_7','p_b_7','p_a_9','p_b_9','p_a_11','p_b_11','p_a_13','p_b_13','p_a_15','p_b_15','g_a_5','g_b_5','g_a_20','g_b_20','g_a_23','g_b_23','g_a_25','g_b_25','g_a_28','g_b_28']                                                                         #list of instruments. must be in order that they appear in folder
totalInd = ['p','g']*10
totalInd.sort(reverse=True)
# print(totalInd)
############                CHANGE THIS                                     ###################
# folder = 'cupA/'
# instListShort = ['pa7','pa9','pa11','pa13','pa15','ga5','ga20','ga23','ga25','ga28']
# totalInd = ['p','p','p','p','p','g','g','g','g','g']

# folder = 'cupB/'
# instListShort = ['pb7','pb9','pb11','pb13','pb15','gb5','gb20','gb23','gb25','gb28']
# totalInd = ['p','p','p','p','p','g','g','g','g','g']


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

    
    pgTemp = []
    pTemp = []
    gTemp = []
    pgList = []
    variance = []

    
    count = 0
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[0][0]                                     #collect temperatures while heating
        peakSamp = []
        for peak in peakSampList:
            peakSamp.append(max(peak))
            pgTemp.append(max(peak))                                                              #collect maximum (denature) temps for each cycle
            if 'p' in totalInd[count]:
                pgList.append('p')
                pTemp.append(max(peak))
            else:
                pgList.append('g')
                gTemp.append(max(peak))
        variance.append(np.var(peakSamp))
        
            
        count += 1

    dfTemp = pd.DataFrame({'Temp':pgTemp,'Type':pgList})

    # m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Type'], alpha=alpha)      #use tukey method to compare runs
    # # m_compMult = pairwise_tukeyhsd(endog=dfTot['Mean'],groups=dfTot['type'],alpha=alpha)
    # print(m_compMult)
    # formula = 'Temp ~ Type'
    # model = ols(formula, dfTemp).fit()
    # aov_table = anova_lm(model, typ=1)
    # print(aov_table)



    dfVar = pd.DataFrame({'Var':variance,'Type':totalInd})
    m_compMult = pairwise_tukeyhsd(endog=dfVar['Var'], groups=dfVar['Type'], alpha=alpha)      #use tukey method to compare runs
    # m_compMult = pairwise_tukeyhsd(endog=dfTot['Mean'],groups=dfTot['type'],alpha=alpha)
    print(m_compMult)
    formula = 'Var ~ Type'
    model = ols(formula, dfVar).fit()
    aov_table = anova_lm(model, typ=1)
    print(aov_table)
    # if stats.anderson(dfTemp['Temp'],dist='norm')[0] < stats.anderson(dfTemp['Temp'],dist='norm')[1][2]:
    #     print('data normal')
    # else:
    #     print('data not normal')
    #     print(stats.anderson(dfTemp['Temp'],dist='norm'))
        
    #     dfTemp.hist('Temp',density=True)
    #     x = np.linspace(min(dfTemp['Temp']),max(dfTemp['Temp']))
    #     plt.plot(x,stats.norm.pdf(x,loc=np.mean(dfTemp['Temp']),scale=np.std(dfTemp['Temp'])))
    #     plt.show()

    if stats.anderson(dfVar['Var'],dist='norm')[0] < stats.anderson(dfVar['Var'],dist='norm')[1][2]:
        print('data normal')
    else:
        print('data not normal')
        print(stats.anderson(dfVar['Var'],dist='norm'))
        
        dfVar.hist('Var',density=True)
        x = np.linspace(min(dfVar['Var']),max(dfVar['Var']))
        plt.plot(x,stats.norm.pdf(x,loc=np.mean(dfVar['Var']),scale=np.std(dfVar['Var'])))
        plt.show()
# denature()





def anneal():                                                                                     #create function to analyze denature temp
    instList = instListShort*replicate                                                              #list of total runs
    if replicate > 1:
        instList.sort()                                                                                 #sort instrument list to match with order in directory

    instListVar = []
    for inst in instListShort:                                                                         
        for rep in range(replicate):
            instListVar.append(''.join([str(inst),'.',str(rep)]))                                        #make list of replicates

    
    pgTemp = []
    pTemp = []
    gTemp = []
    pgList = []
    variance = []
    
    count = 0
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[1][0]                                     #collect temperatures while heating
        peakSamp = []
        for peak in peakSampList:
            peakSamp.append(max(peak))
            pgTemp.append(max(peak))                                                              #collect maximum (denature) temps for each cycle
            if 'p' in totalInd[count]:
                pgList.append('p')
                pTemp.append(max(peak))
            else:
                pgList.append('g')
                gTemp.append(max(peak))
        variance.append(np.var(peakSamp))
        
            
        count += 1

    dfTemp = pd.DataFrame({'Temp':pgTemp,'Type':pgList})

    # m_compMult = pairwise_tukeyhsd(endog=dfTemp['Temp'], groups=dfTemp['Type'], alpha=alpha)      #use tukey method to compare runs
    # # m_compMult = pairwise_tukeyhsd(endog=dfTot['Mean'],groups=dfTot['type'],alpha=alpha)
    # print(m_compMult)
    # formula = 'Temp ~ Type'
    # model = ols(formula, dfTemp).fit()
    # aov_table = anova_lm(model, typ=1)
    # print(aov_table)




    dfVar = pd.DataFrame({'Var':variance,'Type':totalInd})
    m_compMult = pairwise_tukeyhsd(endog=dfVar['Var'], groups=dfVar['Type'], alpha=alpha)      #use tukey method to compare runs
    # m_compMult = pairwise_tukeyhsd(endog=dfTot['Mean'],groups=dfTot['type'],alpha=alpha)
    print(m_compMult)
    formula = 'Var ~ Type'
    model = ols(formula, dfVar).fit()
    aov_table = anova_lm(model, typ=1)
    print(aov_table)

    if stats.anderson(dfTemp['Temp'],dist='norm')[0] < stats.anderson(dfTemp['Temp'],dist='norm')[1][2]:
        print('data normal')
    else:
        print('data not normal')
        print(stats.anderson(dfTemp['Temp'],dist='norm'))
        
        dfTemp.hist('Temp',density=True)
        x = np.linspace(min(dfTemp['Temp']),max(dfTemp['Temp']))
        plt.plot(x,stats.norm.pdf(x,loc=np.mean(dfTemp['Temp']),scale=np.std(dfTemp['Temp'])))
        plt.show()
anneal()
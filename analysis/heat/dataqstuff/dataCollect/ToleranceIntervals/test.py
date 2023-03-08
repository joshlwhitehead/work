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

    padTemps = []
    greaseTemps = []
    for i in range(len(totalInd)):
        if 'p' in [i]:
            

    
denature()
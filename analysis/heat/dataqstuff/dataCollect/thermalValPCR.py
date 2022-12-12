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



def DV():
    total = dat.DV
    instListShort = [1,2,3,4,6,7,10,13,15,25,26,27]
    instList = instListShort*3
    instList.sort()
    cupList = [3,3,3,3,3,3,3,3,3,9,9,9,8,8,8,8,8,8,10,10,10,5,5,5,5,5,5,8,8,8,5,5,5,8,8,8]
    cupListClump = [3,3,3,9,8,8,10,5,5,8,5,8]
    
    colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive','peru','maroon']

    cycle = 6
    modelMax = []
    sampleMax = []
    modelStuff = []
    sampleStuff = []
    
    
    for k in total:
        maxes = []
        maxes2 = []
        indx = []
        count = 0
        for i in k[5]:
            if i == 90:
                indx.append(count)
            count += 1



        modelNew = []
        modelLists = []
        sampleNew = []
        sampleLists = []
        count = 0
        for i in indx:
            if indx[count] != indx[-1] and i+1 == indx[count+1]:
                modelNew.append(k[4][i])
                sampleNew.append(k[2][i])
            else:
                modelLists.append(modelNew)
                sampleLists.append(sampleNew)
                sampleNew = []
                modelNew = []
            count += 1
        count = 2
        for i in modelLists[2:-1]:
            maxes.append(max(i))
            maxes2.append(max(sampleLists[count]))
            count += 1
        modelMax.append(maxes)
        sampleMax.append(maxes2)
    print(sampleMax)
DV()

                



























    
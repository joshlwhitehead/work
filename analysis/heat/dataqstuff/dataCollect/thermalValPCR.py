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
    instListShort = [1,2,3,4]
    instList = instListShort*3
    instList.sort()
    cupList = [3,3,3,3,3,3,3,3,3,9,9,9]
    cupListClump = [3,3,3,9]
    
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
    

    count = 0
    n = 0
    for i in range(len(modelMax)):
        if i == 0:
            plt.plot(modelMax[i],'k',label='model')
        else:
            plt.plot(modelMax[i],'k')
        if i == 0 or i ==3 or i == 6 or i == 9:
            plt.plot(sampleMax[i],color=colors[n],label=''.join(['adv',str(instList[i])]))
        else:
            plt.plot(sampleMax[i],color=colors[n])
        count += 1
        if count%3 == 0:
            n+=1

    plt.grid()
    plt.legend()
    plt.show()










def wet():
    total = dat.wet
    instListShort = [1,4,5,8,11,14,16,18]
    instList = instListShort*3
    instList.sort()
    cupList = [61,61,61,61,61,61,65,65,65,61,61,61,61,61,61,61,61,61,61,61,61,65,65,65]
    cupListClump = [61,61,65,61,61,61,61,65]
    
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
    
    count = 0
    n = 0
    for i in range(len(modelMax)):
        if i == 0:
            plt.plot(modelMax[i],'k',label='model')
        else:
            plt.plot(modelMax[i],'k')
        if i == 0 or i ==3 or i == 6 or i == 9 or i == 12:
            plt.plot(sampleMax[i],color=colors[n],label=''.join(['adv',str(instList[i])]))
        else:
            plt.plot(sampleMax[i],color=colors[n])
        count += 1
        if count%3 == 0:
            n+=1

    plt.grid()
    plt.legend()
    plt.show()


def both():
    return
DV()

                



























    
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

total = dat.DV
instList = [6,7,13,15,25,27]*3
instList.sort()
colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']
count = 0
n=0
for i in total:
    time = i[0]
    model = i[4]
    samp = i[2]
    # plt.close('all')
    # plt.plot(time,samp,'o-')
    # plt.plot(time,model)
    # plt.hlines(90,0,max(time),'k')
    # # plt.hlines(94,0,max(time),'k')
    # plt.show()
    peakSamp = []
    peakModel = []
    for i in range(len(samp)):
        if samp[i] >90 and samp[i]>samp[i-1] and samp[i-1]>samp[i-2] and samp[i-2]>samp[i-3] and samp[i-3]>samp[i-4] and samp[i]>samp[i+1] and samp[i+1]>samp[i+2] and samp[i+2]>samp[i+3] and samp[i+3]>samp[i+4]:
            peakSamp.append(samp[i])
        if model[i] >90 and model[i]>model[i-1] and model[i-1]>model[i-2] and model[i]>model[i+1] and model[i+1]>model[i+2]:
            peakModel.append(model[i])

    
    plt.plot(peakSamp[:-3],label=instList[count])
    plt.plot(peakModel)
    count += 1
    # print(len(peakSamp[:-1]))
plt.legend()
plt.show()




            # plt.plot(sampleMax[i],color=colors[n],label=''.join(['adv',str(instList[i])]))
        
            
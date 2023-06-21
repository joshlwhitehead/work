"""attempt to analyze pcr melts. dataToVar no longer used.
DO NOT USE! this script uses data based on a semi-arbitrary window rather than using raw data to find when melt starts/stops"""

import numpy as np
import obsoleteDataProcessing.dataToVar as dat
import matplotlib.pyplot as plt
import pandas as pd
# from thermalCompareQuant import listAvg, listStd, listRms, listGrad, interppp
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
from statsmodels.graphics.factorplots import interaction_plot
# import statsmodels.api as sm
import os

# for i in os.listdir('data/18Jan2023'):
#     print(i)
alpha=0.05
total = dat.proposeModb
instListShort = ['104post_1.31','104post_1.31b','107post_1.31','108post_1.31','108post_1.31b','114post_1.31','13post_1.31','15post_1.31']



# plt.plot(total[0],total[2])
# plt.plot(total[2][4])
# plt.plot(total[2][2])
    # for i in total:
    #     time = i[0]
    #     model = i[4]
    #     samp = i[2]

# plt.grid()
# plt.show()'

"""         DEFINE WINDOW           """
def melt(time,model,samp):
    meltTemp = []
    meltTime = []
    meltModel = []

    for u in range(len(time)):
        if time[u] > 590 and time[u] < 660 and samp[u] > 65 and samp[u] < 90:
            meltTemp.append(samp[u])
            meltTime.append(time[u])
            meltModel.append(model[u])
    meltTemp = np.array(meltTemp)
    meltTime = np.array(meltTime)
    meltModel = np.array(meltModel)
    a,b = np.polyfit(meltTime,meltTemp,1)
    c,d = np.polyfit(meltTime,meltModel,1)
    
    plt.plot(meltTime,meltTemp,'o')
    plt.plot(meltTime,a*meltTime+b)
    plt.plot(meltTime,meltModel,'o')
    plt.plot(meltTime,c*meltTime+d)
    plt.grid()
    plt.show()

    cc,dd = np.polyfit(meltModel,meltTime,1)
    return (a,b),(c,d),(cc,dd)



def tmShift(expected,time,model,samp):
    a = melt(time,model,samp)[0][0]
    b = melt(time,model,samp)[0][1]
    cc = melt(time,model,samp)[2][0]
    dd = melt(time,model,samp)[2][1]
    

    modTime = cc*expected+dd
    realTemp = a*modTime+b
    return realTemp

for i in total:
    print(tmShift(82,i[0],i[4],i[2]))




    # def r2(y,fit):
    #     st = sum((y-np.average(y))**2)
    #     sr = sum((y-fit)**2)
    #     r2 = 1-sr/st
    #     return r2


    # print(r2(y,fit))

  
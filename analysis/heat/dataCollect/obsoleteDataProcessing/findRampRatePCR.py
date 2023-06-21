"""NON FUNCTIONAL!
script to analyze ramp rates for PCR
this method looks for certain coordinates rather than detecting when the ramping starts/ends"""

import numpy as np
import matplotlib.pyplot as plt
# import obsoleteDataProcessing.dataToVar as dat
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
import pandas as pd
import os
folder = 'data/18Jan2023'
total = dat.proposeModb         #dataToVar no longer in use. use alternate approach to parse/format data
# for i in total:
#     plt.plot(i[0],i[2])
# plt.grid()
# plt.show()

def heatRamp(time,samp):
    count = 0
    count2 = 0
    tempVal = []
    timeVal = []
    for i in (range(len(samp))):
        if len(tempVal) == 0:
            tempVal.append([])
            timeVal.append([])
        elif samp[i]>65 and samp[i]<85 and samp[count-1]<samp[i] and time[i]>350 and time[i]<550:
            if len(tempVal[count2]) == 0 or samp[i]>tempVal[count2][-1]:
                tempVal[count2].append(samp[i])
                timeVal[count2].append(time[i])
            elif samp[i]<tempVal[count2][-1]:
                count2+=1
                tempVal.append([])
                timeVal.append([])
                tempVal[count2].append(samp[i])
                timeVal[count2].append(time[i])
        count +=1

    rr = []
    for i in range(len(tempVal)):
        rr.append((tempVal[i][-1]-tempVal[i][0])/(timeVal[i][-1]-timeVal[i][0]))
    return rr



def coolRamp(time,samp):
    count = 0
    count2 = 0
    tempVal = []
    timeVal = []
    for i in (range(len(samp))):
        if len(tempVal) == 0:
            tempVal.append([])
            timeVal.append([])
        elif samp[i]>65 and samp[i]<85 and samp[count-1]>samp[i]:
            if len(tempVal[count2]) == 0 or samp[i]<tempVal[count2][-1]:
                tempVal[count2].append(samp[i])
                timeVal[count2].append(time[i])
            elif samp[i]>tempVal[count2][-1]:
                count2+=1
                tempVal.append([])
                timeVal.append([])
                tempVal[count2].append(samp[i])
                timeVal[count2].append(time[i])
        count +=1

    rr = []
    for i in range(len(tempVal)):
        rr.append((tempVal[i][-1]-tempVal[i][0])/(timeVal[i][-1]-timeVal[i][0]))
    return rr



def testNorm(dist,dF,label):                            #data must be dataframe
    if stats.anderson(dF.rr,dist=dist)[0] < stats.anderson(dF.rr,dist=dist)[1][2]:
        print(''.join([label,' data ',dist]))
    else:
        print(''.join([label,' data not ',dist]))
        print(stats.anderson(dF.rr,dist=dist))
        x = np.linspace(min(dF.rr),max(dF.rr))
        dF.hist('rr',density=True)
        plt.plot(x,stats.norm.pdf(x,loc=np.mean(dF.rr),scale=np.std(dF.rr)))
        plt.show()



def CI(data):
    mean_er = np.mean(data) # sample mean
    std_dev_er = np.std(data, ddof=1) # sample standard devialtion
    se = std_dev_er / np.sqrt(len(data)) # standard error
    n = len(data) # sample size, n
    dof = n - 1 # degrees of freedom
    t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    moe = t_star * se # margin of error
    ci = np.array([mean_er - moe, mean_er + moe])
    return ci




count = 0
indep = []
tot = []
for i in total:
    data = i
    alpha = 0.05

    # plt.plot(data[2])
    # plt.plot(data[0],data[4])
    # plt.grid()
    # plt.show()

    time = data[0][550:1950]
    samp = data[2][550:1950]


    """HEATING"""
    a = heatRamp(time,samp)
    
    for i in a:
        indep.append(os.listdir(folder)[count])
        tot.append(i)

    
    dfA = pd.DataFrame({'type':['a']*len(a),'rr':a})
   
    dist = 'norm'
    

    # testNorm(dist,dfA,'')

    count += 1
dFTot = pd.DataFrame({'type':indep,'rr':tot})
m_compMM = pairwise_tukeyhsd(endog=dFTot.rr, groups=dFTot.type, alpha=alpha)
print(m_compMM)

dFTot.boxplot('rr',by='type',rot=10)
# plt.set_xticks(rotatation=45)
plt.show()


print(CI(dfA.rr))

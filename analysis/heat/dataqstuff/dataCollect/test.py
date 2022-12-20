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

alpha=0.05
total = dat.wet
instListShort = [10,12,17]
instList = instListShort*3
instList.sort()
# colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']
count = 0
n=0
means=[]
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
    plt.plot(peakModel[:len(peakSamp[:-3])],'k')
    
    count += 1
    # print(len(peakSamp[:-1]))
    mean = np.mean(peakSamp[:-3])
    means.append(mean)
plt.grid()
plt.legend()
plt.show()

dfAnova = pd.DataFrame({'Instrument':instList,'Mean':means})
if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:
        print('data are normal')
else:
    print('data are not normal')

m_comp = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], alpha=alpha)
print(m_comp)
dfAnova.boxplot('Mean',by='Instrument')
plt.show()

clumpMeans = [means[i:i+3] for i in range(0,len(means),3)]
clumpInst = [instList[i:i+3] for i in range(0,len(instList),3)]
    
limitLow = 105 - 3
limitHigh = 105 + 3
count = 0
probs = []
for i in clumpMeans:
    mean_er = np.mean(i) # sample mean
    std_dev_er = np.std(i, ddof=1) # sample standard devialtion
    se = std_dev_er / np.sqrt(len(i)) # standard error
    n = len(i) # sample size, n
    dof = n - 1 # degrees of freedom
    t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    moe = t_star * se # margin of error
    ci = np.array([mean_er - moe, mean_er + moe])
    t_limitLow = (limitLow - mean_er) / se
    t_limitHigh = (limitHigh - mean_er) / se
    prLow = stats.t.cdf(t_limitLow, dof)
    prHigh = 1 - stats.t.cdf(t_limitHigh, dof)
    probs.append(prHigh+prLow)
    

    plt.hlines(count,ci[0],ci[1],lw=5)
    plt.plot(mean_er,count,'o',color='r',ms=7)
    count+=1

plt.yticks(np.arange(0,len(clumpMeans)),instListShort)
plt.grid()
plt.xlabel('Mean Temp (c)')
plt.ylabel('AdvB')
plt.show()


plt.plot(probs,'o')
plt.grid()
plt.xlabel('AdvB')
plt.ylabel('Prob Mean < Model-5c')
plt.xticks(np.arange(0,len(clumpMeans)),instListShort)
plt.show()
print(probs)



    
            
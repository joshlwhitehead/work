"""calculate tolerance area for complex populations"""

import numpy as np
import matplotlib.pyplot as plt
from confidenceFun import CI,TI
from PCR_cycle_time import cycleTimeFun
import os









folder = 'betaAlpha/'

instlist = np.arange(0,len(os.listdir(folder)))

folder2 = 'betaBeta/'
# folder2 = 'oldButUseful/tape/'
instList2 = np.arange(0,len(os.listdir(folder2)))

folder3 = 'alphaAlpha/'
instList3 = np.arange(0,len(os.listdir(folder3)))

alpha = 0.1
p = 0.9
def fullCI(means,stdevs):    

    mean = np.mean(means)

    return mean,means,stdevs

def toleranceArea(means,stdevs):
    meanMeans = np.mean(means)
    meanStd = np.mean(stdevs)
    tiMean = TI(means,alpha,p)
    tiStd = TI(stdevs,alpha,p)
    if tiStd[0] < 0:
        tiStd[0] = 0
    if tiMean[0] < 0:
        tiMean[0] = 0
    return {'meanMeans':meanMeans,'meanStd':meanStd,
            'tiMean':tiMean,'tiStd':tiStd}
    
means2 = cycleTimeFun(folder2,instList2)[0]
std2 = cycleTimeFun(folder2,instList2)[1]

meanMeans2 = toleranceArea(means2,std2)['meanMeans']
meanStd2 = toleranceArea(means2,std2)['meanStd']

ciMean2 = toleranceArea(means2,std2)['tiMean']
ciStd2 = toleranceArea(means2,std2)['tiStd']


means = cycleTimeFun(folder,instlist)[0]
std = cycleTimeFun(folder,instlist)[1]

meanMeans = toleranceArea(means,std)['meanMeans']
meanStd = toleranceArea(means,std)['meanStd']

ciMean = toleranceArea(means,std)['tiMean']
ciStd = toleranceArea(means,std)['tiStd']


means3 = cycleTimeFun(folder3,instList3)[0]
std3 = cycleTimeFun(folder3,instList3)[1]

meanMeans3 = toleranceArea(means3,std3)['meanMeans']
meanStd3 = toleranceArea(means3,std3)['meanStd']

ciMean3 = toleranceArea(means3,std3)['tiMean']
ciStd3 = toleranceArea(means3,std3)['tiStd']





plt.plot(means2,std2,'o',color='g',label='Beta units - beta model')
plt.hlines(meanStd2,ciMean2[0],ciMean2[1],lw=4,color='g')
plt.vlines(meanMeans2,ciStd2[0],ciStd2[1],lw=4,color='g')
plt.plot(meanMeans2,meanStd2,'o',color='r')
plt.plot(means,std,'o',color='tab:blue',label='Beta units - alpha model')
plt.hlines(meanStd,ciMean[0],ciMean[1],lw=4,color='tab:blue')
plt.vlines(meanMeans,ciStd[0],ciStd[1],lw=4,color='tab:blue')
plt.plot(meanMeans,meanStd,'o',color='r')

plt.plot(means3,std3,'o',color='purple',label='Alpha units - alpha model')
plt.hlines(meanStd3,ciMean3[0],ciMean3[1],lw=4,color='purple')
plt.vlines(meanMeans3,ciStd3[0],ciStd3[1],lw=4,color='purple')
plt.plot(meanMeans3,meanStd3,'o',color='r')
plt.title('90-90 Tolerance Area for PCR Cycle Times')
plt.xlabel('Mean Cycle Time (sec)')
plt.ylabel('Standard Deviation (sec)')
plt.legend()
plt.grid()
plt.show()



from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import pandas as pd
totalstd = []
types = []
for i in means:
    totalstd.append(i)
    types.append('beta')
for i in means2:
    totalstd.append(i)
    types.append('verification')

dF = pd.DataFrame({'type':types,'std':totalstd})

formula = 'std ~ type'
model = ols(formula, dF).fit()
aov_table = anova_lm(model, typ=1)
print(aov_table)


m_compMult = pairwise_tukeyhsd(endog=dF['std'],groups=dF['type'],alpha=alpha)
print(m_compMult)





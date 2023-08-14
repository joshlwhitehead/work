"""calculate tolerance area for complex populations"""

import numpy as np
import matplotlib.pyplot as plt
from confidenceFun import CI,TI
from PCR_cycle_time import cycleTimeFun
import os









folder = 'betaAlpha2Maybe/'

instlist = np.arange(0,len(os.listdir(folder)))

folder2 = 'betaBeta/'
# folder2 = 'oldButUseful/tape/'
instList2 = np.arange(0,len(os.listdir(folder2)))

folder3 = 'alphaAlpha2Maybe/'
instList3 = np.arange(0,len(os.listdir(folder3)))

alpha = 0.1
def fullCI(folder,instlistshort):
    
    means = cycleTimeFun(folder,instlistshort)[0]
    # cis = np.array(cycleTimeFun(folder,instlistshort)[1]).T
    stdevs = cycleTimeFun(folder,instlistshort)[1]
    

    mean = np.mean(means)
    meanCI = CI(means,alpha)
    ciLCI = [0,0]#CI(ciL,alpha)
    ciRCI = [0,0]#CI(ciR,alpha)
    

    # plt.scatter(mean,0)
    # plt.hlines(0,meanCI[0],meanCI[1])
    # plt.hlines(1,ciLCI[0],ciLCI[1],color='r',lw=5)
    # plt.hlines(1,ciRCI[0],ciRCI[1],color='green')
    # plt.grid()
    # plt.show()

    return mean,ciLCI[0],ciRCI[1],means,stdevs

# meanAnneal3 = anneal(folder3,[1])[0]
# stdAnneal3 = anneal(folder3,[1])[2]
# print(meanAnneal3)
means2 = fullCI(folder2,instList2)[3]
std2 = fullCI(folder2,instList2)[4]

meanMeans2 = np.mean(means2)
meanStd2 = np.mean(std2)

ciMean2 = TI(means2,alpha,.90)
ciStd2 = TI(std2,alpha,.90)
if ciStd2[0] < 0:
    ciStd2[0] = 0

means = fullCI(folder,instlist)[3]
std = fullCI(folder,instlist)[4]

meanMeans = np.mean(means)
meanStd = np.mean(std)

# ciMean = CI(means,.01)
# cistd = CI(std,.05)
ciMean = TI(means,alpha,.90)
ciStd = TI(std,alpha,.90)
if ciStd[0] < 0:
    ciStd[0] = 0


means3 = fullCI(folder3,instList3)[3]
std3 = fullCI(folder3,instList3)[4]

meanMeans3 = np.mean(means3)
meanStd3 = np.mean(std3)

ciMean3 = TI(means3,alpha,.90)
ciStd3 = TI(std3,alpha,.90)
if ciStd3[0] < 0:
    ciStd3[0] = 0

distFromMean = []
distFromMean2 = []
distFromMean3 = []
for i in range(len(means)):
    distFromMean.append(np.sqrt((means[i]-meanMeans)**2+(std[i]-meanStd)**2))
for i in range(len(means2)):
    distFromMean2.append(np.sqrt((means2[i]-meanMeans2)**2+(std2[i]-meanStd2)**2))
for i in range(len(means3)):
    distFromMean3.append(np.sqrt((means3[i]-meanMeans3)**2+(std3[i]-meanStd3)**2))

s1 = np.mean(distFromMean)
s2 = np.mean(distFromMean2)
s3 = np.mean(distFromMean3)

meanDiff = np.sqrt((meanMeans-meanMeans2)**2+(meanStd-meanStd2)**2)

SE = np.sqrt(s1**2/len(means)+s2**2/len(means2))
print(''.join([str(meanDiff),'+/-',str(6*SE)]))

print(meanMeans,ciMean[1]-meanMeans)
print(meanStd,ciStd[1]-meanStd)
# plt.plot(means,np.ones(len(means))*.7,'o',color='k')
# plt.plot(np.ones(len(std))*53,std,'o',color='k')
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
# plt.plot(meanAnneal3,stdAnneal3,'o',color='purple',label='roomTemp')
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





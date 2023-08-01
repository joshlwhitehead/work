"""calculate tolerance area for complex populations"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from PCR_TI_USE import anneal,denature
from melt_rampRate_USE import melting
from confidenceFun import CI,TI
from PCR_rampRate_USE import heating,cooling
import os

temp = 4


folder = 'betaAlpha/'

instlist = np.arange(0,len(os.listdir(folder)))

folder2 = 'alphaAlpha/'
# folder2 = 'oldButUseful/tape/'
instList2 = np.arange(0,len(os.listdir(folder2)))

# folder3 = 'data/'

alpha = 0.1
def fullCI(folder,instlistshort):
    if temp == 0:
        means = denature(folder,instlistshort)[0]
        cis = np.array(denature(folder,instlistshort)[1]).T
        variances = denature(folder,instlistshort)[3]
    elif temp == 1:
        means = anneal(folder,instlistshort)[0]
        cis = np.array(anneal(folder,instlistshort)[1]).T
        variances = anneal(folder,instlistshort)[3]
    elif temp == 2:
        means = melting(folder,alpha,.9)[0]
        variances = melting(folder,alpha,.9)[1]
        cis = 0
    elif temp == 3:
        means = heating(folder,alpha,.9)[0]
        variances = heating(folder,alpha,.9)[1]
        cis = 0
    elif temp == 4:
        means = cooling(folder,alpha,.9)[0]
        variances = cooling(folder,alpha,.9)[1]
        cis = 0

    # ciL = cis[0]
    # ciR = cis[1]



    
    
    







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

    return mean,ciLCI[0],ciRCI[1],means,cis,variances

# meanAnneal3 = anneal(folder3,[1])[0]
# varAnneal3 = anneal(folder3,[1])[2]
# print(meanAnneal3)
means2 = fullCI(folder2,instList2)[3]
var2 = fullCI(folder2,instList2)[5]

meanMeans2 = np.mean(means2)
meanVar2 = np.mean(var2)

# ciMean = CI(means,.01)
# ciVar = CI(var,.05)
ciMean2 = TI(means2,alpha,.90)
ciVar2 = TI(var2,alpha,.90)
if ciVar2[0] < 0:
    ciVar2[0] = 0

means = fullCI(folder,instlist)[3]
var = fullCI(folder,instlist)[5]

meanMeans = np.mean(means)
meanVar = np.mean(var)

# ciMean = CI(means,.01)
# ciVar = CI(var,.05)
ciMean = TI(means,alpha,.90)
ciVar = TI(var,alpha,.90)
if ciVar[0] < 0:
    ciVar[0] = 0


distFromMean = []
distFromMean2 = []
for i in range(len(means)):
    distFromMean.append(np.sqrt((means[i]-meanMeans)**2+(var[i]-meanVar)**2))
for i in range(len(means2)):
    distFromMean2.append(np.sqrt((means2[i]-meanMeans2)**2+(var2[i]-meanVar2)**2))

s1 = np.mean(distFromMean)
s2 = np.mean(distFromMean2)

meanDiff = np.sqrt((meanMeans-meanMeans2)**2+(meanVar-meanVar2)**2)

SE = np.sqrt(s1**2/len(means)+s2**2/len(means2))
print(''.join([str(meanDiff),'+/-',str(6*SE)]))

print(meanMeans,ciMean[1]-meanMeans)
print(meanVar,ciVar[1]-meanVar)
# plt.plot(means,np.ones(len(means))*.7,'o',color='k')
# plt.plot(np.ones(len(var))*53,var,'o',color='k')
plt.plot(means2,var2,'o',color='g',label='V units - alpha model')
plt.hlines(meanVar2,ciMean2[0],ciMean2[1],lw=4,color='g')
plt.vlines(meanMeans2,ciVar2[0],ciVar2[1],lw=4,color='g')
plt.plot(meanMeans2,meanVar2,'o',color='r')
plt.plot(means,var,'o',color='tab:blue',label='Beta units - alpha model')
plt.hlines(meanVar,ciMean[0],ciMean[1],lw=4,color='tab:blue')
plt.vlines(meanMeans,ciVar[0],ciVar[1],lw=4,color='tab:blue')
plt.plot(meanMeans,meanVar,'o',color='r')
# plt.plot(meanAnneal3,varAnneal3,'o',color='purple',label='roomTemp')
plt.title('Tolerance Area for Complex Populations')
plt.xlabel('Mean Ramp Rate (c/sec)')
plt.ylabel('Standard Deviation (c/sec)')
plt.legend()
plt.grid()
plt.show()



from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import pandas as pd
totalVar = []
types = []
for i in means:
    totalVar.append(i)
    types.append('beta')
for i in means2:
    totalVar.append(i)
    types.append('verification')

dF = pd.DataFrame({'type':types,'var':totalVar})

formula = 'var ~ type'
model = ols(formula, dF).fit()
aov_table = anova_lm(model, typ=1)
print(aov_table)


m_compMult = pairwise_tukeyhsd(endog=dF['var'],groups=dF['type'],alpha=alpha)
print(m_compMult)





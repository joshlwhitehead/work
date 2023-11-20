"""calculate tolerance area for complex populations"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from PCR_TI_USE import anneal,denature
from melt_rampRate_USE import melting
from confidenceFun import CI,TI
from PCR_rampRate_USE import heating,cooling
from TC_TI_USE import kill,act
import os
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
temp = 1
folders = []
instListList = []
bigFolder = 'sydInf4'
for i in os.listdir(bigFolder):
    
    folders.append(''.join([bigFolder,'/',i,'/']))
    instListList.append(np.arange(0,len(os.listdir(''.join([bigFolder,'/',i])))))

folder = folders[0]

instlist = instListList[0]

folder2 = folders[1]

# folder2 = 'oldButUseful/tape/'
instList2 = instListList[1]

# folder3 = 'data/'

alpha = 0.1
p = 0.9
def fullCI(folder,instlistshort):
    if temp == 0:
        means = act(folder,instlistshort)[0]
        stdevs = act(folder,instlistshort)[1]
    elif temp == 1:
        means = kill(folder,instlistshort)[0]
        stdevs = kill(folder,instlistshort)[1]
    
    mean = np.mean(means)  
    
    return mean,means,stdevs
def fullCITherm(folder,instlistshort):
    if temp == 0:
        means = act(folder,instlistshort)[2]
        stdevs = act(folder,instlistshort)[3]
    elif temp == 1:
        means = kill(folder,instlistshort)[2]
        stdevs = kill(folder,instlistshort)[3]
    
    mean = np.mean(means)  
    
    return mean,means,stdevs

def condense(fold,list):
    means = fullCI(fold,list)[1]
    std  = fullCI(fold,list)[2]
    meanMeans = np.mean(means)
    meanStd = np.mean(std)
    tiMean = TI(means,alpha,p)
    tiStd = TI(std,alpha,p)
    if tiStd[0] < 0:
        tiStd[0] = 0
    return means,std,meanMeans,meanStd,tiMean,tiStd
# means2 = fullCI(folder2,instList2)[1]
# var2 = fullCI(folder2,instList2)[2]

# meanMeans2 = np.mean(means2)
# meanVar2 = np.mean(var2)
# means = fullCI(folder,instlist)[1]
# var = fullCI(folder,instlist)[2]
# ciMean = CI(means,.01)
# ciVar = CI(var,.05)
# ciMean2 = TI(means2,alpha,.90)
# ciVar2 = TI(var2,alpha,.90)
# if ciVar2[0] < 0:
#     ciVar2[0] = 0



# meanMeans = np.mean(means)
# meanVar = np.mean(var)

# ciMean = CI(means,.01)
# ciVar = CI(var,.05)
# ciMean = TI(means,alpha,.90)
# ciVar = TI(var,alpha,.90)
# if ciVar[0] < 0:
#     ciVar[0] = 0


# distFromMean = []
# distFromMean2 = []
# for i in range(len(means)):
#     distFromMean.append(np.sqrt((means[i]-meanMeans)**2+(var[i]-meanVar)**2))
# for i in range(len(means2)):
#     distFromMean2.append(np.sqrt((means2[i]-meanMeans2)**2+(var2[i]-meanVar2)**2))

# s1 = np.mean(distFromMean)
# s2 = np.mean(distFromMean2)

# meanDiff = np.sqrt((meanMeans-meanMeans2)**2+(meanVar-meanVar2)**2)

# # SE = np.sqrt(s1**2/len(means)+s2**2/len(means2))
# # print(''.join([str(meanDiff),'+/-',str(6*SE)]))

# print(meanMeans,ciMean[1]-meanMeans)
# print(meanVar,ciVar[1]-meanVar)
# plt.plot(means,np.ones(len(means))*.7,'o',color='k')
# plt.plot(np.ones(len(var))*53,var,'o',color='k')



def plots(folder,list,color):
    data = condense(folder,list)
    means = data[0]
    std = data[1]
    meanMeans = data[2]
    meanStd = data[3]
    tiMean = data[4]
    tiStd = data[5]

    plt.plot(means,std,'o',color=color,label=folder[len(bigFolder)+1:-1])
    plt.hlines(meanStd,tiMean[0],tiMean[1],lw=4,color=color)
    plt.vlines(meanMeans,tiStd[0],tiStd[1],lw=4,color=color)
    plt.plot(meanMeans,meanStd,'o',color='k')

for indx,val in enumerate(folders[:]):
    print(val)
    plots(val,instListList[indx],colors[indx])


# b = condense(folders[1],instListList[1])
# a = condense(folders[0],instListList[0])
# means2 = b[0]
# var2 = b[1]
# meanMeans2 = b[2]
# meanVar2 = b[3]
# ciMean2 = b[4]
# ciVar2 = b[5]
# means = a[0]
# var = a[1]
# meanMeans = a[2]
# meanVar = a[3]
# ciMean = a[4]
# ciVar = a[5]

# plt.plot(means2,var2,'o',color='g',label='Heat Spreader Thermistor')
# plt.hlines(meanVar2,ciMean2[0],ciMean2[1],lw=4,color='g')
# plt.vlines(meanMeans2,ciVar2[0],ciVar2[1],lw=4,color='g')
# plt.plot(meanMeans2,meanVar2,'o',color='r')

# plt.plot(means,var,'o',color='tab:blue',label='Cup Thermistor')
# plt.hlines(meanVar,ciMean[0],ciMean[1],lw=4,color='tab:blue')
# plt.vlines(meanMeans,ciVar[0],ciVar[1],lw=4,color='tab:blue')
# plt.plot(meanMeans,meanVar,'o',color='r')
# plt.plot(meanAnneal3,varAnneal3,'o',color='purple',label='roomTemp')
if temp == 0:
    plt.title('Activation Tolerance Area')
elif temp == 1:
    plt.title('Heat Kill Tolerance Area')
plt.xlabel('Mean Temp (c)')
plt.ylabel('Standard Deviation (c)')
plt.legend()
plt.grid()
plt.show()



# from statsmodels.stats.multicomp import pairwise_tukeyhsd
# from statsmodels.stats.anova import anova_lm
# from statsmodels.formula.api import ols
# import pandas as pd
# totalVar = []
# types = []
# for i in means:
#     totalVar.append(i)
#     types.append('beta')
# for i in means2:
#     totalVar.append(i)
#     types.append('verification')

# dF = pd.DataFrame({'type':types,'var':totalVar})

# formula = 'var ~ type'
# model = ols(formula, dF).fit()
# aov_table = anova_lm(model, typ=1)
# print(aov_table)


# m_compMult = pairwise_tukeyhsd(endog=dF['var'],groups=dF['type'],alpha=alpha)
# print(m_compMult)





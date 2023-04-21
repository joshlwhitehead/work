import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from PCR_TI_USE import anneal,denature
from confidenceFun import CI,TI
import os


folder = 'justin/'

instlist = np.arange(0,len(os.listdir(folder)))

folder2 = 'padVpaste/'
instList2 = ['w86_7','w87_7','w86_9','w87_9','w86_11','w87_11','w86_13','w87_13','w86_15','w87_15','w86_5','w87_5','w86_20','w87_20','w86_23','w87_23','w86_25','w87_25','w86_28','w87_28']

alpha = 0.1
def fullCI(folder,instlistshort):
    means = anneal(folder,instlistshort)[0]
    cis = np.array(anneal(folder,instlistshort)[1]).T
    variances = anneal(folder,instlistshort)[2]

    ciL = cis[0]
    ciR = cis[1]



    
    
    







    mean = np.mean(means)
    meanCI = CI(means,alpha)
    ciLCI = CI(ciL,alpha)
    ciRCI = CI(ciR,alpha)
    

    # plt.scatter(mean,0)
    # plt.hlines(0,meanCI[0],meanCI[1])
    # plt.hlines(1,ciLCI[0],ciLCI[1],color='r',lw=5)
    # plt.hlines(1,ciRCI[0],ciRCI[1],color='green')
    # plt.grid()
    # plt.show()

    return mean,ciLCI[0],ciRCI[1],means,cis,variances


means2 = fullCI(folder2,instList2)[3]
var2 = fullCI(folder2,instList2)[5]

meanMeans2 = np.mean(means2)
meanVar2 = np.mean(var2)

# ciMean = CI(means,.01)
# ciVar = CI(var,.05)
ciMean2 = TI(means2,.1,.90)
ciVar2 = TI(var2,.1,.90)


means = fullCI(folder,instlist)[3]
var = fullCI(folder,instlist)[5]

meanMeans = np.mean(means)
meanVar = np.mean(var)

# ciMean = CI(means,.01)
# ciVar = CI(var,.05)
ciMean = TI(means,.1,.90)
ciVar = TI(var,.1,.90)

print(meanMeans,ciMean[1]-meanMeans)
print(meanVar,ciVar[1]-meanVar)
# plt.plot(means,np.ones(len(means))*.7,'o',color='k')
# plt.plot(np.ones(len(var))*53,var,'o',color='k')
plt.plot(means2,var2,'o',color='k',label='wet fill')
plt.hlines(meanVar2,ciMean2[0],ciMean2[1],lw=5)
plt.vlines(meanMeans2,ciVar2[0],ciVar2[1],lw=5)
plt.plot(meanMeans2,meanVar2,'o',color='r')
plt.plot(means,var,'o',color='green',label='tape')
plt.hlines(meanVar,ciMean[0],ciMean[1],lw=5)
plt.vlines(meanMeans,ciVar[0],ciVar[1],lw=5)
plt.plot(meanMeans,meanVar,'o',color='r')
plt.title('Tolerance Area for Population of Populations')
plt.xlabel('Possible Mean Temp (c)')
plt.ylabel('Possible Variance')
plt.legend()
plt.grid()
plt.show()



from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import pandas as pd
totalVar = []
types = []
for i in var:
    totalVar.append(i)
    types.append('tape')
for i in var2:
    totalVar.append(i)
    types.append('wet fill')

dF = pd.DataFrame({'type':types,'var':totalVar})

formula = 'var ~ type'
model = ols(formula, dF).fit()
aov_table = anova_lm(model, typ=1)
print(aov_table)


m_compMult = pairwise_tukeyhsd(endog=dF['var'],groups=dF['type'],alpha=alpha)
print(m_compMult)

# plt.show()



# x = np.linspace(min(var),max(var))
# plt.hist(var,density=True)
# plt.plot(x,t.pdf(x,loc=np.mean(var),scale=np.std(var),df=len(var)-1))
# plt.show()





# print(fullCI(folder2,instList2)[5])

# for i in range(len(fullCI(folder2,instList2)[3])):
#     plt.hlines(i,fullCI(folder2,instList2)[4][0][i],fullCI(folder2,instList2)[4][1][i],lw=5)
#     plt.plot(fullCI(folder2,instList2)[3][i],i,'o',color='r')
# plt.hlines(-1,fullCI(folder2,instList2)[1],fullCI(folder2,instList2)[2])

# plt.yticks(np.arange(0,len(fullCI(folder2,instList2)[3])),instList2)
# plt.grid()

# plt.show()


# plt.hlines(0,fullCI(folder,instlist)[1],fullCI(folder,instlist)[2],lw=5)

# plt.hlines(1,fullCI(folder2,instList2)[1],fullCI(folder2,instList2)[2],lw=5)
# plt.plot(fullCI(folder,instlist)[0],0,'o',color='r')
# plt.plot(fullCI(folder2,instList2)[0],1,'o',color='r')
# # plt.yticks([0,1],['No-Recess','Recess'])
# plt.title(''.join([str((1-alpha)*100),'% Confidence Interval of the Mean']))
# plt.xlabel('Temperature (c)')
# plt.ylabel('')
# plt.grid()
# plt.show()
# n1 = len(instlist)
# n2 = len(instList2)

# t1 = t.ppf(1.0 - 0.5 * alpha,n1-1)
# t2 = t.ppf(1-.5*alpha,n2-1)

# s1 = (fullCI(folder,instlist)[0] - fullCI(folder,instlist)[1])*np.sqrt(len(instlist))/t1
# s2 = (fullCI(folder2,instList2)[0] - fullCI(folder2,instList2)[1])*np.sqrt(len(instList2))/t2

# SE = np.sqrt(s1**2/n1+s2**2/n2)

# dof = (s1**2/n1+s2**2/n2)**2/((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))

# tStar = t.ppf(1-.5*alpha,dof)
# moe = SE*tStar
# meanDiff = fullCI(folder,instlist)[0] - fullCI(folder2,instList2)[0]

# print(meanDiff-moe,meanDiff+moe)





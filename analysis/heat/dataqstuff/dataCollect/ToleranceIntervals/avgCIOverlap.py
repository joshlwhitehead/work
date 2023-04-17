import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.stats import t
from PCR_TI import anneal, denature


folder = 'padVpaste/'
folder2 = 'tape/'

instList = np.arange(0,len(os.listdir(folder)))
instList2 = np.arange(0,len(os.listdir(folder2)))

# print(len(instList))
overlap = 0
cis2 = anneal(folder2,instList2)
cis = anneal(folder,instList)


def CI(data,alpha):
    mean_er = np.mean(data)                                                     #mean denature temp of run
    std_dev_er = np.std(data)                                                   #stdev of each run
    n = len(data)                                                               
    se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
    dof = n - 1                                                                 #degree of fredom
    t_star = t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
    moe = t_star * se                                                           #margin of error
    ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
    print('CI:',round(mean_er,3),'+/-',round(moe,4))
    return (ciMult)
cisLeft = np.array([item[0] for item in cis])
cis2Right = np.array([item[1] for item in cis2])
cisRight = np.array([item[1] for item in cis])
cis2Left = np.array([item[0] for item in cis2])

def overlap():

    # print(cisLeft)

    for i in range(len(cisLeft)):
        for u in range(len(cis2Right)):
            if cis2Right[u] - cisLeft[i] > 0:
                overlap += (cis2Right[u]-cisLeft[i])

    totalCi = 0
    for i in cis:
        totalCi += i[1]-i[0]
    for i in cis2:
        totalCi += i[1]-i[0]





    # print(overlap/totalCi)


meanMeans = []
for i in cis:
    meanMeans.append((i[0]+i[1])/2)
meanMeans2 = []
for i in cis2:
    meanMeans2.append((i[0]+i[1])/2)

# CI(cisLeft,.05)
# CI(meanMeans,.05)
# CI(cisRight,.05)

# print()

# CI(cis2Left,.05)
# CI(meanMeans2,.05)
# CI(cis2Right,.05)

alpha = .05

plt.hlines(0,np.mean(cisLeft),np.mean(cisRight),lw=5)
plt.plot(np.mean(meanMeans),0,'o',color='r')
plt.hlines(0,CI(cisLeft,alpha)[0],CI(cisLeft,alpha)[1],color='r')
plt.hlines(0,CI(cisRight,alpha)[0],CI(cisRight,alpha)[1],color='r')

plt.hlines(1,np.mean(cis2Left),np.mean(cis2Right),lw=5)
plt.plot(np.mean(meanMeans2),1,'o',color='r')
plt.hlines(1,CI(cis2Left,alpha)[0],CI(cis2Left,alpha)[1],color='r')
plt.hlines(1,CI(cis2Right,alpha)[0],CI(cis2Right,alpha)[1],color='r')

plt.grid()

plt.show()


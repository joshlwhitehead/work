"""get fluorimetry data and calc basic stats (mean, std, ci, ti) to be used for future analysis and comparison"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from confidenceFun import CI
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def parseCsv(csv):
    data = pd.read_csv(csv)

    dataDict = {}
    for i in data.columns:
        dataDict[i] = list(data[i])
        dF = pd.DataFrame(dataDict)
    return dF

def tukey(df,ind,dep,alpha):
    m_comp = pairwise_tukeyhsd(endog=df[dep], groups=df[ind],alpha=alpha)
    return m_comp


def stats(pop,alpha):
    pop = list(pop)
    newPop = []
    for i in pop:
        if str(i) != 'nan':
            newPop.append(i)
    mean = np.mean(newPop)
    std = np.std(newPop)
    ci = CI(newPop,alpha)
    return mean,std,ci

test = 'cq'

x = parseCsv('baseline.csv')
print(tukey(x,'inst',test,0.1))
x.boxplot(test,by='inst')
plt.show()


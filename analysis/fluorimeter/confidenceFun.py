"""general functions for confidence/tolerance interval"""
import numpy as np
from scipy.stats import t
import toleranceinterval as ti
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

nameConvention = {
    'melt start':['Initial Melt Value','RFU'],
    'melt stop':['Final Melt Value','RFU'],
    'melt range':['Melt Range','RFU'],
    'fmax':['Fmax','RFU'],
    'mean pcr':['445 Baseline','RFU'],
    'pcr start':['Initial PCR Value','RFU'],
    'pcr stop':['Final PCR Value','RFU'],
    'cq':['Cq','Cycle'],
    'reverse cq':['Reverse Cq','Cycle'],
    'pcr min':['Minimum PCR Value','RFU'],
    'instrument':'Instrument',
    'config':'Configuration'
}



def CI(sample, alpha):
    mean_er = np.mean(sample) # sample mean
    std_dev_er = np.std(sample, ddof=1) # sample standard devialtion
    se = std_dev_er / np.sqrt(len(sample)) # standard error
    n = len(sample) # sample size, n
    dof = n - 1 # degrees of freedom
    t_star = t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    moe = t_star * se # margin of error
    ci = np.array([mean_er - moe, mean_er + moe])
    
    return ci



def TI(sample,alpha,p):
    bound = ti.twoside.normal(sample,p,1-alpha)
    return bound[0]



def tukey(df,ind,dep,alpha):
    m_comp = pairwise_tukeyhsd(endog=df[dep], groups=df[ind],alpha=alpha)
    return m_comp

def tolArea(complexPop,alpha,p):
    means = []
    stdevs = []
    for i in complexPop:
        means.append(np.mean(i))
        stdevs.append(np.std(i))
    means = [i for i in means if 0/i == 0]
    stdevs = [i for i in stdevs if 0/i == 0]
    meanTI = TI(means,alpha,p)
    stdTI = TI(stdevs,alpha,p)
    if stdTI[0] < 0:
        stdTI[0] = 0
    if meanTI[0] < 0:
        meanTI[0] = 0
    meanMeans = np.mean(means)
    meanStdevs = np.mean(stdevs)
    return (means,stdevs),(meanMeans,meanStdevs),(meanTI,stdTI)


def confArea(complesPop,alpha):
    means = []
    stdevs = []
    for i in complesPop:
        means.append(np.mean(i))
        stdevs.append(np.std(i))
    means = [i for i in means if 0/i == 0]
    stdevs = [i for i in stdevs if 0/i == 0]
    meanCI = CI(means,alpha)
    stdCI = CI(stdevs,alpha)
    if stdCI[0] < 0:
        stdCI[0] = 0
    if meanCI[0] < 0:
        meanCI[0] = 0
    meanMeans = np.mean(means)
    meanStdevs = np.mean(stdevs)
    return (means,stdevs),(meanMeans,meanStdevs),(meanCI,stdCI)


def taPlot(compoundPop,alpha,p,col,name):                #compoundPop should be of format[[pop1],[pop2],...]
    dat = tolArea(compoundPop,alpha,p)
    mid = dat[1]
    points = dat[0]
    tis = dat[2]
    tiL,tiR = tis[0]
    tiB,tiT = tis[1]

    # print(mid[0])
    for i in points[0]:
        print(type(i))
    plt.plot(points[0],points[1],'o',color=col,label=name)
    plt.hlines(mid[1],tiL,tiR,lw=5,colors=col)
    plt.vlines(mid[0],tiB,tiT,lw=5,colors=col)
    plt.plot(mid[0],mid[1],'o',color='r')
    plt.xlabel('Mean Melt Range (RFU)')
    plt.ylabel('Standard Deviation (RFU)')
    plt.title('90% Tolerance Area (p=90)')
    plt.grid()
    plt.show()


def caPlot(compoundPop,alpha,col,compWhat,chan,config):                #compoundPop should be of format[[pop1],[pop2],...]
    dat = confArea(compoundPop,alpha)
    mid = dat[1]
    points = dat[0]
    cis = dat[2]
    ciL,ciR = cis[0]
    ciB,ciT = cis[1]

    # print(mid[0])
    print(points[0])
    if config == 0:
        plt.plot(points[0],points[1],'o',color=col,label='baseline')
    else:
        plt.plot(points[0],points[1],'o',color=col,label='new config')
    plt.hlines(mid[1],ciL,ciR,lw=5,colors=col)
    plt.vlines(mid[0],ciB,ciT,lw=5,colors=col)
    plt.plot(mid[0],mid[1],'o',color='r')
    plt.xlabel(''.join(['Mean ',nameConvention[compWhat][0],' (',nameConvention[compWhat][1],')']))
    plt.ylabel(''.join(['Standard Deviation (',nameConvention[compWhat][1],')']))
    plt.title('90% Confidence Area')
    # plt.grid()
    plt.legend()
    plt.savefig(''.join(['plots2/',str(chan),'_',compWhat,'_CA.png']))



def anova(dataDict,csvFile,dep,ind):
    dF = pd.DataFrame(dataDict)
    dF.to_csv(csvFile)
    csvData = pd.read_csv(csvFile)
    formula = ' ~ '.join([dep,ind])
    model = ols(formula, csvData).fit()
    aov_table = anova_lm(model, typ=1)
    return aov_table

def anovaPrep(listOfPopsDep,listOfPopsInd,dep,ind):

    dict = {ind:[],dep:[]}
    for indx,val in enumerate(listOfPopsDep):
        for i in val:
            dict[ind].append(listOfPopsInd[indx])
            dict[dep].append(i)
    
    return dict


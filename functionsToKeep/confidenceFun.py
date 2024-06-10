import numpy as np
from scipy.stats import t
import toleranceinterval as ti
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2


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



def anova(df,ind,dep):
    formula = ' ~ '.join([dep,ind])
    model = ols(formula, df).fit()
    aov_table = anova_lm(model, typ=1)
    return aov_table



def tolArea(complexPop,alpha,p):
    means = []
    stdevs = []
    for i in complexPop:
        means.append(np.mean(i))
        stdevs.append(np.std(i))
    meanTI = TI(means,alpha,p)
    stdTI = TI(stdevs,alpha,p)
    if stdTI[0] < 0:
        stdTI[0] = 0
    if meanTI[0] < 0:
        meanTI[0] = 0
    if meanTI[1] > 1:
        meanTI[1] = 1
    meanMeans = np.mean(means)
    meanStdevs = np.mean(stdevs)
    return (means,stdevs),(meanMeans,meanStdevs),(meanTI,stdTI)


def confArea(complexPop,alpha):
    means = []
    stdevs = []
    for i in complexPop:
        means.append(np.mean(i))
        stdevs.append(np.std(i))
    meanCI = CI(means,alpha)
    stdCI = CI(stdevs,alpha)
    if stdCI[0] < 0:
        stdCI[0] = 0
    if meanCI[0] < 0:
        meanCI[0] = 0
    if meanCI[1] > 1:
        meanCI[1] = 1
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
    print(points[0])
    plt.plot(points[0],points[1],'o',color=col,label=name)
    plt.hlines(mid[1],tiL,tiR,lw=5,colors=col)
    plt.vlines(mid[0],tiB,tiT,lw=5,colors=col)
    plt.plot(mid[0],mid[1],'o',color='r')
    plt.xlabel('Mean R2')
    plt.ylabel('Standard Deviation')
    plt.title('90% Tolerance Area (p=90)')
    plt.grid()


def caPlot(compoundPop,alpha,col,name):                #compoundPop should be of format[[pop1],[pop2],...]
    dat = confArea(compoundPop,alpha)
    mid = dat[1]
    points = dat[0]
    cis = dat[2]
    ciL,ciR = cis[0]
    ciB,ciT = cis[1]

    # print(mid[0])
    # print(name,points[0])
    # print(name,points[1])
    plt.plot(points[0],points[1],'o',color=col,label=name)
    plt.hlines(mid[1],ciL,ciR,lw=5,colors=col)
    plt.vlines(mid[0],ciB,ciT,lw=5,colors=col)
    plt.plot(mid[0],mid[1],'o',color='k')
    plt.xlabel('Mean R2')
    plt.ylabel('Standard Deviation')
    plt.title('90% Confidence Area')
    plt.grid()
    
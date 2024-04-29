"""general functions for confidence/tolerance interval"""
import numpy as np
from scipy.stats import t
import toleranceinterval as ti
from statsmodels.stats.multicomp import pairwise_tukeyhsd



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
    meanTI = TI(means,alpha,p)
    stdTI = TI(stdevs,alpha,p)
    if stdTI[0] < 0:
        stdTI[0] = 0
    if meanTI[0] < 0:
        meanTI[0] = 0
    meanMeans = np.mean(means)
    meanStdevs = np.mean(stdevs)
    return (means,stdevs),(meanMeans,meanStdevs),(meanTI,stdTI)
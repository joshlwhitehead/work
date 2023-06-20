from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

file = ['data/fillStuff/Adv10DecFills.csv','data/fillStuff/Adv18DecFills.csv']
fillTot = []
instTot = []
cis = []
count = 10
alpha = 0.05
for i in file:

    data = pd.read_csv(i)
    fill = list(data['numericValue'])
    inst = np.ones(len(fill))*count
    data['inst'] = inst

    x = np.linspace(.8,1.5)
    plt.hist(fill,density=True)
    plt.plot(x,stats.norm.pdf(x,loc=np.mean(fill),scale=np.std(fill)))

    # print(stats.anderson(fill))


    
    mean_er = np.mean(fill) # sample mean
    std_dev_er = np.std(fill) # sample standard devialtion
    se = std_dev_er / np.sqrt(len(fill)) # standard error
    n = len(fill) # sample size, n
    dof = n - 1 # degrees of freedom
    t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    moe = t_star * se # margin of error
    ci = np.array([mean_er - moe, mean_er + moe])
    cis.append(ci)
    plt.show()

    for i in fill:
        fillTot.append(i)
    for i in inst:
        instTot.append(i)
    count+=8
x = np.linspace(min(fillTot),max(fillTot))
# plt.hist(fillTot,density=True)
# plt.plot(x,stats.t.pdf(x,df=len(x)-1,loc=np.mean(fillTot),scale=np.std(fillTot)))
print(stats.anderson(fillTot))

dfAnova = pd.DataFrame({'inst':instTot,'fill':fillTot})

m_comp = pairwise_tukeyhsd(endog=dfAnova['fill'], groups=dfAnova['inst'], alpha=alpha)
# plt.show()
count = 10
for i in cis:
    plt.plot((i[1]-i[0])*.5+i[0],count,'o',ms=7,color='r')
    plt.hlines(count,i[0],i[1],lw=5)
    
    count += 8
print(m_comp)
plt.grid()
plt.show()

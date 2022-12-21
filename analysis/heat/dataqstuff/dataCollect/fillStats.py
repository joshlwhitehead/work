from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = ['data/fillStuff/Adv10DecFills.csv','data/fillStuff/Adv18DecFills.csv']
fillTot = []
instTot = []
count = 10
for i in file:

    data = pd.read_csv(i)
    fill = list(data['numericValue'])
    inst = np.ones(len(fill))*count
    data['inst'] = inst

    x = np.linspace(min(fill),max(fill))
    plt.hist(fill,density=True)
    plt.plot(x,stats.norm.pdf(x,loc=np.mean(fill),scale=np.std(fill)))

    print(stats.anderson(fill))
    alpha = 0.05
    mean_er = np.mean(fill) # sample mean
    std_dev_er = np.std(fill) # sample standard devialtion
    se = std_dev_er / np.sqrt(len(fill)) # standard error
    n = len(fill) # sample size, n
    dof = n - 1 # degrees of freedom
    t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    moe = t_star * se # margin of error
    ci = np.array([mean_er - moe, mean_er + moe])
    print(ci)
    plt.show()

    for i in fill:
        fillTot.append(i)
    for i in inst:
        instTot.append(i)
    count+=8

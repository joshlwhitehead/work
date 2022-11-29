import numpy as np
import dataToVar as dat
import matplotlib.pyplot as plt
import pandas as pd
from thermalCompareQuant import listAvg, listStd, listRms, listGrad, interppp
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats



data = dat.forward3
samp = data[2]
time = data[0][:len(samp)]
mod = data[4][:len(samp)]


count = 0
flatMod = []
flatSamp = []
flatTime = []
for i in range(len(mod)):
    if count > 7:
        dm = (mod[count] - mod[count-6])/(time[count] - time[count-6])
        if dm <= 0.075 and dm >= -0.075 and mod[i] < 86 and mod[i] > 84:
            flatMod.append(mod[i])
            flatSamp.append(samp[i])
            flatTime.append(time[i])
    count += 1

dataType = np.ones(len(flatMod)).tolist() + (np.ones(len(flatSamp))*2).tolist()
# print(dataType)
dfAnova = pd.DataFrame({'type':dataType,'temp':flatMod+flatSamp})

formula = 'temp ~ type' 
model = ols(formula, dfAnova).fit()
aov_table = anova_lm(model, typ=1)
print(aov_table)

# plt.plot(data['timeSinceBoot'],data['Stage1 Thermocouple TempC'])
# plt.plot(flatTime,flatMod,'o')
# plt.plot(flatTime,flatSamp,'o')
# plt.plot(time,samp)
# plt.plot(time,mod)
# plt.show()

m_comp = pairwise_tukeyhsd(endog=dfAnova['temp'], groups=dfAnova['type'], 
                           alpha=0.05)
print(m_comp)

# dfAnova.boxplot('temp',by='type')
# plt.show()


def simple_stats1(sample, alpha):
    mean_er = np.mean(sample) # sample mean
    std_dev_er = np.std(sample, ddof=1) # sample standard devialtion
    se = std_dev_er / np.sqrt(len(sample)) # standard error
    z_star = stats.norm.ppf(1.0 - 0.5 * alpha) # using normal distribution
    moe = z_star * se # margin of error
    nci = np.array([mean_er - moe, mean_er + moe]) # normal confidence interval
    print(nci)
    return

simple_stats1(flatSamp, 0.05)
simple_stats1(flatMod, 0.05)
print(len(flatSamp))
plt.hist(flatSamp,bins=int(np.sqrt(len(flatSamp))))
# plt.hist(flatMod,bins=int(np.sqrt(len(f   latMod))))

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.graphics.factorplots import interaction_plot
import seaborn as sns
sns.set_style(style="whitegrid")


data = pd.read_csv('pmmv_255.csv')
data.dropna()
inst = (data['inst']).tolist()
fmax = (data['fmax']).tolist()
if 'pcr noise' in data.columns:
    noisePcr = (data['pcr noise']).tolist()
else:
    noisePcr = np.ones(len(inst))
if 'melt noise' in data.columns:
    noiseMelt = (data['melt noise']).tolist()
else:
    noiseMelt = np.ones(len(inst))
if 'cq' in data.columns:
    cq = (data['cq']).tolist()
else:
    cq = np.ones(len(inst))
if 'tm' in data.columns:
    tm = (data['tm']).tolist()
else:
    tm = np.ones(len(inst))
if 'memo' in data.columns:
    memo = (data['memo']).tolist()
    config = []
    for i in memo:
        if 'F.' in i:
            config.append(i[i.index('F.')+2:i.index('F.')+4])
        # elif 'F. ' in i:
        #     config.append(i[i.index('F.')+3:i.index('F.')+5])
else:
    memo = np.ones(len(inst))
    config = np.ones(len(inst))
if 'lot' in data.columns:
    lot = (data['lot']).tolist()
else:
    lot = np.ones(len(inst))



fmaxGood = []
instGood = []
pcrGood = []
meltGood = []
cqGood = []
tmGood = []
lotGood = []
configGood = []

for i in range(len(inst)):
    if str(noiseMelt[i]) != '  ' and str(cq[i]) != ' ' and str(tm[i]) != ' ' and fmax[i] > 0 and str(cq[i]) != 'nan':
        fmaxGood.append(fmax[i])
        instGood.append(inst[i])
        pcrGood.append(float(noisePcr[i]))
        meltGood.append(float(noiseMelt[i]))
        cqGood.append(float(cq[i]))
        tmGood.append(float(tm[i]))
        lotGood.append(float(lot[i]))
        configGood.append(float(config[i]))

dfAnova = pd.DataFrame({'inst':instGood,'fmax':fmaxGood,'cq':cqGood,'pcr noise':pcrGood,'melt noise':meltGood,'config':configGood,'lot':lotGood})
dfAnova = dfAnova.dropna()


fig = sns.catplot(x="config", y="fmax", hue="inst", col="lot",
                capsize=.2, palette="YlGnBu_d", height=4, aspect=.75,
                kind="point", data=dfAnova)
plt.show()


formula = 'fmax ~ lot + config + inst + lot:config + \
            lot:inst + config:inst + lot:config:inst'
model = ols(formula, dfAnova).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)


m_comp = pairwise_tukeyhsd(endog=dfAnova['fmax'], groups=dfAnova['lot'], 
                           alpha=0.05)
print(m_comp)
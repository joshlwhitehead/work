import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.graphics.factorplots import interaction_plot

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

for i in range(len(config)):
    print(i,config[i])

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


fig = interaction_plot(dfAnova['inst'], dfAnova['config'], dfAnova['fmax'],
                       ms=10)
plt.grid()
plt.show()

formula = 'fmax ~ config + inst'  
# don't include interaction term, ' + C(Filter):C(Day)', unless Kij > 1.
model = ols(formula, dfAnova).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)





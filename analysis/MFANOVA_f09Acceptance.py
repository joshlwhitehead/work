import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.graphics.factorplots import interaction_plot


data = pd.read_csv('f09AT.csv')


# data[data['type']=='SNP928 With PK'].hist('fmax')
# plt.show()
# data[data['type']=='SNP928 With PK'].boxplot('fmax',by='inst')
# # data[data['type']=='PMMV With PK'].hist('fmax')
# # data[data['type']=='SNP928 No PK'].hist('fmax')
# plt.show()

AD = stats.anderson(data[data['type']=='SNP928 With PK'].fmax,dist='norm')
print(AD)

dfAnova = {'inst':data[data['type']=='SNP928 With PK'].inst,'fmax':data[data['type']=='SNP928 With PK'].fmax,
    'lot':data[data['type']=='SNP928 With PK'].lot}

formula = 'fmax ~ inst'
model = ols(formula, dfAnova).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)

m_comp = pairwise_tukeyhsd(endog=dfAnova['fmax'], groups=dfAnova['inst'], 
                           alpha=0.05)
print(m_comp)

fig = interaction_plot(data['inst'], data['type'], data['fmax'],ms=10)
plt.show()

formula = 'fmax ~ type + inst + type:inst'  
# don't include interaction term, ' + C(Filter):C(Day)', unless Kij > 1.
model = ols(formula, data).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)
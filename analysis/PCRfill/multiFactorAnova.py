import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np


original = pd.read_csv('convertcsv (4).csv')

inst = original['instrument'].tolist()
lot = original['consumable/lot'].tolist()
fill = original['numericValue'].tolist()



new = {}
for i in lot:
    new[i] = {}
    for u in inst:
        if lot[inst.index(u)] == i:
            # print('ok')
            new[i][u] = []

for i in new:
    for u in new[i]:
        for j in range(len(lot)):
            if lot[j] == i and inst[j] == u:
                new[i][u].append(fill[j])

for i in new:
    for u in new[i]:
        new[i][u] = np.mean(new[i][u])

instNew = []
lotNew = []
fillNew = []
for i in new:
    for u in new[i]:
        instNew.append(u)
        lotNew.append(i)
        fillNew.append(new[i][u])

dF = pd.DataFrame({'inst':instNew,'lot':lotNew,'fill':fillNew})
dF.to_csv('newnew.csv')
# fig = interaction_plot(dF.lot, dF.inst, dF.fill, ms=10)
# plt.show()

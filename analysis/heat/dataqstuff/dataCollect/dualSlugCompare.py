import dataToVar as dat
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from thermalCompareQuant import listAvg,listStd
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# s1 = dat.smallA
# s2 = dat.smallB
l1 = dat.backLargeA
l2 = dat.backLargeB
o1 = dat.backObroundA
o2 = dat.backObroundB




















# sModelTemp = listAvg([s1[0],s2[0]],[s1[4],s2[4]])
lModelTemp = listAvg([l1[0],l2[0]],[l1[4],l2[4]])
oModelTemp = listAvg([o1[0],o2[0]],[o1[4],o2[4]])



# sAvgPlunge = listAvg([s1[0],s2[0]],[s1[2],s2[2]])
lAvgPlunge = listAvg([l1[0],l2[0]],[l1[2],l2[2]])
oAvgPlunge = listAvg([o1[0],o2[0]],[o1[2],o2[2]])

# sAvgEdge = listAvg([s1[0],s2[0]],[s1[3],s2[3]])
lAvgEdge = listAvg([l1[0],l2[0]],[l1[3],l2[3]])
oAvgEdge = listAvg([o1[0],o2[0]],[o1[3],o2[3]])

# sStdPlunge = listStd([s1[0],s2[0]],[s1[2],s2[2]])
lStdPlunge = listStd([l1[0],l2[0]],[l1[2],l2[2]])
oStdPlunge = listStd([o1[0],o2[0]],[o1[2],o2[2]])

# sStdEdge = listStd([s1[0],s2[0]],[s1[3],s2[3]])
lStdEdge = listStd([l1[0],l2[0]],[l1[3],l2[3]])
oStdEdge = listStd([o1[0],o2[0]],[o1[3],o2[3]])


# sModDeltaPlunge = abs(sModelTemp-sAvgPlunge)
lModDeltaPlunge = abs(lModelTemp-lAvgPlunge)
oModDeltaPlunge = abs(oModelTemp-oAvgPlunge)

# sModDeltaEdge = abs(sModelTemp-sAvgEdge)
lModDeltaEdge = abs(lModelTemp-lAvgEdge)
oModDeltaEdge = abs(oModelTemp-oAvgEdge)



# sDif = sAvgPlunge - sAvgEdge
lDif = lAvgPlunge - lAvgEdge
oDif = oAvgPlunge - oAvgEdge
# difTot = [sDif,lDif,oDif]
difList = []
namList = []
nam = ['s','l','o']
count = 0
# for i in difTot:
#     for u in i:
#         difList.append(u)
#         namList.append(nam[count])
#     count += 1

# dataFormat = pd.DataFrame({'slug':namList,'dif':difList})

# formula = 'dif ~ slug'
# model = ols(formula,dataFormat).fit()

# aov_table = anova_lm(model,typ=2)

# m_comp = pairwise_tukeyhsd(endog=dataFormat['dif'],groups=dataFormat['slug'],alpha=0.05)



# print(aov_table)
# print(m_comp)






# plt.plot(sAvgPlunge,'b',label='nominal slug')
# plt.plot(sAvgEdge,'b',ls='-.')
# plt.plot(lAvgPlunge,'r',label='large slug')
# plt.plot(lAvgEdge,'r',ls='-.')
# plt.plot(oAvgPlunge,'g',label='obround slug')
# plt.plot(oAvgEdge,'g',ls='-.')
# plt.plot(sModelTemp,'k',label='model')
# plt.title('Average TC Temp With Different Slugs')
# plt.xlabel('Time (sec)')
# plt.ylabel('Temp (c)')

# plt.grid()
# plt.legend()
# plt.show()

plt.title('Difference Between Plunger TC and Edge TC Backward Facing Insert')
plt.xlabel('Time (sec)')
plt.ylabel('Temp (c)')
# plt.plot(sDif,'b',label='nominal')
plt.plot(lDif,'r',label='large')
plt.plot(oDif,'g',label='obround')

plt.legend()
plt.grid()
plt.show()



# plt.title('Difference Between Model and Plunger TC (|model - plunger|)')
# plt.plot(sModDeltaPlunge,'b',label='nominal')

# plt.plot(lModDeltaPlunge,'r',label='large')

# plt.plot(oModDeltaPlunge,'g',label='obround')
# plt.legend()
# plt.xlabel('Time (sec)')
# plt.ylabel('Temp (c)')
# plt.grid()
# plt.show()

# plt.title('Difference Between Model and Edge TC (|model - edge|)')
# plt.plot(sModDeltaEdge,'b',ls='-.',label='nominal')
# plt.plot(lModDeltaEdge,'r',ls='-.',label='large')
# plt.plot(oModDeltaEdge,'g',ls='-.',label='obround')
# plt.xlabel('Time (sec)')
# plt.ylabel('Temp (c)')
# plt.legend()
# plt.grid()
# plt.show()



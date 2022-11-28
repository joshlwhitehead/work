import numpy as np
import dataToVar as dat
import matplotlib.pyplot as plt
import pandas as pd
from thermalCompareQuant import listAvg, listStd, listRms, listGrad
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd


f1 = dat.forward1
f2 = dat.forward2
f3 = dat.forward3

b1 = dat.backward1
b2 = dat.backward2
b3 = dat.backward3
b4 = dat.backward4


# plt.plot(f1[0][:len(f1[2])],f1[2],label='Insert',color='blue')
# plt.plot(f2[0][:len(f2[2])],f2[2],color='blue')
# plt.plot(f3[0][:len(f3[2])],f3[2],color='blue')
# plt.plot(b1[0][:len(b1[2])],b1[2],label='backward',color='red')
# plt.plot(b2[0][:len(b2[2])],b2[2],color='red')
# # plt.plot(dat.noInsert1[0][:len(dat.noInsert1[2])],dat.noInsert1[2],label='noInsert',color='r')
# # plt.plot(dat.noInsert2[0][:len(dat.noInsert2[2])],dat.noInsert2[2],color='r')

# plt.plot(f1[0][:len(f1[3])],f1[3],color='blue',linestyle='dashdot')
# plt.plot(f2[0][:len(f2[3])],f2[3],color='blue',linestyle='dashdot')
# plt.plot(f3[0][:len(f3[3])],f3[3],color='blue',linestyle='dashdot')
# plt.plot(b1[0][:len(b1[3])],b1[3],color='red',linestyle='dashdot')
# plt.plot(b2[0][:len(b2[3])],b2[3],color='red',linestyle='dashdot')
# plt.plot(b3[0][:len(b3[3])],b3[3],color='red',linestyle='dashdot')
# plt.plot(b4[0][:len(b4[3])],b4[3],color='red',linestyle='dashdot')
# plt.grid()
# plt.show()


"""                 GRADIENT                """

# print(len(f1[0]),len(f1[2]))
# print(len(f2[0]),len(f2[2]))
# print(len(f3[0]),len(f3[2]))



fPlunAvg = listAvg([f1[0],f2[0],f3[0]],[f1[2],f2[2],f3[2]])
bPlunAvg = listAvg([b1[0],b2[0]],[b1[2],b2[2]])
fEdgeAvg = listAvg([f1[0],f2[0],f3[0]],[f1[3],f2[3],f3[3]])
bEdgeAvg = listAvg([b1[0],b2[0],b3[0],b4[0]],[b1[3],b2[3],b3[3],b4[3]])

fPlunRms = listRms([f1[0],f2[0],f3[0]],[f1[2],f2[2],f3[2]])
bPlunRms = listRms([b1[0],b2[0]],[b1[2],b2[2]])
fEdgeRms = listRms([f1[0],f2[0],f3[0]],[f1[3],f2[3],f3[3]])
bEdgeRms = listRms([b1[0],b2[0],b3[0],b4[0]],[b1[3],b2[3],b3[3],b4[3]])

fPlunStd = listStd([f1[0],f2[0],f3[0]],[f1[2],f2[2],f3[2]])
bPlunStd = listStd([b1[0],b2[0]],[b1[2],b2[2]])
fEdgeStd = listStd([f1[0],f2[0],f3[0]],[f1[3],f2[3],f3[3]])
bEdgeStd = listStd([b1[0],b2[0],b3[0],b4[0]],[b1[3],b2[3],b3[3],b4[3]])

# plt.plot(fPlunAvg,'b',label='plunger, forward insert')
# plt.plot(bPlunAvg,'r',label='plunger, backward insert')
# plt.plot(fEdgeAvg,'b',ls='-.',label='edge, forward insert')
# plt.plot(bEdgeAvg,'r',ls='-.',label='edge, backward insert')
# plt.title('Average Temperatures')
# plt.xlabel('Time (sec)')
# plt.ylabel('Temp (c)')
# plt.legend()
# plt.grid()
# plt.show()


fGrad = listGrad([f1[0],f2[0],f3[0]],[f1[2],f2[2],f3[2]],[f1[3],f2[3],f3[3]])
bGrad = listGrad([b1[0],b2[0]],[b1[2],b2[2]],[b1[3],b2[3]])
ff = np.ones(len(fGrad)).tolist()
bb = (np.ones(len(bGrad))*2).tolist()

dfAnova = pd.DataFrame({'orientation':ff+bb,'quant':fGrad+bGrad})


formula = 'quant ~ orientation' 
model = ols(formula, dfAnova).fit()
aov_table = anova_lm(model, typ=1)
print(aov_table)


m_comp = pairwise_tukeyhsd(endog=dfAnova['quant'], groups=dfAnova['orientation'], 
                           alpha=0.05)
print(m_comp)


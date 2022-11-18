import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import importData
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.read_csv('test.csv')
data.dropna()
inst = (data['inst']).tolist()
fmax = (data['fmax']).tolist()
if 'pcr noise' in data.columns():
    noisePcr = (data['pcr noise']).tolist()
else:
    noisePcr = []
if 'melt noise' in data.columns():
    noiseMelt = (data['melt noise']).tolist()
else:
    noiseMelt = []
if 'cq' in data.columns():
    cq = (data['cq']).tolist()
else:
    cq = []
if 'tm' in data.columns():
    tm = (data['tm']).tolist()
else:
    tm = []



fmaxGood = []
instGood = []
pcrGood = []
meltGood = []
cqGood = []
tmGood = []
for i in range(len(inst)):
    if str(noiseMelt[i]) != '  ' and str(cq[i]) != ' ' and str(tm[i]) != ' ' and fmax[i] > 0 and str(cq[i]) != 'nan':
        fmaxGood.append(fmax[i])
        instGood.append(inst[i])
        pcrGood.append(float(noisePcr[i]))
        meltGood.append(float(noiseMelt[i]))
        cqGood.append(float(cq[i]))
        tmGood.append(float(tm[i]))

dfAnova = pd.DataFrame({'inst':instGood,'fmax':fmaxGood,'cq':cqGood,'pcr noise':pcrGood,'melt noise':meltGood})
dfAnova = dfAnova.dropna()
dfAnova.boxplot('fmax',by='inst')
plt.show()

instSimp = [*set(instGood)]

formula = 'fmax ~ inst' 
model = ols(formula, dfAnova).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)

m_comp = pairwise_tukeyhsd(endog=dfAnova['fmax'], groups=dfAnova['inst'], 
                           alpha=0.05)
print(m_comp)

qdotInst = []
qdotRat = []
for i in range(len(importData.inst)):
    if importData.inst[i] in instSimp:
        qdotInst.append(importData.inst[i])
        qdotRat.append(importData.avg[i])



count = 0
while len(instSimp) != len(qdotInst):
    if qdotInst[count] != instSimp[count]:
        instSimp.pop(count)
        count -= 1
    count += 1
        
 



fmaxMean = []
pcrMean = []
meltMean = []
cqMean = []
tmMean = []

for i in instSimp:
    mean1 = []
    mean2 = []
    mean3 = []
    mean4 = []
    mean5 = []
    for u in range(len(instGood)):
        if instGood[u] == i:
            mean1.append(fmaxGood[u])
            mean2.append(pcrGood[u])
            mean3.append(meltGood[u])
            mean4.append(cqGood[u])
            mean5.append(tmGood[u])
    fmaxMean.append(np.mean(mean1))
    pcrMean.append(np.mean(mean2))
    meltMean.append(np.mean(mean3))
    cqMean.append(np.mean(mean4))
    tmMean.append(np.mean(mean5))










                                 
# plt.plot(instGood,fmaxGood,'o')
# plt.plot(instSimp,fmaxMean,'o')
# plt.grid()
# plt.show()

# plt.plot(qdotRat,fmaxMean,'o')
# plt.plot(qdotRat,fmaxMean,'o')
# plt.grid()
# plt.show()

# plt.plot(qdotRat,pcrMean,'o')
# plt.grid()
# plt.show()

# plt.plot(qdotRat,meltMean,'o')
# plt.grid()
# plt.show()

# plt.plot(qdotRat,cqMean,'o')
# plt.grid()
# plt.show()
# print(len(qdotRat),len(fmaxMean))

qdotAdj = []
fmaxAdj = []
use = [5,6,7,8,9,10,25,26]
for i in range(len(qdotInst)):
    if qdotInst[i] in use:
        qdotAdj.append(qdotRat[i])
        fmaxAdj.append(fmaxMean[i])


a,b = np.polyfit(qdotAdj,fmaxAdj,1)
c,d = np.polyfit(qdotRat,pcrMean,1)
e,f = np.polyfit(qdotRat,meltMean,1)
g,h = np.polyfit(qdotRat,cqMean,1)


qdotRat = np.array(qdotRat)

# plt.plot(qdotRat,fmaxMean,'o')
# plt.plot(qdotRat,a*qdotRat+b)
# plt.grid()
# plt.show()


# print(cqGood)


fig,ax = plt.subplots(2,2)
ax[0,0].plot(qdotAdj,fmaxAdj,'o')
ax[0,1].plot(qdotRat,pcrMean,'o')
ax[1,0].plot(qdotRat,meltMean,'o')
ax[1,1].plot(qdotRat,cqMean,'o')
ax[0,0].plot(qdotRat,a*qdotRat+b)
ax[0,1].plot(qdotRat,c*qdotRat+d)
ax[1,0].plot(qdotRat,e*qdotRat+f)
ax[1,1].plot(qdotRat,g*qdotRat+h)
ax[0,0].title.set_text('fmax')
ax[0,1].title.set_text('pcr noise')
ax[1,0].title.set_text('melt noise')
ax[1,1].title.set_text('cq')
ax[0,0].grid()
ax[0,1].grid()
ax[1,0].grid()
ax[1,1].grid()
plt.show()




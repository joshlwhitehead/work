import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import importData

data = pd.read_csv('pmmv_255.csv')

inst = (data['inst']).tolist()
fmax = (data['fmax']).tolist()
noisePcr = (data['pcr noise']).tolist()
noiseMelt = (data['melt noise']).tolist()
cq = (data['cq']).tolist()
tm = (data['tm']).tolist()

instSimp = [*set(inst)]

fmaxGood = []
instGood = []
pcrGood = []
meltGood = []
cqGood = []
tmGood = []
for i in range(len(inst)):
    if str(noisePcr[i]) != 'nan' and str(noiseMelt[i]) != 'nan' and str(fmax[i] != 'nan') and str(cq[i]) != 'nan' and str(tm[i]) != 'nan' and str(noiseMelt[i]) != '  ' and str(cq[i]) != ' ' and str(tm[i]) != ' ':
        fmaxGood.append(fmax[i])
        instGood.append(inst[i])
        pcrGood.append(float(noisePcr[i]))
        # print(noiseMelt[i])
        meltGood.append(float(noiseMelt[i]))
        cqGood.append(float(cq[i]))

        tmGood.append(float(tm[i]))




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


qdotInst = []
qdotFmax = []
for i in range(len(importData.inst)):
    if importData.inst[i] in instSimp:
        qdotInst.append(importData.inst[i])
        qdotFmax.append(importData.avg[i])

fmaxMean.remove(fmaxMean[3])
plt.plot(qdotFmax,fmaxMean,'o')
# # plt.plot(qdotInst,qdotFmax,'o')
plt.show()



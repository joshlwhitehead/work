import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import importData

data = pd.read_csv('f07Snp.csv')

inst = (data['inst']).tolist()
fmax = (data['fmax']).tolist()
noisePcr = (data['pcr noise']).tolist()
noiseMelt = (data['melt noise']).tolist()

instSimp = [*set(inst)]

fmaxGood = []
instGood = []
pcrGood = []
meltGood = []
for i in range(len(fmax)):
    if fmax[i] >= 0 and str(noisePcr[i]) != 'nan' and str(noiseMelt[i]) != 'nan' and str(fmax[i] != 'nan'):
        fmaxGood.append(fmax[i])
        instGood.append(inst[i])
        pcrGood.append(float(noisePcr[i]))
        meltGood.append(float(noiseMelt[i]))




fmaxMean = []
pcrMean = []
meltMean = []

for i in instSimp:
    mean1 = []
    mean2 = []
    mean3 = []
    for u in range(len(instGood)):
        if instGood[u] == i:
            mean1.append(fmaxGood[u])
            mean2.append(pcrGood[u])
            mean3.append(meltGood[u])
    fmaxMean.append(np.mean(mean1))
    pcrMean.append(np.mean(mean2))
    meltMean.append(np.mean(mean3))


instQdot = [5,6,7,10,13,25,26,27]

qdotfmax = []
qdotpcr = []
qdotmelt = []
for i in range(len(instSimp)):
    if instSimp[i] in instQdot:
        qdotfmax.append(fmaxMean[i])
        qdotpcr.append(pcrMean[i])
        qdotmelt.append(meltMean[i])
# plt.scatter(instSimp,fmaxMean)
# plt.grid()
# plt.show()

# plt.plot(instSimp,pcrMean)
# plt.plot(instSimp,meltMean)
# plt.show()


# plt.scatter(instGood,fmaxGood)
# plt.xlabel('Instrument')
# plt.ylabel('fmax')
# plt.grid()
# plt.show()


# plt.scatter(instGood,pcrGood)
# plt.scatter(instGood,meltGood)
# plt.xlabel('Instrument')
# plt.ylabel('noise')
# plt.grid()
# plt.show()


plt.scatter(importData.avg,qdotmelt)
plt.xlabel('qdot 515/480')
plt.ylabel('snp pcr noise')
plt.grid()
plt.show()


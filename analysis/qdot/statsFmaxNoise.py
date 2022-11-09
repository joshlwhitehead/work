import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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

# plt.scatter(instSimp,fmaxMean)
# plt.show()
# plt.plot(instSimp,pcrMean)
# plt.plot(instSimp,meltMean)
# plt.show()
plt.scatter(instGood,fmaxGood)
plt.grid()
plt.show()
plt.scatter(instGood,pcrGood)
plt.scatter(instGood,meltGood)

plt.grid()
plt.show()





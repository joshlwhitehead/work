import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import importData

data = pd.read_csv('pmmv_255.csv')
data.dropna()
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
    if fmax[i] > 0 and str(noiseMelt[i]) != '  ' and str(cq[i]) != ' ' and str(tm[i]) != ' ':
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
pcrMean.remove(pcrMean[3])
meltMean.remove(meltMean[3])
cqMean.remove(cqMean[3])





# plt.plot(qdotFmax,fmaxMean,'o')
# plt.plot(qdotFmax,fmaxMean,'o')
# plt.grid()
# plt.show()

# plt.plot(qdotFmax,pcrMean,'o')
# plt.grid()
# plt.show()

# plt.plot(qdotFmax,meltMean,'o')
# plt.grid()
# plt.show()

# plt.plot(qdotFmax,cqMean,'o')
# plt.grid()
# plt.show()

a,b = np.polyfit(qdotFmax,fmaxMean,1)
c,d = np.polyfit(qdotFmax,pcrMean,1)
e,f = np.polyfit(qdotFmax,meltMean,1)
g,h = np.polyfit(qdotFmax,cqMean,1)


qdotFmax = np.array(qdotFmax)
print(np.mean(qdotFmax))


fig,ax = plt.subplots(2,2)
ax[0,0].plot(qdotFmax,fmaxMean,'o')
ax[0,1].plot(qdotFmax,pcrMean,'o')
ax[1,0].plot(qdotFmax,meltMean,'o')
ax[1,1].plot(qdotFmax,cqMean,'o')
ax[0,0].plot(qdotFmax,a*qdotFmax+b)
ax[0,1].plot(qdotFmax,c*qdotFmax+d)
ax[1,0].plot(qdotFmax,e*qdotFmax+f)
ax[1,1].plot(qdotFmax,g*qdotFmax+h)
ax[0,0].title.set_text('fmax')
ax[0,1].title.set_text('pcr noise')
ax[1,0].title.set_text('melt noise')
ax[1,1].title.set_text('cq')
ax[0,0].grid()
ax[0,1].grid()
ax[1,0].grid()
ax[1,1].grid()
plt.show()




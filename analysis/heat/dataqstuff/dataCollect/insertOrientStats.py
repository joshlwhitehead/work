import numpy as np
import dataToVar as dat
import matplotlib.pyplot as plt
from scipy import stats


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


totalPlun = [f1[2],f2[2],f3[2],b1[2],b2[2]]
totalFran = [f1[3],f2[3],f3[3],b1[3],b2[3],b3[3],b4[3]]
meanPlun = []
meanFran = []
for i in totalPlun:
    meanPlun.append(np.mean(i))

for i in totalFran:
    meanFran.append(np.mean(i))


meanFranF = np.mean(meanFran[:3])
meanFranB = np.mean(meanFran[3:])
meanPlunF = np.mean(meanPlun[:3])
meanPlunB = np.mean(meanPlun[3:])


stdFranF = np.std(meanFran[:3])
stdFranB = np.std(meanFran[3:])
stdPlunF = np.std(meanPlun[:3])
stdPlunB = np.std(meanPlun[3:])


meanDif = meanPlunF - meanPlunB
nPlunF = 3
nPlunB = 2
dof = nPlunF+nPlunB-2
sPool = np.sqrt(((nPlunF-1)*stdPlunF**2 + (nPlunB-1)*stdPlunB**2)/dof)

SE = sPool*np.sqrt(1/nPlunF+1/nPlunB)

alpha = 0.5

tStar = stats.t.ppf(1-0.5*alpha,dof)
moe = tStar*SE
ci = (meanDif-moe,meanDif+moe)
print(ci)



# meanDif = meanFranF - meanFranB
# nFranF = 3
# nFranB = 4
# dof = nFranF+nFranB-2
# sPool = np.sqrt(((nFranF-1)*stdFranF**2 + (nFranB-1)*stdFranB**2)/dof)

# SE = sPool*np.sqrt(1/nFranF+1/nFranB)

# alpha = 0.5

# tStar = stats.t.ppf(1-0.5*alpha,dof)
# moe = tStar*SE

# ci = (meanDif-moe,meanDif+moe)
# print(ci)

# tDif = meanDif/SE

# pVal = 1*stats.t.cdf(tDif,dof)
# print(pVal)







import numpy as np
from parsTxt import meltRamp
import os
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.stats import norm, t


def r2(y,fit):
    y = np.array(y)
    fit = np.array(fit)
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2

folder = 'tape/'
rr = []
for i in os.listdir(folder):
    mod = meltRamp(''.join([folder,i]))[1][0]
    timeMod = meltRamp(''.join([folder,i]))[1][1]

    melt = meltRamp(''.join([folder,i]))[0][0]
    timeM = meltRamp(''.join([folder,i]))[0][1]

    interp = interp1d(timeM,melt)
    r = r2(interp(timeMod[3:-4]),mod[3:-4])
    # print(r)
    rr.append(r)


plt.plot(rr,t.pdf(rr,df=len(rr)-1))
plt.show()



#     plt.plot(timeMod,mod)
#     plt.plot(timeM,melt,'o')
# plt.grid()
# plt.show()


# print(interp(timeMod[:-1]))
    



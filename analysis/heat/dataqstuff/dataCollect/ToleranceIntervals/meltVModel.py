import numpy as np
from parsTxt import meltRamp
import os
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.stats import norm, t,beta
from scipy.optimize import fsolve


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



mean = np.mean(rr)
var = np.var(rr)

print(mean)
print(var)
def solve(x):

    return [x[0]/(x[0]+x[1])-mean,x[0]*x[1]/(x[0]+x[1])**2/(x[0]+x[1]+1)-var]

root = fsolve(solve,[480,5])



plt.hist(rr,density=True)
x = np.linspace(min(rr),max(rr))

plt.plot(x,beta.pdf(x,root[0],root[1]))
plt.plot(x,norm.pdf(x,loc=np.mean(rr),scale=np.std(rr)))
plt.plot(x,t.pdf(x,df=len(rr)-1,loc=np.mean(rr),scale=np.std(rr)))
plt.show()



#     plt.plot(timeMod,mod)
#     plt.plot(timeM,melt,'o')
# plt.grid()
# plt.show()


# print(interp(timeMod[:-1]))
    



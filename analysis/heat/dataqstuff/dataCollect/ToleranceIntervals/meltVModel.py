import numpy as np
from parsTxt import meltRamp
import os
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.stats import t,beta
from scipy.optimize import fsolve
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd


def r2(y,fit):
    y = np.array(y)
    fit = np.array(fit)
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2

folder = 'padVpaste/'
folder2 = 'tape/'
def rVal(folder):
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
    return rr



mean = np.mean(rVal(folder))
var = np.var(rVal(folder))

print(mean)
print(var)
def solve(x):

    return [x[0]/(x[0]+x[1])-mean,x[0]*x[1]/(x[0]+x[1])**2/(x[0]+x[1]+1)-var]





def CI(data,alpha):
    mean_er = np.mean(data)                                                     #mean denature temp of run
    std_dev_er = np.std(data)                                                   #stdev of each run
    n = len(data)                                                               
    se = std_dev_er / np.sqrt(n)                                                #standard error for t-test stat
    dof = n - 1                                                                 #degree of fredom
    t_star = t.ppf(1.0 - 0.5 * alpha, dof)                                #t* get from t-dist ppf
    moe = t_star * se                                                           #margin of error
    ciMult = np.array([mean_er - moe, mean_er + moe])                           #1-alpha confidence interval
    # print('CI:',round(mean_er,3),'+/-',round(moe,4))
    return (ciMult)



root = fsolve(solve,[480,5])

full = []
fullName = []
for i in rVal(folder2):
    full.append(i)
    fullName.append('tape')
for i in rVal(folder):
    full.append(i)
    fullName.append('wet')


dF = pd.DataFrame({'type':fullName,'r2':full})



formula = 'r2 ~ type'
model = ols(formula, dF).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)


m_comp = pairwise_tukeyhsd(endog=dF['r2'], groups=dF['type'], alpha=0.05)
print(m_comp)




plt.hlines(1,CI(rVal(folder),.05)[0],CI(rVal(folder),.05)[1],lw=5)
plt.hlines(2,CI(rVal(folder2),.05)[0],CI(rVal(folder2),.05)[1],lw=5)
plt.plot([np.mean(rVal(folder)),np.mean(rVal(folder2))],[1,2],'o',color='r')
plt.yticks([1,2],['Wet Fill','Tape'])
plt.grid()
plt.xlabel(''.join([r'$r^2$',' Value of the Melt']))
plt.ylabel('Tool Used to Acquire Data')
plt.title('95% Confidence Interval of the Mean')
plt.show()



# plt.hist(rVal(folder),density=True)
# x = np.linspace(min(rVal(folder)),max(rVal(folder)))

# plt.plot(x,beta.pdf(x,root[0],root[1]))
# # plt.plot(x,norm.pdf(x,loc=np.mean(rr),scale=np.std(rr)))
# plt.plot(x,t.pdf(x,df=len(rVal(folder))-1,loc=np.mean(rVal(folder)),scale=np.std(rVal(folder))))

# plt.show()






#     plt.plot(timeMod,mod)
#     plt.plot(timeM,melt,'o')
# plt.grid()
# plt.show()


# print(interp(timeMod[:-1]))
    



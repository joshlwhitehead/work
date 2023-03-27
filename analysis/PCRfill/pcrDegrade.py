import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import t
from statsmodels.formula.api import ols


file = pd.read_csv('pcrFillData.csv')
date = file['date']
m1 = file['m1']
m2 = file['m2']
m3 = file['m3']
m4 = file['m4']

t1 = file['t1']
t2 = file['t2']
t3 = file['t3']
t4 = file['t4']


m = ['m1','m2','m3','m4']
thick = ['t1','t2','t3','t4']

dateSplit = []
for i in date:
    x = i.split('-')
    dateSplit.append(x)


day = []
for i in dateSplit:
    if 'Jan' in i:
        day.append(int(i[0])-int(dateSplit[0][0]))
    elif 'Feb' in i:
        day.append(int(i[0])-int(dateSplit[0][0])+31)
    elif 'Mar' in i:
        day.append(int(i[0])-int(dateSplit[0][0])+31+29)
day = np.array(day)

file['day'] = day





# plt.plot(day,m1,'o')
# plt.plot(day,a*day+b)
# plt.show()
alpha = 0.05
def CI(col):
    n = len(file[col])
    dof = n-2
    model = ols(''.join([col,' ~ day']),file).fit()
    slope = model.params[1]
    se = np.sqrt(model.mse_resid)
    Sxx = np.var(file[col]) * n
    t_star = t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    ciMin = slope-t_star*se/np.sqrt(Sxx)
    ciMax = slope+t_star*se/np.sqrt(Sxx)
    print(ciMin,ciMax)


for i in thick:
    CI(i)


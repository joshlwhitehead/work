import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats,integrate
csv = pd.read_csv('data/fmax.csv')

colOrigin = list(csv.columns)
colNew = ['consumableId','415','445','480','515','555','590','630','680','NIR','CLR','DARK']
newDict = {}

count = 0
for i in colOrigin:
    newDict[colNew[count]] = list(csv[i])
    count += 1


x = np.linspace(-4,4,99999)
y = np.random.normal(0,1,999)
# print(y)
yy = stats.norm.pdf(x)


def pdf(x):
    return stats.norm.pdf(x)

start = 1
end = 2

xx = np.linspace(start,end,len(yy))
yyy = stats.norm.pdf(xx)
z,dddd = integrate.quad(pdf,start,end)
zz = integrate.trapz(yyy,xx)
zzz = stats.norm.cdf(end) - stats.norm.cdf(start)
print('quad',z)
print('trapz',zz)
print('cdf',zzz)

# plt.hist(y,density=True)
plt.plot(x,yy)
plt.fill_between(x,yy,where=(x>=start) & (x<=end))
plt.grid()
# plt.show()
plt.savefig('test.png')

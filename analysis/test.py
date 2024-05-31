import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


mean = np.random.rand()
std = abs(np.random.rand())
n = 3000

distOfMeans = np.random.normal(mean,std,n)

mean2 = abs(np.random.rand())
std2 = abs(np.random.rand())

distOfStds = np.random.normal(mean2,std2,n)
print(distOfStds)

pops = []
for indx,val in enumerate(distOfMeans):
    pops.append(np.random.normal(val,distOfStds[indx],n))
print(pops)
# z = np.linspace(min(test),max(test),n)
# pdf = stats.norm.pdf(z,loc=mean,scale=std)
# plt.hist(test,int(np.sqrt(n)),density=True)
# plt.plot(z,pdf)
# plt.grid()
# plt.savefig('test.png')
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


mean = [0.5405474802695841, 0.9621379361318532, 0.5402961792994324, 0.5691713491196706,
        0.8242439718832835, 0.8485203245261861, 0.8328894026110384, 0.7660107065115768,
        0.793595661078436, 0.9673612442706213]
std = [0.4707277008460138, 0.03454569089502284, 0.44098787423294344, 0.421227993247715,
       0.33932140442848013, 0.3464307760013458, 0.3410250323674084, 0.3669482936802967,
       0.33268302447931464, 0.03447945925398713]


meanMean = np.mean(mean)
meanStd = np.mean(std)
stdMean = np.std(mean)
stdStd = np.std(std)

n = 1000

distOfMeans = np.random.normal(meanMean,stdMean,n)
distOfStds = np.random.normal(meanStd,stdStd,n)


z = np.linspace(min(distOfMeans),max(distOfMeans),n)
zz = np.linspace(min(mean),max(mean),len(mean))

pdfz = stats.norm.pdf(z,loc=np.mean(distOfMeans),scale=np.std(distOfMeans))
pdfzz = stats.norm.pdf(zz,loc=meanMean,scale=stdMean)
plt.hist(mean,int(np.sqrt(len(mean))),density=1)
plt.hist(distOfMeans,int(np.sqrt(n)),density=1)
plt.plot(z,pdfz,color='C0')
plt.plot(zz,pdfzz,color='C1')


plt.show()


# for indx,val in enumerate(mean):
#     plt.scatter(val,std[indx],color='C0')
# for indx,val in enumerate(distOfMeans):
#     plt.scatter(val,distOfStds[indx],color='C1')
# plt.scatter(np.mean(mean),np.mean(std),color='r')
# plt.scatter(np.mean(distOfMeans),np.mean(distOfStds),color='k')
# plt.grid()
# plt.show()
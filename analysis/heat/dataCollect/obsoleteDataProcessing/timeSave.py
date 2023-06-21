"""Calculate difference in time it takes to finish for different configs
DO NOT USE! Uses an old way to process/format data."""
import obsoleteDataProcessing.dataToVar as dat
from scipy.interpolate import interp1d as interp
from obsoleteDataProcessing.thermalCompareQuant import listAvg
import numpy as np
import matplotlib.pyplot as plt


large45 = listAvg([dat.springV04r52a[0],dat.springV04r52b[0],dat.springV04r52c[0]],[dat.springV04r52a[2],dat.springV04r52b[2],dat.springV04r52c[2]])

small25 = listAvg([dat.slugV04r52a[0],dat.slugV04r52b[0],dat.slugV04r52c[0],dat.slugV04r52d[0]],[dat.slugV04r52a[2],dat.slugV04r52b[2],dat.slugV04r52c[2],dat.slugV04r52d[2]])

large45Time = np.arange(0,len(large45))
small25Time = np.arange(0,len(small25))

interp45 = interp(large45Time,large45)
interp25 = interp(small25Time,small25)

interpTime45 = interp(large45,large45Time)
interpTime25 = interp(small25,small25Time)


# plt.plot(interp45(large45Time))
# plt.grid()
# plt.show()


for i in large45[:100]:

    if i <=65:
        xx = i
for i in large45[100:200]:
    if i <= 85:
        yy = i
for i in large45[300:]-large45[300:][0]+85:
    if i >=small25[-1]:
        zz = i

for i in small25[:100]:
    if i <=65:
        aa = i
for i in small25[100:200]:
    if i <=85:
        bb = i
for i in small25[300:]-small25[300:][0]+85:
    if i <=small25[-1]:
        cc = i


print(small25.index(aa)+small25.index(bb)+list(small25[300:]-small25[300:][0]+85).index(cc)-
    large45.index(xx)-large45.index(yy)-list(large45[300:]-large45[300:][0]+85).index(zz))


print(list(small25[300:]-small25[300:][0]+85).index(cc)-list(large45[300:]-large45[300:][0]+85).index(zz))





import matplotlib.pyplot as plt
from thermalCompareQuant import interppp,listAvg
import dataToVar as dat





plt.figure()
# plt.plot(interppp([dat.slugV04r52a[0]],[dat.slugV04r52a[2]])[0],color='b',label='Larger Slug')
# plt.plot(interppp([dat.slugV04r52b[0]],[dat.slugV04r52b[2]])[0],color='b')
# plt.plot(interppp([dat.slugV04r52c[0]],[dat.slugV04r52c[2]])[0],color='b')
# plt.plot(interppp([dat.slugV04r52d[0]],[dat.slugV04r52d[2]])[0],color='b')

# plt.plot(interppp([dat.v04r52a[0]],[dat.v04r52a[2]])[0],color='g',label='Smaller Slug')
# plt.plot(interppp([dat.v04r52b[0]],[dat.v04r52b[2]])[0],color='g')
# plt.plot(interppp([dat.v04r52e[0]],[dat.v04r52e[2]])[0],color='g')
# plt.plot(interppp([dat.v04r52d[0]],[dat.v04r52d[2]])[0],color='g')
# plt.plot(interppp([dat.v04r52d[0]],[dat.v04r52d[4]])[0],color='k')

plt.plot(listAvg([dat.slugV04r52a[0],dat.slugV04r52b[0],dat.slugV04r52c[0],dat.slugV04r52d[0]],[dat.slugV04r52a[2],dat.slugV04r52b[2],dat.slugV04r52c[2],dat.slugV04r52d[2]]),label='Avg Large Slug')
plt.plot(listAvg([dat.v04r52a[0],dat.v04r52b[0],dat.v04r52e[0],dat.v04r52d[0]],[dat.v04r52a[2],dat.v04r52b[2],dat.v04r52e[2],dat.v04r52d[2]]),color='g',label='Avg Small Slug')
plt.plot(interppp([dat.v04r52d[0]],[dat.v04r52d[4]])[0],color='k')
plt.grid()
plt.ylabel('Temp (c)')
plt.xlabel('Time (sec)')
plt.title('Larger Slug vs Smaller Slug V04 5.2mm Insert')
plt.legend()
plt.show()

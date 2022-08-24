import matplotlib.pyplot as plt
from thermalCompareQuant import interppp,listAvg
import dataToVar as dat

# plt.plot(interppp([dat.springV04r52a[0]],[dat.springV04r52a[2]])[0],color='blue',label='Large Slug 4.5')
# plt.plot(interppp([dat.springV04r52b[0]],[dat.springV04r52b[2]])[0],color='blue')
# plt.plot(interppp([dat.springV04r52c[0]],[dat.springV04r52c[2]])[0],color='blue')

# plt.plot(interppp([dat.springV05r52a[0]],[dat.springV05r52a[2]])[0],color='red',label='Small Slug 4.5')
# plt.plot(interppp([dat.springV05r52b[0]],[dat.springV05r52b[2]])[0],color='red')
# plt.plot(interppp([dat.springV05r52c[0]],[dat.springV05r52c[2]])[0],color='red')


# plt.plot(interppp([dat.slugV04r52a[0]],[dat.slugV04r52a[2]])[0],color='orange',label='Large Slug 2.5')
# plt.plot(interppp([dat.slugV04r52b[0]],[dat.slugV04r52b[2]])[0],color='orange')
# plt.plot(interppp([dat.slugV04r52c[0]],[dat.slugV04r52c[2]])[0],color='orange')
# plt.plot(interppp([dat.slugV04r52d[0]],[dat.slugV04r52d[2]])[0],color='orange')

# plt.plot(interppp([dat.v04r52a[0]],[dat.v04r52a[2]])[0],color='g',label='Small Slug 2.5')
# plt.plot(interppp([dat.v04r52b[0]],[dat.v04r52b[2]])[0],color='g')
# plt.plot(interppp([dat.v04r52e[0]],[dat.v04r52e[2]])[0],color='g')
# plt.plot(interppp([dat.v04r52d[0]],[dat.v04r52d[2]])[0],color='g')
# plt.plot(interppp([dat.v04r52d[0]],[dat.v04r52d[4]])[0],color='k')


plt.plot(listAvg([dat.springV04r52a[0],dat.springV04r52b[0],dat.springV04r52c[0]],[dat.springV04r52a[2],dat.springV04r52b[2],dat.springV04r52c[2]]),color='b',label='Avg LargeSlug 4.5lb')
# plt.plot(listAvg([dat.springV05r52a[0],dat.springV05r52b[0],dat.springV05r52c[0]],[dat.springV05r52a[2],dat.springV05r52b[2],dat.springV05r52c[2]]),color='r',label='Avg small Slug 4.5lb')

# plt.plot(listAvg([dat.slugV04r52a[0],dat.slugV04r52b[0],dat.slugV04r52c[0],dat.slugV04r52d[0]],[dat.slugV04r52a[2],dat.slugV04r52b[2],dat.slugV04r52c[2],dat.slugV04r52d[2]]),color='orange',label='Avg Large Slug 2.5lb')
plt.plot(listAvg([dat.v04r52a[0],dat.v04r52b[0],dat.v04r52e[0],dat.v04r52d[0]],[dat.v04r52a[2],dat.v04r52b[2],dat.v04r52e[2],dat.v04r52d[2]]),color='g',label='Avg Small Slug 2.5lb')
plt.plot(interppp([dat.v04r52d[0]],[dat.v04r52d[4]])[0],color='k')
plt.grid()
plt.ylabel('Temp (c)')
plt.xlabel('Time (sec)')
plt.title('TC Spring Hold Down')
plt.legend()

plt.show()
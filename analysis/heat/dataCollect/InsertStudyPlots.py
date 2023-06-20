import matplotlib.pyplot as plt
import dataToVar as dat
from thermalCompareQuant import listStd,listAvg


plt.figure()
# plt.plot(dat.v04r46a[0][:len(dat.v04r46a[2])],dat.v04r46a[2],color='blue',label='4.6 Recessed')
# plt.plot(dat.v04r46b[0][:len(dat.v04r46b[2])],dat.v04r46b[2],color='blue')
# plt.plot(dat.v04r46c[0][:len(dat.v04r46c[2])],dat.v04r46c[2],color='blue')
# plt.plot(dat.v04r46d[0][:len(dat.v04r46d[2])],dat.v04r46d[2],color='blue')
# plt.plot(dat.v04r46e[0][:len(dat.v04r46e[2])],dat.v04r46e[2],color='blue')


plt.plot(dat.v04r52a[0][:len(dat.v04r52a[2])],dat.v04r52a[2],color='green',label='5.2 Recessed')
plt.plot(dat.v04r52b[0][:len(dat.v04r52b[2])],dat.v04r52b[2],color='green')
plt.plot(dat.v04r52c[0][:len(dat.v04r52c[2])],dat.v04r52c[2],color='green')
plt.plot(dat.v04r52d[0][:len(dat.v04r52d[2])],dat.v04r52d[2],color='green')
plt.plot(dat.v04r52e[0][:len(dat.v04r52e[2])],dat.v04r52e[2],color='green')

plt.plot(dat.v05r52a[0][:len(dat.v05r52a[2])],dat.v05r52a[2],color='green')
plt.plot(dat.v05r52b[0][:len(dat.v05r52b[2])],dat.v05r52b[2],color='green')
plt.plot(dat.v05r52c[0][:len(dat.v05r52c[2])],dat.v05r52c[2],color='green')
plt.plot(dat.v05r52d[0][:len(dat.v05r52d[2])],dat.v05r52d[2],color='green')

plt.plot(dat.v06r52a[0][:len(dat.v06r52a[2])],dat.v06r52a[2],color='green')
plt.plot(dat.v06r52b[0][:len(dat.v06r52b[2])],dat.v06r52b[2],color='green')
plt.plot(dat.v06r52c[0][:len(dat.v06r52c[2])],dat.v06r52c[2],color='green')
plt.plot(dat.v06r52d[0][:len(dat.v06r52d[2])],dat.v06r52d[2],color='green')
plt.plot(dat.v06r52e[0][:len(dat.v06r52e[2])],dat.v06r52e[2],color='green')


# plt.plot(dat.v04r57a[0][:len(dat.v04r57a[2])],dat.v04r57a[2],color='orange',label='5.7 Recessed')
# plt.plot(dat.v04r57b[0][:len(dat.v04r57b[2])],dat.v04r57b[2],color='orange')
# plt.plot(dat.v04r57c[0][:len(dat.v04r57c[2])],dat.v04r57c[2],color='orange')
# plt.plot(dat.v04r57d[0][:len(dat.v04r57d[2])],dat.v04r57d[2],color='orange')
# plt.plot(dat.v04r57e[0][:len(dat.v04r57e[2])],dat.v04r57e[2],color='orange')

# plt.plot(dat.v05r57a[0][:len(dat.v05r57a[2])],dat.v05r57a[2],color='orange')
# plt.plot(dat.v05r57b[0][:len(dat.v05r57b[2])],dat.v05r57b[2],color='orange')
# plt.plot(dat.v05r57c[0][:len(dat.v05r57c[2])],dat.v05r57c[2],color='orange')
# plt.plot(dat.v05r57d[0][:len(dat.v05r57d[2])],dat.v05r57d[2],color='orange')

# plt.plot(dat.v06r57a[0][:len(dat.v06r57a[2])],dat.v06r57a[2],color='orange')
# plt.plot(dat.v06r57b[0][:len(dat.v06r57b[2])],dat.v06r57b[2],color='orange')
# plt.plot(dat.v06r57c[0][:len(dat.v06r57c[2])],dat.v06r57c[2],color='orange')
# plt.plot(dat.v06r57d[0][:len(dat.v06r57d[2])],dat.v06r57d[2],color='orange')

plt.plot(dat.v04r46a[0][:len(dat.v04r46a[4])],dat.v04r46a[4],color='k')


plt.plot(dat.f06FlatFilla[0][:len(dat.f06FlatFilla[2])],dat.f06FlatFilla[2],color='purple',label='No Pedestal Fill')
plt.plot(dat.f06FlatFillb[0][:len(dat.f06FlatFillb[2])],dat.f06FlatFillb[2],color='purple')
plt.plot(dat.f06FlatFillc[0][:len(dat.f06FlatFillc[2])],dat.f06FlatFillc[2],color='purple')
plt.plot(dat.f06FlatFilld[0][:len(dat.f06FlatFilld[2])],dat.f06FlatFilld[2],color='purple')
plt.plot(dat.f06FlatFille[0][:len(dat.f06FlatFille[2])],dat.f06FlatFille[2],color='purple')

plt.plot(dat.f06FlatFillSeala[0][:len(dat.f06FlatFillSeala[2])],dat.f06FlatFillSeala[2],color='red',label='No Pedestal Fill Sealed')
plt.plot(dat.f06FlatFillSealb[0][:len(dat.f06FlatFillSealb[2])],dat.f06FlatFillSealb[2],color='red')
plt.plot(dat.f06FlatFillSealc[0][:len(dat.f06FlatFillSealc[2])],dat.f06FlatFillSealc[2],color='red')
plt.grid()
plt.title('Insert Height Comparison on Recessed Deck')
plt.ylabel('Temperature (C)')
plt.xlabel('Time (sec)')
plt.legend()


plt.figure() 
plt.plot(listStd([dat.v04r46a[0],dat.v04r46b[0],dat.v04r46c[0],dat.v04r46d[0],dat.v04r46e[0]],
    [dat.v04r46a[2],dat.v04r46b[2],dat.v04r46c[2],dat.v04r46d[2],dat.v04r46e[2]]),
    color='blue',label='4.6 Recessed')


plt.plot(listStd([dat.v04r52a[0],dat.v04r52b[0],dat.v04r52c[0],dat.v04r52d[0],dat.v04r52e[0],dat.v05r52a[0],dat.v05r52b[0],dat.v05r52c[0],dat.v05r52d[0],
    dat.v06r52a[0],dat.v06r52b[0],dat.v06r52c[0],dat.v06r52d[0],dat.v06r52e[0]],
    [dat.v04r52a[2],dat.v04r52b[2],dat.v04r52c[2],dat.v04r52d[2],dat.v04r52e[2],dat.v05r52a[2],dat.v05r52b[2],dat.v05r52c[2],dat.v05r52d[2],
    dat.v06r52a[2],dat.v06r52b[2],dat.v06r52c[2],dat.v06r52d[2],dat.v06r52e[2]]),
    color='green',label='5.2 Recessed')

plt.plot(listStd([dat.v04r57a[0],dat.v04r57b[0],dat.v04r57c[0],dat.v04r57d[0],dat.v04r57e[0],dat.v05r57a[0],dat.v05r57b[0],dat.v05r57c[0],dat.v05r57d[0],
    dat.v06r57a[0],dat.v06r57b[0],dat.v06r57c[0],dat.v06r57d[0]],
    [dat.v04r57a[2],dat.v04r57b[2],dat.v04r57c[2],dat.v04r57d[2],dat.v04r57e[2],dat.v05r57a[2],dat.v05r57b[2],dat.v05r57c[2],dat.v05r57d[2],
    dat.v06r57a[2],dat.v06r57b[2],dat.v06r57c[2],dat.v06r57d[2]]),
    color='orange',label='5.7 Recessed')
# plt.plot(dat.r46a[4],color='k')
plt.title('stdev by Insert')
plt.xlabel('Time (sec)')
plt.legend()
plt.grid()

plt.show()
import dataToVar as dat
import matplotlib.pyplot as plt


plt.plot(dat.a[2],label='proposed')
# plt.plot(dat.a[1])
plt.plot(dat.b[2],label='current')
# plt.plot(dat.b[1])
plt.legend()
plt.grid()
plt.show()
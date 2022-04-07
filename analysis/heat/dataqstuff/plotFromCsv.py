import dataToVar as dat
import matplotlib.pyplot as plt


plt.plot(dat.testa[2],label='proposed')
# plt.plot(dat.testa[1])
plt.plot(dat.testb[2],label='current')
# plt.plot(dat.testb[1])
plt.legend()
plt.grid()
plt.show()
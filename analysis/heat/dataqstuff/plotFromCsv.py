import dataToVar as dat
import matplotlib.pyplot as plt


# plt.plot(dat.testb[2],label='current')
# plt.plot(dat.testa[2],label='proposed')
# plt.plot(dat.b[2],label='new mod')
plt.plot(dat.test2[2],label='old')
plt.plot(dat.test1[2],label='new')
plt.plot(dat.test1[1])
plt.legend()
plt.grid()
plt.show()


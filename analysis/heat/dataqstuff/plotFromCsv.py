import dataToVar as dat
import matplotlib.pyplot as plt


# plt.plot(dat.testb[2],label='current')
# plt.plot(dat.testa[2],label='proposed')
# plt.plot(dat.b[2],label='new mod')
plt.plot(dat.uL700[2],label='700')
plt.plot(dat.uL800[2],label='800')
plt.plot(dat.test1[1])
plt.legend()
plt.grid()
plt.show()


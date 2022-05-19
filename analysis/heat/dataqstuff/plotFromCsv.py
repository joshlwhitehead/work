import dataToVar as dat
import matplotlib.pyplot as plt


# plt.plot(dat.testb[2],label='current')
# plt.plot(dat.testa[2],label='proposed')
# plt.plot(dat.b[2],label='new mod')
# plt.plot(dat.uL700[2],label='700')
# plt.plot(dat.uL800[2],label='800')
# plt.plot(dat.uL900[2],label='900')
# plt.plot(dat.uL700[1],'--')

plt.plot(dat.tight[2],label= 'tight')
plt.plot(dat.loose[2],label='saggy')
plt.plot(dat.loose[1])
plt.legend()
plt.grid()

plt.show()


from matplotlib.lines import lineStyles
import dataToVar as dat
import matplotlib.pyplot as plt
from thermalCompareQuant import listAvg,listStd

plt.plot(dat.forward1[0][:len(dat.forward1[2])],dat.forward1[2],label='Insert',color='blue')
plt.plot(dat.forward2[0][:len(dat.forward2[2])],dat.forward2[2],color='blue')
plt.plot(dat.forward3[0][:len(dat.forward3[2])],dat.forward3[2],color='blue')
# plt.plot(dat.backward1[0][:len(dat.backward1[2])],dat.backward1[2],label='backward',color='red')
# plt.plot(dat.backward2[0][:len(dat.backward2[2])],dat.backward2[2],color='red')
plt.plot(dat.noInsert1[0][:len(dat.noInsert1[2])],dat.noInsert1[2],label='noInsert',color='r')
plt.plot(dat.noInsert2[0][:len(dat.noInsert2[2])],dat.noInsert2[2],color='r')

plt.plot(dat.forward1[0][:len(dat.forward1[3])],dat.forward1[3],color='blue',linestyle='dashdot')
plt.plot(dat.forward2[0][:len(dat.forward2[3])],dat.forward2[3],color='blue',linestyle='dashdot')
plt.plot(dat.forward3[0][:len(dat.forward3[3])],dat.forward3[3],color='blue',linestyle='dashdot')
# plt.plot(dat.backward1[0][:len(dat.backward1[3])],dat.backward1[3],color='red',linestyle='dashdot')
# plt.plot(dat.backward2[0][:len(dat.backward2[3])],dat.backward2[3],color='red',linestyle='dashdot')
# plt.plot(dat.backward3[0][:len(dat.backward3[3])],dat.backward3[3],color='red',linestyle='dashdot')
# plt.plot(dat.backward4[0][:len(dat.backward4[3])],dat.backward4[3],color='red',linestyle='dashdot')
plt.plot(dat.noInsert1[0][:len(dat.noInsert1[3])],dat.noInsert1[3],color='r',linestyle='dashdot')
plt.plot(dat.noInsert2[0][:len(dat.noInsert2[3])],dat.noInsert2[3],color='r',linestyle='dashdot')



plt.grid()
plt.legend()

plt.show()
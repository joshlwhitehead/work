import matplotlib.pyplot as plt
import dataToVar as dat
from thermalCompareQuant import listAvg, listStd


"""ADV01"""

# plt.plot(dat.adv01_1[0][:len(dat.adv01_1[2])],dat.adv01_1[2])
# plt.plot(dat.adv01_2[0][:len(dat.adv01_2[2])],dat.adv01_2[2])
# plt.plot(dat.adv01_3[0][:len(dat.adv01_3[2])],dat.adv01_3[2])
# plt.plot(dat.adv01_1[0][:len(dat.adv01_1[4])],dat.adv01_1[4],'k',label='Model')
# plt.title('Adv01 Acceptance PCR Thermals')

plt.plot(listStd([dat.adv01_1[0],dat.adv01_2[0],dat.adv01_3[0]],
    [dat.adv01_1[2],dat.adv01_2[2],dat.adv01_3[2]]),
    label='Adv01')


"""ADV02"""
# plt.plot(dat.adv02_1[0][:len(dat.adv02_1[2])],dat.adv02_1[2])
# plt.plot(dat.adv02_2[0][:len(dat.adv02_2[2])],dat.adv02_2[2])
# plt.plot(dat.adv02_3[0][:len(dat.adv02_3[2])],dat.adv02_3[2])
# plt.plot(dat.adv02_1[0][:len(dat.adv02_1[4])],dat.adv02_1[4],'k',label='Model')
# plt.title('Adv02 Acceptance PCR Thermals')

plt.plot(listStd([dat.adv02_1[0],dat.adv02_2[0],dat.adv02_3[0]],
    [dat.adv02_1[2],dat.adv02_2[2],dat.adv02_3[2]]),
    label='Adv02')


"""ADV03"""
# plt.plot(dat.adv03_1[0][:len(dat.adv03_1[2])],dat.adv03_1[2])
# plt.plot(dat.adv03_2[0][:len(dat.adv03_2[2])],dat.adv03_2[2])
# plt.plot(dat.adv03_3[0][:len(dat.adv03_3[2])],dat.adv03_3[2])
# plt.plot(dat.adv03_1[0][:len(dat.adv03_1[4])],dat.adv03_1[4],'k',label='Model')
# plt.title('Adv03 Acceptance PCR Thermals')

plt.plot(listStd([dat.adv03_1[0],dat.adv03_2[0],dat.adv03_3[0]],
    [dat.adv03_1[2],dat.adv03_2[2],dat.adv03_3[2]]),
    label='Adv03')


"""ADV04"""
# plt.plot(dat.adv04_1[0][:len(dat.adv04_1[2])],dat.adv04_1[2])
# plt.plot(dat.adv04_2[0][:len(dat.adv04_2[2])],dat.adv04_2[2])
# plt.plot(dat.adv04_3[0][:len(dat.adv04_3[2])],dat.adv04_3[2])
# plt.plot(dat.adv04_1[0][:len(dat.adv04_1[4])],dat.adv04_1[4],'k',label='Model')
# plt.title('Adv04 Acceptance PCR Thermals')

plt.plot(listStd([dat.adv04_1[0],dat.adv04_2[0],dat.adv04_3[0]],
    [dat.adv04_1[2],dat.adv04_2[2],dat.adv04_3[2]]),
    label='Adv04')


plt.title('Acceptance PCR Stdev')
plt.xlabel('Time (sec)')
plt.ylabel('Temp (c)')
plt.legend()

plt.grid()
plt.show()
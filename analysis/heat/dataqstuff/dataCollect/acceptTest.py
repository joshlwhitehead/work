import matplotlib.pyplot as plt
import dataToVar as dat




# plt.plot(dat.adv01_1[0][:len(dat.adv01_1[2])],dat.adv01_1[2])
# plt.plot(dat.adv01_2[0][:len(dat.adv01_2[2])],dat.adv01_2[2])
# plt.plot(dat.adv01_3[0][:len(dat.adv01_3[2])],dat.adv01_3[2])
# plt.plot(dat.adv01_1[0][:len(dat.adv01_1[4])],dat.adv01_1[4],'k',label='Model')
# plt.title('Adv01 Acceptance TC Thermals')

# plt.plot(dat.adv02_1[0][:len(dat.adv02_1[2])],dat.adv02_1[2])
# plt.plot(dat.adv02_2[0][:len(dat.adv02_2[2])],dat.adv02_2[2])
# plt.plot(dat.adv02_3[0][:len(dat.adv02_3[2])],dat.adv02_3[2])
# plt.plot(dat.adv02_1[0][:len(dat.adv02_1[4])],dat.adv02_1[4],'k',label='Model')
# plt.title('Adv02 Acceptance TC Thermals')

# plt.plot(dat.adv03_1[0][:len(dat.adv03_1[2])],dat.adv03_1[2])
# plt.plot(dat.adv03_2[0][:len(dat.adv03_2[2])],dat.adv03_2[2])
# plt.plot(dat.adv03_3[0][:len(dat.adv03_3[2])],dat.adv03_3[2])
# plt.plot(dat.adv03_1[0][:len(dat.adv03_1[4])],dat.adv03_1[4],'k',label='Model')
# plt.title('Adv03 Acceptance TC Thermals')


plt.plot(dat.adv04_1[0][:len(dat.adv04_1[2])],dat.adv04_1[2])
plt.plot(dat.adv04_2[0][:len(dat.adv04_2[2])],dat.adv04_2[2])
plt.plot(dat.adv04_3[0][:len(dat.adv04_3[2])],dat.adv04_3[2])
plt.plot(dat.adv04_1[0][:len(dat.adv04_1[4])],dat.adv04_1[4],'k',label='Model')
plt.title('Adv04 Acceptance TC Thermals')

# plt.title('Adv03 Acceptance TC Thermals')
plt.xlabel('Time (sec)')
plt.ylabel('Temp (c)')
plt.legend()

plt.grid()
plt.show()
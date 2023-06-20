import dataToVar as dat
import matplotlib.pyplot as plt

plt.plot(dat.adv10_1[0][:len(dat.adv10_1[2])],dat.adv10_1[2])
plt.plot(dat.adv10_2[0][:len(dat.adv10_2[2])],dat.adv10_2[2])
plt.plot(dat.adv10_1[0][:len(dat.adv10_1[4])],dat.adv10_1[4],'k',label='Model')

plt.title('Adv10')

plt.xlabel('Time (sec)')
plt.ylabel('Temp (c)')
plt.legend()

plt.grid()
plt.show()
import dataToVar as dat
import matplotlib.pyplot as plt


# plt.plot(dat.testb[2],label='current')
# plt.plot(dat.testa[2],label='proposed')
# plt.plot(dat.b[2],label='new mod')
# plt.plot(dat.uL700[2],label='700')
# plt.plot(dat.uL800[2],label='800')
# plt.plot(dat.uL900[2],label='900')
# plt.plot(dat.uL700[1],'--')

# plt.plot(dat.tight[2],label= 'tight')
# plt.plot(dat.loose[2],label='saggy')
# plt.plot(dat.loose[1])
# plt.plot(dat.uL600_b[2],label='600')

# # plt.plot(dat.uL600[0][:len(dat.uL600[1])],dat.uL600[1],label='600Thermister')
plt.plot(dat.uL700[0][:len(dat.uL700[1])],dat.uL700[1],label='700')
# # plt.plot(dat.uL700[0][:len(dat.uL700[1])],dat.uL700[1],label='700Thermister')
plt.plot(dat.uL800[0][:len(dat.uL800[1])],dat.uL800[1],label='800')
plt.plot(dat.uL600[0][:len(dat.uL600[1])],dat.uL600[1],label='600')
# plt.plot(dat.uL700_d[1],label='700')

# plt.plot(dat.uL800_d[1],label='800')

# plt.plot(dat.uL600[0][:len(dat.uL600[1])],dat.uL600[1],label='600Thermister')
# plt.plot(dat.uL700_b[1],label='700')
# plt.plot(dat.uL700[0][:len(dat.uL700[1])],dat.uL700[1],label='700Thermister')

# plt.plot(dat.f1[0],dat.f1[1])
# plt.plot(dat.f2[0],dat.f2[1])
# plt.plot(dat.f3[0],dat.f3[1])
# plt.plot(dat.f4[0],dat.f4[1])

plt.legend()
plt.grid()

plt.show()


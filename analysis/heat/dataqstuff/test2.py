import dataToVar as dat
import matplotlib.pyplot as plt


# data1 = dat.frCupB_replace1
# # data = dat.frCupB_protB
# # data = dat.frCupB_ramp3
# data2 = dat.frCupB_replace2
# data = dat.fr_cupB_cons4_a
# # cons1B = dat.frCupB_cons1_b
# cons1C = dat.frCupB_cons1_c
# cons2A = dat.frCupB_cons2_a
# cons2B = dat.frCupB_cons2_b
# cons0A = dat.frCupB_cons0_a
data = dat.test4



therm = data[1][:]
samp = data[0][:]

trust = .9798
# Tset = 90
# offset = 0.16685153045254167*Tset - 4.854731864921983

new = []
old = samp[0]
count = 0
for i in therm:
    if count <= 100:
        Tset = 90
        offset = 0.16685153045254167*Tset - 4.854731864921983
    elif count > 100 and count <= 226:
        Tset = 75
        offset = 0.16685153045254167*Tset - 4.854731864921983
    elif count > 226 and count <= 286:
        Tset = 115
        offset = 0.16685153045254167*Tset - 4.854731864921983
    elif count > 286 and count <= 430:
        Tset = 105
        offset = 0.16685153045254167*Tset - 4.854731864921983
    elif count > 467 and count <= 534:
        Tset = 30
        offset = 0.16685153045254167*Tset - 4.854731864921983
    else:
        Tset = 60
        offset = 0.16685153045254167*Tset - 4.854731864921983
    new.append(old)
    old = trust*old+(1-trust)*(i-offset)
    count+=1
plt.plot(therm,label='thermister')
plt.plot(samp,label='new cup0')
plt.plot(new,label='mod')
# plt.plot(dat.noSeal1[0][:],label='2A')
# plt.plot(data1[0],label='new cup0')
# plt.plot(data2[0],label='x')
# plt.plot(cons2A[0][100:],label='cup2A')

plt.xlabel('time (sec)')
plt.ylabel('temp (c)')
plt.legend()
plt.grid()

plt.show()
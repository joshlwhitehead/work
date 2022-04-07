
"""
import dataToVar as dat
# from parsModTemp import parse

samp1 = dat.test1[0]
therm = dat.test1[1]
samp2 = dat.test2[0]
samp3 = dat.test3[0]

# mod = parse('data/15Mar2022/test.txt')
# count = 0
# newMod = []
# for i in mod:
#     if count%7 == 0:
#         newMod.append(i)
#     count+=1

import matplotlib.pyplot as plt
plt.plot(samp1)
plt.plot(samp2)
plt.plot(samp3)

# plt.plot(newMod)

plt.show()
# print(len(samp),len(mod))
"""


























import matplotlib.pyplot as plt
import numpy as np
import dataToVar as dat



fif = dat.cupB50
sev = dat.cupB70
nin = dat.cupB90
one = dat.cupB100









fifSamp = np.array(fif[0][100:len(sev[0])])
fifTherm = np.array(fif[1][100:len(sev[0])])
sevSamp = np.array(sev[0][100:len(sev[0])])
sevTherm = np.array(sev[1][100:len(sev[0])])
ninSamp = np.array(nin[0][100:len(sev[0])])
ninTherm = np.array(nin[1][100:len(sev[0])])
oneSamp = np.array(one[0][100:len(sev[0])])
oneTherm = np.array(one[1][100:len(sev[0])])
fifOff = fifTherm-fifSamp
sevOff = sevTherm-sevSamp
ninOff = ninTherm-ninSamp
oneOff = oneTherm-oneSamp








integral = []
ninSamp = ninSamp.tolist()
ninTherm = ninTherm.tolist()
for i in range(len(ninSamp)-1):
    x = 4
    A = (ninTherm[i+1] - ninTherm[i]) * ninOff[i]
    integral.append(A)

plt.plot(ninTherm[:-1],integral)
plt.grid()
plt.show()

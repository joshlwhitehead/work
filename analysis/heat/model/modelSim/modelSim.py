import matplotlib.pyplot as plt
import numpy as np
from parseTxt import TCTotal


def calculation(T0,offset,someTemp,lam,time):                               #someTemp is either thermistor temp or set temp
    return (-someTemp+offset+T0)*np.exp(-lam*(time))+someTemp-offset
def off(someTemp):
    a = -0.00272625
    b = .4613
    c = -12.603375
    return a*someTemp**2+b*someTemp+c

file = 'TCModelTuneTest.txt'

thermData = TCTotal(file)[1][0]
thermDataTime = TCTotal(file)[1][1]
sampData = TCTotal(file)[0][0]
sampDataTime = TCTotal(file)[0][1]
modelData = TCTotal(file)[2][0]
modelDataTime = TCTotal(file)[2][1]



start = 33

test = calculation(24,off(thermData),thermData,.1056,thermDataTime-52.136)
# print(test)

plt.plot(thermData[:])
plt.plot(sampData)
plt.plot(modelData)
plt.plot(test)
plt.grid()
plt.show()
# plt.savefig('test.png')


samp1 = sampData[33:69]
therm1 = thermData[33:69]
samp2 = sampData

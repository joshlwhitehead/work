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

plt.plot(thermDataTime,thermData[:],label='thermistor')
plt.plot(sampDataTime,sampData,label='sample')
plt.plot(modelDataTime,modelData,label='old model')
# plt.plot(thermDataTime,test,label='new model')
plt.grid()
plt.legend()
plt.show()
# plt.savefig('test.png')



therm1 = thermData[33:69]



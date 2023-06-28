import matplotlib.pyplot as plt
import numpy as np
from parseTxt import TCTotal


def calculation(T0,offset,someTemp,lam,time):                               #someTemp is either thermistor temp or set temp
    return (-someTemp+offset+T0)*np.exp(-lam*time)+someTemp-offset


file = 'TCModelTuneTest.txt'

thermData = TCTotal(file)[1][0]
thermDataTime = TCTotal(file)[1][1]
sampData = TCTotal(file)[0][0]
sampDataTime = TCTotal(file)[0][1]
modelData = TCTotal(file)[2][0]
modelDataTime = TCTotal(file)[2][1]


test = calculation(modelData[0],5.3,thermData,.1056,thermDataTime)


plt.plot(thermDataTime,thermData)
plt.plot(sampDataTime,sampData)
plt.plot(thermDataTime,test)
plt.show()
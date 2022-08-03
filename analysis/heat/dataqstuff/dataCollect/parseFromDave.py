import matplotlib.pyplot as plt
import numpy as np

file = open("data/02Aug2022/slowCool2.txt",'r')
file2 = open("data/02Aug2022/normCool1.txt",'r')

temp = []
for i in file:
    if "DATAQ:" in i:
        temp.append(float(i[27:32]))

time = np.arange(0,len(temp)*.5,.5)

temp2 = []
for i in file2:
    if "DATAQ:" in i:
        temp2.append(float(i[27:32]))

time2 = np.arange(0,len(temp2)*.5,.5)


plt.plot(time,temp)
plt.plot(time2,temp2)
plt.show()
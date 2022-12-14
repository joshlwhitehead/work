import os
import numpy as np

time = []
temp = []

for i in os.listdir('data'):
    file = open(''.join(['data/',i]),'r')
    time2 = []
    temp2 = []
    for u in file:
        if 'TC-' in u:
            u = u.split()
            if float(u[5][:-1]) >= 25:
                time2.append(float(u[0][1:-1])/1000)
                temp2.append(float(u[5][:-1]))
    time.append(np.array(time2)-time2[0])
    temp.append(temp2)
x = []
import matplotlib.pyplot as plt
for i in range(len(time)):
    
    plt.plot(time[i],temp[i])
    x.append(min(abs(90-np.array(temp[i]))))
    y = 
        

plt.show()



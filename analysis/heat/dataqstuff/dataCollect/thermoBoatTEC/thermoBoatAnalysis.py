import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





time = []
temp = []
indx = []
for i in os.listdir('data'):


    fileName = i#'Thermalboat 20221207 Rebuilt Run 3.txt'
    file = open(''.join(['data/',fileName]),'r')
    tempC = 90
    time2 = []
    temp2 = []
    absDif = []

    for u in file:
        if 'TC-' in u:
            u = u.split()
            if float(u[5][:-1]) >= 25:
                time2.append(float(u[0][1:-1])/1000)
                temp2.append(float(u[5][:-1]))
                absDif.append(abs(tempC-float(u[5][:-1])))
                
                

                
    time.append(np.array(time2)-time2[0])
    temp.append(temp2)
    indx.append(absDif.index(min(absDif)))
    timeNorm = np.array(time2)-time2[0]

    a,b,c,d = np.polyfit(timeNorm,temp2,3)


    # plt.plot(timeNorm,temp2,'o',label=fileName)
    # plt.plot(timeNorm,a*timeNorm**3+b*timeNorm**2+c*timeNorm+d)
    plt.plot(timeNorm,3*a*timeNorm**2+2*b*timeNorm+c,label=fileName)

    # print('\n',i)



    plt.ylabel('dT/dt (c/s)')
    plt.xlabel('Time (sec)')
    plt.grid()
    plt.legend()
plt.show()


times = []
for i in range(len(temp)):
    times.append(time[i][indx[i]])


temps = np.arange(40,115,10)

dF = pd.DataFrame({'fileName':os.listdir('data')[0]})







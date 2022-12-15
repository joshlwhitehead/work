import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




def timeToTemp(tempC):
    time = []
    temp = []
    indx = []

    for i in os.listdir('data'):
        file = open(''.join(['data/',i]),'r')
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
        
        plt.plot(np.array(time2)-time2[0],temp2,label=i)
    
    # print('\n',i)
    
    

    plt.ylabel('Temp (c)')
    plt.xlabel('Time (sec)')
    plt.grid()
    plt.legend()
    # plt.show()
    times = []
    for i in range(len(temp)):
        times.append(time[i][indx[i]])
    return times

temps = np.arange(40,115,10)

dF = {'fileName':os.listdir('data')}
for i in temps:
    dF[''.join(['timeTo',str(i),'C'])] = timeToTemp(i)

dF = pd.DataFrame(dF)
dF.to_csv('test.csv')






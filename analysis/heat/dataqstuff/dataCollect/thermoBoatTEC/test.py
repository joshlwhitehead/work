import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

timeTo = []
tempc = np.arange(40,115,10)
for k in os.listdir('data'):
    fileName = k#'Thermalboat 20221207 Rebuilt Run 3.txt'
    file = open(''.join(['data/',fileName]),'r')
    # tempC = 90
    time = []
    temp = []
    absDif = []

    for u in file:
        if 'TC-' in u:
            u = u.split()
            if float(u[5][:-1]) >= 25:
                time.append(float(u[0][1:-1])/1000)
                temp.append(float(u[5][:-1]))
                # absDif.append(abs(tempC-float(u[5][:-1])))
                
    

                


    time = np.array(time)-time[0]


    
    for u in tempc:
        absDif = []
        indx = []
        for i in temp:
            absDif.append(abs(u-i))

        indx = absDif.index(min(absDif))
        # print(time[indx])

        timeTo.append(time[indx])


timeTo = [timeTo[i:i+len(tempc)] for i in range(0,len(timeTo),len(tempc))]
print(np.array(timeTo).T)



dF = pd.DataFrame({'fileName':os.listdir('data')})



dF.to_csv('data.csv')








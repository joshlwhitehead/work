import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



file = pd.read_csv('pcrFillData.csv')
date = file['date']
m1 = file['m1']
m2 = file['m2']
m3 = file['m3']
m4 = file['m4']

t1 = file['t1']
t2 = file['t2']
t3 = file['t3']
t4 = file['t4']


m = [m1,m2,m3,m4]
t = [t1,t2,t3,t4]

dateSplit = []
for i in date:
    x = i.split('-')
    dateSplit.append(x)


day = []
for i in dateSplit:
    if 'Jan' in i:
        day.append(int(i[0])-int(dateSplit[0][0]))
    elif 'Feb' in i:
        day.append(int(i[0])-int(dateSplit[0][0])+31)
    elif 'Mar' in i:
        day.append(int(i[0])-int(dateSplit[0][0])+31+29)
day = np.array(day)


a,b = np.polyfit(day,m1,1)

plt.plot(day,m1,'o')
plt.plot(day,a*day+b)
plt.show()


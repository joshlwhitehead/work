import os

time = []
temp = []

for i in os.listdir('data'):
    file = open(''.join(['data/',i]),'r')
    time2 = []
    temp2 = []
    for u in file:
        if 'TC-' in u:
            u = u.split()
            time2.append(float(u[0][1:-1])/1000)
            temp2.append(float(u[5][:-1]))
    time.append(time2)
    temp.append(temp2)

import matplotlib.pyplot as plt
for i range(len(time))
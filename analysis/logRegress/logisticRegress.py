from testParse import parsPCRTxt
import matplotlib.pyplot as plt
import numpy as np
import os

folder = 'data/'

heatTherm = []
heatSamp = []
for i in os.listdir(folder):
    upsTherm = parsPCRTxt(''.join([folder,i]))[4][0]
    upsSamp = parsPCRTxt(''.join([folder,i]))[0][0]
    maxesTherm = []
    maxesSamp = []
    for u in range(len(upsTherm)):
        maxesTherm.append(max(upsTherm[u]))
    for u in maxesTherm:
        heatTherm.append(u)
    for u in range(len(upsSamp)):
        maxesSamp.append(max(upsSamp[u]))
    for u in maxesSamp:
        heatSamp.append(u)

# thermUps = parsPCRTxt('data/PThermo_AdvBuild07_w86_230301_run1.txt')[4][0]
# sampUps = parsPCRTxt('data/PThermo_AdvBuild07_w86_230301_run1.txt')[0][0]

# for i in thermUps:
#     heatTherm.append(max(i))
# for i in sampUps:
#     heatSamp.append(max(i))


plt.plot(heatTherm,heatSamp,'o')
plt.grid()
plt.show()


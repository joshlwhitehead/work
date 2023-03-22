from parsTxt import parsPCRTxt



data = 'Thermo_AdvBuild25_w87_230301_run1.txt'



heat = parsPCRTxt(data)[0][0]
timeHeat = parsPCRTxt(data)[0][1]
cool = parsPCRTxt(data)[1][0]
timeCool = parsPCRTxt(data)[1][1]



import matplotlib.pyplot as plt


total = []
count = 0
for i in range(len(heat)):
    for u in heat[i]:
        total.append(u)
    for u in cool[i]:
        total.append(u)

totalTime = []
for i in range(len(timeHeat)):
    for u in timeHeat[i]:
        totalTime.append(u)
    for u in timeCool[i]:
        totalTime.append(u)

plt.plot(totalTime,total,'o-')
plt.show()
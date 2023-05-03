import toleranceinterval as ti
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('dataForTI.csv')
part = data['Parts']
measure = data['Measurement'].tolist()


sort = []
count1 = 0
count2 = 18
for i in range(10):
    sort.append(measure[count1:count2])
    count1 += 18
    count2 += 18

count = 0
count3 = 0
y = np.arange(0,10)
for i in sort:
    x = ti.twoside.normal(i,.9,.9)
    xx = np.mean(i)
    print(part[count],x[0])
    plt.hlines(y[count3],x[0][0],x[0][1],lw=5)
    count += 18
    count3 += 1
plt.grid()
plt.title('90-90 TI')
plt.xlabel('PCR Thickness (mm)')
plt.ylabel('Cup')
plt.show()
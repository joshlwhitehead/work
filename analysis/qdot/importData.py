import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data5 = pd.read_excel('qDotJosh.xlsx','05 LED')
data6 = pd.read_excel('qDotJosh.xlsx','06 LED')
data7 = pd.read_excel('qDotJosh.xlsx','07 LED')
data10 = pd.read_excel('qDotJosh.xlsx','10 LED')
data13 = pd.read_excel('qDotJosh.xlsx','13 LED')
data25 = pd.read_excel('qDotJosh.xlsx','25 LED')
data26 = pd.read_excel('qDotJosh.xlsx','26 LED')
data27 = pd.read_excel('qDotJosh.xlsx','27 LED')


instData = [data5,data6,data7,data10,data13,data25,data26,data27]
inst = [5,6,7,10,13,25,26,27]


avg = []
for i in instData:
    avg.append(i['avg'][14])
avg = np.array(avg)

plt.scatter(inst,avg)
plt.grid()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data5 = pd.read_excel('qDotJosh.xlsx','05 LED')
data6 = pd.read_excel('qDotJosh.xlsx','06 LED')
data7 = pd.read_excel('qDotJosh.xlsx','07 LED')
data9 = pd.read_excel('qDotJosh.xlsx','09 LED')
data10 = pd.read_excel('qDotJosh.xlsx','10 LED')
data13 = pd.read_excel('qDotJosh.xlsx','13 LED')
data25 = pd.read_excel('qDotJosh.xlsx','25 LED')
data26 = pd.read_excel('qDotJosh.xlsx','26 LED')
data27 = pd.read_excel('qDotJosh.xlsx','27 LED')

data1 = pd.read_excel('qDotJosh.xlsx','01 Laser')
data2 = pd.read_excel('qDotJosh.xlsx','02 Laser')
data8 = pd.read_excel('qDotJosh.xlsx','08 Laser')
data11 = pd.read_excel('qDotJosh.xlsx','11 Laser')
data12 = pd.read_excel('qDotJosh.xlsx','12 Laser')
data15 = pd.read_excel('qDotJosh.xlsx','15 Laser')



instData = [data1,data2,data5,data6,data7,data8,data9,data10,data11,data12,data13,data15,data25,data26,data27]
inst = [1,2,5,6,7,8,9,10,11,12,13,15,25,26,27]


avg = []
for i in instData:
    avg.append(i['avg'][14])
avg = np.array(avg)

# plt.scatter(inst,avg)
# plt.grid()
# plt.show()


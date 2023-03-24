from parseTxt import parsPCRTxt
import matplotlib.pyplot as plt
import numpy as np


data = 'Josh_ADV13_03222023_Run1.txt'
model = parsPCRTxt(data)[0][0]
modTime = parsPCRTxt(data)[0][1]
fluor = parsPCRTxt(data)[1][0]
fluorTime = parsPCRTxt(data)[1][1]


# print(fluor)



count = 0
for i in range(len(model)-1):
    print((model[i+1]-model[i])/(modTime[i+1]-modTime[i]))

for i in range(len(fluor))


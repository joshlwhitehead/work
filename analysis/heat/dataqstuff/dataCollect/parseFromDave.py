import matplotlib.pyplot as plt
import numpy as np

with open('data/29Sep2022/triple_TC_short_Adv01_1.txt') as f:
    lines = f.readlines()


goodLines = []

for i in lines:
    if 'DATAQ:' in i:
        goodLines.append(i)
newFile = open('data/29Sep2022/triple_TC_short_Adv01_1_FIXED.txt','x')
newLines = []
for i in goodLines:
    newLines.append(i.replace(i,''.join([i[:83],'3',i[84:]])))



for i in newLines:
    newFile.writelines(i)
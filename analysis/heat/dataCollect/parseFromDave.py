import matplotlib.pyplot as plt
import numpy as np

with open('data/29Sep2022/triple_TC_short_Adv01_1.txt') as f:
    lines = f.readlines()



newLines = []

for i in lines:
    if 'DATAQ:' not in i:
        newLines.append(i)
    else:
        newLines.append(i.replace(i,''.join([i[:83],'3',i[84:]])))

newFile = open('data/29Sep2022/triple_TC_short_ADV01_1_FIXED.txt','w')
for i in newLines:
    newFile.write(i)

f.close()
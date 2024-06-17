import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd

p = "C:/Users/JoshWhitehea_5801ztl/work/functionsToKeep"
sys.path.append(p)
from confidenceFun import tukey



folderNom = 'injMold4_injMold5'
folderSwap = 'injMold4_injMold5_swap'


def fileList(folder):
    file = []
    for i in os.listdir(folder):
        if 'covered' not in i and '_cup' not in i:
            file.append(i)
            # print(i)
    return file

def parse(file,folder):
    with open('/'.join([folder,file])) as f:
        nm445 = []
        nm480 = []
        for i in f:
            try:
                if type(int(i[0])) == int:
                    x = i.split(',')
                    nm445.append(int(x[1]))
                    nm480.append(int(x[2]))
            except:
                pass
    return np.mean(nm445),np.mean(nm480)



def combineByWave(wave,folder):
    if wave == 445:
        y = 0
    elif wave == 480:
        y = 1
    injMold4 = []
    injMold5 = []
    for i in fileList(folder):
        if 'injMold4' in i:
            injMold4.append(parse(i,folder)[y])
        elif 'injMold5' in i:
            injMold5.append(parse(i,folder)[y])
    return injMold4,injMold5


im4 = combineByWave(445,folderNom)[0]
im5 = combineByWave(445,folderNom)[1]

im4Swap = combineByWave(445,folderSwap)[0]
im5Swap = combineByWave(445,folderSwap)[1]

newDict = {'config':[],'RFU':[]}
for i in im4:
    newDict['config'].append('im4')
    newDict['RFU'].append(i)
for i in im5:
    newDict['config'].append('im5')
    newDict['RFU'].append(i)

for i in im4Swap:
    newDict['config'].append('im4Swap')
    newDict['RFU'].append(i)
for i in im5Swap:
    newDict['config'].append('im5Swap')
    newDict['RFU'].append(i)

# print(newDict)

df = pd.DataFrame(newDict)



print(tukey(df,'config','RFU',0.1))





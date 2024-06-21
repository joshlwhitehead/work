import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd

p = "../../../functionsToKeep"
sys.path.append(p)
# print(sys.path)
from confidenceFun import tukey,caPlot



folderNom = 'injMold4_injMold5'
folderSwap = 'injMold4_injMold5_swap'
folderFluorSwap = 'im4_im5_fluorSwap'
folderrr = 'im4_im5_lastTry'


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
    return np.mean(nm445),np.mean(nm480),nm445,nm480

x = {}
for i in os.listdir(folderrr):
    z = i.split('_')
    z.remove(z[-1])
    z = '_'.join(z)
    if z in x.keys():
        x[z].append(parse(i,folderrr)[2])
    else:
        x[z] = [parse(i,folderrr)[2]]
# for i in os.listdir(folderSwap):
#     z = i.split('_')
#     z.remove(z[-1])
#     z = '_'.join(z)
#     if z in x.keys():
#         x[z].append(parse(i,folderSwap)[2])
#     else:
#         x[z] = [parse(i,folderSwap)[2]]
print(x.keys())

colors = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9']
count = 0
for i in x:
    if 'noCup' in i and 'covered' not in i:
        caPlot(x[i],0.1,colors[count],i)
        count += 1
plt.grid()
plt.legend()
plt.xlabel('Mean RFU')
# plt.show()

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

# im4Swap = combineByWave(445,folderSwap)[0]
# im5Swap = combineByWave(445,folderSwap)[1]

newDict = {'config':[],'RFU':[]}
for i in im4:
    newDict['config'].append('im4')
    newDict['RFU'].append(i)
for i in im5:
    newDict['config'].append('im5')
    newDict['RFU'].append(i)

# for i in im4Swap:
#     newDict['config'].append('im4Swap')
#     newDict['RFU'].append(i)
# for i in im5Swap:
#     newDict['config'].append('im5Swap')
#     newDict['RFU'].append(i)

# print(newDict)


        


# print(tukey(df,'config','RFU',0.1))





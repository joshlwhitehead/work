import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

both = pd.read_csv('Both.csv')
gblock = pd.read_csv('gBlock.csv')
lam = pd.read_csv('LAM.csv')
ntc = pd.read_csv('NTC.csv')

samp = [ntc,gblock,both,lam]
channels = ['515']
lab = ['NTC','ACTB','Both','LAM']

newlist = []
av5 = []
for i in samp:
    av = np.average(i['515'][:6])
    av5.append(av)
    newlist.append(np.array(i['515'].tolist()))
# print(av5)

backsub = []
count = 0
for i in newlist:
    backsub.append(i-av5[count])
    count+=1
# print(backsub)

count = 0
for i in backsub:
    plt.plot(i,label=''.join([lab[count],' 515nm']))
    count+=1
plt.grid()
plt.title('ACTB Lambda Duplex')
plt.ylabel('Fluorescence')
plt.xlabel('Cycle')
plt.legend()


plt.savefig('ampDuplex.png')
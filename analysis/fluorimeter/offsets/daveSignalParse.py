import numpy as np
import matplotlib.pyplot as plt
import os

folder = 'daveData/heelToToe'
folder2 = 'plots'
channelUsed = '515'

def parse(file):
    chan = {
        '415':[],'445':[],'480':[],'515':[],
        '555':[],'590':[],'630':[],'680':[],
        'NIR':[],'CLR':[],'DRK':[]
        }


    with open(file) as f:
        for i in f.readlines():
            for u in list(chan.keys()):
                if ''.join([u,':']) in i:
                    x = int(i.split(':')[-1])
                    chan[u].append(x)

    return chan
count = 0
for i in os.listdir(folder):
    x = parse('/'.join([folder,i]))[channelUsed]
    plt.plot(count,np.mean(x),'o')
    # plt.xticks(rotation=45)
    count += 1
plt.grid()
plt.ylabel('Signal (RFU)')
plt.xlabel('Number of Lines Drawn')
plt.title('515 nm')
plt.savefig(''.join([folder,'_',channelUsed,'.png']))
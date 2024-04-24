import numpy as np
import matplotlib.pyplot as plt
import os

folder = 'daveData/toeToHeel'
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

for i in os.listdir(folder):
    x = parse('/'.join([folder,i]))[channelUsed]
    plt.plot(i[:-4],np.mean(x),'o')
    plt.xticks(rotation=45)
plt.grid()
plt.savefig(''.join([channelUsed,'.png']))
import numpy as np

"""52"""



def listAvg(data):                              #all data should be same size
    avgData = []
    stdev = []
    for i in np.array(data).transpose():
        avgData.append(np.average(i))
        stdev.append(np.std(i))
    return avgData,stdev







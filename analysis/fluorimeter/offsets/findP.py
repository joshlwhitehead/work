import pandas as pd
import numpy as np

def findP(file):
    instList = [604,608,609,610,617,619,620,622,623,625]

    thumpP = 0
    noThumpP = 0
    totalThump = 0
    totalNoThump = 0
    for i in instList:
        data = pd.read_excel(file,str(i))
        thump = list(data['thumper'])
        offset = list(data['445 signal offset'])
        for indx,val in enumerate(thump):
            if val == 0:
                noThumpP += offset[indx]
                totalNoThump += 1
            else:
                thumpP += offset[indx]
                totalThump += 1
    return (thumpP,totalThump),(noThumpP,totalThump)


def findPByInst(file,tilt):

    instList = [604,608,609,610,617,619,620,622,623,625]
    thumpPList = []
    noThumpPList = []
    thumpThump = []
    thumpNoThump = []
    for i in instList:
        thumpNoise = 0
        noThumpNoise = 0
        totalThump = 0
        totalNoThump = 0
        data = pd.read_excel(file,str(i))
        thumper = list(data['thumper'])
        offset = list(data['445 signal offset'])
        for indx,val in enumerate(thumper):
            if val == 0:
                noThumpNoise += offset[indx]
                totalNoThump += 1
            else:
                thumpNoise += offset[indx]
                totalThump += 1

        thumpPList.append(thumpNoise/totalThump*100)
        noThumpPList.append(noThumpNoise/totalNoThump*100)
        if tilt == 0:
            thumpThump = ['thump no tilt']*len(thumpPList)
            thumpNoThump = ['no thump no tilt']*len(noThumpPList)
        else:
            thumpThump = ['thump tilt']*len(thumpPList)
            thumpNoThump = ['no thump tilt']*len(noThumpPList)
    totalFail = noThumpPList + thumpPList
    totalThump = thumpNoThump + thumpThump
    # print(len(totalFail),len(totalThump))
    return totalFail,totalThump





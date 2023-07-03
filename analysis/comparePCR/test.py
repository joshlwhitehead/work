import pandas as pd
data = pd.read_csv('BetaVAlpha.csv')
memo = data['memo']
inst = data['inst']

runOrder = {}
for indx,var in enumerate(memo):
    runOrder[int(var.split('.')[-1])] = inst[indx]



keys = list(runOrder.keys())
keys.sort()

sortDict = {i: runOrder[i] for i in keys}

for i in sortDict:
    if 'Beta' not in sortDict[i]:
        sortDict[i] = ''.join(['V',sortDict[i]])
keysFin = sortDict.keys()
valFin = sortDict.values()
newDict = {'run':keysFin,'inst':valFin}
dF = pd.DataFrame(newDict)
dF.to_csv('test.csv')




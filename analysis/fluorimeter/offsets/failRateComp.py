import pandas as pd
from confidenceFun import tukey
import numpy as np
import matplotlib.pyplot as plt
from findP import findPByInst

noTiltData = findPByInst('expandedData.xlsx',0)
tiltData = findPByInst('expandedTiltData.xlsx',1)
noTilt = noTiltData[0]
noTiltThump = noTiltData[1]
tilt = tiltData[0]
tiltThump = tiltData[1]


# tilt = np.array([7/7,5/7,6/7,.5/7,0/7,.5/7])*100
# noTilt = np.array([6.5/7,6.5/7,7/7,4/7,3/7,1.5/7])*100
# thumpSmall = ['no thump','no thump','no thump','thump','thump','thump']
# thumpLarge = sorted(['no thump','thump']*10)
# noTiltLarge = np.array([7/7,7/7,6.5/7,7/7,6.5/7,6/7,6/7,7/7,7/7,7/7,
#                         1/7,7/7,5.5/7,1.5/7,1/7,1.5/7,1/6,6.5/7,3.5/7,4/7])*100
# tiltLarge = np.array([7/7,7/7,4/7,7/7,7/7,6/7,5/7,6/7,6/7,7/7,
#                       0/7,.5/7,0/7,3/7,.5/7,2.5/7,0/7,2.5/7,1/7,1.5/7])*100

# j = tiltLarge[:10]
# print(j)
# print(np.mean(j))
# print(np.std(j))

thump = noTiltThump + tiltThump
fail = noTilt + tilt
df = {
    'thump':thump,
    'fail':fail
    }
df = pd.DataFrame(df)
df.boxplot(by='thump')
plt.title('')
plt.suptitle('')
plt.xlabel('Protocol')
plt.ylabel('Runs with Noise (%)')
plt.show()
print('THIS COMPARES INSTRUMENT FAIL RATES ON THUMPER VS NO THUMPER RUNS')
print(tukey(df,'thump','fail',.1))


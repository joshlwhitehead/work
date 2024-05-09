import pandas as pd
from confidenceFun import tukey
import numpy as np
import matplotlib.pyplot as plt



tilt = np.array([7/7,5/7,6/7,.5/7,0/7,.5/7])*100
noTilt = np.array([6.5/7,6.5/7,7/7,4/7,3/7,1.5/7])*100
thumpSmall = ['no thump','no thump','no thump','thump','thump','thump']
thumpLarge = sorted(['no thump','thump']*10)
noTiltLarge = np.array([7/7,7/7,6.5/7,7/7,6.5/7,6/7,6/7,7/7,7/7,7/7,
                        1/7,7/7,5.5/7,1.5/7,1/7,1.5/7,1/6,6.5/7,3.5/7,4/7])*100

j = noTiltLarge[10:]
print(j)
print(np.mean(j))
print(np.std(j))
df = {
    'thump':thumpLarge,
    'fail':noTiltLarge
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


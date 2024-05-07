import pandas as pd
from confidenceFun import tukey
import numpy as np
import matplotlib.pyplot as plt

j = [4/7,3/7,1.5/7]
print(np.mean(j))
print(np.std(j))

tilt = np.array([7/7,5/7,6/7,.5/7,0/7,.5/7])*100
noTilt = np.array([6.5/7,6.5/7,7/7,4/7,3/7,1.5/7])*100

df = {
    'thump':['no thump','no thump','no thump','thump','thump','thump'],
    'fail':tilt
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


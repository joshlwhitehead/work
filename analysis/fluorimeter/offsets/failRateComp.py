import pandas as pd
from confidenceFun import tukey
import numpy as np

# j = [3/7,1/7,3/7]
# print(np.std(j))



df = {
    'thump':['no thump','no thump','no thump','thump','thump','thump'],
    'fail':[6/7,7/7,6/7,3/7,3/7,1/7]
    }

print(tukey(df,'thump','fail',.1))


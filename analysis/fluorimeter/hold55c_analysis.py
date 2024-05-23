import pandas as pd
import numpy as np

base = pd.read_csv('hold55c/baseline.csv')
byInst = {585:[],591:[],602:[],599:[],588:[]}
for i in byInst:
    left = base['-'.join([str(i),'0'])]
    right = base['-'.join([str(i),'0'])]
    summary = np.mean([np.mean(left),np.mean(right)])
    byInst[i].append(summary)
    print(byInst[i])

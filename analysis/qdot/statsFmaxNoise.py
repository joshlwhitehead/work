import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('f07Snp.csv')

inst = (data['inst']).tolist()
fmax = (data['fmax']).tolist()
noisePcr = (data['pcr noise']).tolist()
noiseMelt = (data['melt noise']).tolist()

instSimp = [*set(inst)]
print(instSimp)
fmaxGood = []
instGood = []
pcrGood = []
meltGood = []
for i in range(len(fmax)):
    if fmax[i] >= 0:
        fmaxGood.append(fmax[i])
        instGood.append(fmax[i])
        pcrGood.append(fmax[i])
        meltGood.append(fmax[i])









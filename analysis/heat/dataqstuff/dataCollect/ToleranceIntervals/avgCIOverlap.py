import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.stats import t
from PCR_TI import anneal, denature


folder = 'padVpaste/'
folder2 = 'tape/'

instList = np.arange(0,len(os.listdir(folder)))
instList2 = np.arange(0,len(os.listdir(folder2)))

# print(len(instList))
overlap = 0
cis2 = anneal(folder2,instList2)
cis = anneal(folder,instList)


cisLeft = np.array([item[0] for item in cis])
cis2Right = np.array([item[1] for item in cis2])
# print(cisLeft)

for i in range(len(cisLeft)):
    for u in range(len(cis2Right)):
        if cis2Right[u] - cisLeft[i] > 0:
            overlap += (cis2Right[u]-cisLeft[i])

totalCi = 0
for i in cis:
    totalCi += i[1]-i[0]
for i in cis2:
    totalCi += i[1]-i[0]





print(overlap/totalCi )
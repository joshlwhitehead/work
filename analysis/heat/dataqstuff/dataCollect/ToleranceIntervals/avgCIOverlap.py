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
b = anneal(folder2,instList2)
a = anneal(folder,instList)
c = []
d = []
for i in a:
    c.append(i[0])
for i in b:
    d.append(i[1])
c = np.array(c)
d = np.array(d)
overlap = 0
for i in c:
    for u in d:
        test = u - i
        if test > 0:
            overlap += test


print(overlap)


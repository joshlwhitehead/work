# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:14:13 2021

@author: joshl
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


trial1_data = pd.read_csv('20210108 CF07 JW_4 amp data.csv')
run = trial1_data["Index"]
sample1= trial1_data['Sample 1']
sample2= trial1_data['Sample 2']
sample3= trial1_data['Sample 3']
sample4= trial1_data['Sample 4']



plt.close('all')

plt.plot(run,sample1,lw=4)
plt.plot(run,sample2,lw=4)
plt.plot(run,sample3,lw=4)
plt.plot(run,sample4,lw=4)

plt.xlabel('Cycle',size=40)
plt.ylabel('Fluorescence',size=40)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlim(0,39)
plt.ylim(0,np.max(sample4))
plt.grid()
plt.show()

print('F_max:',np.max(sample4))
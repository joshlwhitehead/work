# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:37:44 2021

@author: joshl
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


###IMPORT DATA INTO ARRAYS###

amp_data = pd.read_csv('seqtot.csv')

samp1 = amp_data['Deriv1']
samp2 = amp_data['Deriv2']
samp3 = amp_data['Deriv3']
samp4 = amp_data['Deriv4']
samp5 = amp_data['Deriv5']
samp6 = amp_data['Deriv6']

Temp1 = amp_data['Temp1']
Temp2 = amp_data['Temp2']
Temp3 = amp_data['Temp3']
Temp4 = amp_data['Temp4']
Temp5 = amp_data['Temp5']
Temp6 = amp_data['Temp6']

plt.close('all')

fig, ax=plt.subplots()

ax.plot(Temp1,samp1,lw=5,label='seq1')
ax.plot(Temp2,samp2,lw=5,label='seq2')
ax.plot(Temp3,samp3,lw=5,label='seq3')
ax.plot(Temp4,samp4,lw=5,label='seq4')
ax.plot(Temp5,samp5,lw=5,label='seq5')
ax.plot(Temp6,samp6,lw=5,label='seq6')
ax.tick_params(labelsize=30)

plt.ylim(0,80,5)
ax.legend(prop={'size':40})

plt.xlabel('Temperature',size=40)
plt.ylabel('-dF/dt',size=40)
ax.grid()
plt.show()
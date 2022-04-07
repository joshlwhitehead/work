import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('maddisonRun.csv')
x = data['Temp C']
y = data['515']

deriv = []
for i in range(len(y)-1):
    deriv.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    print('ok')

plt.plot(deriv)
plt.xlabel('T (c)')
plt.ylabel('F')
plt.grid()
plt.show()



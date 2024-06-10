from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-4,4,999)

pdf = stats.norm.pdf(z,scale=.5)
pdf2 = stats.norm.pdf(z)
pdf3 = stats.norm.pdf(z,scale=2)

plt.plot(z,pdf2,lw=3,label='std = 1')
plt.plot(z,pdf,lw=3,label='std = 0.5')
plt.plot(z,pdf3,lw=3,label='std = 2')
plt.vlines(0,0,0.8,linestyles='--',lw=3,color='k',label='mean = 0')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.grid()
plt.legend()
plt.savefig('test.png')
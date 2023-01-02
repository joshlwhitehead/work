import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats




data = pd.read_csv('convertcsv (1).csv')

x = np.linspace(min(data['numericValue']),max(data['numericValue']))





print(stats.anderson(data['numericValue']))






data.hist('numericValue')





plt.plot(x,stats.norm.pdf(x,loc=np.mean(data['numericValue']),scale=np.std(data['numericValue'])))
plt.show()



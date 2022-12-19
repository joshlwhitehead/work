import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


data = pd.read_csv('f09AT.csv')
# data.fmax.dropna
data.boxplot('fmax',by='inst')
# data.boxplot('tm',by='inst')
plt.show()
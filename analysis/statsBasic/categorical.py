import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('Book1.csv')

data[['alg call','hum call']].hist(stacked=True)

plt.show()
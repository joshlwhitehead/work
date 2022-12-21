from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('data/fillStuff/Adv10DecFills.csv')
fill = data['numericValue']
inst = np.ones(len(fill))*10
data['inst'] = inst



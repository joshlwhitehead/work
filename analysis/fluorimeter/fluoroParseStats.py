"""get fluorimetry data and calc basic stats (mean, std, ci, ti) to be used for future analysis and comparison"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from confidenceFun import CI

def parseCsv(csv):
    data = pd.read_csv(csv)
    dataDict = {}
    for i in data.columns:
        dataDict[i] = list(data[i])
    return dataDict


def stats(pop,alpha):
    mean = np.mean(pop)
    std = np.std(pop)
    ci = CI(pop,alpha)
    return mean,std,ci






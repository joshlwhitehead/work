import toleranceinterval as ti
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


test = [1.278,1.294,1.3,1.304,1.309,1.312,1.317,1.353]

print(ti.twoside.normal(test,.9,.95))
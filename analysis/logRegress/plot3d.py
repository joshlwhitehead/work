# importing mplot3d toolkits
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection ='3d')
data = pd.read_csv('dataForTI.csv')
# defining axes
z = data['Measurement']
x = data['Operators']
y = data['Parts']
# c = x + y
ax.scatter(x, y, z, c = 'r')
ax.set_xlabel('Operator')
ax.set_ylabel('Part')
ax.set_zlabel('Measurementc')

# syntax for plotting
ax.set_title('3d Scatter plot geeks for geeks')
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
x = np.array([1,2,3,4,5])
y = np.array([5,4,3,4,5])

x1,y1 = np.meshgrid(x,y)
z =x1*y1



# ax = plt.axes(projection='3d')

# ax.plot_surface(x1,y1,z)
# plt.show()
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def f(x, y):
    return np.log(x**3)+3*y
plt.close('all')
x = np.array([0,1,2,3,4,5])
y = np.array([1,2,3,4,5])

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,200)
plt.show()

# data = 'test_deriv.csv'




# temp = pd.read_csv(data)['T']
# channels = np.array([515,555,590,630,680])
# T = np.array(temp.tolist())
# yes,no = np.meshgrid(T,channels)




# def fun(a):
#     c = []
#     for i in a:
#         c.append(np.array(pd.read_csv(data)[str(i)].tolist()))
#     return np.array(c)
# hal = fun(channels)





# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(yes,hal,no,200)

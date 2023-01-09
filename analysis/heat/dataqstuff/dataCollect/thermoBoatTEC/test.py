import numpy as np


josh = np.array([1,2,3,4])
tess = np.array([1,1,1,1])
if np.any(josh) > np.any(tess):
    print('y')

print(np.any(josh))
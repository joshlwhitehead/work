import numpy as np
from scipy import interpolate as interp
import matplotlib.pyplot as plt



josh = [1.1,2.1,3.234,4.44]
tess = [1,2,3,4]


x = interp.interp1d(tess,josh)


print(x([2.5,3]))

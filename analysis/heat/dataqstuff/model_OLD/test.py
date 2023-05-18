import dataToVar as dat
import numpy as np
import matplotlib.pyplot as plt

a = dat.h100
b = dat.h90
c = dat.h70
d = dat.h50




plt.plot(a[0][:-4],a[2])
plt.plot(b[0][:-4],b[2])
plt.plot(c[0][:-4],c[2])
plt.plot(d[0][:-4],d[2])
plt.show()
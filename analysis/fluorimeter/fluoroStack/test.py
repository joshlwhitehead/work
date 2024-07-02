<<<<<<< HEAD
import numpy as np
print(np.exp(3))
=======
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

mean = 0
std = 1


x = np.linspace(-4,4,999)
y = norm.pdf(x,loc=mean,scale=std)
yy = norm.pdf(x,loc=mean,scale=.8)
yyy = norm.pdf(x,loc=mean,scale=2)

plt.plot(x,y)
plt.plot(x,yy)
plt.plot(x,yyy)
plt.grid()
plt.show()
>>>>>>> 4ea4d9b354a83d57d0c7fe827d69a1ce4aaf321f

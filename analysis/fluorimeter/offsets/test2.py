import numpy as np
from scipy.stats import norm
alpha = 0.1
n = 21
p = 8/21
mean = n*p
stdev = np.sqrt(mean*(1-p))

se = stdev/np.sqrt(n)
z = norm.ppf(1-.5*alpha)
moe = z*se
print(moe)
print((mean-moe)/21,(mean+moe)/21)
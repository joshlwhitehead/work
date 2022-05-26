from scipy import integrate
import numpy as np


T = np.arange(295,380,5)
def k(temp):
    return -7.78122E-6*temp**2 + 6.14773E-03*temp- 5.30691E-1
fun = []
for i in T:

    inte = integrate.quad(k,i,i+1)
print(inte)
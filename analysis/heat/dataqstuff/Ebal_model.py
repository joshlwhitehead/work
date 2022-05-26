import numpy as np
k1 = .2
k2 = .2
l1 = .00013
l2 = .0006
Tinf = 30
ro = 997
cp = 4.2
dx = .006

def dTdt(T1,T2):
    return (T2*(-k1/l1-k2/l2)+k1/l1*T1+k2/l2*Tinf)/ro/cp/dx
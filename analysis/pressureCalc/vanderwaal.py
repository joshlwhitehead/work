import numpy as np

R = 8.314
V = .7
ro = 1/18
Tc = 647.3
Pc = 22.12

a = 27/64*R**2*Tc**2/Pc
b = R*Tc/8/Pc

def P(T):
    P = R*T/(V-b)-a/V**2
    return P

print(P(293.15))


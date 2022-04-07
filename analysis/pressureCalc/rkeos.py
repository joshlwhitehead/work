import numpy as np

R = 8.314
V = 18/.7
w = .344
om = .48+1.57*w-.176*w**2
Tc = 647.3                                      #K
Pc = 22.12 

b = .08664*R*Tc/Pc

def P(T):
    a = 0.42748*R*2*Tc**2/Pc*(1+om*(1-np.sqrt(T/Tc)))**2

    return R*T/(V-b) - a/(V**2+b*V)


print(P(373.15))
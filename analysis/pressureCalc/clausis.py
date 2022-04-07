import numpy as np

T1 = 90+273.15
P1 = .0702
P2 = np.linspace(.0702,.1987)

dHv = 2282.49 * 18
R = 8.314

def T(P):
    inv = 1/T1-np.log(P/P1)*R/dHv
    return 1/inv

def P(T):
    return np.exp(dHv/R*(1/T1-1/T))*P1
# print(P(115+273.15))
# print(T(P2)-273.15)

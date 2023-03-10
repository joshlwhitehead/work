import numpy as np
import matplotlib.pyplot as plt

def flux(k,L,Ts,Ti,F0):
    return k*(Ts-Ti)/L/np.sqrt(np.pi*F0)



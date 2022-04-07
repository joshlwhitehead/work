import numpy as np

k = 0.598
z2 = .00448
T1 = 100
T2 = 23
ro = 997
cp = 4186

c1 = (k*(T2-T1)-ro*cp*z2**2/2)/2
c2 = k*T1

r = .007225

A = np.pi*r**2
h = 20
Bi = (z2/k/A)/(1/h/A)
print(Bi)
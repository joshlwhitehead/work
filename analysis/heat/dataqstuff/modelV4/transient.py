import numpy as np
import matplotlib.pyplot as plt

def interpBasic(y1,y2,x,x1,x2):
    y = y1+(x-x1)*(y2-y1)/(x2-x1)
    return y

Tinf = 90
Ti = 20
k = .648
h = 10
L = .011
ro = 982.36
cp = 4190
Bi = h*L/k
x = np.linspace(0,L)
t = np.linspace(0,100,10)

si1 = interpBasic(.1987,.2425,Bi,.06,.04)
si2 = interpBasic(3.1543,3.1606,Bi,.06,.04)
si3 = interpBasic(6.2895,6.2927,Bi,.06,.04)
si4 = interpBasic(9.429,9.4311,Bi,.06,.04)
si = np.array([si1,si2,si3,si4])

def theta(si,F0,xStar):
    ans = 0
    for i in si:
        Cn = 4*np.sin(i)/(2*i+np.sin(2*i))
        ans += Cn*np.exp(-i**2*F0)*np.cos(i*xStar)

    return ans*(Ti-Tinf)+Tinf

# F = k*5/ro/cp/L**2
# theta(si,F,x/L)

for i in t:
    plt.plot(x,theta(si,k*i/ro/cp/L**2,x/L))

plt.show()
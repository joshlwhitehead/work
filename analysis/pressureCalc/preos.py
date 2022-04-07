import numpy as np

R = 8.314                                       #MPa*mL/mol/K
Tc = 647.3                                      #K
Pc = 22.12                                      #MPa
w = .344                                         
k = 0.37464+1.54226*w-0.26992*w**2
ro = 18                                #mol



ac = 0.45723553*R**2*Tc**2/Pc

b = 0.07779607*R*Tc/Pc


def P(T):
    alpha = (1+k*(1-np.sqrt(T/Tc)))**2
    P = R*T/(ro-b) - ac*alpha/(ro**2+2*b*ro-b**2)
    return P

print(P(373.15))


# def dP(T):
#     alpha = (1+k*(1-np.sqrt(T/Tc)))**2
#     p = R*ro/(1-b*ro) - ro**2*-ac*k*np.sqrt(alpha*T/Tc)/T/(1+2*b*ro-b**2*ro**2)
#     return p
# print(dP(273.15+110))




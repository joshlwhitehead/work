R = 8.314                                   #MPa*cm3/mol/k
Tc = 374+273.15                                    #K
Pc = 22.064                                 #MPa

a = 0.42748 * R**2 * Tc**2.5/Pc
b = 0.08664*R*Tc/Pc


def P(T,V):
    P = R*T/(V-b) - (a/T**.5)/(V**2+b*V)
    return P

print(P(95+273.15,.7))
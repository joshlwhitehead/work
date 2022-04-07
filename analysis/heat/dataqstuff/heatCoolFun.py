import numpy as np

a = 0.11625215
b = 1.02276983
c = 4.34675494
d = -.19308765
e = .12217722
f = 1.57726581
g = 20.43056504
h = 30.51632196

aa = 5.30247176e-2
bb = 1.74564579e1
cc = 6.91011121e2
dd = -1.05344032
ee = 2.87545538e-1
ff = 9.18976500e-1
gg = -2.69715607e-1
hh = 7.08959527



def TsampHeat(time,T0,Tset,Tmax):#,a,b,c,d,e,f,g,h):
    return (a*np.log(time**b+c)+d)*(e*(Tset-Tmax)**f+g)+h-T0+30

def TsampCool(time,T0,Tset):#,aa,bb,cc,dd,ee,ff,gg,hh):
    return -1*((aa*np.log(time**bb+cc)+dd)*(ee*(T0-Tset)**ff+gg)+hh)+T0+1

def TsetHeat(Tmax,Tsamp,T0,time):#,a,b,c,d,e,f,g,h):
    return Tmax + (((Tsamp+T0-30+h)/(a*np.log(time**b+c)+d)-g)/e)**(1/f)

def TsetCool(T0,Tsamp,time):#,aa,bb,cc,dd,ee,ff,gg,hh):
    return T0-(((T0+1-hh-Tsamp)/(aa*np.log(time**bb+cc)+dd)-gg)/ee)**(1/ff)

def timeHeat(T0,Tsamp,Tmax,Tset):#,a,b,c,d,e,f,g,h):
    return (np.exp(((Tsamp-h+T0-30)/(e*(Tset-Tmax)**f+g)-d)/a)-c)**(1/b)

def timeCool(T0,Tsamp,Tset):#,aa,bb,cc,dd,ee,ff,gg,hh):
    (np.exp(((T0+1-Tsamp)/((ee*(T0-Tset)**ff+gg)+hh)-dd)/aa)-cc)**(1/bb)



print(TsampHeat(120,30,90,30))


print(timeHeat(30,70,30,130))



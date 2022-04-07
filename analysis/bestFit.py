import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

y = np.array([0,2,3,4,3,3,5,3,4,5,4,7,5,8,10,10,9,6,11])
x = np.arange(0,len(y))

def logFun(x,a,b,c,d,e):
    return a*np.log(x+b)+c
def polyWut(x,a,A,b,B,c,C,d,D):
    return a*x**A+b*x**B+c*x**C+d*x**D
r2 = []
for i in range(1,6):
    if i ==1:
        try:
            a,b = np.polyfit(x,y,i)
            fitFun = a*x+b
            st = sum((y-np.average(y))**2)
            sr = sum((y-fitFun)**2)
            r2.append(round(1-sr/st,3))
        except:
            pass
    elif i == 2:
        try:
            a,b,c = np.polyfit(x,y,i)
            fitFun = a*x**2+b*x+c
            st = sum((y-np.average(y))**2)
            sr = sum((y-fitFun)**2)
            r2.append(round(1-sr/st,3))
        except:
            pass
    elif i == 3:
        try:
            a,b,c,d = np.polyfit(x,y,i)
            fitFun = a*x**3+b*x**2+c*x+d
            st = sum((y-np.average(y))**2)
            sr = sum((y-fitFun)**2)
            r2.append(round(1-sr/st,3))
        except:
            pass
    elif i == 4:
        try:
            param,xxx = opt.curve_fit(logFun,x,y)
            fitFun = logFun(x,*param)
            st = sum((y-np.average(y))**2)
            sr = sum((y-fitFun)**2)
            r2.append(round(1-sr/st,3))
        except:
            pass
    elif i ==5:
        try:
            param,xxx = opt.curve_fit(polyWut,x,y)
            fitFun = polyWut(x,*param)
            st = sum((y-np.average(y))**2)
            sr = sum((y-fitFun)**2)
            r2.append(round(1-sr/st,3))
            
        except:
            pass

    


print(r2,'\n',len(r2))

plt.plot(y,'o')
# plt.plot(a*x+b)
plt.show()
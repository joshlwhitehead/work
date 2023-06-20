import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit



def parse(file):
    with open(file,'r') as readFile:                                                                                        #convert lines in file to list
        file = readFile.readlines()

    stop = False
    thermData = []
    thermTime = []
    tCoupData = []
    tCoupTime = []
    countLines = 0
    for i in file:
        if 'DATAQ:' in i and not stop:
            tCoupData.append(float(i.split()[4].strip(',')))
            try:
                    tCoupTime.append(float(file[countLines-1].split()[0].strip('()'))/1000)
                    # totalTime.append(float(file[countLines-1].split()[0].strip('()'))/1000)
            except:
                if file[countLines+1].split()[0] != 'DATAQ:':
                    tCoupTime.append(float(file[countLines+1].split()[0].strip('()'))/1000)
                else:
                    try:
                        tCoupTime.append(float(file[countLines-2].split()[0].strip('()'))/1000)
                    except:
                        try:
                            tCoupTime.append(float(file[countLines+2].split()[0].strip('()'))/1000)
                        except:
                            print(file[countLines])
                            tCoupTime.append(float(file[countLines-3].split()[0].strip('()'))/1000)
        elif 'modeled' in i and not stop:
            thermData.append(float(i.split()[4].strip(',')))
            thermTime.append(float(i.split()[0].strip('()'))/1000)
            if float(i.split()[4].strip(',')) > 114:
                stop = True
        
        countLines += 1
    thermTime = np.array(thermTime)-thermTime[0]
    tCoupTime = np.array(tCoupTime)-tCoupTime[0]
    return (thermTime,thermData),(tCoupTime,tCoupData)
def r2(y,fit):
    y = np.array(y)
    fit = np.array(fit)
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2

def test(x,a,b):
    return a*np.log(x+8.11522678)+b



file = 'data/JW_mod4_tcInMiddle_1.txt'


x1,y1 = parse(file)[0]
x2,y2 = parse(file)[1]





pop1,pcov1 = curve_fit(test,x1,y1)
pop2,pcov2 = curve_fit(test,x2,y2)








newX1 = interp1d(x1,y1)
newX2 = interp1d(x2,y2)
x11 = np.linspace(x1[0],x1[-1])
y11 = newX1(x11)
x22 = np.linspace(x2[0],x2[-1])
y22 = newX2(x22)




def d3fun(xt,a,b,c,d,e,f,g,h):
    x,t = xt
    return (a*np.log(t**b+c)+d)*(e*x**f+g)+h
dx = [0,.0021]
x = []
t = []
T = []

for i in dx:
    for u in y22:
        x.append(i)

y = [x11,x22]
z = np.array([y11,y22])
for i in y:
    for u in i:
        t.append(u)
for i in z:
    for u in i:
        T.append(u)
print(len(x),len(t),len(T))


# pop3,pcov3 = curve_fit(d3fun,[x,t],T)


from sklearn import linear_model
import pandas as pd

dftime = x22.tolist()*2
dfdist = []
for i in dx:
    for u in x22:
        dfdist.append(i)
dftemp = []
for i in z:
    for u in i:
        dftemp.append(u)

dFx = {'time':dftime,'dist':dfdist,'temp':dftemp}
dF = pd.DataFrame(dFx)
# print(len(dftemp),len(dftime),len(dfdist))

X = dF[['time', 'dist']]
y = dF['temp']

regr = linear_model.LinearRegression()
regr.fit(X, y)

timetime = np.linspace(min(x22),max(x22))
distdist = np.linspace(0,0.0021)

pre = regr.predict([[5,0.0021]])
print(pre)

time,dist = np.meshgrid(x11,dx)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(time,dist,z,label='data')
# ax.plot_wireframe(timetime,distdist,regr.predict([[timetime,distdist]]))
# ax.plot_wireframe(time,dist,d3fun([time,dist],*pop3),color='orange',label='fit')
ax.legend()
plt.show()


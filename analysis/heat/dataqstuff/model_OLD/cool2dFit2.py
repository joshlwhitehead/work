import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import dataToVar as dat

c30 = np.array(dat.cNewCup30)
c50 = np.array(dat.cNewCup50)
c70 = np.array(dat.cNewCup70)

thirSamp = c30[0][500:]*-1-np.min(c30[0][500:]*-1)
fifSamp = c50[0][500:]*-1-np.min(c50[0][500:]*-1)
sevSamp = c70[0][500:]*-1-np.min(c70[0][500:]*-1)

thirTherm = (c30[1][500:]*-1+90)/60
fifTherm = (c50[1][500:]*-1+90)/40                  #***********************************
sevTherm = (c70[1][500:]*-1+90)/20
# print(np.min(c30[0][500:]*-1))
# print(np.min(c70[0][500:]*-1))
# plt.plot(thirTherm,thirSamp)
# plt.plot(fifTherm,fifSamp)
# plt.plot(sevTherm,sevSamp)
# plt.grid()
# plt.show()


lessOne = []
for i in fifTherm:
    if i <= 1:
        # print(i)
        lessOne.append(i)
    else:
        break
lessOne = np.array(lessOne)

a,b,c,d = np.polyfit(lessOne,thirSamp[:len(lessOne)],3)
print(a,b,c,d)
def fitFun(x,a,b,c,d,e,f,g):
    return a*(x+b)**c+d
    
coef1,xxx = opt.curve_fit(fitFun,lessOne,thirSamp[:len(lessOne)])

def r2(y,fun):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fun)**2)
    r2 = 1-sr/st
    return round(r2,3)

# print(r2(thirSamp[:len(lessOne)],a*lessOne**3+b*lessOne**2+c*lessOne+d))
# # print(r2(thirSamp[:len(lessOne)],fitFun(lessOne,*coef1)))
# plt.plot(lessOne,thirSamp[:len(lessOne)])
# plt.plot(lessOne,a*lessOne**3+b*lessOne**2+c*lessOne+d)
# # plt.plot(lessOne,fitFun(lessOne,*coef1))
# # plt.plot(lessOne,fifSamp[:len(lessOne)])
# # plt.plot(lessOne,sevSamp[:len(lessOne)])
# plt.grid()
# plt.show()






# plt.plot(thirSamp[len(lessOne):])
# plt.plot(fifSamp[len(lessOne):])
# plt.plot(sevSamp[len(lessOne):])
# plt.show()

def percFit(list):
    err = []
    ratioBot = np.average(list[-100:])/list
    for i in ratioBot:
        if i>1.05:
            err.append(i)
    # percy = list[100:len(err)]
    # percx = np.arange(0,len(percy))
    
    return np.array(list[:len(err)])

percThir = percFit(thirSamp[len(lessOne):])
percFif = percFit(fifSamp[len(lessOne):])
percSev = percFit(sevSamp[len(lessOne):])

thir2 = (percThir)#-percThir[0])
fif2 = (fifSamp[len(lessOne):len(percThir)+len(lessOne)])#-fifSamp[len(lessOne):len(percThir)+len(lessOne)][0])
sev2 = (sevSamp[len(lessOne):len(percThir)+len(lessOne)])#-sevSamp[len(lessOne):len(percThir)+len(lessOne)][0])

# plt.plot(thir2)
# plt.plot(fif2)
# plt.plot(sev2)
# plt.savefig('x')

tset = [20,40,60]
num = np.arange(0,len(thir2))
SAMP = np.array([thir2,fif2,sev2])
NUM,TSET = np.meshgrid(num,tset)


x = []
y = []
z = []
for i in tset:
    for u in num:
        y.append(i)
        x.append(u)
for i in SAMP:
    for u in i:
        z.append(u)

def fitSurf(xy,a,b,c,d,e,f,g):
    x = xy[0]
    y = xy[1]
    return (a*np.log(x+b)+c) * (d*(y+e)**f+g)                                                              #############################################################################################################




coef3d,xxx = opt.curve_fit(fitSurf,[x,y],z)

print(coef3d)
def r2surf():
    zlist = []
    for i in SAMP:
        for u in i:
            zlist.append(u)
    zlistfit = []
    for i in fitSurf([NUM,TSET],*coef3d):
        for u in i:
            zlistfit.append(u)
    zlist = np.array(zlist)
    zlistfit = np.array(zlistfit)

    st = sum((zlist-np.average(zlist))**2)
    sr = sum((zlist-zlistfit)**2)
    r2 = 1-sr/st
    return round(r2,3)

print(r2surf())

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(NUM,TSET,SAMP)
ax.plot_wireframe(NUM,TSET,fitSurf([NUM,TSET],*coef3d),color='orange')
plt.show()



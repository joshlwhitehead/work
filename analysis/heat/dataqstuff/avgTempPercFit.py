from avgTemp import fit, avgTrial
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

xx= fit('30_90_bothInside_a.csv','04Jan2022')
yy= fit('30_90_bothInside_b.csv','04Jan2022')
zz=fit('30_90_bothInside_c.csv','04Jan2022')

x=fit('30_70_bothInsideBot_a.csv','05Jan2022')
y=fit('30_70_bothInsideBot_b.csv','05Jan2022')
z=fit('30_70_bothInsideBot_c.csv','05Jan2022')

xxx = fit('30_110_d.csv','11Jan2022')
yyy = fit('30_110_e.csv','13Jan2022')
zzz = fit('30_110_f.csv','13Jan2022')



fif = fit('30_50_bothInsideBot_a.csv','05Jan2022')
fif1 = fit('30_50_bothInsideBot_b.csv','05Jan2022')
fif2 = fit('30_50_bothInsideBot_c.csv','06Jan2022')

sev = avgTrial(x,y,z)
nin = avgTrial(xx,yy,zz)
onet = avgTrial(xxx,yyy,zzz)
fiff = avgTrial(fif,fif1,fif2)


def percFit(list,Tset):
    err = []
    ratioBot = np.average(list[-100:])/list
    for i in ratioBot:
        if i>1.05:
            err.append(i)
    percy = list[100:len(err)]
    percx = np.arange(0,len(percy))
    
    

    param,xxx = opt.curve_fit(fitFun,percx,percy)
    
    return list[100:len(err)],param,percx


def fitFun(x,a,A,b,c):
    return a*np.log(x+b)+c
# print(percFit(sev,70)[1])

# percFit(sev,9)[1]
def makeCsv():
    ninFit = percFit(nin,90)[0].tolist()
    sevFit = sev[100:len(ninFit)+100]
    fifFit = fiff[100:len(ninFit)+100]
    onetFit = onet[100:len(ninFit)+100]
    # sevFit = percFit(sev,70)[0].tolist()
    # fifFit = percFit(fiff,50)[0].tolist()
    # onetFit = percFit(onet,110)[0].tolist()
    while len(sevFit) < len(ninFit):
        sevFit.append(sevFit[-1])
    while len(fifFit) < len(ninFit):
        fifFit.append(fifFit[-1])
    while len(onetFit)< len(ninFit):
        onetFit.append(onetFit[-1])
    # print(len(fifFit),len(sevFit),len(ninFit),len(onetFit))
    print(len(ninFit),len(sevFit),len(onetFit),len(fifFit))
    import pandas as pd
    dF = pd.DataFrame({'time':np.arange(0,len(ninFit)),20:fifFit,40:sevFit,60:ninFit,80:onetFit})
    dF.to_csv('percData.csv')
# makeCsv()


def plot():
    plt.plot(percFit(nin,90)[0])
    # plt.plot(fitFun(percFit(sev,70)[2],*percFit(sev,90)[1]),label='fit70')
    plt.plot(percFit(sev,70)[0])
    plt.plot(percFit(onet,110)[0])
    plt.plot(percFit(fiff,50)[0])
    plt.grid()
    plt.legend()
    plt.savefig('fit')
    # print(len(percFit(nin,90)[0]))
    # print(len(percFit(sev,70)[0]))
    # print(len(percFit(onet,110)[0]))
    # print(len(percFit(fiff,50)[0]))
# plot()




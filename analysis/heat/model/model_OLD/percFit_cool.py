from avgTemp import fit, avgTrial
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

fif1 = fit('30_90_50_a.csv','13Jan2022')
fif2 = fit('30_90_50_b.csv','13Jan2022')
fif3 = fit('30_90_50_c.csv','14Jan2022')

sev1 = fit('30_90_70_a.csv','13Jan2022')
sev2 = fit('30_90_70_b.csv','13Jan2022')
sev3 = fit('30_90_70_c.csv','13Jan2022')

thir1 = fit('30_90_30_a.csv','14Jan2022')
thir2 = fit('30_90_30_b.csv','14Jan2022')
thir3 = fit('30_90_30_c.csv','14Jan2022')
thir4 = fit('30_90_30_d.csv','18Jan2022')
thir5 = fit('30_90_30_e.csv','18Jan2022')

sev = avgTrial(sev1,sev2,sev3)
fif = avgTrial(fif1,fif2,fif3)
thir = avgTrial(thir1,thir4,thir5)

def percFit(list,Tset):
    err = []
    ratioBot = list/np.average(list[-100:])
    for i in ratioBot:
        if i>1.04:
            err.append(i)
  
    
    return list[:len(err)]



# print(np.average(sev[-100:]))
# print(np.average(fif[-100:]))
# print(np.average(thir[-100:]))



def plot():
    plt.plot(thir[thir.tolist().index(np.max(thir)):])    
    plt.plot(sev[sev.tolist().index(np.max(sev)):])
    plt.plot(fif[fif.tolist().index(np.max(fif)):])

    plt.plot(percFit(thir[thir.tolist().index(np.max(thir)):],50))
    plt.plot(percFit(sev[sev.tolist().index(np.max(sev)):],70))
    plt.plot(percFit(fif[fif.tolist().index(np.max(fif)):],70))
  
    plt.grid()
    plt.legend()
    plt.show()
    # print(len(percFit(nin,90)[0]))
    # print(len(percFit(sev,70)[0]))
    # print(len(percFit(onet,110)[0]))
    # print(len(percFit(fiff,50)[0]))
# plot()


















def makeCsv():
    thirFit = 81-1*np.array(percFit(thir[thir.tolist().index(np.max(thir)):],50).tolist())
    sevFit = 81-1*sev[sev.tolist().index(np.max(sev)):len(thirFit)+sev.tolist().index(np.max(sev))]
    fifFit = 81-1*fif[fif.tolist().index(np.max(fif)):len(thirFit)+fif.tolist().index(np.max(fif))]

    
    print(len(thirFit),len(sevFit),len(fifFit))
    import pandas as pd
    dF = pd.DataFrame({'time':np.arange(0,len(thirFit)),10:sevFit,30:fifFit,50:thirFit})
    dF.to_csv('negCoolData.csv')
makeCsv()
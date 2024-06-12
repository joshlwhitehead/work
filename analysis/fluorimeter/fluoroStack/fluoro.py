import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd



def fwhmToStd(fwhm):
    return fwhm/2/np.sqrt(2*np.log(2))


peaks = {
    415:55,
    445:110,
    480:210,
    515:390,
    555:590,
    590:840,
    630:1350,
    680:1070
    }


colors = {
    415:'purple',
    445:'b',
    480:'C0',
    515:'cyan',
    555:'g',
    590:'y',
    630:'orange',
    680:'r'
    }
def plotSensor(wave):
    
    FWHM = {
        415:26,
        445:30,
        480:36,
        515:39,
        555:39,
        590:40,
        630:50,
        680:52
        }

    STD = {}
    for i in FWHM:
        STD[i] = fwhmToStd(FWHM[i])

    if wave == 'all':

        for i in STD:
            tail = 2*FWHM[i]
            x = np.linspace(i-tail,i+tail,999)
            z = stats.norm.pdf(x,loc=i,scale=STD[i])
            z *= peaks[i]/max(z)/max(peaks.values())
            plt.plot(x,z,color=colors[i],label=i)
    else:
        for i in wave:
            x = np.linspace(i-2*FWHM[i],i+2*FWHM[i],999)
            z = stats.norm.pdf(x,loc=i,scale=STD[i])
            zz = stats.norm.pdf(x,loc=i-10,scale=STD[i])
            zzz = stats.norm.pdf(x,loc=i+10,scale=STD[i])
            z *= peaks[i]/max(z)/max(peaks.values())
            zz *= peaks[i]/max(zz)/max(peaks.values())
            zzz *= peaks[i]/max(zzz)/max(peaks.values())
            plt.plot(x,z,color=colors[i],lw=3,label=' '.join(['nominal',str(i)]))
            plt.plot(x,zz,linestyle=':',color=colors[i],lw=3,label=' '.join([str(i),'+10 nm']))
            plt.plot(x,zzz,linestyle='--',color=colors[i],lw=3,label=' '.join([str(i),'-10 nm']))
    plt.vlines(479,0,.2,'k',ls='--',lw=3)
    plt.vlines(476,0,.2,'k',lw=3)
    plt.vlines(473,0,.2,'k',ls=':',lw=3)
    plt.legend()
    plt.grid()
    plt.show()


data = pd.read_csv('sampleStack.csv')

x = data['LED wave']
LEDy = data['440 trans']
LEDFilty = data['LED filt']
sensFilty = data['sens filt']

sytoxx = data['sytox wave']
excite = data['excite']
emit = data['emit']

# plt.plot(x,LEDy,label='440nm LED')
# plt.plot(x,LEDFilty,label='LED filter')
# plt.plot(x,sensFilty,label='sensor filter')
# # plt.plot(sytoxx,excite,label='sytox excitation')
# plt.plot(sytoxx,emit,label='sytox emission')
# plt.grid()
# plt.legend()
# plt.show()

plotSensor([445,480])
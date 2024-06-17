import numpy as np
from scipy import stats,integrate
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
def plotSensor(wave):
    
    

    

    if wave == 'all':

        for i in STD:
            tail = 2*FWHM[i]
            x = np.linspace(i-tail,i+tail,999)
            z = stats.norm.pdf(x,loc=i,scale=STD[i])
            zz = stats.norm.pdf(x,loc=i-10,scale=STD[i])
            zzz = stats.norm.pdf(x,loc=i+10,scale=STD[i])
            z *= peaks[i]/max(z)/max(peaks.values())
            zz *= peaks[i]/max(zz)/max(peaks.values())
            zzz *= peaks[i]/max(zzz)/max(peaks.values())
            plt.plot(x,z,color=colors[i],lw=3,label=' '.join([str(i)]))
            plt.plot(x,zz,color=colors[i],ls=':',lw=3)#,label=' '.join([str(i),'-10 nm']))
            plt.plot(x,zzz,color=colors[i],ls='--',lw=3)#,label=' '.join([str(i),'+10 nm']))
            
    else:
        for i in wave:
            x = np.linspace(i-2*FWHM[i],i+2*FWHM[i],999)
            z = stats.norm.pdf(x,loc=i,scale=STD[i])
            zz = stats.norm.pdf(x,loc=i-10,scale=STD[i])
            zzz = stats.norm.pdf(x,loc=i+10,scale=STD[i])
            z *= peaks[i]/max(z)/max(peaks.values())
            zz *= peaks[i]/max(zz)/max(peaks.values())
            zzz *= peaks[i]/max(zzz)/max(peaks.values())
            plt.plot(x,z,color=colors[i],lw=3,label=' '.join([str(i)]))
            # plt.plot(x,zz,linestyle=':',color=colors[i],lw=3)#,label=' '.join([str(i),'-10 nm']))
            # plt.plot(x,zzz,linestyle='--',color=colors[i],lw=3,label='445 +10nm')#,label=' '.join([str(i),'+10 nm']))
    # plt.vlines(479,0,.1,'k',ls='--',lw=3,label='sensor filter +3nm')
    plt.vlines(476,0,.1,'k',lw=3,label='sensor filter')#,label='sensor filter')
    # plt.vlines(473,0,.1,'k',ls=':',lw=3,label='sensor filter -3nm')
    plt.fill_between(x,z,where=(x>=476),color='grey')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Relative Sensitivity')
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

# plt.plot(x,LEDy,lw=3,label='440nm LED')
# plt.plot(x,LEDFilty,lw=3,label='LED filter')
# plt.plot(x,sensFilty,lw=3,label='sensor filter')
# plt.plot(sytoxx,excite,lw=3,label='sytox excitation')
# plt.plot(sytoxx,emit,lw=3,label='sytox emission')
# plt.xlabel('Wavelength (nm)')
# plt.ylabel('Transmission (%)')
# plt.ylabel
# plt.grid()
# plt.legend()
# plt.show()

# plotSensor([445])
def pdf(x,wave,sensorShift):
    y = stats.norm.pdf(x,loc=wave+sensorShift,scale=STD[wave])


def detected(wave,lowLim,sensorShift):
    x = np.linspace(wave-2*FWHM[wave],wave+2*FWHM[wave],999)
    y = stats.norm.pdf(x,loc=wave+sensorShift,scale=STD[wave])
    xx = np.linspace(lowLim,x[-1],len(y))
    area = integrate.trapz(y,xx)
    return area
nom = detected(445,476,0)
worst = detected(445,473,10)
best = detected(445,479,-10)

print('nom',nom)
print('worst',worst)
print('best',best)

print(best/worst)



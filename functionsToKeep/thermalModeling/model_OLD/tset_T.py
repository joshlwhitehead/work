import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('roughTemp.csv')
datatime = data['time']
datat1 = data['T1']
datat2 = data['T2']
dataset = data['Tset']

data2 = pd.read_csv('short try2.csv')
data2time = data2['time2']
data2t = data2['temp2']

step1 = 146
step2 = step1 + 125
step3 = step2 + 145
step4 = step3 + 185
step5 = step4 + 105
step6 = step5 + 115

step1in = 90
step2in = step1in + 120
step3in = step2in + 40
step4in = step3in + 180
step5in = step4in + 50
step6in = step5in + 90
# print(step6in)
# step1in =step1
# step2in = step2
# step3in = step3
# step4in = step4
# step5in = step5
# step6in = step6
# print(step6in-step6)
Tset1 = 90
Tset2 = 75
Tset3 = 115
Tset4 = 105
Tset5 = 45
Tset6 = 55

# print(step5)
# time1 = np.arange(1,step1in,1)
# time2 = np.arange(step1in,step2in+(step1-step1in),1)
# time3 = np.arange(step2in+(step1-step1in),step3in+(step2-step2in),1)
# time4 = np.arange(step3in+(step2-step2in),step4in+(step3-step3in),1)
# time5 = np.arange(step4in+(step3-step3in),step5in+(step4-step4in),1)
# time6 = np.arange(step5in+(step4-step4in),step6in+(step5-step5in),1)
time1 = np.arange(1,step1in,1)
time2= np.arange(step1in,step2in,1)
time3 = np.arange(step2in,step3in,1)
time4 = np.arange(step3in,step4in,1)
time5 = np.arange(step4in,step5in,1)
time6 = np.arange(step5in,step6in,1)

a = np.ones(len(time1))*Tset1
b = np.ones(len(time2))*Tset2
c = np.ones(len(time3))*Tset3
d = np.ones(len(time4))*Tset4
e = np.ones(len(time5))*Tset5
f = np.ones(len(time6))*Tset6

# print(time3[-1])
x = sum([step1,step2,step3,step4,step5])
y = sum([step1])
def t1(Tset,t,step):
    if step == 1:
        y = (0.0748*np.log(t)+0.4584)*Tset                 #R2 = .9905
    elif step == 2:
        y = (-4.53e-5*t + 0.9176)*Tset                                    #R2 = 0.2665
    elif step == 3:
        y = (0.0678*np.log(t-(time2[-1]))+.4584)*Tset1+t1(Tset2,step2in,2)-t1(Tset1,1,1)             #R2 = .9721
    elif step == 4:
        y = (-6.58e-7*(t+(step3-time3[-1]))**2 + 8.26e-4*(t+(step3-time3[-1])) + 0.6293)*Tset                       #R2 = .9795

    elif step == 5:
        y = (6.62e-5*(t+(step4-time4[-1]))**2 - .0915*(t+(step4-time4[-1])) + 32.779)*Tset
        # y = -7.81679e-7*(t+600)**3 + 1.60455e-3*(t+600)**2 - 1.09935*(t+600) + 2.52603e2
        # y = -1.24*(0.06*np.log(t-time4[-1])+.4584)*Tset + t1(Tset4,step4in,4)                     #R2 = .9119
        
    elif step == 6:
        y = (7.23e-6*(t+(step5-time5[-1]))**2 - 1.19e-2*(t+(step5-time5[-1])) + 5.89)*Tset          #R2 = .9679
    return y


def t2(Tset,t,step):
    if step == 1:
        y = (0.3741*np.exp(0.00336*t))*Tset                            #R2 = .9925
    elif step ==2:
        y = (5.83e-5*t + .7111)*Tset                                      #R2 = .9092
    elif step == 3:
        y = (.00153*t + .0556) *Tset                                    #R2 = .9913
    elif step == 4:
        y = (-5.68e-7*t**2 + .000653*t + .5742)*Tset                        #R2 = .9272
    elif step == 5:
        y = (-3.88e-3*t + 4.0049)*Tset  #R2 = .9119
    elif step == 6:
        y = (7.32e-6*t**2 - 0.0125*t + 6.2385)*Tset                     #R2 = .9975
    return y


totalMod1 = []
totalTime1 = []

for i in range(len(time1)):
    totalMod1.append(t1(Tset1,time1,1)[i])
    totalTime1.append(time1[i])
for i in range(len(time2)):
    totalMod1.append(t1(Tset2,time2,2)[i])
    totalTime1.append(time2[i])
for i in range(len(time3)):
    totalMod1.append(t1(Tset3,time3,3)[i])
    totalTime1.append(time3[i])
for i in range(len(time4)):
    totalMod1.append(t1(Tset4,time4,4)[i])
    totalTime1.append(time4[i])
for i in range(len(time5)):
    totalMod1.append(t1(Tset5,time5,5)[i])
    totalTime1.append(time5[i])
for i in range(len(time6)):
    totalMod1.append(t1(Tset6,time6,6)[i])
    totalTime1.append(time6[i])


totalMod2 = []
totalTime2 = []
for i in range(len(time1)):
    totalMod2.append(t2(Tset1,time1,1)[i])
    totalTime2.append(time1[i])
for i in range(len(time2)):
    totalMod2.append(t2(Tset2,time2,2)[i])
    totalTime2.append(time2[i])
for i in range(len(time3)):
    totalMod2.append(t2(Tset3,time3,3)[i])
    totalTime2.append(time3[i])
for i in range(len(time4)):
    totalMod2.append(t2(Tset4,time4,4)[i])
    totalTime2.append(time4[i])
for i in range(len(time5)):
    totalMod2.append(t2(Tset5,time5,5)[i])
    totalTime2.append(time5[i])
for i in range(len(time6)):
    totalMod2.append(t2(Tset6,time6,6)[i])
    totalTime2.append(time6[i])


# plt.plot(time1,a,time2,b,time3,c,time4,d,time5,e,time6,f)
# plt.plot(datatime,dataset,label='set temp')

plt.plot(data2time,data2t,label='data bottom')
plt.plot(totalTime1,totalMod1,label='model bottom')

# plt.plot(datatime,datat2,label='data top')
# plt.plot(totalTime2,totalMod2,label='model top')



plt.legend()
plt.grid()
# plt.ylim(40,140)
# plt.xlim(400,500)
plt.show()


# print(t1(Tset1,.001,1))










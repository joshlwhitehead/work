import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def fit(filename,plotname,tset):
    fullSheet = pd.read_csv(''.join(['data/',filename]))
    bot = fullSheet['dataQStage1Heatsink'].tolist()
    top = fullSheet['dataQLiquidStg1'].tolist()
    time = fullSheet['timeSinceBootSeconds'].tolist()


    newBot = []
    newTime = []
    newTop = []
    for temp in bot:
        y = str(temp)
        if y !='nan':
            y=float(temp)
            newBot.append(temp)
            newTop.append(top[bot.index(temp)])
            newTime.append(time[bot.index(temp)])
    newBot = np.array(newBot)
    newTop = np.array(newTop)
    newTime = np.array(newTime)

   
    return newBot,newTop


  
    

 
    # plt.plot((newTop[:]),label='top')
    # plt.plot(tset/newBot[:],label=str(tset))
   


    # plt.grid()
    # plt.legend()
    # # plt.ylim(0,100)
    # # plt.show()
    # plt.savefig(plotname)
# plt.plot(fit('110long_5ramp.csv','trash',90)[0],label='ramp5')
# plt.plot(fit('110long_5ramp.csv','trash',90)[1],'--',label='ramp5')
# plt.plot(fit('110long.csv','trash',70)[0],label='ramp0')
# plt.plot(fit('110long.csv','trash',70)[1],'--',label='ramp0')
plt.plot(fit('90long_5ramp.csv','trash',90)[0][:345])
# plt.hlines(90,0,1000)

plt.grid()
plt.legend()
plt.show()
# fit('70long.csv','trash',70)
# fit('90long.csv','trash',90)
# fit('110long.csv','trash',110)

# fit('170long.csv','trash',170)
# print(fit('90long_5ramp.csv','trash',90)[0][:10])

count = 0
err = []

x = np.array(fit('90long_5ramp.csv','trash',90)[0])/np.average(fit('90long_5ramp.csv','trash',90)[0][-100:])
# print(np.average(fit('90long_5ramp.csv','trash',90)[0][-100:]))
for i in x:
    if i>1.1:
        err.append(i)
print(len(err))
# plt.plot()
plt.show()





































# print(paramTop)
# u2=27
# sT = 0
# xx = np.average(newTop[:])

# s = (np.square(newTop[:]-xx))
# sT = sum(s)

# r = (np.square(newTop[:]-hope(test1,*josh)[:]))
# sR = sum(r)

# print('R^2:',(sT-sR)/sT)
# print(hope(test1,*josh))
# print(*josh)

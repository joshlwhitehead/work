import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
date = '05Jan2022'
def fit(filename,name):
    fullSheet = pd.read_csv(''.join(['data/',date,'/',filename]))
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

####################################################################################################################

    err = []

    ratioBot = np.average(newBot[-100:])/newBot
    for i in ratioBot:
        if i>1.05:
            err.append(i)


    percy = newBot[100:len(err)]
    percx = np.arange(0,len(percy))
    
    a,b,c,d = np.polyfit(percx,percy,3)
    print('\n',a,b,c,d,'\n')

    # plt.plot((newTop[:]),label='top')


    newfun = a*percx**3+b*percx**2+c*percx+d


    #########scipy######################
    def optfun(x,a,b,c,d,A,B,C,D,e,E):
        return a*np.log(x+b)+c

    param,xxx = opt.curve_fit(optfun,percx,percy)
    # print(param)


    ####################        R2          #############################
    st = sum((percy-np.average(percy))**2)
    sr = sum((percy-newfun)**2)
    r2 = 1-sr/st

    srOpt = sum((percy-optfun(percx,*param))**2)
    r2Opt = 1-srOpt/st
    print('r2 poly:',round(r2,3),'\n'
        'r2 opt',round(r2Opt,3))










    # plt.plot(newBot,label=name)
    # plt.plot(newBot[201:])
    plt.plot(newBot[100:len(err)],label=name)
    plt.plot(newfun,label='poly')
    plt.plot(optfun(percx,*param),label='opt')

  


    plt.legend()
    # print(newBot[-1])
    # print(newBot[len(err)])
    # print(len(newBot[:len(err)]))
    # print(np.average(newBot[-100:]),'\n')


# fit('30_90_bothInside_a.csv','both inside')
# fit('30_90_oneInsideBot.csv','oneIn')
# fit('30_90.csv','90fit',90,'ramp0')
# fit('30_90_1ramp.csv','90fit',90,'ramp1')
# fit('30_90_ramp0.5.csv','90fit',90,'ramp0.5')
# fit('30_90_0ramp_b.csv','90fit',90,'30_ramp0')
# fit('30_90_0.125ramp.csv','90fit',90,'ramp0.125')
# fit('50_90.csv','90fit',90,'50_90ramp0')
# fit('50_90_0.25ramp.csv','90fit',90,'50_ramp0.25')
# fit('50_0.25ramp_90_0.25ramp.csv','90fit',90,'50_0.25ramp')
fit('30_90_insideBot_b.csv','')

plt.grid()
# plt.savefig('percentFit')
plt.show()










































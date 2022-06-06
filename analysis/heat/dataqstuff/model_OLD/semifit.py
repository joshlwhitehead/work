import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def fit(filename,name):
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

####################################################################################################################

    err = []

    ratioBot = np.average(newBot[-100:])/newBot
    for i in ratioBot:
        if i>1.03:
            err.append(i)

    test = np.arange(0,len(err))



    def hope(x,a,A,b,B,c,C,d,D,e,E,f,F,g,G):
        return a*np.log((x+A)**b*c+d)**f+e
    def hope2(x,a,A,b,B,c,C,d,D,e,E,f,F,g,G):
        return a*x**A+b*x**B+c*x**C+d*x**D+e*x**E+f*x**F
    
    # print(len(err))

    # paramBot,xxx = opt.curve_fit(hope2,test,newBot[:len(err)])
    # paramBot2,yyy = opt.curve_fit(hope2,test,newBot[u:])
  
    
    test2 = np.arange(0,999)
  
    # plt.plot((newTop[:]),label='top')
    # plt.plot(newBot,label=name)
    plt.plot(newBot[:len(err)],label=name)
    
    # plt.plot(tset-hope2(test,*paramBot))
  


    # plt.grid()
    plt.legend()
    # plt.savefig('trash')
    # plt.show()
    print(newBot[-1])
    print(newBot[len(err)])
    print(len(newBot[:len(err)]))
    print(np.average(newBot[-100:]),'\n')

# fit('90long_5ramp.csv','90fit',90)
# fit('70long_5ramp.csv','90fit',70)
# fit('110long_5ramp.csv','90fit',110)
# fit('170long.csv','90fit',170)
# fit('170long.csv','90fit',170)
# fit('30_70.csv','90fit',70)

# fit('30_90.csv','0try1')
fit('30_90_0ramp_a.csv','0try2')
fit('30_90_0ramp_b.csv','0try3')
fit('30_90_0ramp_bubbles.csv','bubbles')
# fit('30_90_0ramp_noExtraFluid.csv','NoExtraFluid')
# fit('30_90_1ramp.csv','1try1')
fit('30_90_1ramp_a.csv','1try2')
fit('30_90_1ramp_b.csv','1try3')
# fit('30_90_1ramp_c.csv','1try4')

# fit('30_90_ramp0.5.csv','ramp0.5')

# fit('30_90_0.125ramp.csv','90fit',90,'ramp0.125')
# fit('50_90.csv','90fit',90,'50_90ramp0')
# fit('50_90_0.25ramp.csv','90fit',90,'50_ramp0.25')
# fit('50_0.25ramp_90_0.25ramp.csv','90fit',90,'50_0.25ramp')
# fit('30_90_0.25ramp.csv','0.25try1')
fit('30_90_0.25ramp_a.csv','0.25try2')
fit('30_90_0.25ramp_b.csv','0.25try3')
# fit('30_90_0.25ramp_c.csv','0.25try4')



plt.grid()
plt.savefig('trash')
# plt.show()









































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

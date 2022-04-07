import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
date = 'Before 04Jan2022'
def fit(filename,plotname):
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

   

    u = 350
    g = 200
    test = np.arange(0,len(newTop[:202]))
    test3 = np.arange(0,len(newTop[g:]))
    test1 = np.arange(0,len(newTop[:354]))
    test2 = np.arange(0,len(newTop[u:]))

   


    def hope(x,a,A,b,B,c,C,d,D,e,E,f,F,g,G):
        return a*np.log(x**b*c+d)**f+e
    def hope2(x,a,A,b,B,c,C,d,D,e,E,f,F,g,G):
        return a*x**A+b*x**B+c*x**C+d*x**D+e*x**E+f*x**F
        

    # paramBot,xxx = opt.curve_fit(hope,test1,newBot[:354])
    # paramBot2,yyy = opt.curve_fit(hope2,test2,newBot[u:])
    # paramTop,zzz = opt.curve_fit(hope,test,newTop[:202])
    # paramTop2,jjj = opt.curve_fit(hope2,test3,newTop[g:])
    

    # plt.plot(hope(test1,*paramBot)[:],label='fit')
    # plt.plot(np.arange(350+4,len(newTop)),hope2(test2,*paramBot2)[4:],label='fit2')
    plt.plot((newTop[:]),label=''.join(['top ',plotname]))
    plt.plot(newBot[:],label=''.join(['bot ',plotname]))
    # plt.hlines(90,0,len(newBot))
    # plt.plot(hope(test,*paramTop))
    # plt.plot(np.arange(g+2,len(newTop)),hope2(test3,*paramTop2)[2:])


    plt.grid()
    plt.legend()
    plt.title(filename)
    # plt.ylim(0,100)
    
    # plt.savefig(plotname)

    # for i in 
    print(np.average(newBot[-50:])-np.average(newTop[-50:]))
# fit('30_90_0ramp_a.csv','0ramp')
# fit('30_90_bothInside.csv',' bothInside')
# fit('30_90_bothInside_a.csv','bothInside a')
# fit('30_90_bothInside_b.csv','bothInside b')
# fit('30_90_bothInside_noBot.csv','no tape')
# fit('30_90_bothInside_noBot_a.csv','no tape a')
fit('30_90_bothInside_noTape_b.csv','no tape b')
# fit('30_90_insideBot_noTape.csv','one inside')
# fit('30_90_insideBot_noTape_a.csv','one inside')
# fit('30_90_insideOutside.csv','in/out')
# fit('30_90_0.25ramp_a.csv','0.25ramp')
# fit('30_150_0ramp_a.csv','150')
# fit('insideBot_standard.csv','full')
# fit('insideBot_standard_a.csv','full a')
# fit('30_90_oneInsideBot.csv','isideBot')
# fit('30_90_insideBot_a.csv','a')
# fit('30_90_insideBot_b.csv','b')
# fit('30_90_insideBot_c.csv','c')
# fit('30_90_insideBot_d.csv','d')
# fit('30_90_bothInside_a.csv','')
# fit('fastBoil150.csv','150')
# fit('fastBoil160.csv','160')
# fit('fastBoil140.csv','140')
plt.grid()
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

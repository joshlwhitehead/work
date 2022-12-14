"""analyze """

import numpy as np
import dataToVar as dat
import matplotlib.pyplot as plt
import pandas as pd
# from thermalCompareQuant import listAvg, listStd, listRms, listGrad, interppp
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
from statsmodels.graphics.factorplots import interaction_plot
# import statsmodels.api as sm


# total = [dat.adv06c]
total = dat.TC
instList = [6,7,10,12,13,15,17,25,26,27]*3
instList.sort()
instListShort = [6,7,10,12,13,15,17,25,26,27]
cupList = [32,32,32,12,12,12,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,31,30,30,30]
cupListClump = [32,12,30,30,30,30,30,30,30,30]
date = [1011,1011,1011,1012,1012,1012,1102,1102,1102,1003,1003,1003,1018,1018,1018,1017,1017,1017,1003,1003,1003,1020,1020,1020,1020,1021,1021,1021,1021,1021]
dateClump = [1011,1012,1102,1003,1018,1017,1003,1020,1021,1021]

colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive']

        
def hold(temp):
    alpha = 0.05
    rawSamp = []
    magMeans = []
    modelMagMeans = []
    percPass = []
    count2 = 0
    n = 0

    # x = total[0]
    # count = 0
    # for i in range(len(x[4])):
    #     if x[2][i] <= x[4][i]+5 and x[2][i] >= x[4][i]-5:
    #         count +=1
    #     else:
    #         print(x[2][i])
    # print(count/len(x[2]))
    # plt.plot(x[2])
    # plt.plot(x[4])
    # plt.show()
    
    for i in total:
        rawSamp.append(i[2])
        indx = []
        count = 0
        if temp == 90:
            for u in range(len(i[4])):
                if i[4][u] < temp+.1 and i[4][u] > temp-.1:
                    
                    indx.append(u)
        elif temp == 62:
            for u in range(len(i[4])):
                if i[4][u] < temp+.1 and i[4][u] > temp-.1 and i[0][u] <200:
                    
                    indx.append(u)
        # print(indx)
        #     if i[2][u] <= i[4][u]+5 and i[2][u] >= i[4][u]-5:
        #         count+=1 
        # percPass.append(round(count/len(i[2]),2))
        # print(indx[0],indx[-1])
        
        magMean = np.mean(i[2][indx[0]:indx[-1]]) #(max(i[2][indx[0]:indx[-1]])-min(i[2][indx[0]:indx[-1]]))/np.mean(i[2][indx[0]:indx[-1]])
        modelMagMean = np.mean(i[4][indx[0]:indx[-1]]) #(max(i[4][indx[0]:indx[-1]])-min(i[4][indx[0]:indx[-1]]))/np.mean(i[4][indx[0]:indx[-1]])

        
        magMeans.append(magMean)
        modelMagMeans.append(modelMagMean)
        count = 0
        for u in indx:
            if i[2][u] <= temp+5 and i[2][u] >= temp-5:
                count+=1 
            # else:
            #     print(i[2][u])
        # if total.index(i) == 0:
        #     for kk in indx:
                # print(i[0][kk])
        percPass.append(count/len(indx))
        # print(percPass)
        # print(i[0])
        plt.plot(i[0][indx[0]:indx[-1]],i[2][indx[0]:indx[-1]],color=colors[n],label=''.join(['adv',str(instList[total.index(i)]),' ',str(round(magMeans[total.index(i)],2))]))
        plt.plot(i[0][indx[0]:indx[-1]],i[4][indx[0]:indx[-1]],'k')
        plt.hlines(temp-5,40,160,'k')
        count2+=1
        if count2%3 == 0:
            n += 1
        

    plt.legend()
    plt.title(''.join(['Compare Sample to Model at ',str(temp)]))
    plt.ylabel('Temp (c)')
    plt.xlabel('Time (sec)')
    plt.grid()
    
    
    


    dfAnova = pd.DataFrame({'Instrument':instList,'Cup':cupList,'Date':date,'Mean':magMeans,'PercentPass':percPass})
    # dfAnova.hist('PercentPass')
    




    formula = 'Mean ~ Instrument' 
    model = ols(formula, dfAnova).fit()
    aov_table = anova_lm(model, typ=1)

    formula2 = 'PercentPass ~ Instrument' 
    model2 = ols(formula2, dfAnova).fit()
    aov_table2 = anova_lm(model2, typ=1)
    # print(aov_table,'\n',aov_table2)



    m_comp = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], 
                            alpha=alpha)
    # print(m_comp)
    # print(percPass)
    # print(np.array(magMeans)-90)

    dfAnova.boxplot('Mean',by='Instrument')
    count = 1
    for i in range(len(cupListClump)):
        plt.text(count,85,''.join(['p',str(cupListClump[i])]))
        plt.text(count,84.75,str(dateClump[i]))
        count+=1
    plt.hlines(temp,1,10,'r')
    plt.ylabel('Temp (c)')
    dfAnova.boxplot('PercentPass',by='Instrument')
    count = 1
    for i in range(len(cupListClump)):
        plt.text(count,0.4,''.join(['p',str(cupListClump[i])]))
        plt.text(count,.37,str(dateClump[i]))
        count+=1
    # plt.hlines(temp,0,10,'k')
    # fig = interaction_plot(dfAnova.Instrument,dfAnova.Date,dfAnova.Mean,ms=10)
    plt.show()
    

    
    clumpMeans = [magMeans[i:i+3] for i in range(0,len(magMeans),3)]
    clumpInst = [instList[i:i+3] for i in range(0,len(instList),3)]
    
    limit = temp - 5
    count = 0
    probs = []
    for i in clumpMeans:
        mean_er = np.mean(i) # sample mean
        std_dev_er = np.std(i, ddof=1) # sample standard devialtion
        se = std_dev_er / np.sqrt(len(i)) # standard error
        n = len(i) # sample size, n
        dof = n - 1 # degrees of freedom
        t_star = stats.t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
        moe = t_star * se # margin of error
        ci = np.array([mean_er - moe, mean_er + moe])
        t_limit = (limit - mean_er) / se
        pr = stats.t.cdf(t_limit, dof)
        probs.append(pr)
        # print('sample size = {:d}'.format(n))
        # print('sample mean = {:.1f} kg/h'.format(mean_er))
        # print('sample standard deviation = {:.2f} kg/h'.format(std_dev_er))
        # print('standard error = {:.3f} kg/h'.format(se))
        # print('t statistic = {:.3f}'.format(t_star))
        # print('margin of error = {:.2f} kg/h'.format(moe))
        print(clumpInst[count])
        
        # print('95 % CI for mean = {:.1f}, {:.1f}, kg/h'.format(ci[0], ci[1]))
        # print('emission limit = {:.2f} kg/h'.format(limit))
        # print('t limit = {:.2f}'.format(t_limit))
        print('probability sample drops below model-5c =  {:.3f}'.format(pr))

        plt.hlines(count,ci[0],ci[1],lw=5)
        plt.plot(mean_er,count,'o',color='r',ms=7)
        count+=1

    plt.yticks(np.arange(0,len(clumpMeans)),instListShort)
    plt.grid()
    plt.xlabel('Mean Temp (c)')
    plt.ylabel('AdvB')
    plt.show()
    

    plt.plot(probs,'o')
    plt.grid()
    plt.xlabel('AdvB')
    plt.ylabel('Prob Mean < Model-5c')
    plt.xticks(np.arange(0,len(clumpMeans)),instListShort)
    plt.show()

     
    


hold(62)

 
def plotSpec(toPlot):
    for i in toPlot:
        plt.plot(total[i][0],total[i][2])
        plt.plot(total[i][0],total[i][4],'k')

    plt.grid()
    plt.show()
    

# josh = [12,13,14,21,22,23]
josh = [15,16,17,18,19,20]
# plotSpec(josh)






def all():

    magMeans = []
    modelMagMeans = []
    percPass = []
    meanDif = []
    for i in total:
        count = 0
        for u in range(len(i[4])):
            if i[2][u] <= i[4][u]+5 and i[2][u] >= i[4][u]-5:
                count+=1
        
        magMean = (max(i[2])-min(i[2]))/np.mean(i[2])
        modelMagMean = (max(i[4])-min(i[4]))/np.mean(i[4])
        percPass.append(round(count/len(i[2]),2))
        # if magMean > modelMagMean:
        magMeans.append(magMean)
        modelMagMeans.append(modelMagMean)
        meanDif.append(magMean-modelMagMean)


    #     plt.plot(i[0],i[2])
    #     plt.plot(i[0],i[4],'k')
    #     # plt.plot(i[0][indx[0]:indx[-1]],i[1][indx[0]:indx[-1]],'g')
    # plt.show()

    dfAnova = pd.DataFrame({'inst':instList,'magMean':magMeans,'PercentPass':percPass})
    # dfAnova.hist('magMean')
    # plt.show()




    formula = 'percPass ~ inst' 
    model = ols(formula, dfAnova).fit()
    aov_table = anova_lm(model, typ=1)
    print(aov_table)


    m_comp = pairwise_tukeyhsd(endog=dfAnova['PercentPass'], groups=dfAnova['inst'], 
                            alpha=0.05)
    print(m_comp)
    print(percPass)
    print(meanDif)


    dfAnova.boxplot('PercentPass',by='inst')
    dfAnova.boxplot('magMean',by='inst')
    plt.show()


    # x = np.linspace(min(magMeans),max(magMeans),100)
    # pdf = stats.norm.pdf(x,loc=np.mean(magMeans),scale=np.std(magMeans))
    # dfAnova.hist('magMean',density=True)
    # plt.plot(x,pdf)
    # plt.show()
    # s = stats.probplot(magMeans)
    # print(s[1])
    # stats.probplot(magMeans,plot=plt)
    # plt.show()

    for i in range(10,20):
        plt.plot(total[i][0],total[i][2],label=round(magMeans[i],2))
        plt.plot(total[i][0],total[i][4],'k')
    plt.legend()
    plt.grid()
    plt.show()
# all()
# hold(90)



























    


# for i in total:
#     plt.plot(i[0],i[2])
#     plt.plot(i[0],i[4],'k')
# plt.show()
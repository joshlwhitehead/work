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



def DV(temp):
    alpha = 0.05
    total = dat.PCR09
    instListShort = [2,9,18,27]
    instList = instListShort
    instList.sort()
    cupList = [8,8,8,8]
    cupListClump = [8,8,8,8]
    date = [1216,1216,1216,1216]
    
    colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive','peru','maroon']

    cycle = 6
    modelMax = []
    sampleMax = []
    modelStuff = []
    sampleStuff = []
    
    
    for k in total:
        maxes = []
        maxes2 = []
        indx = []
        count = 0

        for i in k[5]:
            if i == temp:
                indx.append(count)
            count += 1



        modelNew = []
        modelLists = []
        sampleNew = []
        sampleLists = []
        count = 0
        for i in indx:
            if indx[count] != indx[-1] and i+1 == indx[count+1]:
                modelNew.append(k[4][i])
                sampleNew.append(k[2][i])
            else:
                modelLists.append(modelNew)
                sampleLists.append(sampleNew)
                sampleNew = []
                modelNew = []
            count += 1
        count = 2
        for i in modelLists[2:-1]:
            maxes.append(max(i))
            maxes2.append(max(sampleLists[count]))
            count += 1
        modelMax.append(maxes)
        sampleMax.append(maxes2)
    
    count = 0
    n = 0
    for i in range(len(modelMax)):
        if i == 0:
            plt.plot(modelMax[i],'k',label='model')
        else:
            plt.plot(modelMax[i],'k')
        # if i == 0 or i ==3 or i == 6 or i == 9 or i == 12:
        plt.plot(sampleMax[i],label=''.join(['adv',str(instList[i])]))
        # else:
            # plt.plot(sampleMax[i],color=colors[n])
        count += 1
        if count%3 == 0:
            n+=1

    plt.grid()
    plt.legend()
    
    percPass = []
    for i in sampleMax:
        count = 0
        for u in i:
            if u > temp-3 and u < temp+3:
                count += 1
        percPass.append(count/len(i))
    
    means = []
    for i in sampleMax:
        means.append(np.mean(i))
    print(len(sampleMax))
    dfAnova = pd.DataFrame({'Instrument':instList,'Cup':cupList,'Date':date,'Mean':means,'PercentPass':percPass})
    
    
    if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:
        print('data are normal')
    else:
        print('data are not normal')
    
    



    formula = 'Mean ~ Instrument' 
    model = ols(formula, dfAnova).fit()
    aov_table = anova_lm(model, typ=1)

    formula2 = 'PercentPass ~ Instrument' 
    model2 = ols(formula2, dfAnova).fit()
    aov_table2 = anova_lm(model2, typ=1)
    print(aov_table,'\n',aov_table2)

    tCurve = np.linspace(min(dfAnova.Mean),max(dfAnova.Mean))
    
    dfAnova.hist('Mean',density=True)
    # plt.figure()
    plt.plot(tCurve,stats.t.pdf(tCurve,df=len(dfAnova.Mean)-1,loc=np.mean(tCurve),scale=np.std(tCurve)))
    plt.figure()
    stats.probplot(dfAnova.Mean,plot=plt,dist='t',sparams=(len(dfAnova.Mean)-1,))
    

    m_comp = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], 
                            alpha=alpha)
    print(m_comp)
    # print(percPass)
    # print(np.array(magMeans)-90)

    dfAnova.boxplot('Mean',by='Instrument')
    count = 1
    for i in range(len(cupListClump)):
        # plt.text(count,85,''.join(['p',str(cupListClump[i])]))
        # plt.text(count,84.75,str(dateClump[i]))
        count+=1
    plt.hlines(temp,1,len(instListShort),'r')
    plt.ylabel('Temp (c)')
    dfAnova.boxplot('PercentPass',by='Instrument')
    count = 1
    for i in range(len(cupListClump)):
        plt.text(count,0.4,''.join(['p',str(cupListClump[i])]))
        # plt.text(count,.37,str(dateClump[i]))
        count+=1
    # plt.hlines(temp,0,10,'k')
    # fig = interaction_plot(dfAnova.Instrument,dfAnova.Date,dfAnova.Mean,ms=10)
    plt.show()
    

    
    clumpMeans = [means[i:i+3] for i in range(0,len(means),3)]
    
    
    limit = temp - 3
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
        # print(clumpInst[count])
        
        # print('95 % CI for mean = {:.1f}, {:.1f}, kg/h'.format(ci[0], ci[1]))
        # print('emission limit = {:.2f} kg/h'.format(limit))
        # print('t limit = {:.2f}'.format(t_limit))
        # print('probability sample drops below model-5c =  {:.3f}'.format(pr))

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










def wet(temp):
    alpha = 0.05
    total = dat.wet
    instListShort = [10,12,17]
    instList = instListShort*3
    instList.sort()
    cupList = [65,65,65,65,65,65,68,68,68]
    cupListClump = [65,65,68]

    date = [1010,1010,1010,1003,1003,1003,929,929,929]
    
    colors = ['blue','crimson','green','orange','purple','cyan','deeppink','gray','brown','olive','peru','maroon']

    cycle = 6
    modelMax = []
    sampleMax = []
    modelStuff = []
    sampleStuff = []
    
    
    for k in total:
        maxes = []
        maxes2 = []
        indx = []
        count = 0

        for i in k[5]:
            if i == temp:
                indx.append(count)
            count += 1



        modelNew = []
        modelLists = []
        sampleNew = []
        sampleLists = []
        count = 0
        for i in indx:
            if indx[count] != indx[-1] and i+1 == indx[count+1]:
                modelNew.append(k[4][i])
                sampleNew.append(k[2][i])
            else:
                modelLists.append(modelNew)
                sampleLists.append(sampleNew)
                sampleNew = []
                modelNew = []
            count += 1
        count = 2
        for i in modelLists[2:-1]:
            maxes.append(max(i))
            maxes2.append(max(sampleLists[count]))
            count += 1
        modelMax.append(maxes)
        sampleMax.append(maxes2)
    
    count = 0
    n = 0
    for i in range(len(modelMax)):
        if i == 0:
            plt.plot(modelMax[i],'k',label='model')
        else:
            plt.plot(modelMax[i],'k')
        if i == 0 or i ==3 or i == 6 or i == 9 or i == 12:
            plt.plot(sampleMax[i],color=colors[n],label=''.join(['adv',str(instList[i])]))
        else:
            plt.plot(sampleMax[i],color=colors[n])
        count += 1
        if count%3 == 0:
            n+=1

    plt.grid()
    plt.legend()
    
    percPass = []
    for i in sampleMax:
        count = 0
        for u in i:
            if u > temp-3 and u < temp+3:
                count += 1
        percPass.append(count/len(i))
    
    means = []
    for i in sampleMax:
        means.append(np.mean(i))
    
    dfAnova = pd.DataFrame({'Instrument':instList,'Cup':cupList,'Date':date,'Mean':means,'PercentPass':percPass})
    
    
    if stats.anderson(dfAnova.Mean,dist='norm')[0] < stats.anderson(dfAnova.Mean,dist='norm')[1][2]:
        print('data are normal')
    else:
        print('data are not normal')
    
    



    formula = 'Mean ~ Instrument' 
    model = ols(formula, dfAnova).fit()
    aov_table = anova_lm(model, typ=1)

    formula2 = 'PercentPass ~ Instrument' 
    model2 = ols(formula2, dfAnova).fit()
    aov_table2 = anova_lm(model2, typ=1)
    print(aov_table,'\n',aov_table2)

    tCurve = np.linspace(min(dfAnova.Mean),max(dfAnova.Mean))
    
    dfAnova.hist('Mean',density=True)
    # plt.figure()
    plt.plot(tCurve,stats.t.pdf(tCurve,df=len(dfAnova.Mean)-1,loc=np.mean(tCurve),scale=np.std(tCurve)))
    plt.figure()
    stats.probplot(dfAnova.Mean,plot=plt,dist='t',sparams=(len(dfAnova.Mean)-1,))
    

    m_comp = pairwise_tukeyhsd(endog=dfAnova['Mean'], groups=dfAnova['Instrument'], 
                            alpha=alpha)
    print(m_comp)
    # print(percPass)
    # print(np.array(magMeans)-90)

    dfAnova.boxplot('Mean',by='Instrument')
    count = 1
    for i in range(len(cupListClump)):
        # plt.text(count,85,''.join(['p',str(cupListClump[i])]))
        # plt.text(count,84.75,str(dateClump[i]))
        count+=1
    plt.hlines(temp,1,len(instListShort),'r')
    plt.ylabel('Temp (c)')
    dfAnova.boxplot('PercentPass',by='Instrument')
    count = 1
    for i in range(len(cupListClump)):
        plt.text(count,0.4,''.join(['p',str(cupListClump[i])]))
        # plt.text(count,.37,str(dateClump[i]))
        count+=1
    # plt.hlines(temp,0,10,'k')
    # fig = interaction_plot(dfAnova.Instrument,dfAnova.Date,dfAnova.Mean,ms=10)
    plt.show()
    

    
    clumpMeans = [means[i:i+3] for i in range(0,len(means),3)]
    
    
    limit = temp - 3
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
        # print(clumpInst[count])
        
        # print('95 % CI for mean = {:.1f}, {:.1f}, kg/h'.format(ci[0], ci[1]))
        # print('emission limit = {:.2f} kg/h'.format(limit))
        # print('t limit = {:.2f}'.format(t_limit))
        # print('probability sample drops below model-5c =  {:.3f}'.format(pr))

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
def both():
    return


DV(95)






                



























    
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from PCR_TI_USE import anneal,denature
from confidenceFun import CI
import os


folder = 'tape/'

instlist = np.arange(0,len(os.listdir(folder)))

folder2 = 'padVpaste/'
instList2 = ['w86_7','w87_7','w86_9','w87_9','w86_11','w87_11','w86_13','w87_13','w86_15','w87_15','w86_5','w87_5','w86_20','w87_20','w86_23','w87_23','w86_25','w87_25','w86_28','w87_28']

alpha = 0.1
def fullCI(folder,instlistshort):
    means = anneal(folder,instlistshort)[0]
    cis = np.array(anneal(folder,instlistshort)[1]).T

    ciL = cis[0]
    ciR = cis[1]



    
    
    







    mean = np.mean(means)
    meanCI = CI(means,alpha)
    ciLCI = CI(ciL,alpha)
    ciRCI = CI(ciR,alpha)

    # plt.scatter(mean,0)
    # plt.hlines(0,meanCI[0],meanCI[1])
    # plt.hlines(1,ciLCI[0],ciLCI[1],color='r',lw=5)
    # plt.hlines(1,ciRCI[0],ciRCI[1],color='green')
    # plt.grid()
    # plt.show()

    return mean,ciLCI[0],ciRCI[1],means,cis


print(fullCI(folder2,instList2)[0],'+/-',fullCI(folder2,instList2)[2]-fullCI(folder2,instList2)[0])

# for i in range(len(fullCI(folder2,instList2)[3])):
#     plt.hlines(i,fullCI(folder2,instList2)[4][0][i],fullCI(folder2,instList2)[4][1][i],lw=5)
#     plt.plot(fullCI(folder2,instList2)[3][i],i,'o',color='r')
# plt.hlines(-1,fullCI(folder2,instList2)[1],fullCI(folder2,instList2)[2])

# plt.yticks(np.arange(0,len(fullCI(folder2,instList2)[3])),instList2)
# plt.grid()

# plt.show()


# plt.hlines(0,fullCI(folder,instlist)[1],fullCI(folder,instlist)[2],lw=5)

# plt.hlines(1,fullCI(folder2,instList2)[1],fullCI(folder2,instList2)[2],lw=5)
# plt.plot(fullCI(folder,instlist)[0],0,'o',color='r')
# plt.plot(fullCI(folder2,instList2)[0],1,'o',color='r')
# # plt.yticks([0,1],['No-Recess','Recess'])
# plt.title(''.join([str((1-alpha)*100),'% Confidence Interval of the Mean']))
# plt.xlabel('Temperature (c)')
# plt.ylabel('')
# plt.grid()
# plt.show()
# n1 = len(instlist)
# n2 = len(instList2)

# t1 = t.ppf(1.0 - 0.5 * alpha,n1-1)
# t2 = t.ppf(1-.5*alpha,n2-1)

# s1 = (fullCI(folder,instlist)[0] - fullCI(folder,instlist)[1])*np.sqrt(len(instlist))/t1
# s2 = (fullCI(folder2,instList2)[0] - fullCI(folder2,instList2)[1])*np.sqrt(len(instList2))/t2

# SE = np.sqrt(s1**2/n1+s2**2/n2)

# dof = (s1**2/n1+s2**2/n2)**2/((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))

# tStar = t.ppf(1-.5*alpha,dof)
# moe = SE*tStar
# meanDiff = fullCI(folder,instlist)[0] - fullCI(folder2,instList2)[0]

# print(meanDiff-moe,meanDiff+moe)





import matplotlib.pyplot as plt
from confidenceFun import tolArea

def taPlot(compoundPop,alpha,p,col,name):                #compoundPop should be of format[[pop1],[pop2],...]
    dat = tolArea(compoundPop,alpha,p)
    mid = dat[1]
    points = dat[0]
    tis = dat[2]
    tiL,tiR = tis[0]
    tiB,tiT = tis[1]

    # print(mid[0])
    print(points[0])
    plt.plot(points[0],points[1],'o',color=col,label=name)
    plt.hlines(mid[1],tiL,tiR,lw=5,colors=col)
    plt.vlines(mid[0],tiB,tiT,lw=5,colors=col)
    plt.plot(mid[0],mid[1],'o',color='r')
    # plt.show()



josh = {'a':[1],'b':[3,4]}
tess = list(josh.values())
print(tess)
import numpy as np


noTiltLarge = np.array([7/7,7/7,6.5/7,7/7,6.5/7,6/7,6/7,7/7,7/7,7/7,
                        1/7,7/7,5.5/7,1.5/7,1/7,1.5/7,1/6,6.5/7,3.5/7,4/7])

instList = [619,608,623,622,617,620,609,604,610,625]

noThump = noTiltLarge[:10]
thump = noTiltLarge[10:]

def compBinom(m,n,x,y):                  #m=total A; n=total B; x=fail in A; y=fail in B
    p1 = x/m
    p2 = y/n
    pq = (x+y)/(m+n)
    z = (p1-p2)/np.sqrt(pq*(1-pq)*(1/m+1/n))
    if z >= 1.645 or z <= -1.645:
        print('different')
    else:
        print('not different')
    return z

# for indx,val in enumerate(instList):
#     print(val)
#     print(testStat(7,7,noThump[indx]*7,thump[indx]*7))
#     print()

print(compBinom(70,69,67,32.5))
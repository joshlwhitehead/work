"""
Josh W's super duper awesome program for determining kalmann filter coeffs used to train the treatment stage model
in the super duper awesome advanced alpha pcr instruments
"""
import SiblingDir
import matplotlib.pyplot as plt
import numpy as np
import dataCollect.dataToVar as dat



"""data"""
fif = dat.h50              # this data is a list of three vectors [time, thermister, thermocouple(sample)]
sev = dat.h70              # the time vector is not relavent in this code
nin = dat.h90
one = dat.h100



change = 0.001                      #change this to adjust accuracy of kalman coeffs.
                                    #the smaller the value the longer it will take to execute
                                    #but the more accurate the output will be

"""find curve r2"""
def r2(y,fit):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fit)**2)
    r2 = 1-sr/st
    return r2


"""find surface r2"""
def r2surf(zlist,zlistfit):
    zlist = np.array(zlist)
    zlistfit = np.array(zlistfit)
    st = sum((zlist-np.average(zlist))**2)
    sr = sum((zlist-zlistfit)**2)
    r2 = 1-sr/st
    return r2




"""average steady state offset"""
a = 50 - np.average(fif[2][-50:])
b = 70 - np.average(sev[2][-50:])
c = 90 - np.average(nin[2][-50:])
d = 100 - np.average(one[2][-50:])


xx = np.array([50,70,90,100])
yy = np.array([a,b,c,d])
aa,bb,cc = np.polyfit(xx,yy,2)                              #offset coeffs
plt.figure()
plt.title('offset curve')
plt.plot(xx,yy,'o')
plt.plot(xx,aa*xx**2+bb*xx+cc)
plt.show()


print('offset r2 = ',r2(yy,aa*xx**2+bb*xx+cc))
print('offset coeffs:',aa,bb,cc)


rr = {}     # initialize surface r2

shortest = min(len(fif[1]),len(fif[2]),len(sev[1]),len(sev[2]),len(nin[1]),len(nin[2]),len(one[1]),len(one[2])) #data with least amount of points
ytot = [fif[2][:shortest],sev[2][:shortest],nin[2][:shortest],one[2][:shortest]]    #sample
xtot = [fif[1][:shortest],sev[1][:shortest],nin[1][:shortest],one[1][:shortest]]    #thermister


zlist = []                      #rearrange data         
for i in ytot:
    for j in i:
        zlist.append(j)



""" This section is the bulk of the program """



trustVals = np.arange(0,1,change)      #loop through values from 0 to 1 to find best fitting coeffs
for i in trustVals:                     
    zlistfit = []
    for j in range(len(ytot)):
        old = ytot[j][0]
       
        count = 0
        for k in xtot[j]:
            if str(k) == 'nan':
                xtot[j][count] = xtot[j][count-1]
            else:
                offset = aa*k**2+bb*k+cc
                old = old*i+(k-offset)*(1-i)
                zlistfit.append(old)
            count += 1
        

    r = r2surf(zlist,zlistfit)                          #look for reasonable r2 value
    if r >0 and r<1:
        rr[r] = i

# print(rr)
print('r2 surf =',max(rr)) 
   
trust = rr[max(rr)] 
print('a =',trust)
# trust = .99802


plt.figure()
for j in range(len(ytot)):
    old = ytot[j][0]
    ans = []
 
    for k in xtot[j]:
        offset = aa*k**2+bb*k+cc
        old = old*trust+(k-offset)*(1-trust)
        ans.append(old)
    plt.plot(ans)

for i in ytot:
    plt.plot(i) 
plt.grid()
plt.yticks(np.arange(25,95,5))
plt.title('kalman fit')
plt.show()



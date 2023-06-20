import matplotlib.pyplot as plt
import dataToVar as dat
import numpy as np




def parse(file):
    f = open(file,'r')
    lines = f.readlines()
    modTemp = []
    for i in lines:
        if 'modeled = ' in i:
            indx = i.index('modeled = ')
            modTemp.append(float(i[indx+10:indx+14]))
    return modTemp
def mod(filename,date):
    return parse(''.join(['data/',date,'/',filename]))
# mod = parse('data/05Apr2022/lid0Cons0_testa_90.txt')
# mod1 = parse('data/24Mar2022/lid0Cons0_fullRun1.txt')
mod = mod('lid0_break_contAcq.txt','05Apr2022')
modShort = []
for i in range(len(mod)):
    if i%7 == 0:
        modShort.append(mod[i])

# plt.figure()

# plt.plot(dat.test[2])

# # plt.ylim(30,100)
# plt.grid()

plt.figure()
plt.title('1')
# plt.plot(dat.test1[0])
plt.plot(dat.break115[1],label='therm')
plt.plot(mod,label='mod')
plt.plot(dat.break115[2],label='sample')
plt.legend()
plt.grid()

# plt.figure()
# plt.title('2')
# # plt.plot(dat.test1[0])
# plt.plot(dat.oldFr[1],label='therm')
# plt.plot(mod,label='mod')
# plt.plot(dat.oldFr[2],label='sample')
# plt.legend()
# plt.grid()




plt.show()
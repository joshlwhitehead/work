import matplotlib.pyplot as plt
import numpy as np
import dataToVar as dat


x = dat.cupBfr[1]#[:150]
y = dat.cupBfr[0]#[:150]
yy = dat.cupBfr_b[0]
yyy = dat.cupBfr_c[0]
yyyy = dat.cupBfr_d[0]
trust = .9924
offset = 0.35968253451750004*90 - 12.221281458691655
a = dat.cupB90[0]                                           #fresh
b  =dat.cupB90_b[0]                                         #run without replacing cap. possible bubbles
c = dat.cupB90_c[0]                                         # replaced cap
d = dat.cupB90_d[0]                                         # run without replacing cap again
e = dat.cupB90_e[0]                                         #replaced cap again
f = dat.cupB90_f[0]                                         #without removing from inst

g = dat.cupB90_g[0]

old = y[0]
new = []
for i in x:
    old = (trust*old)+(1-trust)*(i-offset)
    new.append(old)

# plt.plot(y,label='run1')
plt.plot(a,label='replace cap')
plt.plot(b)
plt.plot(c,label='replace cap')
plt.plot(d)
plt.plot(e,label='replace cap')
plt.plot(f)
plt.plot(g)

# plt.plot(yy,label='run2')
# plt.plot(yyy,label='run3')
# plt.plot(yyyy,label='run4')
# plt.plot(new)
# plt.plot(x)
# plt.plot(dat.cupBfr_b[1])
plt.grid()
plt.legend()
plt.ylabel('temp (c)')
plt.xlabel('time (sec)')
plt.savefig('test')
print(offset)

# for i in range(len(x)):
#     if str(x[i]) == 'nan':
#         print(i)
avg90 = []
avg70 = []
avg100 = []
aa = dat.cupA70[0]
bb = dat.cupB70[0]
aaa = dat.cupA100[0]
bbb = dat.cupB100[0]
for i in range(len(aa)):
    avg90.append(np.average([a[i],b[i]]))
    avg70.append(np.average([aa[i],bb[i]]))
    avg100.append(np.average([aaa[i],bbb[i]]))
# plt.plot(avg90)
# plt.plot(avg70)
# plt.plot(avg100)
# plt.show()

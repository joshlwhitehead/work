import numpy as np
import matplotlib.pyplot as plt


channel = [480,515,555,590]
melt1 = [38.8,23.3,6.6,3.0]

melt2 = [15.2,6.5,2.4,0.82]
melt3 = [52.6,30,8.7,3.9]
melt4 = [44.2,21.3,7.9,2.6]
# plt.plot(channel,melt1)
# plt.plot(channel,melt2)
# plt.plot(channel,melt3)
# plt.plot(channel,melt4)
# plt.grid()
# plt.show()
chanRat = [515/480,555/515,590/555]
a = []
b = []
c = []
d = []

meltTot = [melt1,melt2,melt3,melt4]
for i in meltTot:
    a.append(i[1]/i[0])
    b.append(i[2]/i[1])
    c.append(i[3]/i[2])
    # d.append(i[0]/i[3])

plt.plot(a)
plt.plot(b)
plt.plot(c)
# plt.plot(d)
plt.show()
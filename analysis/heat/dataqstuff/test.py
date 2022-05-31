# import dataToVar as dat
# import matplotlib.pyplot as plt
# import numpy as np

# aH = 0.06990949622396307
# bH = 3.263507922780718
# trust = 0.99576 + .5*(1-.99576)
# full = dat.break115
# sampa = full[2]
# therma = full[1][:len(sampa)]
# for i in range(len(therma)):
#     if str(therma[i]) == 'nan':
#         print(i)

# def plotMod():                                              #plot mod and sample
#     # plt.figure(figsize=(16,9))

#     old = sampa[0]
#     ans = []
    
#     for k in range(len(therma)):
#         # if k <= 3088:
#         offset = aH*therma[k]+bH
#         old = old*trust+(therma[k]-offset)*(1-trust)
#         ans.append(old)
#         # print(old)
#         # else:
#         #     offset = aC*therma[k]+bC
#         #     old = old*trustC+(therma[k]-offset)*(1-trustC)
#         #     ans.append(old)
#     plt.plot(full[0][:len(sampa)],ans,label='mod')


#     plt.plot(full[0][:len(sampa)],sampa,label='dat')
#     plt.plot(full[0][:len(sampa)],therma) 
#     plt.grid()
#     plt.yticks(np.arange(25,110,5))
#     plt.legend()
#     plt.show()
    
# plotMod()

import matplotlib.pyplot as plt
import dataToVar as dat

plt.plot(dat.h90_c[0][:len(dat.h90_c[2])],dat.h90_c[2])
plt.plot(dat.lid0Cons0_90[0][:len(dat.lid0Cons0_90[2])],dat.lid0Cons0_90[2])
plt.show()
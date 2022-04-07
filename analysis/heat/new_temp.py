import pandas as pd

temp = pd.read_csv('cham1tempReal.csv')['dataQLiquidStg1']
newTemp = []
for i in temp:
    if i != 0:
        newTemp.append(i)
























# time1 = pd.read_csv('cham1tempReal.csv')['Time']
# time1 = time1.tolist()
# temp1 = pd.read_csv('cham1tempReal.csv')['stage1TempC']
# temp1 = temp1.tolist()
# time2 = []
# temp2 = []
# count = 0
# # print(len(time1-1))

# for i in range(len(time1)):
#     if time1[i] >=count:
#         if temp1[i] != 0:
#             time2.append(time1[i])
#             temp2.append(temp1[i])
#         else:
#             time2.append(time1[i-1])
#             temp2.append(temp1[i-1]) 
#         count +=1

# for i in range(len(time2[:-1])):
#     pass
#     # print(time2[i+1]-time2[i])
# # print(time2[30:40])


# dF = {'time':time2,'temp':temp2}

# # print(dF)

# dF = pd.DataFrame(dF)
# dF.to_csv('temp1sec.csv')
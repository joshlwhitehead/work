import pandas as pd


x = {'a':[1],'b':[2],'c':[3]}
y = {'a':[4],'c':[55]}
# x.update(y)
dfx = pd.DataFrame(x)
dfy = pd.DataFrame(y)



# dfx.update(dfy)
# print(dfx)


z = pd.concat([dfx,dfy],ignore_index=1)
print(z)

# z = dfx.append(dfy)
# print(z)
z.to_csv('test.csv')
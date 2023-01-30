x = int(input('how many replicates '))

y = input('instruments ')
y = y.split()


z = []
for u in y:
    for i in range(x):
        z.append(u+'.'+str(i))

print(z)
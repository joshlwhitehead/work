data = open('data\PCR #1 202301041.txt','r').readlines()
count = 0

for i in range(len(data)):
    print(data[count])
    count += 1

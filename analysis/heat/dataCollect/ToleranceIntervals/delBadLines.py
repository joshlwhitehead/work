import os 

def delBad(folder,file):
    try:
        with open(''.join([folder,file]),'r') as readFile:                                                                                        #convert lines in file to list
            goodLines =[]
            for i in readFile:
                if 'd' not in i[:4] and '=' not in i[:4] and 't' not in i[:4]:
                    goodLines.append(i)
        with open(''.join([folder,'NEW',file]),'w') as writeFile:
            for i in goodLines:
            # if i.split()[0] == 'd':
            #     print(i)
                writeFile.write(i)

    except:
        print(file)
        
for i in os.listdir('verif'):
    delBad('verif/',i) 

# x = [1,2,3,2,1]

# with open('test.txt','a') as f:
#     for i in x:
#         f.write(str(i))
    
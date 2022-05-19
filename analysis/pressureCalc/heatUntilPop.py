import matplotlib.pyplot as plt

c115 =[111,162,200]
c110 = [270,375,450]
c105 = [150,0,0]
c100 = [245]



for i in c115:
    plt.scatter(115,i)
for i in c110:
    plt.scatter(110,i)
for i in c105:
    plt.scatter(105,i)
for i in c100:
    plt.scatter(100,i)
plt.grid()
plt.ylabel('time @ frange break (sec)')
plt.xlabel('temperature (c)')
plt.title('Thermister temperature and frange breaks')
plt.show()

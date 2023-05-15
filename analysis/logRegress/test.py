import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


passFail = np.array([0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
x = np.array([1,2,3,4,3,5,4,5,6,5,6,7,8,9,10,9])
X=x.reshape( -1,1)

logr = linear_model.LogisticRegression()
logr.fit(X,passFail)


predicted = logr.predict(np.array([np.linspace(0,15)]).reshape(-1,1))

a,b = np.polyfit(x,passFail,1)
def log(x,a,b):
    return 1/(1+np.exp(-(a*x+b)))
print(a,b)
print(np.linspace(0,15))
print(predicted)

plt.plot(X,passFail,'o')
plt.plot(x,a*x+b)
plt.plot(np.linspace(0,15),log(np.linspace(0,15),a,b))



plt.grid()
plt.show()

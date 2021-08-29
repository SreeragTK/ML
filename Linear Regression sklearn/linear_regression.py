import numpy as np
import random
import matplotlib.pyplot as plt
import sklearn.datasets as datasets
from sklearn.linear_model import LinearRegression
X= np.random.randint(0,50,(150))
C= np.random.randint(-30,30,(150))
Y=[]
for i in range(150):
    k=6*X[i] + C[i]
    Y.append(k)
#printing the datas
plt.scatter(X,Y, label="data")
#Reshapping the array for doing linear regression
x=np.array(X).reshape((-1,1))
reg=LinearRegression().fit(x,Y)
#printing slope and intercept of the fit
print('intercept', reg.intercept_)
print('slope',reg.coef_)
#printing the datas with the fit
plt.plot
plt.plot(X, reg.predict(x), color='k')
k=np.array(X).reshape((5,-1))
k2=k[2]
print(k2)
print(k2[1])
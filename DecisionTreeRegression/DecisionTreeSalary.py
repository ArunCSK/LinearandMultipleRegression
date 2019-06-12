import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("Position_Salaries.csv")
X = data.iloc[:, 1:2].values
Y = data.iloc[:, 2].values

from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state=0)
reg.fit(X,Y)

ypred= reg.predict(X)
#print(ypred)

#plt.plot(X, ypred,color='g')
x_grid = np.arange(min(X), max(X), 0.01)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(X,Y, color='r')
plt.plot(x_grid, reg.predict(x_grid), color='b')
r2 = reg.score(x_grid, reg.predict(x_grid))
print(r2)
plt.show()


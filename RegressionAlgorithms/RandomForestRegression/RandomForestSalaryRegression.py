import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('Position_Salaries.csv')
#data = pd.read_csv('D:/Arundev/py/LinearRegression/RandomForestRegression/Position_Salaries.csv')
X = data.iloc[:, 1:2].values
y = data.iloc[:, 2].values

reg = RandomForestRegressor(n_estimators=100, random_state=0)
reg.fit(X,y)


#y_pred = reg.predict(np.array([6.5]).reshape(-1,1))
#print(y_pred)
X_grid = np.arange(min(X), max(X),  0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X,y, color='r')
plt.plot(X_grid, reg.predict(X_grid),color='b')
plt.show()
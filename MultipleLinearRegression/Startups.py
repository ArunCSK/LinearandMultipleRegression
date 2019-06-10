
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("50_Startups.csv")
#print(dataset)


X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, 4]

states=pd.get_dummies(X['State'],drop_first=True)
#print(Y)


X=X.drop('State',axis=1)
X=pd.concat([X,states],axis=1)
regressor = LinearRegression()
regressor.fit(X, Y)
y_pred = regressor.predict(X)

plt.plot(X, y_pred)
r2 = regressor.score(X,y_pred)
print(r2)
plt.show()



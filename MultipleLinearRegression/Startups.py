
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("50_Startups.csv")


X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

#states=pd.get_dummies(X['State'])

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()
#print(X)
X = X[:, 1:]

#from sklearn.cross_validation import train_test_split
#X_train , X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

reg = LinearRegression()
reg.fit(X, Y)
y_pred = reg.predict(X)
print(y_pred)
plt.scatter(X, Y, color='r')
plt.plot(X, y_pred, color='b')
plt.show()

#X=X.drop('State',axis=1)
#X=pd.concat([X,states],axis=1)
#reg = LinearRegression()
#reg.fit(X, Y)
#y_pred = reg.predict(X)
#plt.plot(X, y_pred)


#plt.scatter(dataset['Marketing Spend'], dataset['Profit'],color='g')
#reg.fit(market_reshape, profit_reshape)
#market_pred = reg.predict(market_reshape)
#plt.plot(dataset["Marketing Spend"],market_pred,color='g',label='Marketing Spend')

#plt.xlabel("Profit")
#plt.ylabel("Feature")
#plt.legend(loc="outer right")
#r2 = reg.score(X,y_pred)
#print(r2)
#plt.show()



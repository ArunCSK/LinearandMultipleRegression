import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("/home/admin1/Desktop/PythonVM/LinearRegProblem/bike_sharing.csv")

data.rename(columns={'weathersit':'weather',
                     'mnth':'month',
                     'hr':'hour',
                     'hum': 'humidity',
                     'cnt':'count'},inplace=True)


data = data.drop(['instant','dteday','yr'], axis=1)

data_dummy = data

def dummify_dataset(df, column):
    df = pd.concat([df, pd.get_dummies(df[column], prefix= column , drop_first=True)] , axis= 1)
    return df

column_to_dumify = ['season', 'month', 'hour', 'holiday', 'weekday', 'workingday','weather']

for column in column_to_dumify:
    data_dummy = dummify_dataset(data_dummy, column)

y= data_dummy["count"]
X = data_dummy.drop(['count'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33, random_state=42)

models = [DecisionTreeRegressor()]

def test_algorithms(model):
    kfold = model_selection.KFold(n_splits=10, random_state=0)
    predicted = model_selection.cross_val_score(model, X_test, y_test,cv=kfold, scoring='neg_mean_squared_error')
    print(predicted.mean())

for model in models:
    test_algorithms(model)


#decision graph
data = data.iloc[1:20,:]
X = data["temp"].values
y = data["count"].values

reg = DecisionTreeRegressor(random_state=0)

reg.fit(X.reshape(-1,1),y.reshape(-1,1))
plt.scatter(X,y, color='r')
x_grid = np.arange(min(X), max(X), 0.01)
x_grid = x_grid.reshape(len(x_grid),1)


plt.plot(x_grid,reg.predict(x_grid))
r2 = reg.score(x_grid,reg.predict(x_grid))
print(r2)
plt.show()

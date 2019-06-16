import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#read csv file
data = pd.read_csv('bike_sharing.csv')
#print(data)

#data_train = data.sample(frac=0.8,random_state=0)
#print(data_train)

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

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

#Random Forest Model
reg = RandomForestRegressor(n_estimators=10,  random_state=10)
reg.fit(X_train, y_train)

#Graph
X_grid = np.arange(min(X_train), max(X_train),  0.1)
print(X_grid)
X_grid = X_grid.reshape(len(X_grid),1)



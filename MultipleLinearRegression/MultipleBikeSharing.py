import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, Ridge, HuberRegressor, ElasticNetCV
from sklearn.ensemble import BaggingRegressor, ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor


data = pd.read_csv("/home/admin1/Desktop/PythonVM/LinearRegProblem/bike_sharing.csv")
#print(data.shape)
#print(data.head())
#print(data.dtypes)

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

#print(data_dummy.head(1))

y= data_dummy["count"]
X = data_dummy.drop(['count'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33, random_state=42)

models = [LinearRegression()]


def test_algorithms(model):
    kfold = model_selection.KFold(n_splits=10, random_state=0)
    predicted = model_selection.cross_val_score(model, X_train, y_train,cv=kfold, scoring='neg_mean_squared_error')
    print(predicted.mean())

for model in models:
    test_algorithms(model)

#for ploting graph
data_count = data["count"].values
data_temp = data["temp"].values
data_holiday = data["holiday"].values
data_weekday = data["weekday"].values
data_humidity = data["humidity"].values
data_casual = data["casual"].values
data_register = data["registered"].values


#graph scatter plot
plt.scatter(data_count,data_temp, color='r')


data_count = data_count.reshape(-1,1)
data_temp = data_temp.reshape(-1,1)
data_holiday = data_holiday.reshape(-1,1)
data_weekday = data_weekday.reshape(-1,1)
data_humidity = data_humidity.reshape(-1,1)
data_casual = data_casual.reshape(-1,1)
data_register = data_register.reshape(-1,1)

reg = LinearRegression()
reg.fit(data_count,data_temp)
ypred = reg.predict(data_count)
#print("Temperature:",ypred)
plt.plot(data_count, ypred)
#plt.show()

reg.fit(data_holiday,data_count)
ypred1 = reg.predict(data_holiday)
#print("Holiday:",ypred1)

reg.fit(data_weekday, data_count)
ypred2 = reg.predict(data_weekday)
#print("Weekday:",ypred2)

reg.fit(data_casual, data_count)
ypred3 = reg.predict(data_casual)
#print("Casual:",ypred3)


reg.fit(data_humidity,data_count)
ypred4 = reg.predict(data_humidity)
#print("Weekday:",ypred4)

reg.fit(data_humidity,data_count)
ypred4 = reg.predict(data_humidity)
#print("Humaidity:",ypred4)


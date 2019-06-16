import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import pickle

data = pd.read_csv('Position_Salaries.csv')
#data = pd.read_csv('D:\Arundev\py\LinearRegression\SupportVectorRegression\Position_Salaries.csv')
X = data.iloc[:, 1:2].values
y = data.iloc[:, 2].values
length_old = len(data.columns)


sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X.reshape(-1,1))
y = sc_y.fit_transform(y.reshape(-1,1))

reg = SVR(kernel='rbf')
reg.fit(X,y)


#y_pred = reg.predict(np.array([5]).reshape(-1,1))

r2 = reg.score(X,y)
print(r2)

#y_pred = reg.predict(np.array([6.5]).reshape(-1,1))
#print(y_pred)
plt.scatter(X,y, color='r')
plt.plot(X, reg.predict(X),color='b')
plt.show()


# Importing dataset
#dataSet = pd.read_csv('D:\Arundev\py\LinearRegression\SupportVectorRegression\Position_Salaries.csv')
length_old = len(dataSet.columns)

# Handling categorical data
positions = pd.get_dummies(dataSet['Position'])
dataSet = dataSet.drop('Position', axis=1)
dataSet = pd.concat([dataSet, positions], axis=1)

# Splitting dataset into 2 different csv files
df_training = dataSet.sample(frac=0.7)
df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)
length_new = len(dataSet.columns)
y_index = dataSet.columns.get_loc("Salary")
df_training.to_csv('training_data.csv', header=True, index=None)
df_test.to_csv('test_data.csv', header=True, index=None)

dataSet = pd.read_csv('training_data.csv')

#save model
file_name = 'RandomForestRegression.pkl'
pkl_file = open(file_name, 'wb')
model = pickle.dump(reg, pkl_file)
# Loading pickle model to predict data from test_data.csv file
pkl_file = open(file_name, 'rb')
model_pkl = pickle.load(pkl_file)

dataSet_testdata = pd.read_csv('test_data.csv')

x_testdata = dataSet_testdata.iloc[:, (len(data.columns)-1): len(dataSet)]
y_testdata = dataSet_testdata.iloc[:, y_index:(y_index+1)]
y_pred_pkl = model_pkl.predict(x_testdata)

print(y_pred_pkl)

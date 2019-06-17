# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import pickle

# Importing dataset
dataSet = pd.read_csv('Position_Salaries.csv')
length_old = len(dataSet.columns)

# Handling categorical data
positions = pd.get_dummies(dataSet['Position'])
dataSet = dataSet.drop('Position', axis=1)
dataSet = pd.concat([dataSet, positions], axis=1)

# Splitting dataset into 2 different csv files
df_training = dataSet.sample(frac=0.7)
df_test = pd.concat([dataSet, df_training]).drop_duplicates(keep=False)

#df_training.to_csv('../inputFiles/training_data.csv', header=True, index=None)
#df_test.to_csv('../inputFiles/test_data.csv', header=True, index=None)

#dataSet = pd.read_csv('../inputFiles/training_data.csv')

length_new = len(dataSet.columns)

y_index = dataSet.columns.get_loc("Salary")

y = dataSet.iloc[:, y_index:(y_index+1)]
x = dataSet.iloc[:, (length_old-1):length_new]

# Checking for null values
if y['Salary'].isnull().sum() > 0:
    print("Taking care of null values of Salary column")
    y = y.fillna(y.mean())

# Feature scaling
scX = StandardScaler()
x = scX.fit_transform(x)

# Splitting data into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Fitting training data into model
regression = SVR(kernel='rbf', gamma='auto')
regression.fit(x_train, y_train.values.ravel())

# Using model to predict test data
y_pred = regression.predict(x_test)

# Calculating accuracy
accuracy = r2_score(y_test, y_pred)
print("Accuracy from model is : ", accuracy)

# Dumping model into pickle
#if accuracy > 0.8:
file_name = 'RandomForestRegression.pkl'
pkl_file = open(file_name, 'wb')
model = pickle.dump(regression, pkl_file)

# Loading pickle model to predict data from test_data.csv file
pkl_file = open(file_name, 'rb')
model_pkl = pickle.load(pkl_file)

dataSet_testdata = pd.read_csv('test_data.csv')

x_testdata = dataSet_testdata.iloc[:, (length_old-1):length_new]
y_testdata = dataSet_testdata.iloc[:, y_index:(y_index+1)]

y_pred_pkl = model_pkl.predict(x_testdata)
#print("y_pred_pkl:"+y_pred_pkl)
# Calculating accuracy from pickle model
accuracy_pk = r2_score(y_testdata, y_pred_pkl)
print("Accuracy by pickle model ", accuracy_pk)

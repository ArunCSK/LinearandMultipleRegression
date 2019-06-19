import numpy as np
import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.metrics import confusion_matrix
import csv
#windows file path
Data_746 = pd.read_csv("D:\\Arundev\\py\\MachineLearningAlgorithms\\ClassificationAlgorithms\\newHIV-1_data\\746Data.txt", sep=',',names=["Octomer","result"])
#Data_1625 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/1625Data.txt")
#Data_impens = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/impensData.txt")
#Data_schilling = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/schillingData.txt")

#linux file path
#Data_746 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/746Data.txt", sep=',',names=["Octomer","Cleaved/Non-Cleaved"])
#Data_1625 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/1625Data.txt")
#Data_impens = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/impensData.txt")
#Data_schilling = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/schillingData.txt")
#with open("D:\\Arundev\\py\\MachineLearningAlgorithms\\ClassificationAlgorithms\\newHIV-1_data\\746Data.txt") as filename:
#   template=csv.reader(filename)
#   for row in template:
#       df.append(row)








#print(np.array([x1]).reshape(len(x1),1))


#X = Data_746["Octomer"].str.split(" ", n = 1, expand = True) 
#new_df = pd.DataFrame(df.City.str.split('').tolist(), index=df.EmployeeId).stack()
#new_df = new_df.reset_index([0, 'EmployeeId'])
y = Data_746["result"].values
#print(X)
#Data_746['Octomer'] = Data_746['Octomer'].astype('category')
#print(Data_746["Octomer"])
X = Data_746["Octomer"]
df = pd.DataFrame({'Octomer':[X]}) 
x = pd.DataFrame(Data_746.Octomer.str.split("").tolist())
#x = x.reset_index([0,'result'])
#print(x.iloc[:, 1:8])

X = x.iloc[:, 1:8]
#print(df)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 0 )
#train['day'] = train['day'].astype('category')

#feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
#print(X_train)

#classifier = LogisticRegression()
#classifier.fit(X_train.reshape(-1,1), y_train)


#y_pred = classifier.predict(X_test.reshape(-1,1))

#cm = confusion_matrix(y_test, y_pred)
#print(cm)









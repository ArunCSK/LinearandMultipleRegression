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

X = x.iloc[:, 1:9 ]
#print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 0 )
#print(X_train)

#onehotencoding
# labelencoder_X = LabelEncoder()
# X_train = labelencoder_X.fit_transform(X_train)
# onehotencoder = OneHotEncoder(categorical_features=[1,2,3,4,5,6,7,8])
# X = onehotencoder.fit_transform(X_train).toarray()

#Replace maping
#replace = {'char' : {'A':1, 'B': 2 , 'C':3, 'D': 4 , 'E': 5 , 'F': 6, 'G': 7 , 'H': 8 , 'I':9, 'J':10 , 'K':11, 'J':12, 'L':13,'M':14,'N':15,'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'V':21, 'W':22, 'Y':23}}
replace = {'char' : {'A':1, 'C':2, 'D': 3 , 'E': 4 , 'F': 5, 'G': 6 , 'H': 7 , 'I':8, 'K':9, 'L':10,'M':11,'N':12,'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'Y':20}}
labels = X_train[1].astype('category').cat.categories.tolist()

replace_map_comp = {'char' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
#print(replace_map_comp)
x1 = X_train[1]
#print(x1)
x1.replace(replace_map_comp,inplace=True)

print(x1.head())


#feature scaling
sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)
#print(X_train)

#classifier = LogisticRegression()
#classifier.fit(X_train.reshape(-1,1), y_train)


#y_pred = classifier.predict(X_test.reshape(-1,1))

#cm = confusion_matrix(y_test, y_pred)
#print(cm)









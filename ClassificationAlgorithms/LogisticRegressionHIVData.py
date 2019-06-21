#importing libariries
import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


#windows file path
Data_746 = pd.read_csv("D:\\Arundev\\py\\MachineLearningAlgorithms\\ClassificationAlgorithms\\newHIV-1_data\\746Data.txt", sep=',',names=["Octomer","result"])
#Data_1625 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/1625Data.txt")
#Data_impens = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/impensData.txt")
#Data_schilling = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/schillingData.txt")

##linux file path
#Data_746 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/746Data.txt", sep=',',names=["Octomer","result"])
#Data_1625 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/1625Data.txt", sep=',',names=["Octomer","result"])
#Data_impens = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/impensData.txt",sep=',',names=["Octomer","result"])
#Data_schilling = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/schillingData.txt",sep=',',names=["Octomer","result"])


##reading CSV using import csv
#import csv
#with open("D:\\Arundev\\py\\MachineLearningAlgorithms\\ClassificationAlgorithms\\newHIV-1_data\\746Data.txt") as filename:
#   template=csv.reader(filename)
#   for row in template:
#       df.append(row)


#new_df = pd.DataFrame(df.City.str.split('').tolist(), index=df.EmployeeId).stack()
#new_df = new_df.reset_index([0, 'EmployeeId'])


#working in windows
#X = pd.DataFrame(Data_746.Octomer.str.split('').tolist())
#x = x.reset_index([0,'result'])
#y = Data_746["result"].values

#working in both linux and windows
X = Data_746['Octomer'].apply(lambda x: pd.Series(list(x)))
y = Data_746["result"].values
#X = Data_1625['Octomer'].apply(lambda x: pd.Series(list(x)))
#y = Data_1625["result"].values
#X = Data_impens['Octomer'].apply(lambda x: pd.Series(list(x)))
#y = Data_impens["result"].values
#X = Data_schilling['Octomer'].apply(lambda x: pd.Series(list(x)))
#y = Data_schilling["result"].values



#print(x)
#X = x.iloc[:, 1:9 ]
#print(X)

#Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30 , random_state = 0 )
#print(type(X_train))


#Replace maping
#replace = {'char' : {'A':1, 'B': 2 , 'C':3, 'D': 4 , 'E': 5 , 'F': 6, 'G': 7 , 'H': 8 , 'I':9, 'J':10 , 'K':11, 'J':12, 'L':13,'M':14,'N':15,'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'V':21, 'W':22, 'Y':23}}
#replace = {'1' : {'A':1, 'C':2, 'D': 3 , 'E': 4 , 'F': 5, 'G': 6 , 'H': 7 , 'I':8, 'K':9, 'L':10,'M':11,'N':12,'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'Y':20}}
#pd.value_counts(X_train.values.flatten())
#labels = X_train[1].astype('category').cat.categories.tolist()
#print(labels)
#replace_map_comp = {'char' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
#print(replace_map_comp)
#x1 = X_train[1].copy()
#print(x1)
#X_train[1].replace(replace_map_comp,inplace=True)



#Get Dummies
#X_Train_dummies = pd.get_dummies(X_train.iloc[:,0:9] ,columns=[0,1,2,3,4,5,6,7])
#X_Test_dummies = pd.get_dummies(X_test.iloc[:,0:9] ,columns=[0,1,2,3,4,5,6,7])
X_Train_dummies = pd.get_dummies(X_train.iloc[:,3:5] ,columns=[3,4])
X_Test_dummies = pd.get_dummies(X_test.iloc[:,3:5] ,columns=[3,4])
#print(X_Train_dummies.head())

#feature scaling
sc_X = StandardScaler()
sc_X_test = StandardScaler()
X_train = sc_X.fit_transform(X_Train_dummies)
X_test = sc_X_test.fit_transform(X_Test_dummies)
#print(X_train)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
print(y_pred)
cm = confusion_matrix(y_test, y_pred)


print(accuracy_score(y_test,y_pred)%100)
print(cm)









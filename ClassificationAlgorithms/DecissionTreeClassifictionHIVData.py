import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

##linux file path
Data_746 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/746Data.txt", sep=',',names=["Octomer","result"])
Data_1625 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/1625Data.txt", sep=',',names=["Octomer","result"])
Data_impens = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/impensData.txt",sep=',',names=["Octomer","result"])
Data_schilling = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/schillingData.txt",sep=',',names=["Octomer","result"])


#working in linux
X = Data_746['Octomer'].apply(lambda x: pd.Series(list(x)))
y = Data_746["result"].values
#X = Data_1625['Octomer'].apply(lambda x: pd.Series(list(x)))
#y = Data_1625["result"].values
#X = Data_impens['Octomer'].apply(lambda x: pd.Series(list(x)))
#y = Data_impens["result"].values
#X = Data_schilling['Octomer'].apply(lambda x: pd.Series(list(x)))
#y = Data_schilling["result"].values

#Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30 , random_state = 0 )

#Get Dummies
#X_Train_dummies = pd.get_dummies(X_train.iloc[:,0:9] ,columns=[0,1,2,3,4,5,6,7])
#X_Test_dummies = pd.get_dummies(X_test.iloc[:,0:9] ,columns=[0,1,2,3,4,5,6,7])
X_Train_dummies = pd.get_dummies(X_train.iloc[:,3:5] )
X_Test_dummies = pd.get_dummies(X_test.iloc[:,3:5] )

#feature scaling
sc_X = StandardScaler()
sc_X_test = StandardScaler()
X_train = sc_X.fit_transform(X_Train_dummies)
X_test = sc_X_test.fit_transform(X_Test_dummies)

classifier = DecisionTreeClassifier(random_state=0)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
print(y_pred)
cm = confusion_matrix(y_test, y_pred)


print(accuracy_score(y_test,y_pred)%100)
print(cm)

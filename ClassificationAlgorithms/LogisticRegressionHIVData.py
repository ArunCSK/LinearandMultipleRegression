import numpy as np
import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.metrics import confusion_matrix

Data_746 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/746Data.txt", sep=',',names=["Octomer","Cleaved/Non-Cleaved"])
Data_1625 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/1625Data.txt")

#print(Data_746)

Data_impens = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/impensData.txt")
Data_schilling = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/schillingData.txt")
print(Data_746)


'''x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
for i in octomer:
    for k in range(len(i)):
        for j in i:
            if k ==1:
                x1 += j
            elif k == 2:
                x2 += j
            elif k == 3:
                x3 += j
            elif k == 4:
                x4 += j
            elif k == 5:
                x5 += j
            elif k == 6:
                x6 += j'''


#print(np.array([x1]).reshape(len(x1),1))

X = Data_746["Octomer"].values
y = Data_746["Cleaved/Non-Cleaved"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 0 )

#feature scaling
#X_test = sc_X.transform(X_test)
print(X_train)

classifier = LogisticRegression()
classifier.fit(X_train.reshape(-1,1), y_train)


y_pred = classifier.predict(X_test.reshape(-1,1))

cm = confusion_matrix(y_test, y_pred)
#print(cm)









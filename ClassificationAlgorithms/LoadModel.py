import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection  import train_test_split
from sklearn.metrics import confusion_matrix

#file_name = "LogisticRegression.pkl"
file_name = "RandomForestClassification.pkl"
pkl_file = open(file_name, 'rb')
model_pkl = pickle.load(pkl_file)

#Load Data
data = pd.read_csv("Social_Network_Ads.csv")
x_test = data.iloc[:,[2,3]].values
y_test = data.iloc[:,4].values

#Split Data
#X_train, X_test, y_train, y_test = train_test_split(x_test, y_test, test_size = 0.25 , random_state = 0 )

sc_X = StandardScaler()
X_train = sc_X.fit_transform(x_test)

y_pred_pkl = model_pkl.predict(X_train)

#cm = confusion_matrix(y_test, y_pred_pkl)
print(y_pred_pkl)

#print(y_pred_pkl)

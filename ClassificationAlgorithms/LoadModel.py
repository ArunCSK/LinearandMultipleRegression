import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

file_name = "LogisticRegression.pkl"
#file_name = "RandomForestClassification.pkl"
pkl_file = open(file_name, 'rb')
model_pkl = pickle.load(pkl_file)

#Load Data
data = pd.read_csv("Social_Network_Ads.csv")
x_test = data.iloc[:,2:3].values
y_test = data.iloc[:,4].values

sc_X = StandardScaler()
x = sc_X.fit_transform(x_test)

y_pred_pkl = model_pkl.predict(x_test)
#print(x_test)

#print(y_pred_pkl)

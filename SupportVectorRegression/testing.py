import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import pickle

pkl_file = open('RandomForestRegression.pkl', 'rb')
model_pkl = pickle.load(pkl_file)

#dataSet_testdata = pd.read_csv('test_data.csv')

#x_testdata = dataSet_testdata.iloc[:, (len(data.columns)-1): len(dataSet)]
#
y_pred_pkl = model_pkl.predict(np.array([6.5]).reshape(-1,1))

print(y_pred_pkl)
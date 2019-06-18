import numpy as np
import pandas as pd

Data_746 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/746Data.txt")
Data_1625 = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/1625Data.txt")

#print(Data_746)

Data_impens = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/impensData.txt")
Data_schilling = pd.read_csv("/home/admin1/Desktop/PythonVM/ClassificationAlgorithms/newHIV-1_data/schillingData.txt")

cleaved = np.where(
print(cleaved)
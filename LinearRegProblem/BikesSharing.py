import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("/home/admin1/Desktop/PythonVM/LinearRegProblem/bike_sharing.csv")
#print(data)

data_humidity  = data["temp"].values
data_count= data["cnt"].values

plt.scatter(data_count, data_humidity, color='r')

reg = LinearRegression()

m = len(data_count)
data_count = data_count.reshape(m,1)
data_humidity = data_humidity.reshape(m,1)
reg.fit(data_count, data_humidity)
y_pred = reg.predict(data_count)
plt.plot(data_count, y_pred, color='b')
r2 = reg.score(data_count, data_humidity)
print(r2)
plt.show()

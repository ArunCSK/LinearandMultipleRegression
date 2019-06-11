import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("/home/admin1/Desktop/PythonVM/LinearRegProblem/bike_sharing.csv")
#print(data)

data_count = data["cnt"].values
data_temp = data["temp"].values
data_holiday = data["holiday"].values
data_weekday = data["weekday"].values
data_humidity = data["hum"].values
data_casual = data["casual"].values
data_register = data["registered"].values

data_count = data_count.reshape(-1,1)
data_temp = data_temp.reshape(-1,1)
data_holiday = data_holiday.reshape(-1,1)
data_weekday = data_weekday.reshape(-1,1)
data_humidity = data_humidity.reshape(-1,1)
data_casual = data_casual.reshape(-1,1)
data_register = data_register.reshape(-1,1)


reg = LinearRegression()
reg.fit(data_temp, data_count)
ypred = reg.predict(data_count)
print("Temperature:",ypred)
plt.plot(data_count, ypred)
plt.show()

reg.fit(data_holiday,data_count)
ypred1 = reg.predict(data_holiday)
print("Holiday:",ypred1)

reg.fit(data_weekday, data_count)
ypred2 = reg.predict(data_weekday)
print("Weekday:",ypred2)


reg.fit(data_casual, data_count)
ypred3 = reg.predict(data_casual)
print("Casual:",ypred3)


reg.fit(data_humidity,data_count)
ypred4 = reg.predict(data_humidity)
print("Weekday:",ypred4)

reg.fit(data_humidity,data_count)
ypred4 = reg.predict(data_humidity)
print("Humaidity:",ypred4)

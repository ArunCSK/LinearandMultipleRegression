import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("/home/admin1/Desktop/PythonVM/LinearRegProblem/Salary_Data.csv")
data_exp = data["YearsExperience"].values
data_salary = data["Salary"].values

plt.scatter(data_exp, data_salary, color='r')


m = len(data_exp)
data_exp = data_exp.reshape((m,1))
data_salary = data_salary.reshape((m,1))
reg = LinearRegression()
reg.fit(data_exp, data_salary)
Y_pred = reg.predict(data_exp)

r2_score = reg.score(data_exp , data_salary)
plt.plot(data_exp, Y_pred, color='b')
plt.show()

#print(r2_score)



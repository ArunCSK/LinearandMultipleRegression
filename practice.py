# Databricks notebook source
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

dbutils.widgets.text("output", "","")
dbutils.widgets.get("output")
FilePath = getArgument("output")

dbutils.widgets.text("filename", "","")
dbutils.widgets.get("filename")
filename = getArgument("filename")
storage_account_name = "arunstorage"
storage_account_access_key = "La0RcP2uBJK2j1mqI2vatAhFs7LfKYpxI4CrHvhd99xQ2ACe7dsoUSRf2DEB66XmGDBeEWQERB9JBXmioP9z8Q=="


spark.conf.set(
 "fs.azure.account.key."+storage_account_name+".blob.core.windows.net",
 storage_account_access_key)


file_location = "wasbs://aruncontainer@arunstorage.blob.core.windows.net"+FilePath+"/"+filename
print(file_location)
file_type = "csv"


df = spark.read.format(file_type).option("inferSchema", "true").load(file_location)
#df.show()

data = df.toPandas()
X_train = data.iloc[2:len(data), 2:6]
y_train = data.iloc[2:len(data), 1]

reg = LinearRegression()
model = reg.fit(X_train,y_train)

filename = "linear.pkl"
pklfile = open(filename, 'wb')
model = pickle.dump(model, pklfile)
pklfile.close()

display(dbutils.fs.ls("file:/databricks/driver/"))

#display(dbutils("files:databricks/driver"))

dbutils.fs.mount(
  source = "wasbs://aruncontainer@arunstorage.blob.core.windows.net",
  mount_point = "/mnt/Arun",
  extra_configs = {"fs.azure.account.key.week6storage.blob.core.windows.net": "La0RcP2uBJK2j1mqI2vatAhFs7LfKYpxI4CrHvhd99xQ2ACe7dsoUSRf2DEB66XmGDBeEWQERB9JBXmioP9z8Q=="})

dbutils.fs.cp("file:/databricks/driver/linear.pkl","/mnt/Arun")



# COMMAND ----------



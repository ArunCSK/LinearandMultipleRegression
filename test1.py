import requests
import json
from time import sleep
from kafka import KafkaProducer

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=compact&apikey=0D8RR9NDGU7URNQT")
data = response.json()

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='wn0-arunka.o04a3kjzrqlu3ermjx0gsiua3e.cx.internal.cloudapp.net:9092,wn1-arunka.o04a3kjzrqlu3ermjx0gsiua3e.cx.internal.cloudapp.net:9092',value_serializer=str.encode)


for time in data["Time Series (1min)"]:
    values = "Open:"+data["Time Series (1min)"][time]["1. open"],", High:"+data["Time Series (1min)"][time]["2. high"]," Low:"+data["Time Series (1min)"][time]["3. low"]," Close:"+data["Time Series (1min)"][time]["4. close"],", Volume:",data["Time Series (1min)"][time]["5. volume"]
    producer.send("test", value=values)

producer.close()

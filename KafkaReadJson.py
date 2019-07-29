import requests
import json
import ast
from kafka import KafkaConsumer
from time import sleep
from kafka import KafkaProducer

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=compact&apikey=0D8RR9NDGU7URNQT")
data = response.json()
#print(data)

#producer = KafkaProducer(bootstrap_servers='wn0-arunka.o04a3kjzrqlu3ermjx0gsiua3e.cx.internal.cloudapp.net:9092,wn1-arunka.o04a3kjzrqlu3ermjx0gsiua3e.cx.internal.cloudapp.net:9092')
producer = KafkaProducer(bootstrap_servers='wn0-arunka.o04a3kjzrqlu3ermjx0gsiua3e.cx.internal.cloudapp.net:9092,wn1-arunka.o04a3kjzrqlu3ermjx0gsiua3e.cx.internal.cloudapp.net:9092',value_serializer=lambda m: json.dumps(m).encode('ascii'))
for time in data["Time Series (1min)"]:
    values = "Open:"+data["Time Series (1min)"][time]["1. open"],", High:"+data["Time Series (1min)"][time]["2. high"]," Low:"+data["Time Series (1min)"][time]["3. low"]," Close:"+data["Time Series (1min)"][time]["4. close"],", Volume:",data["Time Series (1min)"][time]["5. volume"]
    producer.send('StockPriceJsontopic', { "Open": data["Time Series (1min)"][time]["1. open"],"High": data["Time Series (1min)"][time]["2. high"],"Low" : data["Time Series (1min)"][time]["3. low"],"Close": data["Time Series (1min)"][time]["4. close"],"Volume": data["Time Series (1min)"][time]["5. volume"] })
    #print(values)
    values = ''
    sleep(5)        


consumer = KafkaConsumer("StockPriceJsontopic",bootstrap_servers='10.0.0.18:9092,10.0.0.19:9092,10.0.0.20:9092,10.0.0.21:9092',auto_offset_reset="earliest")
consumer.subscribe(["StockPriceJsontopic"])
data = {}

for message in consumer:
    #print("Hello",message.value)
    data = ast.literal_eval(message.value.decode('utf-8'))
    print(data)
    b = ast.literal_eval(data)
    #print(b)
    #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))

consumer.close()





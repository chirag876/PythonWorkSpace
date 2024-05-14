from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name='Python'
producer = KafkaProducer(bootstrap_servers=['192.168.0.113:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    print(data)
    producer.send(topic_name, value=data)
    sleep(5)
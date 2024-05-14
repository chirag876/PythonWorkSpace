from kafka import KafkaProducer

def produce_messages():
    # Kafka producer configuration
    producer = KafkaProducer(bootstrap_servers='192.168.0.113:9092')

    # Produce messages
    for i in range(10):
        message = "Message {}".format(i)
        producer.send('Python', message.encode('utf-8'))
        print("Produced: ", message)

    # Flush the producer
    producer.flush()
    # Close the producer
    producer.close()

if __name__ == "__main__":
    produce_messages()

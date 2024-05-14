from kafka import KafkaConsumer

def consume_messages():
    # Kafka consumer configuration
    consumer = KafkaConsumer('Python', bootstrap_servers='192.168.0.113:9092',
                             auto_offset_reset='earliest', group_id=None)

    # Consume messages
    for message in consumer:
        print("Consumed: ", message.value.decode('utf-8'))

if __name__ == "__main__":
    consume_messages()


from confluent_kafka import Producer
import gzip
import json

# Kafka broker configuration
bootstrap_servers = ''
sasl_username = ''
sasl_password = ''
topic = 'topic_0'

# Create a Kafka producer configuration
producer_config = {
    # 'bootstrap.servers': bootstrap_servers,
    # 'sasl.mechanism': 'PLAIN',
    # 'security.protocol': 'SASL_SSL',
    # 'sasl.username': sasl_username,
    # 'sasl.password': sasl_password,
}

# Create a Kafka producer instance
producer = Producer(producer_config)

def delivery_report(err, msg):
    """Delivery report callback function called on producing message."""
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Send Sms Message  
def send_sms_message(producer, message):
    json_message = json.dumps(message)
    # producer.produce(topic=topic, key='process_status', value=json_message, callback=delivery_report)
    # producer.poll(0)  # Trigger delivery report callbacks
    # producer.flush()

def publish_sms_to_kafka(process_status):   
        
       
    if(process_status == 'exist'):
        sms_message={
            "schema_found": "True",
            "input_file": "input_myorg_v1.csv",
            "schema_file": "schema.csv",
            "output_file": "processed_files.zip",
            "error": "No Error Found"
        }
       

    elif(process_status == 'not_exist'):
        sms_message={
            "schema_found": "False",
            "input_file": "input_myorg_v1.csv",
            "schema_file": "schema.csv"
        }

            
    # print("kafka sms send ")
    #     # Send the SMS message
    #send_sms_message(producer, sms_message)


    # Close the Kafka producer
    producer.flush()

            
    # print("kafka sms send ")
    #     # Send the SMS message
    send_sms_message(producer, sms_message)


    # Close the Kafka producer
    producer.flush()


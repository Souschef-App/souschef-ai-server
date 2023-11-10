
from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer(bootstrap_servers='localhost:1234')
    consumer.subscribe(['my_favorite_topic'])
    for msg in consumer:
        print (msg)

if __name__ == "__main__":
    main()
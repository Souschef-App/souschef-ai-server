
from kafka import KafkaConsumer

import logging
logging.basicConfig(level=logging.INFO)

def main():
    print("Running AI")

    logger = logging.getLogger(__name__)
    try:

        consumer = KafkaConsumer('my-topic',
                                group_id='my-group',
                                bootstrap_servers=['kafka:9092'])

        for message in consumer:
            logger.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value))
    except Exception as ex:
        logger.error(ex)


if __name__ == "__main__":
    main()
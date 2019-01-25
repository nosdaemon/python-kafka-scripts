from kafka import KafkaProducer


def producer():
    data = {'desc': 'testing', 'data': 'testing single node multi broker'}
    topic = 'test1'
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=[
            "10.211.55.48:9092", "l10.211.55.49:9092", "10.211.55.50:9092"
        ])

    producer.send(topic, data)

    producer.flush()
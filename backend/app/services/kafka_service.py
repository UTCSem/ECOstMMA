
# Placeholder for Kafka producer/consumer utilities.
# In production, use aiokafka for async producers/consumers.
from kafka import KafkaProducer, KafkaConsumer
import json, os

BOOTSTRAP = os.getenv('KAFKA_BOOTSTRAP', 'localhost:9092')

def get_producer():
    return KafkaProducer(bootstrap_servers=[BOOTSTRAP], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_telemetry(topic, payload):
    p = get_producer()
    p.send(topic, payload)
    p.flush()

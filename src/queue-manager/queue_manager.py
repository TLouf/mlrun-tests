import json
import os
import urllib.request

from kafka import KafkaProducer


# here default trigger (by hand i guess), stays on and consumes from kafka to grow the queue
def init_context(context):

    producer = KafkaProducer(
        bootstrap_servers=["my-cluster-kafka-brokers.kafka:9092"], #os.environ.get("KAFKA_BROKER")],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    )

    setattr(context, "producer", producer)



def handler(context, event):
    context.producer.send("channels", value={'ho': 'ha'})


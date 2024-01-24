import json
import os
import urllib.request

import fsspec
from kafka import KafkaProducer


def init_context(context):
    access_key = "minio"
    secret = "minio123"
    minio_host = "192.168.49.2"
    minio_port = "30080"
    minio_home = f"{minio_host}:{minio_port}"
    storage_options = {
        'endpoint_url': f'http://{minio_home}',
        'key': access_key,
        'secret': secret,
    }
    fs = fsspec.filesystem('s3', **storage_options)

    # producer = KafkaProducer(
    #     bootstrap_servers=[os.environ.get("KAFKA_BROKER")],
    #     value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    # )

    # setattr(context, "producer", producer)
    setattr(context, "fs", fs)



def handler(context, event):
    data = json.loads(event.body.decode("utf-8"))
    context.fs.open('channels/mdr', 'w').write(json.dumps(data))

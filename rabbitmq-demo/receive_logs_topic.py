import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

result = channel.queue_declare(queue="", exclusive=True)

queue_name = result.method.queue

binding_keys = sys.argv[1:]

for key in binding_keys:
    channel.queue_bind(exchange="topic_logs", queue=queue_name, routing_key=key)

print("Waiting...")


def callback(ch, method, properties, body):
    print(method.routing_key, body.decode())


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

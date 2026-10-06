import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

routing_key = sys.argv[1]

message = " ".join(sys.argv[2:])

channel.basic_publish(exchange="topic_logs", routing_key=routing_key, body=message)

print(f"Sent {routing_key}: {message}")

connection.close()

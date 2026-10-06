import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

# Create queue if it doesn't exist
channel.queue_declare(queue="hello", durable=True, arguments={"x-queue-type": "quorum"})

# Send message
channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")

print("Sent: Hello World!")

connection.close()

import pika
import random
import time


def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"recieved: {body}, will take {processing_time}")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("finished processing the message")


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

# this line of code is responsible for round robin execution
# channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue='letterbox', on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()

import pika
from pika.adapters.blocking_connection import BlockingChannel
import sys

def callback(ch: BlockingChannel, method, properties, body):
    print(method.routing_key)
    print(body)


def main():
    queue_name = sys.argv[1]
    binding_key = sys.argv[2]
    print(f'{queue_name} -> {binding_key}')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel: BlockingChannel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.exchange_declare('logs', exchange_type='topic')
    channel.queue_bind(queue=queue_name, exchange='logs', routing_key=binding_key)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    main()


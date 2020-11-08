import pika
from pika.adapters.blocking_connection import BlockingChannel


def callback(ch: BlockingChannel, method, properties, body):
    print(body)


def main():
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel: BlockingChannel = connection.channel()
        channel.queue_declare(queue="hello")
        channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()


if __name__ == "__main__":
    main()

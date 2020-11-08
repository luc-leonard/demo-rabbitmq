import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    for i in range(0, 100):
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=f'{i}')
    print(" [x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    main()


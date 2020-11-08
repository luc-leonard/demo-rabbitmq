import pika


def main():
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="hello")
        for i in range(0, 100):
            channel.basic_publish(exchange="", routing_key="hello", body=f"{i}".encode())
            print(i)


if __name__ == "__main__":
    main()

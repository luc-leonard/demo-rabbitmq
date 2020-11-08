import itertools
from random import choice
from typing import Optional

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pydantic import BaseModel

systems = ['mail', 'authentication', 'network']
levels = ['debug', 'info', 'warn', 'error']


def main():
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel: BlockingChannel = connection.channel()
        channel.exchange_declare('logs', exchange_type='topic')
        for i in itertools.count(start=0):
            # sleep(1.0)
            channel.basic_publish(exchange='logs',
                                  routing_key=f'{choice(systems)}.{choice(levels)}',
                                  body=f'{i}'.encode())


if __name__ == '__main__':
    main()

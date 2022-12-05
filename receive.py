#!/usr/bin/env python
from dotenv import load_dotenv
import pika, sys, os
load_dotenv()

def main():
    credentials = pika.PlainCredentials(os.environ["USER_NAME"], os.environ["PASSWORD"])
    parameters = pika.ConnectionParameters(os.environ["HOST"],5672,'/',credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
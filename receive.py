#!/usr/bin/env python
from dotenv import load_dotenv
import pika, sys, os
load_dotenv()

def main():
    credentials = pika.PlainCredentials(os.environ["USER_NAME"], os.environ["PASSWORD"])
    parameters = pika.ConnectionParameters(os.environ["HOST"],5672,'/',credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='print_messages')
    channel.queue_declare(queue='read_messages')
    channel.queue_declare(queue='barcode_read_messages')

    def callback(ch, method, properties, body):
        # print message with the channel name
        print(" [" + method.routing_key + "]: " +  body.decode("utf-8"))

    channel.basic_consume(queue='print_messages', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='read_messages', on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue='barcode_read_messages', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages in the print_messages, read_messages and barcode_read_messages queues. To exit press CTRL+C')
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
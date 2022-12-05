#!/usr/bin/env python
import pika, os
from dotenv import load_dotenv
import payloads

load_dotenv()
credentials = pika.PlainCredentials(os.environ["USER_NAME"], os.environ["PASSWORD"])
parameters = pika.ConnectionParameters(os.environ["HOST"],5672,'/',credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='print_messages')

channel.basic_publish(exchange='', routing_key='print_messages', body=payloads.printMessage)
connection.close()
#!/usr/bin/env python
import pika, os
from dotenv import load_dotenv
import payloads

load_dotenv()
credentials = pika.PlainCredentials(os.environ["USER_NAME"], os.environ["PASSWORD"])
parameters = pika.ConnectionParameters(os.environ["HOST"],5672,'/',credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='read_messages')

channel.basic_publish(exchange='', routing_key='read_messages', body=payloads.readMessageEntry)
channel.basic_publish(exchange='', routing_key='read_messages', body=payloads.readMessageUpdate)
channel.basic_publish(exchange='', routing_key='read_messages', body=payloads.readMessageExit)

connection.close()
**Rabbit MQ queue for the perfectmoose production line**

This repo houses information on the setup of the rabbitmq queue for the PM production line.

**Docker**

docker run -d --name rabbitmq -p 5672:5672 -e RABBITMQ_DEFAULT_USER=xxx -e RABBITMQ_DEFAULT_PASS=xxxxxxxxx rabbitmq

**AWS**

runs on a ec2 instance


**Use Repo**

In two seperate terminals run.


Consumer:
```bash
python3 receive.py
```

Producers:
```bash
python3 send_print_message.py
python3 send_barcode_read_message.py
python3 send_read_messages.py
```

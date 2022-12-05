## Rabbit MQ queue for the perfectmoose production line

This repo houses information on the setup of the rabbitmq queue for the PM production line.

# Docker command
docker run -d --name rabbitmq -p 5672:5672 -e RABBITMQ_DEFAULT_USER= -e RABBITMQ_DEFAULT_PASS=xxxxxxxxx rabbitmq

# Running on AWS
runs on a ec2 instance

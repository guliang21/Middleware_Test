import pika

host = "127.0.0.1"
username = "guest"
password = "guest"

queue_name = "hello"
exchange_name = "exchange"
routing_key = "hello"

with pika.BlockingConnection(pika.ConnectionParameters(host)) as connection:
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=routing_key, body='你好')

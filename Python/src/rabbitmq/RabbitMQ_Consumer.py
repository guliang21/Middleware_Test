import pika

host = "127.0.0.1"
queue_name = "hello"

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
channel = connection.channel()

channel.queue_declare(queue=queue_name)


def callback(ch, method, properties, body):
    print("Received： %r" % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

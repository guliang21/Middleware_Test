using RabbitMQ.Client;
using System;
using System.Text;

namespace RabbitMQ_Producer
{
    class Program
    {
        static void Main(string[] args)
        {
            string host = "localhost";
            string queue_name = "hello";
            string routing_key = "hello";

            ConnectionFactory factory = new ConnectionFactory() { HostName = host };
            using (var connection = factory.CreateConnection())
            {
                using (var channel = connection.CreateModel())
                {
                    channel.QueueDeclare(queue: queue_name, durable: false, exclusive: false, autoDelete: false, arguments: null);

                    string message = "Hello World!";
                    var body = Encoding.UTF8.GetBytes(message);

                    channel.BasicPublish(exchange: "", routingKey: routing_key, basicProperties: null, body: body);
                    Console.WriteLine("Sent：{0}", message);
                }
            }

            Console.WriteLine("Press [enter] to exit.");
            Console.ReadLine();
        }
    }
}

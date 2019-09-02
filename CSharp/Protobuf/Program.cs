using Google.Protobuf;
using System;
using Test;

namespace Protobuf
{
    class Program
    {
        static void Main(string[] args)
        {
            Person person = new Person();
            person.Name = "张三";
            person.Age = 20;
            person.Marriage = true;

            // 序列化
            byte[] buffer = person.ToByteArray();

            foreach (byte b in buffer)
            {
                Console.Write(b.ToString("X2") + " ");
            }
            Console.WriteLine();

            // 反序列化
            Person p = Person.Parser.ParseFrom(buffer);

            Console.WriteLine(string.Format("Name: {0}, Age: {1}, Marriage: {2}", p.Name, p.Age, p.Marriage));

            Console.Read();
        }
    }
}

import Person_pb2

person = Person_pb2.Person()
person.Name = '张三'
person.Age = 20
person.Marriage = True

# 序列化
b = person.SerializeToString()
print(b, len(b))

# 反序列化
p = Person_pb2.Person()
p.ParseFromString(b)
print(f'Name: {p.Name}; Age: {p.Age}; Marriage: {p.Marriage}')

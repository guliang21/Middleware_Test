[TOC]

## 一、简介
Protobuf（Protocol Buffers），是 google 开发的一种跨语言、跨平台的可扩展机制，用于序列化结构化数据

与 XML 和 JSON 格式相比，protobuf 更小、更快、更便捷。protobuf 目前支持 C++、Java、Python、Objective-C，如果使用 proto3，还支持 C#、Ruby、Go、PHP、JavaScript 等语言。

官网地址：[https://developers.google.cn/protocol-buffers/](https://developers.google.cn/protocol-buffers/)

GitHub 地址：[https://github.com/protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf)

**优点：**
- 性能好
- 跨语言

**缺点：**
- 二进制格式可读性差：为了提高性能，protobuf 采用了二进制格式进行编码，这直接导致了可读性差。
- 缺乏自描述：XML 是自描述的，而 protobuf 不是，不配合定义的结构体是看不出来什么作用的。

## Windows 下安装
下载地址：[https://github.com/protocolbuffers/protobuf/releases](https://github.com/protocolbuffers/protobuf/releases)

下载 protoc-3.9.1-win64.zip，这个是编译后的压缩包，相当于绿色版，解压后，将其下的 bin 目录添加到环境变量就可以了，省去了安装的麻烦。

![](https://upload-images.jianshu.io/upload_images/14733701-6bf0f204cfe9dca2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然后打开命令提示符，输入命令：
```
protoc --version
```
成功显示版本号，则表示安装成功。如下图：

![protobuf 安装（1）.png](https://upload-images.jianshu.io/upload_images/14733701-f38d32d1f6f9c53c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 二、使用

### 1、编译
使用 protobuf 首先需要定义 .proto 文件，先来看一个简单的例子。

定义 Person.proto 文件，内容如下：
```
syntax = "proto3";
package Test;

message Person {
  string Name = 1;
  int32 Age = 2;
  bool Marriage = 3;
}
```
- `syntax = "proto3";` 指定正在使用 proto3 语法，否则 protobuf 将默认使用的是 proto2。
- `package Test;` 指定命名空间。
- `message` 是关键字，
- 

**protoc 是 protobuf 自带的编译器**，可以将 .proto 文件编译成 java、python、go、C# 等多种语言的代码，直接引用。

```
protoc -I=E:\GL\Test2017 --python_out=E:\GL\Test2017 Person.proto
```
- -I 表示源文件（.proto 文件）所在文件夹路径。
- --python_out 表示目标语言为 python，且指定生成的 .py 文件存放目录。相应的，C# 为 csharp_out，
- Person.proto 为源文件文件名，如果有多个，空格隔开。


### 2、Python
安装 `protobuf`。

Person.proto，编译后生成文件：`Person_pb2.py`，添加至项目中，序列化和反序列化示例如下：

```
import Person_pb2

person = Person_pb2.Person()
person.Name = '张三'
person.Age = 20
person.Marriage = True

# 序列化
b = person.SerializeToString()
print(b)

# 反序列化
p = Person_pb2.Person()
p.ParseFromString(b)
print(f'Name: {p.Name}; Age: {p.Age}; Marriage: {p.Marriage}')
```

**输出：**
```
b'\n\x06\xe5\xbc\xa0\xe4\xb8\x89\x10\x14\x18\x01'
Name: 张三; Age: 20; Marriage: True
```

注意，不能这样写，这是错误的：
```
p = Person_pb2.Person().ParseFromString(b)
```

### 3、C#

C# 下的 Protobuf 有 3 个版本：
- Google.ProtoBuf：Google官方版本，[https://github.com/google/protobuf/tree/master/csharp](https://github.com/google/protobuf/tree/master/csharp)
- protobuf-net：.net 社区版本，由 .net 社区爱好者开发，[https://github.com/mgravell/protobuf-net](https://github.com/mgravell/protobuf-net)
- Google.ProtocolBuffers：据说是由谷歌的 .net 员工在官方版本还未出来的时候开发的，[https://github.com/jskeet/protobuf-csharp-port](https://github.com/jskeet/protobuf-csharp-port)

这里我们介绍谷歌官方版本。

在 VS 中，通过 NuGet 安装 'google.protobuf' 包。


```
using Google.Protobuf;

Person person = new Person();
person.Name = "张三";
person.Age = 20;
person.Marriage = true;

// 序列化
byte[] buffer = person.ToByteArray();

// 反序列化
Person p = Person.Parser.ParseFrom(buffer);
```

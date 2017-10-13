<h1>Windows C++ SDK 集成指南</h1>


## 概述

JMessage Windows SDK 使用 C++ 语言开发, 基于 Web SDK 协议，提供易用的 C++ 接口，编译器支持 VS2017(vc141)，兼容系统 Windows 7、Windows 8/8.1、Windows 10。


### 功能

- 实时消息，离线消息，单聊，群聊
- 消息类型支持文本，语音，图片，文件，位置，自定义消息等
- 异步接口，以[ cpprestsdk ](https://github.com/Microsoft/cpprestsdk)为基础， 请参考[ Programming with Tasks ](https://github.com/Microsoft/cpprestsdk/wiki/Programming-with-Tasks)
- 功能基于Web SDK，开发者可参考 [Web SDK 开发指南](https://docs.jiguang.cn/jmessage/client/im_sdk_js_v2/) 



### 鉴权

SDK在初始化的时候，需要提供相关参数

* appkey : 开发者在极光平台注册的 IM 应用 appkey
* randomStr : 20-36 长度的随机字符串，作为签名 salt 使用
* timestamp : 当前时间戳，用于防止重放攻击，精确到毫秒
* signature : 签名，10 分钟后失效

签名生成算法如下:

```
signature = md5("appkey={appkey}&timestamp={timestamp}&random_str={randomStr}&key={secret}")
```

其中 secret 为开发者在极光平台注册的 IM 应用 masterSecret

不建议在客户端计算签名，有泄漏masterSecret的风险

```
签名生成示例(Qt):
auto timestamp = QDateTime::currentDateTime().toMSecsSinceEpoch();
auto str = QString("appkey=4f7aef34fb361292c566a1cc&timestamp=%1&random_str=022cd9fd995849b58b3ef0e943421ed9&key=054d6103823a726fc12d0422").arg(time);

auto signature = QCryptographicHash::hash(str.toUtf8(), QCryptographicHash::Md5).toHex().toStdString();
```



## 快速开始

### 依赖

- 编译器:VS2017

- 第三方库: <https://github.com/Microsoft/cpprestsdk>


### 简单示例

1.[下载 SDK](https://docs.jiguang.cn/jmessage/resources/) ，SDK 压缩包内包含:

 -  lib 

     - SDK 导入库

 -  include 

     - SDK 头文件

 -  bin

     -  SDK 运行库 

 -  example

     -  SDK 使用简单示例工程

2.在 Visual Studio 中使用

 - 将 SDK include 目录添加到 VC++ 头文件包含路径
 - 将 SDK lib 目录添加到 VC++ 库目录

3.包括头文件，链接 SDK 库

```
#include <Jmcpp/Client.h>
#pragma comment(lib,"Jmcpp.lib")
```

4.创建 Client

 - Client 类提供了 SDK 的主要功能，所以先创建一个 Client 对象
 - Configuration 参数配置 Client，包括自定义服务器地址，SDK 缓存路径，日志级别等，一般默认即可

```
Jmcpp::Configuration cfg; // 默认配置
Jmcpp::Client client(cfg); //创建Client对象
```

5.在登录前，SDK 应该设置相应的监听回调，处理消息接收与事件

- SDK 提供监听消息接收的回调接口，消息分为实时消息(用户在线时收到的消息)与离线消息

```
// 监听实时消息
client.onMessageReceive([](Jmcpp::MessagePtr msg)
{
   	auto content = msg->content;
   	if(std::holds_alternative<Jmcpp::TextContent>(content))
   	{
   		auto&& imageCont = std::get<Jmcpp::TextContent>(content);
   		std::cout
   				<< msg->sender.username << " send to "
   				<< msg->receiver.username << " : "
   				<< imageCont.text
   				<< std::endl;
   	}
   	else if(std::holds_alternative<Jmcpp::ImageContent>(content))
   	{
   		///...
   	}
   	else
   	{
   		//...
   	}
});
// 监听同步消息
client.onMessageSync([](std::vector<Jmcpp::MessagePtr> msgs)
{
		
});
```

- SDK 提供监听事件的回调接口，同样事件分为实时事件与同步事件，

```
  // 监听事件
client.onEventReceive([](Jmcpp::Event ev)
{
   	if(std::holds_alternative<Jmcpp::ForceLogoutEvent>(ev))
   	{
   		auto&& e = std::get<Jmcpp::ForceLogoutEvent>(ev);
   		//...
   	}
   	else if(std::holds_alternative<Jmcpp::MessageRetractedEvent>(ev))
   	{
   		auto&& e = std::get<Jmcpp::MessageRetractedEvent>(ev);
   	}
   	else
   	{
   		//...
   	}
});
// 监听事件同步
client.onEventSync([](std::vector<Jmcpp::Event> ev)
{
		
});
```

6.登录，鉴权，发送消息

- SDK 登录注册需要开发者鉴权，其中签名开发者应该通过某个服务或其它方式得到，不建议在客户端通过 masterSecret 计算，这里只是演示用法

```
Jmcpp::Authorization auth;
auth.appKey = "25b693b31d2c2ad5f072ef0c";
auth.randomStr = "022cd9fd995849b58b3ef0e943421ed9";
auth.timestamp = "1467967210887";// 使用时应该获取当前事件戳,这里只是演示
auth.signature = "D97C2DDA3E46E5E6D482E9E8EE84AF93";//使用时应该动态计算得到,这里只是演示

//登录
client.login("yourUsername", "yourPassword",auth).get();

// 创建一条文本消息内容
auto content = client.createTextContent("hello!").get();
// 创建消息,包含要发送的用户或群
auto msg = client.buildMessage(Jmcpp::UserId("targetUsername"), content);
// 发送消息
client.sendMessage(msg).get();
```

7.退出登录，销毁 Client

```
client.logout();
```

8.错误处理

```
try
{
    client.login("yourUsername", "yourPassword",auth).get();
   	auto content = client.createTextContent("hello!").get();
   	auto msg = client.buildMessage(Jmcpp::UserId("targetUsername"), content);
   	client.sendMessage(msg).get();
   	client.logout();
}
catch(Jmcpp::ServerException& e)
{
   // API 服务器调用返回的错误
   std::cout << e.what() << std::endl;
}
catch(std::system_error& e)
{
   // API 调用产生的其它错误
   std::cout << e.what() << std::endl;
}
```

完整示例请查看 SDK 压缩包内的 example



## 参考文档

错误码定义：[IM Web SDK 错误码列表](https://docs.jiguang.cn/jmessage/client/im_errorcode_js/)

完整 API 文档：[Windows C++ SDK API]()










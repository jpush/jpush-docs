<h1>Windows C++ SDK 集成指南</h1>


## 概述

JMessage Windows SDK 使用 C++ 语言开发， 基于 Web SDK 协议，提供易用的 C++ 接口，编译器支持 VS2017(vc141)，兼容系统 Windows 7、Windows 8/8.1、Windows 10。


### 功能

- 实时消息，离线消息，单聊，群聊，聊天室
- 消息类型支持文本，语音，图片，文件，位置，自定义消息等
- 基于[cpprestsdk](https://github.com/Microsoft/cpprestsdk/wiki/Programming-with-Tasks)的task/then异步接口[(更多关于task)](https://docs.microsoft.com/zh-cn/cpp/parallel/concrt/reference/task-class?f1url=https%3A%2F%2Fmsdn.microsoft.com%2Fquery%2Fdev15.query%3FappId%3DDev15IDEF1%26l%3DZH-CN%26k%3Dk(PPLTASKS%2FConcurrency%3A%3Atask)%3Bk(Concurrency%3A%3Atask)%3Bk(task)%3Bk(DevLang-C%2B%2B)%3Bk(TargetOS-Windows)%26rd%3Dtrue) ，上层可以使用回调或co_await方式调用异步接口
- 功能基于WEB SDK，开发者可参考 [Web SDK](https://docs.jiguang.cn/jmessage/client/im_sdk_js_v2/) 



### 鉴权

SDK在初始化的时候，需要提供相关参数

* appkey : 开发者在极光平台注册的 IM 应用 appkey
* randomStr : 20-36 长度的随机字符串， 作为签名 salt 使用
* timestamp : 当前时间戳，用于防止重放攻击，精确到毫秒
* signature : 签名，10 分钟后失效

签名生成算法如下:

```
signature = md5("appkey={appkey}&timestamp={timestamp}&random_str={randomStr}&key={secret}")
```

其中 secret 为开发者在极光平台注册的 IM 应用 masterSecret

不建议在客户端计算签名，有泄漏masterSecret的风险

```
//签名生成示例(Qt):
auto timestamp = QDateTime::currentDateTime().toMSecsSinceEpoch();
auto str = QString("appkey=007a1134fb361233c566a1cc&timestamp=%1&random_str=022cd9fd995849b58b3ef0e943421ed9&key=122d61038232226fc12d0422").arg(time);

auto signature = QCryptographicHash::hash(str.toUtf8()， QCryptographicHash::Md5).toHex().toStdString();
```



## 快速开始

### 依赖

- 编译器:VS2017
- 第三方库: <https://github.com/Microsoft/cpprestsdk>


### 简单示例

1.使用SDK包，有两种方式:

   1. 使用NuGet程序包， 在Visual Studio 中右键单击你的项目， 选择`管理Nuget程序包`

      选择浏览页，搜索`jmessage-cpp` ， 然后安装需要的版本SDK即可

   2. 手动下载[SDK](https://docs.jiguang.cn/jmessage/resources/) ，解压

      * 将SDK include目录添加到`工程属性页-> C/C++ -> 常规->附加包含目录`
      * 将SDK lib 目录添加到`工程属性页-> 链接器 -> 常规->附加库目录`
      * 链接SDK库， 在`工程属性页->链接器-> 输入->附加依赖项` 中， Release配置加入Jmcpp.lib， Debug配置加入Jmcppd.lib


2.创建Client

   * Client类提供了SDK的主要功能，所以先创建一个Client对象
   * Configuration 参数配置Client， 包括SDK缓存路径， 日志级别等， 一般默认即可
   ```
    #include <Jmcpp/Client.h> // 包含头文件
    Jmcpp::Configuration cfg; // 默认配置
    Jmcpp::Client client(cfg); //创建Client对象
   ```


3.在登录前， SDK应该设置相应的监听回调，处理消息接收与事件

  * SDK提供监听消息接收的回调接口，消息分为实时消息(用户在线时收到的消息)与离线消息
   ```
	// 监听消息
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

		}
		else
		{
		}
	});

	// 监听同步消息
	client.onMessageSync([](std::vector<Jmcpp::MessagePtr> msgs)
	{
	});
   ```

  * SDK提供监听事件的回调接口，同样事件分为实时事件与同步事件
   ```
	// 监听实时事件
	client.onEventReceive([](Jmcpp::Event ev)
	{
		if(std::holds_alternative<Jmcpp::ForceLogoutEvent>(ev))
		{
			auto&& e = std::get<Jmcpp::ForceLogoutEvent>(ev);

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
		//...
	});
   ```


4.登录，鉴权，发送消息

  * SDK登录注册需要开发者鉴权，其中签名开发者应该通过某个服务或其它方式得到，不建议在客户端通过masterSecret计算，这里只是演示用法
   ```
    Jmcpp::Authorization auth;
    auth.appKey = "25b693b31d2c2ad5f072ef0c";
    auth.randomStr = "022cd9fd995849b58b3ef0e943421ed9";
    auth.timestamp = "1467967210887";// 使用时应该获取当前事件戳，这里只是演示
    auth.signature = "D97C2DDA3E46E5E6D482E9E8EE84AF93";//使用时应该动态计算得到，这里只是演示

    //登录
    client.login("yourUsername", "yourPassword",auth).get();

    // 创建一条文本消息内容
    auto content = client.createTextContent("hello!").get();
    // 创建消息，包含要发送的用户或群
    auto msg = client.buildMessage(Jmcpp::UserId("targetUsername"), content);
    // 发送消息
    client.sendMessage(msg).get();
   ```


5.退出登录，销毁Client

   ```
     client.logout();
   ```

6.错误处理

   ```
try{
		client.login("yourUsername", "yourPassword", getAuthorization()).get();
		auto content = client.createTextContent("hello!").get();
		auto msg = client.buildMessage(Jmcpp::UserId("test"), content);
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

   

完整示例请查看SDK压缩包内的example


## 参考文档

错误码定义：[IM web SDK 错误码列表](https://docs.jiguang.cn/jmessage/client/im_errorcode_js/)

完整 API 文档：[Windows C++ SDK API](https://docs.jiguang.cn/jmessage/client/im_win_api_docs/)










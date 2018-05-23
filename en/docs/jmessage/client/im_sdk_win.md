<h1>JMessage PC SDK Development Guide</h1>

## Overview

JMessage PC SDK develops with C++ languageon the basis of Web SDK protocol, and provides an easy-to-use C++ interface.

The compiler supports VS2017 (msvc141) and is compatible with Windows 7, Windows 8/8.1, and Windows 10.

MacOS supports Clang5+, MacOS 10.13 (x86_64)

### Function

+ Real-time messages, offline messages, single chats, group chats, chat rooms
+ Message types support text, voice, pictures, files, location, custom messages, etc.
+ task/then asynchronous interface based on [cpprestsdk](https://github.com/Microsoft/cpprestsdk/wiki/Programming-with-Tasks) ([more about the task](https://docs.microsoft.com/zh-cn/cpp/parallel/concrt/reference/task-class)). The upper layer can invoke the asynchronous interface by using the callback or co_await mode.
+ Features based on WEB SDK. Developers can refer to [Web SDK](https://docs.jiguang.cn/jmessage/client/im_sdk_js_v2/).

## Authentication

Need to provide relevant parameters When the SDK is initializing.

+ appkey : an IM application appkey registered by the developer on Jiguang platform
+ randomStr : a random string of 20-36 lengths, used as a signature salt
+ timestamp : current timestamp, used to prevent replay attacks. Accurate to millisecond.
+ signature : signature, which is expired after 10 minutes

The generation algorithm of signature is as follows

```
signature = md5("appkey={appkey}&timestamp={timestamp}&random_str={randomStr}&key={secret}")
```

Secret is an IM application masterSecret registered by the developer on Jiguang platforms

It is not recommended to calculate the signature on the client, since there is a risk of leaking masterSecret

```
//签名生成示例(Qt):
auto timestamp = QDateTime::currentDateTime().toMSecsSinceEpoch();
auto str = QString("appkey=007a1134fb361233c566a1cc&timestamp=%1&random_str=022cd9fd995849b58b3ef0e943421ed9&key=122d61038232226fc12d0422").arg(time);

auto signature = QCryptographicHash::hash(str.toUtf8()， QCryptographicHash::Md5).toHex().toStdString();
```

## Quick Start

### Dependence

+ Compiler: VS2017
+ Third-party library: <https://github.com/Microsoft/cpprestsdk>

### Simple Examples

1. There are two ways to use the SDK package:

    1. Using the NuGet package, right-click your project in Visual Studio and select `Manage Nuget Packages`

        Select the browse page, search for jmessage-cpp, and install the required SDK version

    2. Manually download the [SDK](https://docs.jiguang.cn/jmessage/resources/) and unzip it

        + Add SDK include directory to Project property page -> C/C++ -> General -> Additional include directory
        + Add the SDK lib directory to thc Project property page -> Linker -> General -> Additional include directory
        + Link the SDK library and add Jmcpp.libin the Release configuration and Jmcppd.lib in the Debug configuration in  Project property page -> Linker -> Input -> Additional dependencies

2. Create Client

+ Client class provides the main function of the SDK, so first create a Client object
+ The Configuration parameter configures the Client, including the SDK cache path, log level, etc. Generally choose the default.

```
#include <Jmcpp/Client.h> // 包含头文件
Jmcpp::Configuration cfg; // 默认配置
Jmcpp::Client client(cfg); //创建Client对象
```

3. Before logging in, the SDK should set the corresponding listener callback to handle message reception events.

+ The SDK provides a callback interface for message listening. The messages are divided into real-time messages (messages received when users are online) and offline messages.

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

+ The SDK provides a callback interface for event listening. The events are divided into real-time events and synchronization events.

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

4. Login, Authentication, and Send Messages

+ Login and registration of SDK requires developer’s authentication, where the signature should be obtained by the developer through a service or other means. It is not recommended to use the masterSecret calculation on the client. Here just a demonstration usage.

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

5. Log out and Destroy Client

```
client.logout();
```

6. Error Handling

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

Please see the example in the SDK archive for complete example.

## Reference Documents

Error Code Definition: [Error Code List of IM Web SDK](https://docs.jiguang.cn/jmessage/client/im_errorcode_js/)

Full API Documentation: [Windows C++ SDK API](https://docs.jiguang.cn/jmessage/client/im_win_api_docs/)


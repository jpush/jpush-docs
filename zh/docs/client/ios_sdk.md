# iOS SDK

## JPush iOS 的意义

由于 iOS 平台的特殊性不允许在后台常驻工作，推送采用统一的下发通道：APNs（Apple Push Notification Service）。

JPush iOS 推送也是基于对 APNs 的封装。但是JPush iOS 推送比起开发者直接对接 APNS 有如下几个方面的优势。

+ 减少开发及维护成本：
	+ 应用开发者不需要去开发维护自己的推送服务器与 APNs 对接。
	+ 集成了JPush iOS SDK后可以通过 JPush 的 web portal 直接推送通知。也可以调用JPush的 Http 协议 API 来完成。
+ 统一推送服务：
	+ 极光推送同时推送 Android 与 iOS 两个平台，支持统一的 API与推送界面，以及别名与标签用户绑定方法。
+ 更方便的推送：
	+ JPush iOS 推送同样支持标签，广播和别名的推送方式，开发者只需要一次推送，JPush服务器会根据匹配条件逐条发送到 APNs 服务器，提高了推送性能。
+ 应用内推送：
	+ 嵌入了 JPush iOS SDK 的应用，当应用启动后，可以在应用内从 JPush 的服务器上直接获取推送消息以及获取离线消息，极大的保证了推送的可靠性。

## APNs 通知

APNs 通知：是指开发者向应用推送通知后由 APNs 服务器下发的到系统，由 iOS 系统提供展现方式。用户可以通过系统的 “设置” >> “通知” 进行设置。

[获取 APNs 推送内容](../ios_api)

## 应用内消息

应用内消息：为了保证推送的可靠性，JPush SDK 提供了应用内消息，当应用打开后可以直接从JPush server 获取推送消息。此消息不经过 APNS 服务器。 

[获取应用内推送信息](../ios_api)

## APNs消息与应用内消息对比

如果只需要发送通知，则可以忽略应用内消息的处理。对于两种消息的代码处理可以参考API部分的描述。

||APNS|应用内消息|
|-|-|-|
|推送原则|每次推送都会发给APNS 服务器发送经由APNS服务器下发到手机。|每次推送都会尝试发送，如果用户在线则立即发送。|
|离线消息	|离线消息由APNS服务器缓存按照apple的逻辑处理。|用户不在线JPush server 会保存离线消息。离线消息保留5条。|
|是否有APNS生产和开发环境区别。|是，只有证书和应用环境匹配才可以收到。|否，应用内消息与iOS 环境这是状态无关。|
|接收方式|应用退出，后台或者是打开是都会收到APNS|需要应用打并与jpush 建立连接，然后接收离线消息和在线消息。|
|展示效果|如果应用后台或退出，会以系统通知方式展现。<p>如果应用处于打开状态，不展示。|默认不展示。|
|处理函数|didReceiveRemoteNotification|networkDidReceiveMessage|

## iOS实现与架构图

JPush APNs 的实现可以参考极光博客的一篇文章：[http://blog.jpush.cn/apns/](http://blog.jpush.cn/apns/)

## 开发者贡献：集成到其他平台

+ [客户端 SDK集成插件](../client_plugins)



# iOS SDK 概述

+ [iOS 常见问题](ios_faq)
+ [iOS 客户端 SDK 下载](../../resources/#ios-sdk)

## JPush iOS

![jpush_ios](../image/jpush_ios.png)

从上图可以看出，JPush iOS Push 包括 2 个部分，APNs 推送（代理），与 JPush 应用内消息。

红色部分是 APNs 推送，JPush 代理开发者的应用（需要基于开发者提供的应用证书），向苹果 APNs 服务器推送。由 APNs Server 推送到 iOS 设备上。

蓝色部分是 JPush 应用内推送部分，即 App 启动时，内嵌的 JPush SDK 会开启长连接到 JPush Server，从而 JPush Server 可以推送消息到 App 里。

### APNs 通知

APNs 通知：是指通过向 Apple APNs 服务器发送通知，到达 iOS 设备，由 iOS 系统提供展现的推送。用户可以通过 IOS 系统的 “设置” >> “通知” 进行设置，开启或者关闭某一个 App 的推送能力。

JPush iOS SDK 不负责 APNs 通知的展现，只是向 JPush 服务器端上传 Device Token 信息，JPush 服务器端代理开发者向 Apple APNs 推送通知。

[获取 APNs 推送内容](ios_api/#apns)

### 应用内消息

应用内消息：JPush iOS SDK 提供的应用内消息功能，在 App 在前台时能够收到推送下来的消息。App 可使用此功能来做消息下发动作。

此消息不经过 APNs 服务器，完全由 JPush 提供功能支持。

[获取应用内消息推送内容](ios_api/#_24)

### APNs通知与应用内消息对比

如果只需要发送通知，则可以忽略应用内消息的处理。对于两种消息的代码处理可以参考API 部分的描述。

JPush API v3 支持同时一次调用同时推送 APNs 通知与 JPush 应用内消息。这在某些应用场景里是有意义的。


<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th ></th>
      <th >APNS</th>
      <th >应用内消息</th>
    </tr>
    <tr >
      <td>推送原则</td>
      <td>由JPush服务器发送至APNS服务器，再下发到手机。</td>
      <td>由JPush直接下发，每次推送都会尝试发送，如果用户在线则立即收到。否则保存为离线。</td>
    </tr>
    <tr >
      <td>离线消息</td>
      <td>离线消息由APNS服务器缓存按照Apple的逻辑处理。</td>
      <td>用户不在线JPush server 会保存离线消息,时长默认保留一天。离线消息保留5条。</td>
    </tr>
    <tr >
      <td>推送与证书环境</td>
      <td>应用证书和推送指定的iOS环境匹配才可以收到。</td>
      <td>自定义消息与APNS证书环境无关。</td>
    </tr>
    <tr >
      <td>接收方式</td>
      <td>应用退出，后台以及打开状态都能收到APNS</td>
      <td>需要应用打开，与JPush 建立连接才能收到。</td>
    </tr>
    <tr >
      <td>展示效果</td>
      <td>如果应用后台或退出，会有系统的APNS提醒。<p>如果应用处于打开状态，则不展示。</td>
      <td>非APNS，默认不展示。可通过获取接口自行编码处理。</td>
    </tr>
    <tr >
      <td>处理函数</td>
      <td>Apple提供的接口：<a href="../ios_api/#apns">didReceiveRemoteNotification</a></td>
      <td>JPush提供的接口：<a href="../ios_api/#_19">networkDidReceiveMessage</a></td>
    </tr>
  </table>
</div>




## iOS SDK 集成

请参考以下文档与教程，来集成 IOS SDK。

+ [IOS 集成指南](ios_guide_new)




## iOS SDK 说明

### iOS 版本支持

+ 支持的iOS版本为5.0及以上版本。
+ 支持iOS版本为10.0以上的版本时需知。
	+ Notification Service Extension证书配置时需要注意BundleID不能与Main Target一致，证书需要单独额外配置。
	+ 请将Notification Service Extension中的Deployment Target设置为10.0。
	+ 在XCode7或者更低的版本中删除Notification Service Extension所对应的Target。
	+ 在XCode7或者更低的版本中请将引入的'UserNotifications.framework'删除。


### 组成

+ 头文件 APService.h
+ 静态库文件 libPushSDK.a

### 注意事项
+ [请参考iOS常见问题](ios_faq)

## JPush APNs 通知的意义

iOS 平台上推送通知，只有 APNs 这个官方的通道，是可以随时送达的。一般开发者都是自己部署应用服务器向 APNs Server 推送。

JPush iOS 推送相比直接向 APNs 推送有什么好处呢？

+ 减少开发及维护成本：
	+ 应用开发者不需要去开发维护自己的推送服务器与 APNs 对接。
	+ 集成了 JPush iOS SDK 后不必自己维护更新 device token。
	+ 通过 JPush 的 Web Portal 直接推送，也可以调用JPush的 HTTP 协议 API 来完成，开发工作量大大减少。
+ 减少运营成本：
	+ 极光推送支持一次推送，同时向 Android, iOS, WinPhone 三个平台。支持统一的 API 与推送界面。
	+ 极光推送提供标签、别名绑定机制，以及提供了非常细分的用户分群方式，运营起来非常简单、直观。
+ 提供应用内推送：
	+ 除了使得 APNs 推送更简单，也另外提供应用内消息推送。这在类似于聊天的场景里很有必要。

## JPush APNs 实现

JPush APNs 的实现可以参考极光博客的一篇文章：[http://blog.jiguang.cn/apns/](http://blog.jiguang.cn/apns/)



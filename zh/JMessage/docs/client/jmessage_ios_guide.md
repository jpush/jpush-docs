# JMessage iOS SDK 集成指南

<style>
img[alt=jmessage_ios] { width: 800px; }
</style>

### 文档说明

本文是极光IM iOS SDK 的集成指南文档。

在你看到本文档时，可能最新的 SDK版本与本文已经不是很适配，建议关注在线文档：

+ [极光文档](http://docs.jpush.io/)网站上，有极光推送相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。
+ [极光问答](https://community.jiguang.cn/latest)网站：大家除了文档之外，还有问题与疑问，会到这里来提问题，以及时地得到解答。
+ 如果您看到本文档时，但还未下载 JMessage SDK，请访问[SDK下载页面](../../resources_jmessage)下载。

### 功能说明

极光IM（JMessage）是一个端到端的即时通讯（IM）云服务，使得多个集成 SDK 的客户端之间可以互发即时消息，让开发者可以轻松地在 App 里集成 IM 的功能，为 App 加上社交功能，从而有效地提升 App 活跃度。极光IM 客户端支持 Android, iOS, Web 三个平台。

本 iOS SDK 方便开发者基于 JMessage 来快捷地为 iOS App 增加 IM 功能。支持的版本≥iOS7。

#### 主要功能

+ 保证消息及时下发，并且不丢失消息；
+ 单聊，群聊；
+ 消息类型：文本、语音、图片；
+ 用户未在线时保存离线消息；
+ 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

#### 主要特点

+ 服务器大容量、稳定；
+ SDK 提供丰富的接口；
+ 同时支持 APNs 通知；

#### 系统要求与开发环境

JMessage iOS SDK 支持 iOS 7 以上系统版本。

#### jmessage-sdk-ios.zip 集成压缩包

* lib文件夹：包含一个文件，JMessage.framework；
* Guideline.md：本开发指南；
* demo文件夹：示例。


#### 包括 JPush SDK

如果你的 App 之前未集成过 JPush，请忽略本节，参考下节的 “SDK集成步骤”。

JMessage SDK 包含 JPush SDK 的全部功能。

如果您原来代码里集成过 JPush iOS SDK，则可大部分保持不变。变更部分如下：

+ 集成到项目工程里的 JPush SDK 的文件删除掉，包括头文件：APService.h，库文件 libPushSDK.a。JMessage.framework 里已经包含 Push 部分，不删除掉会冲突。
+ 配置文件 PushConfig.plist 文件删除掉。不再使用配置文件，而是用代码调用提供基本参数。
+ 原来调用 APService 里 setupWithOption 做初始化，现在要换成 JMessage 里相应的方法。

JMessage 新增的依赖、配置、初始化方面，请继续参考下节。

### SDK集成步骤

#### 1、在极光 Web控制台上创建应用

* 登录[极光Web控制台](https://www.jpush.cn/common/apps)，创建应用，上传 APNs 证书。如果对 Apple APNs 证书不太了解，请参考[iOS 证书设置指南](../client/ios_tutorials/#ios_1)。

![jmessage_ios][0]

* 创建成功后自动生成 AppKey 用以标识该应用。这个后续要用到。

![jmessage_ios][1]

#### 2、导入 SDK 到应用程序项目里

* 把 JMessage.framework 文件加入到项目里。

#### 3、必要的框架

* CoreFoundation.framework
* CoreTelephony.framework
* CoreAudioFramework
* CoreGraphics.framework
* Foundation.framework
* SystemConfiguration.framework
* CFNetwork.framework
* UIKit.framework
* Security.framework
* AudioToolboxFramework
* MobileCoreServices.framework
* libz.dylib
* libsqlite3.0.dylib

#### 4、Build Settings

* 在项目配置，Build Settings，Other Linker Flags 里增加如下 2 项：

```
    -ObjC
    -all_load
```

* 设置 Search Paths 下的 User Header Search Paths 和 Library Search Paths，比如SDK文件夹（默认为lib）与工程文件在同一级目录下，则都设置为"$(SRCROOT)/[文件夹名称]"即可。

#### 6、添加代码

##### API 与 Model

JMessage.framework 里的 Headers 目录下，是 SDK 对外可用的所有头文件定义。这里有详细的注释，可以作为文档使用。基于这些 Headers，我们也使用 Appledoc 生成了在线文档与 docet。

在 App 里，引用 JMessage SDK 的头文件，只需要引用这一个就够了: JMessage.h

| 头文件 | 说明 |
| ----- | ---- |
| JMessage.h | SDK 核心类，提供启动方法，以及全局的定义与方法。这个类导入了其他所有的必需的头文件 |
| JMSGConstants.h | 全局常量定义 |
| JMSGUser.h | 用户 Model，以及用户相关的接口定义
| JMSGGroup.h | 群组 Model，以及群组相关的接口定义
| JMSGMessage.h | 消息 Model，以及消息相关的接口定义
| JMSGConversation.h | 会话 Model，以及会话相关的接口定义
| JPUSHService.h | JPush 接口类
| JMSGAbstractContent | 内容类型的父类
| JMSGTextContent | 文本内容 Model
| JMSGCustomContent | 自定义内容 Model
| JMSGAbstractMediaContent | 媒体内容类型的父类，也继承自 JMSGAbstractContent
| JMSGVoiceContent | 语音内容 Model
| JMSGImageContent | 图片内容 Model
| JMSGEventContent.h | 事件通知内容 Model
| Delegate/JMessageDelegate | 全局的 Delegate，包含其他所有 Delegates
| Delegate/JMSGConversationDelegate | 会话相关 Delegate
| Delegate/JMSGMessageDelegate | 消息相关 Delegate
| Delegate/JMSGGroupDelegate | 群组相关 Delegate
| Delegate/JMSGUserDelegate | 用户相关 Delegate
| Delegate/JMSGDBMigrateDelegate | 数据迁移相关 Delegate

##### 调用代码

监听系统事件，相应地调用 JPush SDK 提供的 API 来实现功能。

以下 ３ 个事件监听与调用 JPush SDK API 都是必须的。请直接复制如下代码块里，注释为 "Required" 的行，到你的应用程序代理类里相应的监听方法里。

```
/// AppDelegate.m 里的启动方法
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  /// Required - 添加 JMessage SDK 监听。这个动作放在启动前
  [JMessage addDelegate:self withConversation:nil];
  
  /// Required - 启动 JMessage SDK
  [JMessage setupJMessage:launchOptions
                   appKey:JMSSAGE_APPKEY
                  channel:CHANNEL 
         apsForProduction:NO
                 category:nil];
  
  /// Required - 注册 APNs 通知
  if ([[UIDevice currentDevice].systemVersion floatValue] >= 8.0) {
    /// 可以添加自定义categories
    [JPUSHService registerForRemoteNotificationTypes:(UIUserNotificationTypeBadge |
                                                   UIUserNotificationTypeSound |
                                                   UIUserNotificationTypeAlert)
                                       categories:nil];
  } else {
    /// categories 必须为nil
    [JPUSHService registerForRemoteNotificationTypes:(UIRemoteNotificationTypeBadge |
                                                   UIRemoteNotificationTypeSound |
                                                   UIRemoteNotificationTypeAlert)
                                       categories:nil];
  }
  return YES;
}
 
- (void)application:(UIApplication *)application 
didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
     
  /// Required - 注册 DeviceToken
  [JPUSHService registerDeviceToken:deviceToken];
}
 
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo {
     
  // Required - 处理收到的通知
  [JPUSHService handleRemoteNotification:userInfo];
}
 
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
 
 
  // IOS 7 Support Required
  [JPUSHService handleRemoteNotification:userInfo];
  completionHandler(UIBackgroundFetchResultNewData);
}

- (void)application:(UIApplication *)application didFailToRegisterForRemoteNotificationsWithError:(NSError *)error {

  //Optional
  NSLog(@"did Fail To Register For Remote Notifications With Error: %@", error);
}
  
```


##### JPush 监听通知

JPush 提供了下面 6 种类型的通知，可以注册 NSNotificationCenter 来监听，以做进一步的逻辑处理。这些是可选的。

```
extern NSString * const kJPFNetworkIsConnectingNotification;       // 正在连接中
extern NSString * const kJPFNetworkDidSetupNotification;           // 建立连接
extern NSString * const kJPFNetworkDidCloseNotification;           // 关闭连接
extern NSString * const kJPFNetworkDidRegisterNotification;        // 注册成功
extern NSString * const kJPFNetworkDidLoginNotification;           // 登录成功
extern NSString * const kJPFNetworkDidReceiveMessageNotification;  // 收到消息(自定义消息，非 APNs)
```

其中，kJPFNetworkDidReceiveMessageNotification 通知是有传递数据的，可以通过NSNotification中 的 userInfo方法获取，包括标题、内容、内容类型、扩展信息等。

##### JMessage 监听通知

从 2.0.0 版本开始，JMessage SDK 向 App 发的消息，改变之前类似于 JPush 发 Notification 的方式，调整为实现 Delegate 协议。

以下代码片断节选自 JChat 项目。

```
extern NSString *const JMSGNotification_ReceiveMessage;          // 收到聊天消息
extern NSString *const JMSGNotification_EventMessage;            // 收到事件
extern NSString *const JMSGNotification_SendMessageResult;       // 发送消息结果返回
extern NSString *const JMSGNotification_ConversationInfoChanged; // 会话更新
extern NSString *const JMSGNotification_GroupChange;             // 群组更新
```

#### JMessage 代码样例

请参考 [JChat iOS 项目源代码](http://github.com/jpush/jchat-ios)，开源放在 Github 上。随着 SDK 下载的压缩包里，也有 JChat 整个的源代码项目。

### 技术支持

邮件联系：[support@jpush.cn][4]

问答社区：[https://community.jiguang.cn/latest][5]

[0]: ./image/create_ios_app.png
[1]: ./image/Screenshot_13-4_2_create.png
[2]: ./image/Screenshot_13-4-15_3_31.png
[3]: ../../client_sdks/ios_api
[4]: mailto:support@jpush.cn
[5]: http://www.jpush.cn/qa/

# iOS SDK 集成指南

## 集成说明

### 适用SDK版本
本文档适配 JMessage iOS SDK V3.0.0 及以后版本。     
已集成之前版本的用户升级或已集成 JPush 的用户想同时集成IM，请参见下文的[注意事项](#注意事项)。

### 系统要求与开发环境

+ JMessage iOS SDK 支持 iOS 7 以上系统版本。


## 集成步骤

### 1、在极光 Web控制台上创建应用

* 登录<a href="https://www.jiguang.cn/accounts/login/form" target="_blank">极光Web控制台</a>，创建应用，上传 APNs 证书。
如果对 Apple APNs 证书不太了解，请参考[iOS 证书设置指南](https://docs.jiguang.cn/jpush/client/iOS/ios_cer_guide/)。

![jmessage_ios][0]

* 创建成功后自动生成 AppKey 用以标识该应用。这个后续要用到。

![jmessage_ios][1]

### 2、SDK 导入
#### Cocoapods 导入
通过 Cocoapods 下载地址：

	pod 'JMessage'

如果需要安装指定版本则使用：

	pod 'JMessage', :head
	
使用用Cocoapods导入SDK则可以跳过步骤3.

#### 手动导入
在极光IM官网下载[最新SDK](https://docs.jiguang.cn/jmessage/resources/)

1. 把 JMessage.framework 文件加入到项目里。
2. 把 JMessafe.framework 目录下的 jcore-ios-x.x.x.a（x.x.x 为jcore 版本号） link 到工程中。

### 3、添加必要的框架

* CoreTelephony.framework
* CoreAudio.framework
* CoreGraphics.framework
* SystemConfiguration.framework
* CFNetwork.framework
* Security.framework
* AudioToolbox.framework
* MobileCoreServices.framework
* libz.dylib
* libsqlite3.0.dylib
* libresolv.tbd

### 4、Build Settings 配置

* 在项目配置，Build Settings，Other Linker Flags 里增加如下 1 项：

```
    -ObjC
```

### 5、初始化极光 IM SDK 

在工程的 AppDelegate 中的以下方法中，调用 SDK 对应方法 ：

```
#import "AppDelegate.h"
#import <JMessage/JMessage.h>

@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Required - 启动 JMessage SDK
    [JMessage setupJMessage:launchOptions appKey:JMSSAGE_APPKEY channel:nil apsForProduction:NO category:nil];
    // Required - 注册 APNs 通知
    if ([[UIDevice currentDevice].systemVersion floatValue] >= 8.0) {
        //可以添加自定义categories
        [JMessage registerForRemoteNotificationTypes:(UIUserNotificationTypeBadge |
                                                          UIUserNotificationTypeSound |
                                                          UIUserNotificationTypeAlert)
                                              categories:nil];
    } else {
        //categories 必须为nil
        [JMessage registerForRemoteNotificationTypes:(UIRemoteNotificationTypeBadge |
                                                          UIRemoteNotificationTypeSound |
                                                          UIRemoteNotificationTypeAlert)
                                              categories:nil];
    }
    return YES;
}
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    // Required - 注册token
    [JMessage registerDeviceToken:deviceToken];
}
@end
```

### 详细使用方法
详细使用可以参见[SDK 开发指南](./im_sdk_ios.md)或者查看下面提供的[Demo](#demo)。

<span id="注意事项"></span>
## 注意事项
### V3.0.0 之前版本用户升级
升级步骤如下：

1. 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件。
2. 将 JMessage.framework 里的 JCore.a link到工程里。
3. 把原Apns注册和token上传的方法通过JMessage类的方法来实现，实现如下：

```
[JMessage registerForRemoteNotificationTypes:(UIRemoteNotificationTypeBadge|UIRemoteNotificationTypeSound | UIRemoteNotificationTypeAlert) categories:nil];

[JMessage registerDeviceToken:deviceToken];
```

### 监听连接状态通知名修改
JMessage iOS SDK V3.0.0 以下版本通过 Push 的通知来监听 SDK 的连接状态，现在已经更新为由JMessage 里提供，原通知名为：

```
extern NSString *const kJPFNetworkIsConnectingNotification; // 正在连接中
extern NSString *const kJPFNetworkDidSetupNotification;     // 建立连接
extern NSString *const kJPFNetworkDidCloseNotification;     // 关闭连接
extern NSString *const kJPFNetworkDidRegisterNotification;  // 注册成功
extern NSString *const kJPFNetworkFailedRegisterNotification; //注册失败
extern NSString *const kJPFNetworkDidLoginNotification;     // 登录成功
extern NSString *const kJPFNetworkDidReceiveMessageNotification;    // 收到消息
extern NSString *const kJPFServiceErrorNotification;  // 错误提示
```

现在修改为：

```
extern NSString *const kJMSGNetworkIsConnectingNotification;          // 正在连接中
extern NSString *const kJMSGNetworkDidSetupNotification;              // 建立连接
extern NSString *const kJMSGNetworkDidCloseNotification;              // 关闭连接
extern NSString *const kJMSGNetworkDidRegisterNotification;           // 注册成功
extern NSString *const kJMSGNetworkFailedRegisterNotification;        // 注册失败
extern NSString *const kJMSGNetworkDidLoginNotification;              // 连接成功
extern NSString *const kJMSGNetworkDidReceiveMessageNotification;     // 收到消息
extern NSString *const kJMSGServiceErrorNotification;                 // 错误提示
```

### 基于 JPush 集成 JMessage
JMessage iOS SDK V3.0.0 及以后版本不再包含 JPush 的功能，需要使用 JPush 的用户需要单独集成 JPush SDK，集成步骤参见[JPush 集成指南](https://docs.jiguang.cn/jpush/client/iOS/ios_guide_new/)

注意以下几点：

1. 版本要求：支持 JPush V3.0.1 或以上版本，JCore 需 V1.1.0 或以上版本。
2. JCore的替换：下载下来的JPush SDK zip包中同样包含了名为jcore-ios-x.x.x.a Lib，集成时需要注意项目中只保留一个 jcore，如果出现JPush和JMessage中所包含的 jcore 版本不一致的情况，则保留最新版本的jcore。

<span id="demo"></span>
## JMessage Demo
极光 IM 提供了一个完整的 IM 场景下的应用 JChat，它就是一个 IM App，供大家下载参考。
<a href="http://github.com/jpush/jchat-ios" target="_blank">JChat iOS 项目源代码</a>，开源放在 Github 上。下载的 SDK 压缩包里，也有 JChat 的源代码。

## 技术支持

邮件联系：[support@jiguang.cn][4]


[0]: ./image/create_ios_app.png
[1]: ./image/Screenshot_13-4_2_create.png
[2]: ./image/Screenshot_13-4-15_3_31.png
[3]: ../../client_sdks/ios_api
[4]: mailto:support@jpush.cn


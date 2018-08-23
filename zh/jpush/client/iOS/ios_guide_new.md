# iOS SDK 集成指南

<style>
img[alt=jpush_ios] { width: 800px; }
</style>

## SDK说明

### 适用版本

本文匹配的 SDK 版本：r2.1.5 以后。
[查看最近更新](../../updates)了解最新的 SDK 更新情况。
使用 Xcode 6 及以上版本可以使用新版 Push SDK，Xcode 5 环境下需要运行旧版本 SDK（1.7.4）


### 资源文件

包名为 JPush-iOS-SDK-{版本号}

* lib 文件夹：包含头文件 JPUSHService.h，静态库文件 jpush-ios-x.x.x.a，jcore-ios-x.x.x.a，支持的 iOS 版本为 6.0 及以上版本。（请注意：模拟器不支持 APNs）
* README 文件：SDK 相关说明
* demo 文件夹：示例

## 创建应用
* 在 JPush 的管理 Portal 上创建应用，创建成功后自动生成 AppKey 用以标识该应用。

* 在推送设置 iOS 模块上传 APNs 证书或配置 Token Authentication。如果对 APNs 证书不太了解 请参考： [iOS 证书设置指南](ios_cer_guide)

* 详细图示见入门指南 》控制台使用指南 》[创建应用](https://docs.jiguang.cn/jpush/console/Instructions/#_1)



## 配置工程
### 导入 SDK
**选择 1：Cocoapods 导入**

* 通过 Cocoapods 下载地址：

```
pod 'JPush'
```
```
注：如果无法导入最新版本，请执行 pod repo update master 这个命令来升级本机的 pod 库，然后重新 pod 'JPush'
```
* 如果需要安装指定版本则使用以下方式（以 3.0.2 版本为例）：

```
pod 'JPush', '3.0.2'
```


**选择 2：手动导入**

* 在极光官网下载[最新 SDK ](http://docs.jiguang.cn/jpush/resources/)
* 将 SDK 包解压，在 Xcode 中选择 “Add files to 'Your project name'...”，将解压后的 lib 子文件夹（包含 JPUSHService.h、jpush-ios-x.x.x.a、jcore-ios-x.x.x.a ）添加到你的工程目录中。
* 添加 Framework
	* CFNetwork.framework
	* CoreFoundation.framework
	* CoreTelephony.framework
	* SystemConfiguration.framework
	* CoreGraphics.framework
	* Foundation.framework
	* UIKit.framework
	* Security.framework
	* libz.tbd（Xcode 7 以下版本是 libz.dylib）
	* AdSupport.framework（获取 IDFA 需要；如果不使用 IDFA，请不要添加）
	* UserNotifications.framework（Xcode 8 及以上）
	* libresolv.tbd（JPush 2.2.0 及以上版本需要，Xcode 7 以下版本是 libresolv.dylib）

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>注意：
如果集成 JPush 3.0.1 及以上版本， 且同时集成极光其他 SDK（如：JMessage 3.0.0 及以上版本）
<br>
1. Cocoapods 导入，建议都更新为线上最新版本，来避免 JCore 版本不一致导致的冲突。
<br>
2. 手动导入，在工程中只需保留一个最新版本的 jcore-ios-x.x.x.a 静态库文件。
</div>

### Build Settings
如果你的工程需要支持小于 7.0 的 iOS 系统，请到 Build Settings 关闭 bitCode 选项，否则将无法正常编译通过。

* 设置 Search Paths 下的 User Header Search Paths 和 Library Search Paths，比如 SDK 文件夹（默认为 lib ）与工程文件在同一级目录下，则都设置为 "$(SRCROOT)/{静态库所在文件夹名称}" 即可。

### Capabilities
如使用 Xcode 8 及以上环境开发，请开启 Application Target 的 Capabilities->Push Notifications 选项，如图：
![jpush_ios][7]

### 允许 Xcode 7 支持 Http 传输方法
如果您使用的是 2.1.9 及以上的版本则不需要配置此步骤    
如果用的是 Xcode 7 或更新版本，需要在 App 项目的 plist 手动配置下 key 和值以支持 http 传输:

**选择1：根据域名配置**

* 在项目的 info.plist 中添加一个 Key：NSAppTransportSecurity，类型为字典类型。
* 然后给它添加一个 NSExceptionDomains，类型为字典类型；
* 把需要的支持的域添加给 NSExceptionDomains。其中 jpush.cn 作为 Key，类型为字典类型。
* 每个域下面需要设置 2 个属性：NSIncludesSubdomains、NSExceptionAllowsInsecureHTTPLoads。
两个属性均为 Boolean 类型，值分别为 YES、YES。

如图：

![jpush_ios][6]


**选择2：全局配置**

```
  <key>NSAppTransportSecurity</key>
  <dict>
  	<key>NSAllowsArbitraryLoads</key>
  	<true/>
  </dict>
```

## 添加头文件
请将以下代码添加到 AppDelegate.m 引用头文件的位置。

```
// 引入 JPush 功能所需头文件
#import "JPUSHService.h"
// iOS10 注册 APNs 所需头文件
#ifdef NSFoundationVersionNumber_iOS_9_x_Max
#import <UserNotifications/UserNotifications.h>
#endif
// 如果需要使用 idfa 功能所需要引入的头文件（可选）
#import <AdSupport/AdSupport.h>
```

## 添加Delegate
为 AppDelegate 添加 Delegate。

参考代码：

```
@interface AppDelegate ()<JPUSHRegisterDelegate>

@end
```

## 添加初始化代码

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>2.1.0 版本开始，API 类名为 JPUSHService，不再使用原先的 APService。
</div>

### 添加初始化APNs代码

请将以下代码添加到
-(BOOL)application:(UIApplication \*)application
didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions

```
  //Required
  //notice: 3.0.0 及以后版本注册可以这样写，也可以继续用之前的注册方式
  JPUSHRegisterEntity * entity = [[JPUSHRegisterEntity alloc] init];
  entity.types = JPAuthorizationOptionAlert|JPAuthorizationOptionBadge|JPAuthorizationOptionSound;
  if ([[UIDevice currentDevice].systemVersion floatValue] >= 8.0) {
    // 可以添加自定义 categories
    // NSSet<UNNotificationCategory *> *categories for iOS10 or later
    // NSSet<UIUserNotificationCategory *> *categories for iOS8 and iOS9
  }
  [JPUSHService registerForRemoteNotificationConfig:entity delegate:self];

```
### 添加初始化 JPush 代码

请将以下代码添加到
-(BOOL)application:(UIApplication \*)application
didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions

```
  // Optional
  // 获取 IDFA
  // 如需使用 IDFA 功能请添加此代码并在初始化方法的 advertisingIdentifier 参数中填写对应值
  NSString *advertisingId = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];

  // Required
  // init Push
  // notice: 2.1.5 版本的 SDK 新增的注册方法，改成可上报 IDFA，如果没有使用 IDFA 直接传 nil
  // 如需继续使用 pushConfig.plist 文件声明 appKey 等配置内容，请依旧使用 [JPUSHService setupWithOption:launchOptions] 方式初始化。
  [JPUSHService setupWithOption:launchOptions appKey:appKey
                        channel:channel
               apsForProduction:isProduction
          advertisingIdentifier:advertisingId];
```
##### 部分参数说明：
* appKey
    * 选择 [Web Portal 上 的应用](https://www.jiguang.cn/dev/#/app/list) ，点击“设置”获取其 appkey 值。请确保应用内配置的 appkey 与 Portal 上创建应用后生成的 appkey 一致。
* channel
    * 指明应用程序包的下载渠道，为方便分渠道统计，具体值由你自行定义，如：App Store。
* apsForProduction
    * 1.3.1 版本新增，用于标识当前应用所使用的 APNs 证书环境。
    * 0（默认值）表示采用的是开发证书，1 表示采用生产证书发布应用。
    * 注：此字段的值要与 Build Settings的Code Signing 配置的证书环境一致。
* advertisingIdentifier
    * 详见[关于 IDFA](#_8)。


### 注册 APNs 成功并上报 DeviceToken
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	
<p>温馨提示：
	<br>
<p>	
JPush 3.0.9 之前的版本，必须调用此接口，注册 token 之后才可以登录极光，使用通知和自定义消息功能。
	<br>
从 JPush 3.0.9 版本开始，不调用此方法也可以登录极光。但是不能使用 APNs 通知功能，只可以使用 JPush 自定义消息。
</div>

请在 AppDelegate.m 实现该回调方法并添加回调方法中的代码

```
- (void)application:(UIApplication *)application
didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {

  /// Required - 注册 DeviceToken
  [JPUSHService registerDeviceToken:deviceToken];
}
```

### 实现注册 APNs 失败接口（可选）

```
- (void)application:(UIApplication *)application didFailToRegisterForRemoteNotificationsWithError:(NSError *)error {
  //Optional
  NSLog(@"did Fail To Register For Remote Notifications With Error: %@", error);
}
```


### 添加处理 APNs 通知回调方法

请在 AppDelegate.m 实现该回调方法并添加回调方法中的代码

```
#pragma mark- JPUSHRegisterDelegate

// iOS 10 Support
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(NSInteger))completionHandler {
  // Required
  NSDictionary * userInfo = notification.request.content.userInfo;
  if([notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) {
    [JPUSHService handleRemoteNotification:userInfo];
  }
  completionHandler(UNNotificationPresentationOptionAlert); // 需要执行这个方法，选择是否提醒用户，有 Badge、Sound、Alert 三种类型可以选择设置
}

// iOS 10 Support
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)())completionHandler {
  // Required
  NSDictionary * userInfo = response.notification.request.content.userInfo;
  if([response.notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) {
    [JPUSHService handleRemoteNotification:userInfo];
  }
  completionHandler();	// 系统要求执行这个方法
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {

  // Required, iOS 7 Support
  [JPUSHService handleRemoteNotification:userInfo];
  completionHandler(UIBackgroundFetchResultNewData);
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo {

  // Required, For systems with less than or equal to iOS 6
  [JPUSHService handleRemoteNotification:userInfo];
}
```

### 添加处理 JPush 自定义消息回调方法

如需使用 JPush 的自定义消息功能，请参考[文档](ios_api/#message)来实现自定义消息的处理回调方法。


## 成功运行

真机调试该项目，如果控制台输出以下日志则代表您已经集成成功。

```
2016-08-19 17:12:12.745823 219b28[1443:286814]  | JPUSH | I - [JPUSHLogin]
----- login result -----
uid:5460310207
registrationID:171976fa8a8620a14a4
```

如果调试运行中遇到问题请参考：[iOS SDK 调试指南](ios_debug_guide)


## 高级功能

### 关于 IDFA
r2.1.5 版本增加一个上传IDFA字符串的接口

	 + (void)setupWithOption:(NSDictionary *)launchingOption
                      appKey:(NSString *)appKey
                     channel:(NSString *)channel
            apsForProduction:(BOOL)isProduction
       advertisingIdentifier:(NSString *)advertisingId;

如果不使用 IDFA，仍可使用接口

	+ (void)setupWithOption:(NSDictionary *)launchingOption
                      appKey:(NSString *)appKey
                     channel:(NSString *)channel
            apsForProduction:(BOOL)isProduction;

### JPush SDK 相关事件监听

建议开发者加上 API 里面提供的以下类型的通知：

extern NSString *const kJPFNetworkIsConnectingNotification; // 正在连接中

extern NSString * const kJPFNetworkDidSetupNotification; // 建立连接

extern NSString * const kJPFNetworkDidCloseNotification; // 关闭连接

extern NSString * const kJPFNetworkDidRegisterNotification; // 注册成功

extern NSString *const kJPFNetworkFailedRegisterNotification; //注册失败

extern NSString * const kJPFNetworkDidLoginNotification; // 登录成功

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示：
  <br>
<p>Registration id 需要添加注册 kJPFNetworkDidLoginNotification 通知的方法里获取，也可以调用 [registrationIDCompletionHandler:] 方法，通过 completionHandler 获取
</div>

extern NSString * const kJPFNetworkDidReceiveMessageNotification; // 收到自定义消息(非 APNs)

其中，kJPFNetworkDidReceiveMessageNotification 传递的数据可以通过 NSNotification 中的 userInfo 方法获取，包括标题、内容、extras 信息等

请参考文档：[iOS SDK API](https://docs.jiguang.cn/jpush/client/iOS/ios_api/#_51)

### 通知送达统计

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示：
  <br>
<p>
iOS 10 新增的 Notification Service Extension 功能，用 mutable-content 字段来控制。 
	<br>
若使用 Web 控制台，需勾选 “可选设置”中 mutable-content 选项；若使用 RESTFul API 需设置 mutable-content 字段为 true。
</div>

从 iOS JPush SDK 3.0.7 版本，开发者可使用 Notification Service Extension SDK 上报每条 APNs 信息的送达状态。

**使用方法：**

+ 将 jpush-extension-ios-xxx.a 和 JPushNotificationExtensionService.h 两个文件引入到您的 Service Extentsion 工程中。
+ 添加 Framework：libz.tbd 和 libresolv.tbd。
+ 调用 [jpushSetAppkey:] 方法设置您的 appkey，请注意这里的 appkey 应该和您极光应用的 appkey 相同。
+ 调用 [jpushReceiveNotificationRequest:] 方法上报您的 apns 消息，完成送达统计；在该方法的 block 回调中进行 apns 的显示。

更具体的使用示例请参考版本压缩包中附带的 Demo 代码。

参考文档：[iOS SDK API](https://docs.jiguang.cn/jpush/client/iOS/ios_api/#notification-service-extension)

## 技术支持

当出现问题时：

+ 请仔细阅读文档，查看是否有遗漏。 [iOS FAQ](../iOS/ios_faq/)
+ 你可以到极光社区搜索类似问题
+ 给我们的 support 发邮件 [support&#64;jpush.cn][4]

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

+ 你需要咨询的产品是 JPush，是否同时使用了极光其他的产品
+ 你所调用的是什么 API，所传参数，完整的报错信息，出现异常的时间点
+ 如果收不到消息，提供应用的 Appkey，消息的 Message ID，设备的 registration ID 信息
+ 如果是 SDK 问题请提供对应的 SDK 版本和完整的日志记录，日志信息请使用 TXT 文件上传
+ 出现异常的设备是 iOS ，列出具体的机型和系统

[0]: ../image/create_ios_app1.png
[1]: ../image/Screenshot_13-4_2_create.jpg
[2]: ../image/Screenshot_13-4-15_3_31.png
[3]: ios_api
[4]: mailto:support&#64;jpush.cn
[6]: ../image/ios_http.png
[7]: ../image/capabilities_intro.jpg

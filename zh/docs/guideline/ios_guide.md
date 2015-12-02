# iOS SDK 集成指南

## 使用提示

本文匹配的 SDK版本：r2.1.0 以后。

查看最近更新了解最新的SDK更新情况。

## 产品功能说明

极光推送（JPush）是一个端到端的推送服务，使得服务器端消息能够及时地推送到终端用户手机上，让开发者积极地保持与用户的连接，从而提高用户活跃度、提高应用的留存率。极光推送客户端支持 Android, iOS 两个平台。

本 iOS SDK 方便开发者基于 JPush 来快捷地为 iOS App 增加推送功能，减少集成 APNs 需要的工作量、开发复杂度。


### 主要功能

* 为 JPush Server 上报 Device Token，免除开发者管理 Device Token 的麻烦
* 应用运行时，应用内 JPush 长连接可以持续地收到推送消息

### 主要特点

* 集成简单
* iOS SDK 集成后，服务器端向 iOS 设备推送简单方便

### 集成压缩包内容

包名为JPush-iOS-SDK-[版本号]

* lib文件夹：包含头文件 JPUSHService.h，静态库文件 libPushSDK.a ，支持的iOS版本为 5.0 及以上版本。（请注意：模拟器不能实现APNS）
* pdf文件：开发指南
* demo文件夹：示例

### 开发环境

* 使用Xcode 6版本运行IOS8版本SDK，XCode 5运行非IOS 8版本SDK

## SDK集成步骤

### 在JPush Portal上创建应用

* 在JPush的管理Portal上 上传证书并创建应用。如果对APNs证书不太了解 请参考 [iOS 证书设置指南](../../client/ios_tutorials/#ios_1) 

![][0]
* 创建成功后自动生成 AppKey 用以标识该应用。 

![][1]

### 导入API开发包到应用程序项目

* 将SDK包解压，在XCode中选择“Add files to 'Your project name'...”，将解压后的lib子文件夹（包含APService.h、libPushSDK.a）添加到你的工程目录中。

### 必要的框架

* CFNetwork.framework
* CoreFoundation.framework
* CoreTelephony.framework
* SystemConfiguration.framework
* CoreGraphics.framework
* Foundation.framework
* UIKit.framework
* Security.framework
* Xcode7需要的是libz.tbd；Xcode7以下版本是libz.dylib

### Build Settings

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>如果你的工程最低支持6.0以下版本时请注意关闭bitCode选项，否则将无法正常编译通过.
</div>

* 设置 Search Paths 下的 User Header Search Paths 和 Library Search Paths，比如SDK文件夹（默认为lib）与工程文件在同一级目录下，则都设置为"$(SRCROOT)/[文件夹名称]"即可。

### 创建并配置PushConfig.plist文件
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>该文件用于2.1.0之前的版本配置appkey 等信息，从 2.1.0 开始，参数配置信息可以直接通过setupWithOption初始化方法参数传入.
</div>

在你的工程中创建一个新的Property List文件，并将其命名为PushConfig.plist，填入Portal为你的应用提供的APP_KEY等参数。

    {
     "APS_FOR_PRODUCTION" = "0";
     "CHANNEL" = "Publish channel";
     "APP_KEY" = "AppKey copied from JPush Portal application";
    }
    

* CHANNEL 
    * 指明应用程序包的下载渠道，为方便分渠道统计。根据你的需求自行定义即可。
* APP_KEY 
    * 在管理Portal上创建应用时自动生成的（AppKey）用以标识该应用。请确保应用内配置的 AppKey 与第1步在 Portal 上创建应用时生成的 AppKey 一致，AppKey 可以在应用详情中查询。


![][2]

* APS_FOR_PRODUCTION 
    * 1.3.1版本新增，表示应用是否采用生产证书发布( Ad_Hoc 或 APP Store )，此参数值需要与应用（code signing）所使用的证书环境一致，0 (默认值)表示采用的是开发者证书，1 表示采用生产证书发布应用。
    * push所指定的环境（apns_production）需要和应用证书环境一致才能收到推送。

* 在1.2.2或之前版本的配置文件中，有 TEST_MODE 这个键，新版的SDK不再使用，可以将它删除。

### 添加代码
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>2.1.0版本后,API类名为JPUSHService，不再使用原先的APService
</div>

#### API

APIs 主要集中在 JPUSHService 接口类里。

- init Push方法分为两个
  + 2.1.0版本前方法适用于JPush老用户不希望修改代码直接兼容新版本。  
  + 2.1.0版本后方法适用于新接入JPush的用户，以及希望不适用plist文件而是代码来填写appKey等信息的老用户。
  
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>使用建议
<br>
<p>init Push方法只能存在一个。同时存在时以第一个设定为准
</div>
<br>

	    @interface JPUSHService : NSObject    
    	// init Push
    	 // init Push(2.1.0版本前注册方法）
        + (void)setupWithOption:(NSDictionary *)launchingOption;
    	// init Push(2.1.0版本后注册方法)
		+ (void)setupWithOption:(NSDictionary *)launchingOption appKey:(NSString *)appKey channel:(NSString *)channel apsForProduction:(BOOL)isProduction;
    
    	// register notification type
    	+ (void)registerForRemoteNotificationTypes:(NSUInteger)types
                                categories:(NSSet *)categories;  // 注册APNS类型
    
         // upload device token
         + (void)registerDeviceToken:(NSData *)deviceToken;
    
        // handle notification recieved
        + (void)handleRemoteNotification:(NSDictionary *)remoteInfo;
    

#### 调用代码

监听系统事件，相应地调用 JPush SDK 提供的 API 来实现功能。

以下 ３ 个事件监听与调用 JPush SDK API 都是必须的。请直接复制如下代码块里，注释为 "Required" 的行，到你的应用程序代理类里相应的监听方法里。

```

    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];
    self.window.backgroundColor = [UIColor whiteColor];
    [self.window makeKeyAndVisible];
 
    // Required
   if ([[UIDevice currentDevice].systemVersion floatValue] >= 8.0) {
    //可以添加自定义categories
    [JPUSHService registerForRemoteNotificationTypes:(UIUserNotificationTypeBadge |
                                                   UIUserNotificationTypeSound |
                                                   UIUserNotificationTypeAlert)
                                       categories:nil];
  } else {
    //categories 必须为nil
    [JPUSHService registerForRemoteNotificationTypes:(UIRemoteNotificationTypeBadge |
                                                   UIRemoteNotificationTypeSound |
                                                   UIRemoteNotificationTypeAlert)
                                       categories:nil];
  }

    // Required
    [JPUSHService setupWithOption:launchOptions appKey:appKey channel:channel apsForProduction:isProduction]; ／／如需兼容旧版本的方式，请依旧使用[JPUSHService setupWithOption:launchOptions]方式初始化和同时使用pushConfig.plist文件声明appKey等配置内容。
    
    return YES;
}
 
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
     
    // Required
    [JPUSHService registerDeviceToken:deviceToken];
}
 
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo {
     
    // Required
    [JPUSHService handleRemoteNotification:userInfo];
}
 
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
 
 
  // IOS 7 Support Required
  [JPUSHService handleRemoteNotification:userInfo];
  completionHandler(UIBackgroundFetchResultNewData);
}
    
```


#### 监听通知

API里面提供了下面 5 种类型的通知：

extern NSString * const kJPFNetworkDidSetupNotification; // 建立连接

extern NSString * const kJPFNetworkDidCloseNotification; // 关闭连接

extern NSString * const kJPFNetworkDidRegisterNotification; // 注册成功

extern NSString * const kJPFNetworkDidLoginNotification; // 登录成功

extern NSString * const kJPFNetworkDidReceiveMessageNotification; // 收到消息(非APNS)

其中，kJPFNetworkDidReceiveMessageNotification通知是有传递数据的，可以通过NSNotification中的userInfo方法获取，包括标题、内容、内容类型、扩展信息等

## 高级功能

请参考：



[标签与别名API](../../../client/ios_api/#api-ios)

[页面的统计](../../../client/ios_api/#_29)

## 技术支持

邮件联系：[support@jpush.cn][4]

问答社区：[http://www.jpush.cn/qa/][5]

[0]: image/create_ios_app.png
[1]: image/Screenshot_13-4_2_create.png
[2]: image/Screenshot_13-4-15_3_31.png
[3]: ../../client_sdks/ios_api
[4]: mailto:support@jpush.cn
[5]: http://www.jpush.cn/qa/
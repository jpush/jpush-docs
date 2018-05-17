# iOS SDK Integration Guide

## Integration instructions

### Applicable to SDK version

This document is compatible with the JMessage iOS SDK V3.0.0 and later. If users who have integrated previous versions or users who have integrated JPush want to integrate IM at the same time, plese see [Precautions](#precautions) below.

### System Requirements and Development Environment

-   The JMessage iOS SDK supports iOS 7 and later versions.

## Integration Steps

### 1、Create an application on the Jiguang Web Console

Log in to the [Jiguang Web Console](https://www.jiguang.cn/accounts/login/form), create applications, and upload APNs certificates. If you do not know much about Apple APNs certificates, please refer to the [iOS Certificate Setup Guide](../jpush/client/iOS/ios_cer_guide/).

![jmessage_ios][0]

AppKey is automatically generated to identify the application after successful creation. This will be used later.

![jmessage_ios][1]

### 2、SDK import

#### Cocoapods import

Download address via Cocoapods

    pod 'JMessage'

Use below if you need to install the specified version

    pod 'JMessage', :head

3\. Skip step 3 if importing SDK via Cocoapods

#### Manually import

Download [latest SDK](https://docs.jiguang.cn/jmessage/resources/) on JMessage official website

1.  Add the JMessage.framework file to the project.

2.  Link jcore-ios-x.x.x.a (x.x.x as jcore version number) in the JMessafe.framework directory to the project.

### 3、Add the necessary framework

-   CoreTelephony.framework

-   CoreAudio.framework

-   CoreGraphics.framework

-   SystemConfiguration.framework

-   CFNetwork.framework

-   Security.framework

-   AudioToolbox.framework

-   MobileCoreServices.framework

-   libz.dylib

-   libsqlite3.0.dylib

-   libresolv.tbd

### 4、Build Settings configuration

-   Add 1 item in Project Configuration, Build Settings, Other Linker Flags

```
-ObjC
```

### 5、Initialize JMessage SDK

In the following method of the project's AppDelegate, call the corresponding SDK method

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

### Detailed usage

For details, please refer to the [SDK Development Guide](./im_sdk_ios/) or check the [Demo](#demo) provided below.


## Precautions

### User upgrades in versions prior to V3.0.0

The upgrade steps are as follows:

1.  Replace the old file with the same name under the original project with the new version of the JMessage.framework file.

2.  Link JCore.a in JMessage.framework to the project.

3.  Implement the method of registering original Apns and uploading the token by the method of the JMessage class. The implementation is as follows:

```
[JMessage registerForRemoteNotificationTypes:(UIRemoteNotificationTypeBadge|UIRemoteNotificationTypeSound | UIRemoteNotificationTypeAlert) categories:nil];

[JMessage registerDeviceToken:deviceToken];
```

### Monitor modification of connection status notification name 

The previous versions of the JMessage iOS SDK V3.0.0 monitor connection status of the SDK through the Push notification. It is provided by the JMessage after updating. The original notification name is

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

Now change to

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

### Integrate JMessage based on JPush

JMessage iOS SDK V3.0.0 and later versions no longer include the functions of JPush. Users who use JPush need to integrate the JPush SDK separately. Refer to [JPush Integration Guide](../jpush/client/iOS/ios_guide_new/) for integration steps.

Note the following points

1.  Version requirements: Supports JPush V3.0.1 or later version. JCore requires V1.1.0 or later version.

2.  Replacement of JCore: The downloaded JPush SDK zip package also contains the name jcore-ios-xxxa Lib. When integrating, it is necessary to note that only one jcore is kept in the project. If the Jcore version contained in JPush and JMessage is inconsistent, keep the latest version of jcore.

## JMessage Demo

JMessage provides a complete application of JChat in the IM scenario. It is an IM App for reference. [JChat iOS project source code](https://github.com/jpush/jchat-ios), open source has been placed on Github. In the downloaded SDK archive, there is also JChat source code.

## Technical Support

E-mail contact: [support@jiguang.cn][4]


[0]: ./image/create_ios_app.png
[1]: ./image/Screenshot_13-4_2_create.png
[2]: ./image/Screenshot_13-4-15_3_31.png
[3]: ../../client_sdks/ios_api
[4]: mailto:support&#64;jpush.cn
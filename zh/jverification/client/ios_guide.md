#iOS SDK 集成指南

##使用提示

本文是JVerification iOS SDK 标准的集成指南文档。

匹配的 SDK 版本为：v2.0.0及以后版本。

+ 如果您想要快速地测试、请参考本文在几分钟内跑通Demo。
+ 极光认证文档网站上，有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。

##产品说明

极光认证整合了三大运营商的网关认证能力，为开发者提供了一键登录和号码认证功能，优化用户注册/登录、号码验证体验，提高安全性。

###主要场景：

* 注册
* 登陆
* 二次验证

###iOS SDK 版本

目前SDK只支持iOS 7以上版本的手机系统。

##接入配置

###添加SDK到工程中

**选择 1: Cocoapods 导入**

+ 通过 Cocoapods 下载地址：

~~~
    pod 'JVerification'
~~~

注：如果无法导入最新版本，请执行 pod repo update master 这个命令来升级本机的 pod 库，然后重新 pod 'JVerification'

+ 如果需要安装指定版本则使用以下方式（以2.2.0版本为例）：

~~~
    pod 'JVerification', '2.3.0'
~~~

**选择 2：手动导入**

+ 在极光官网下载最新 SDK
+ 请在自己的工程中导入libs文件夹下的SDK文件:

    * jcore-ios-2.0.2.a  jcore版本 1.2.3及其以上
    * jverification-ios-2.3.0.a jverification版本 2.0.0及其以上
    * account_verify_sdk_core.framework
    * account_login_sdk_noui_core.framework
    * TYRZSDK.framework
    * JVERIFICATIONService.h
    * EAccountApiSDK.framework

+ 为工程添加相应的Frameworks，需要为项目添加的Frameworks如下

    * AdSupport.framework（获取 IDFA 需要；如果不使用 IDFA，请不要添加）
    * CoreLocation.framework
    * CFNetwork.framework
    * CoreFoundation.framework
    * libresolv.tbd
    * libz.tbd
    * libc++.1.tbd
    * CoreTelephony.framework
    * SystemConfiguration.framework
    * Security.framework
    * CoreGraphics.framework
    * libsqlite3.tbd
    * MobileCoreServices.framework
    * account_verify_sdk_core.framework
    * TYRZSDK.framework
    * account_login_sdk_noui_core.framework
    * EAccountApiSDK.framework
    * jcore-ios-2.0.2.a  jcore版本 1.2.3及其以上
    * jverification-ios-2.3.0.a jverification版本 2.0.0及其以上
    

##配置资源

请将演示Demo中JVerificationResource.bundle拖到自己的工程目录下。 

##接入代码

请将以下代码添加到引用JAuthHelper.h头文件的的相关类中

~~~
    //引入JVERIFICATIONService.h头文件
    #import "JVERIFICATIONService.h"
    // 如果需要使用 idfa 功能所需要引入的头文件（可选）
	#import <AdSupport/AdSupport.h>
~~~

接入的JVerification SDK的应用，必须先初始化JAuthHelper,否则将会无法正常使用，请将以下代码添加到合适的位置

~~~
    // 如需使用 IDFA 功能请添加此代码并在初始化配置类中设置 advertisingId
    NSString *idfaStr = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
    
    JVAuthConfig *config = [[JVAuthConfig alloc] init];
    config.appKey = @"your appkey";
    config.advertisingId = idfaStr;
    [JVERIFICATIONService setupWithConfig:config];
~~~

##更多API

其他 API 的使用方法请参考接口文档：[iOS SDK API](./ios_api)

##运行Demo

压缩包附带的 demo 是一个 API 演示例子。你可以将它导入到你的工程，并将你的
AppKey 填入到 demo 的 ViewController 中，设置上Bundle ID然后直接运行起来测试。

##技术支持

邮件联系：[support&#64;jpush.cn](mailto:support&#64;jpush.cn)

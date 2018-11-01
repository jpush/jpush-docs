#iOS SDK 集成指南

##使用提示

本文是JVerification iOS SDK 标准的集成指南文档。

匹配的 SDK 版本为：v1.0.0及以后版本。

+ 如果您想要快速地测试、请参考本文在几分钟内跑通Demo。
+ 极光认证文档网站上，有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。

##产品说明

极光认证整合了三大运营商的号码认证能力，为开发者提供了快速验证用户输入的手机号码和本机SIM卡号码一致性的功能，提高用户体验和安全性。

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

注：如果无法导入最新版本，请执行 pod repo update master 这个命令来升级本机的 pod 库，然后重新 pod 'JVerification'

+ 如果需要安装指定版本则使用以下方式（以1.0.1版本为例）：

~~~
    pod 'JVerification', '1.0.1'
~~~

**选择 2：手动导入**

+ 在极光官网下载最新 SDK
+ 请在自己的工程中导入libs文件夹下的SDK文件:

    * jcore-ios-x.x.x.a  jcore版本 1.2.3及其以上
    * jverification-ios-x.x.x.a
    * account_verify_sdk_core.framework
    * EAccountSDK.framework
    * TYRZNoUISDK.framework
    * JVERIFICATIONService.h

+ 为工程添加相应的Frameworks，需要为项目添加的Frameworks如下

    * AdSupport.framework
    * CoreLocation.framework
    * CFNetwork.framework
    * CoreFoundation.framework
    * libresolv.tbd
    * libz.tbd
    * CoreTelephony.framework
    * SystemConfiguration.framework
    * Security.framework
    * CoreGraphics.framework
    * libsqlite3.tbd
    * MobileCoreServices.framework
    * account_verify_sdk_core.framework
    * EAccountSDK.framework
    * TYRZNoUISDK.framework
    * jcore-ios-x.x.x.a  jcore版本 1.2.3及其以上
    * jverification-ios-x.x.x.a

##接入代码

请将以下代码添加到引用JAuthHelper.h头文件的的相关类中

~~~
    //引入JVERIFICATIONService.h头文件
		import "JVERIFICATIONService.h"
~~~

接入的JVerification SDK的应用，必须先初始化JAuthHelper,否则将会无法正常使用，请将以下代码添加到合适的位置

~~~
    JVAuthConfig *config = [[JVAuthConfig alloc] init];
    config.appKey = @"your appkey";
    [JVERIFICATIONService setupWithConfig:config];
~~~

##更多API

其他 API 的使用方法请参考接口文档：[iOS SDK API](../ios_api)

##运行Demo

压缩包附带的 demo 是一个 API 演示例子。你可以将它导入到你的工程，并将你的
AppKey 填入到 demo 的 ViewController 中，设置上BundleID然后直接运行起来测试。

## 技术支持

邮件联系：[support&#64;jpush.cn](mailto:support&#64;jpush.cn)

# Android SDK 概述

+ [Android 常见问题](android_faq)
+ [Android 客户端 SDK 下载](../../resources/#android-sdk)

### JPush Android

![jpush_android](../image/jpush_android.png)

开发者集成 JPush Android SDK 到其应用里，JPush Android SDK 创建到 JPush Cloud 的长连接，为 App 提供永远在线的能力。  
当开发者想要及时地推送消息到达 App 时，只需要调用 JPush API 推送，或者使用其他方便的智能推送工具，即可轻松与用户交流。

图中红色部分，是 JPush 与 App 开发者的接触点。手机客户端侧，App 需要集成 JPush SDK；服务器端部分，开发者调用 JPush REST API 来进行推送。

### Android SDK 服务

JPush Android SDK 是作为 Android Service 长期运行在后台的，从而创建并保持长连接，保持永远在线的能力。


#### 多平台支持

JPush Android SDK 除了 jar 包，还有一个 .so 文件。.so 文件的存在 CPU 平台适配的问题。需要支持哪个平台的 CPU，就需要包含这个平台相应的 .so 编译文件。

除支持默认的 ARM CPU 平台之外，JPush SDK 还提供 x86 与 MIPs 平台的 CPU 版本 SDK。请单独到 [资源下载](../../resources/) 页下载。

#### 电量与流量

JPush Android SDK 由于使用自定义协议，协议体做得极致地小，流量消耗非常地小。

电量方面，JPush Android SDK 经过持续地优化，尽可能减少不必要的代码执行；并且，长期的版本升级迭代，不断地调优，在保证一定的网络连接稳定性的要求小，减少电量消耗。


#### 压缩包说明

供下载的 JPush Android SDK 压缩包，一般包含以下几个部分：

+ .jar 文件
+ .so 文件
+ AndroidManifest.xml 配置示例

其中 .jar, .so 文件有版本号后缀，需要互相匹配。请升级时一定记得检查版本号，并删除旧版本。

AndroidManifest.xml 配置示例可能在版本升级时，会有变更。请留意版本发布说明。

### Android SDK 集成

请参考以下文档与教程，来集成 Android SDK。

+ [3分钟快速Demo(Android)](android_3m)
+ [Android 集成指南](android_guide)



### 集成到其他平台

[客户端集成插件](/client/client_plugins)

[0]: ../image/product_android.png
[1]: https://www.jpush.cn/downloads/sdk/android/
[2]: https://www.jpush.cn/downloads/sdk/android-with-x86
[3]: https://www.jpush.cn/downloads/sdk/android-with-mips
[4]: ../../updates

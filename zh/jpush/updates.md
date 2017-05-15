# 最近更新

### JPush Android SDK v3.0.6

#### 更新时间

+ 2017-05-08

#### Change Log
+ 优化: 数据存储性能
+ 优化：提升sdk安全性
+ 新增：设置 tag/alias 增加错误码 6013（时间轴错误）

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.3.jar。用 jpush-android_v3.0.6.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore113.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
    + 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。

+ 如果使用jcenter的方式集成JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JPush Android SDK v3.0.5

#### 更新时间

+ 2017-04-14

#### Change Log
+ 优化存储性能
+ 提升sdk稳定性

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.2.jar。用 jpush-android_v3.0.5.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore112.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
    + 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。

+ 如果使用jcenter的方式集成JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。



### JPush iOS SDK v3.0.5

#### 更新时间
+ 2017-04-14

#### Change Log
+ 修改Bug，提高与其他SDK兼容稳定性

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0及以上版本将不再支持处理器为i386的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC



### JPush iOS SDK v3.0.3

#### 更新时间
+ 2017-04-01

#### Change Log
+ 优化：socket connect 机制
+ 修复：SDK HTTP 上报偶然崩溃的问题，增强健壮性

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0及以上版本将不再支持处理器为i386的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC

### JPush Android SDK v3.0.3

#### 更新时间

+ 2017-03-13

#### Change Log
+ 新增：支持通知呼吸灯提醒。
+ 修改：修复开发者反馈的一些兼容性问题。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.1.jar。用 jpush-android_v3.0.3.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore111.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
    + 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。

+ 如果使用jcenter的方式集成JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。



### JPush iOS SDK v3.0.2

#### 更新时间
+ 2017-02-13

#### Change Log
+ 修复：DNS解析失败带来的崩溃问题，提升稳定性 

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0及以上版本将不再支持处理器为i386的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC


### JPush iOS SDK v3.0.1

#### 更新时间
+ 2017-01-09

#### Change Log
+ 修复：已知bug。
+ 优化：运行性能。 

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0及以上版本将不再支持处理器为i386的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC



### JPush Android SDK v3.0.1

#### 更新时间

+ 2017-01-05

#### Change Log
+ 修复：一些已知问题。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.0.jar。用 jpush-android_v3.0.1.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore110.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
    + 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。

+ 如果使用jcenter的方式集成JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。



### JPush Android SDK v3.0.0

#### 更新时间

+ 2016-12-02

#### Change Log
+ 新增：模块化分离为 JCore，JPush 两部分集成，原有使用的一个 jar 包，分为了 jcore 和 jpush 两个jar 包。
+ 新增：消息通道加密。
+ 新增：支持原生Android的大文本，大图片，inbox 三种样式。
+ 新增：支持通知属性 priority 和 category 。
+ 新增：支持对通知栏添加 Actions 。
+ 修复一些用户反馈的 bug 。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.0.0.jar。用 jpush-android_v3.0.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore100.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


(注意：要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置组件)

### JPush iOS SDK v3.0.0

#### 更新时间
+ 2016-12-02

#### Change Log
+ 新增：模块化分离为 JCore，JPush 两部分，支持与极光统计 SDK 集成。


#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0及以上版本将不再支持处理器为i386的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC




### JPush iOS SDK v2.2.0

#### 更新时间
+ 2016-10-20

#### Change Log
+ 修复已知bug，运行更稳定。
+ 传输消息加密，信息更安全。
+ 优化版本信息上报、日志打印等，设计更合理。
+ 优化IPv6等网络处理，连接更可靠。


#### 升级提示

+ 建议升级！
+ 注意：添加libresolv.tbd库，否则编译运行会报错（2.2.0及以上版本要求）

#### 升级指南
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC


### JPush Android SDK v2.2.0

#### 更新时间

+ 2016-10-12

#### Change Log

+ 优化改进：sdk 内部 https 访问增加证书认证。
+ 优化改进：富文本页面支持双指缩放。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.2.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjpush220.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


(注意：要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置组件)

### JPush iOS SDK v2.1.9

#### 更新时间
+ 2016-09-07

#### Change Log
+ 新增：全面支持 iOS 10 新特性。
+ 修复bug：增加SDK的稳定性。
+ 优化改进：新增获取registrationID的接口，TagAlias支持设置特殊字符。
+ 优化改进：SDK全部使用HTTPS链接。


#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC




### JPush Android SDK v2.1.9

#### 更新时间

+ 2016-08-26

#### Change Log

+ 提升接入服务的稳定性。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包

+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.1.9.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush219.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


(注意：要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置组件)




### JPush Android SDK v2.1.8

#### 更新时间

+ 2016-08-24

#### Change Log

+ 增加 jcenter 集成方式的支持。
+ 增加 crash log 及时上报的功能。
+ 优化代码结构，大幅缩减jar包大小。
+ 优化富媒体推送的功能。
+ 修复在若干机型上出现的 NegativeArraySizeException 异常。


#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包

+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.1.8.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush218.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


(注意：要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置组件)

### JPush Android SDK v2.1.7

#### 更新时间

+ 2016-06-28

#### Change Log

+ 优化：修复一处空指针问题。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包

+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.1.7.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush217.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


(注意：要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置组件)


### JPush Android SDK v2.1.6

#### 更新时间

+ 2016-06-22

#### Change Log
+ 新增：为tag, alias设置增加特殊字符，包括：@!#$&*+=.|￥
+ 修复：设置静音时间的问题。
+ 优化：debug模式下SDK内部提示的通知图标。
+ 优化：处理一些可能出现的崩溃现象。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包

+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.1.6.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush216.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


(注意：要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置组件)



### JPush iOS SDK v2.1.8

#### 更新时间
+ 2016-06-21

#### Change Log

+ 优化IPv6网络下的通信机制。
+ 支持Tag的数量到1000个，但总长度不能超过7000字节。
+ 统计上报升级为https上报。
+ 优化增加SDK稳定性。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC




### JPush iOS SDK v2.1.7

#### 更新时间
+ 2016-05-26

#### Change Log

+ 新增：对IPv6网络的支持。
+ 优化改进：改善用户备份 app，还原到新设备 RegistrationID 不变的问题。
+ 修复：SDK 存在的偶然崩溃问题。
+ 优化改进：使用页面时长统计信息。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC





### JPush Android SDK v2.1.5

#### 更新时间

+ 2016-05-06

#### Change Log
+ 修复: 用API推送 通知＋自定义消息一起的消息在2.1.3版本上仅收到通知的问题。
+ 修复: 在极端情况下 Tag/alias 清理后设置不成功的问题。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包

+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.1.5.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush215.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


(注意：要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置组件)


### JPush iOS SDK v2.1.6

#### 更新时间
+ 2016-04-13

#### Change Log


+ 修复: 2.1.5版本在模拟器调试运行报错的问题。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC




### JPush iOS SDK v2.1.5

#### 更新时间
+ 2016-04-07

#### Change Log

+ 功能增加: 增加 IDFA（广告标识符）设置接口。开发者可通过上传IDFA值增加统计准确性。极光SDK不包含主动调用获取IDFA的代码。
+ 优化改进: 修复 SDK 偶然崩溃的问题，增强健壮性。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC




### JPush Android SDK v2.1.3

#### 更新时间
+ 2016-04-07

#### Change Log
+ 新增:富媒体popwin和landingPage模版。
+ 优化:在android 6.0中已弃掉aorg.apache.http 的引入，现在将http相关代码修改为httpUrlconnection 的google推荐模式。
+ 优化:crash log 上报。
+ 修复:在Android 5.0 以上系统通知栏图标显示不出来的问题，定制图标需替换文件drawable-hdpi/jpush_notification_icon，或使用定制通知栏的接口。
+ 修复:小红伞扫描报错的问题。
+ 修复:一些可能导致崩溃的异常。

#### 升级提示

+ 建议升级

#### 升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.1.3.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush213.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。


### JPush Android SDK v2.1.0

#### 更新时间
+ 2016-03-04

#### Change Log
+ 新增：对 Android 6.0 的支持(注意:如果是compileSdkVersion 23上编译,请在build.gradle的android中加入 useLibrary 'org.apache.http.legacy',用来支持apache的http类);
+ 新增：Android 6.0 请求权限接口:JPushInterface.requestPermission(Activity context),开发者可以在自己的Activity页面调用此接口,请求权限包括{"android.permission.READ_PHONE_STATE","android.permission.WRITE_EXTERNAL_STORAGE","android.permission.READ_EXTERNAL_STORAGE","android.permission.ACCESS_FINE_LOCATION"}.
+ 修复：setPushTime接口的bug。
+ 修复：setLatestNotificationNumber接口的bug。
+ 修复：分离进程导致的部分数据读写异常。
+ 修复：一些测试平台上报的crash。
+ 修复：由.so库导致的异常不使应用崩溃，用Log提示开发者。
+ 优化：设备唯一性判断策略。
+ 优化：网络状态适配。
+ 优化：日志输出。

#### 升级提示

+ 强烈建议升级，适配Android 6.0

#### 升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.1.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush210.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件id。





### JPush Android SDK v2.0.6

#### 更新时间
+ 2016-01-15

#### Change Log
+ 新功能：支持新的富媒体模版。
+ 修复bug：设置别名/标签相关的 bug。
+ 修复bug：在 2.3.x 系统上构建通知的 bug。
+ 优化：优化 init, sis,接入 流程的日志。
+ 优化：处于静默时间,禁止推送时间的提示日志。


#### 升级提示

+ 建议升级！

#### 升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.0.6.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush206.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
官网默认压缩包仅提供了arm架构的.so文件，如要支持x86和mips架构，请到官网“资源下载”页面下载对应版本。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。
请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。
但注意请不要修改所有的文件名，和布局文件中的组件id。

### JPush iOS SDK v2.1.0

#### 更新时间
+ 2016-01-12

#### Change Log

主要对 iOS 9 适配支持。

+ 功能增加: 增加bitcode支持
+ 优化改进: Demo 增加 iPhone 6 和 6plus 支持
+ 优化改进：APService 变更为 JPUSHService
+ 功能增加：增加appKey和channel通过代码初始化API
+ 优化改进: 优化网路差环境DNS解析超时时间过长
+ 优化改进: 修复注册时没有获取到RegistrationID的bug
+ 优化改进: 静态库文件名由"libPushSDK-x.x.x.a"变更为"jpush-ios-x.x.x.a"

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的.a和.h文件,重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：iOS 7 Background Remote Notification
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC






### JPush Android SDK v2.0.5

#### 更新时间
+ 2015-11-06

#### Change Log
+ 新功能：支持将PushService 配置成独立的进程
+ FixBug：解决有些设备的富媒体推送界面actionBar横向不能铺满的问题
+ FIxBug：解决富媒体页面点击返回可能造成的崩溃问题
+ 优化：重构富媒体推送相关代码
+ zip包中的demo工程支持AndroidStudio和Eclipse,有各自对应的AndroidManifest配置


#### 升级提示

+ 建议升级！

#### 升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-2.0.5.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。
用对应CPU文件夹下的 libjpush205.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
官网默认压缩包仅提供了arm架构的.so文件，如要支持x86和mips架构，请到官网“资源下载”页面下载对应版本。

+ 更新AndroidManifest.xml
	+ 压缩包根目录下有针对Eclipse和AndroidStudio 两种开发平台准备的两个AndroidManifest文件。
请对照示例更新跟JPush相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包res中的资源放到项目的对应文件夹，并按照示例AndroidManifest配置PushActivity组件

+ 添加资源文件
	+ 将res文件夹下的资源文件，添加到您项目res/下对应的文件夹中。
根据您应用的界面风格，您可以修改layout文件的配色，字体等属性，或者修改drawable文件夹下的图标。
但注意请不要修改所有的文件名，和布局文件中的组件id。




### JPush iOS SDK v1.8.8

#### 更新时间
+ 2015-10-27

#### Change Log
+ 功能修正：修复了1.8.7在开启bitcode时,archive编译失败的问题

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件
+ 删除项目里旧的 .a 文件，重新导入新的 .a 文件（特别留意）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：iOS 7 Background Remote Notification
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC

### JPush iOS SDK v1.8.7

#### 更新时间
2015-10-20

#### Change Log
+ 功能改进：增加对 iOS 9 新特性 bitcode 的支持

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件
+ 删除项目里旧的 .a 文件，重新导入新的 .a 文件（特别留意）
+ Xcode7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：iOS 7 Background Remote Notification
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC

### JPush Android SDK v1.8.2

#### 更新时间

+ 2015-09-30

#### Change Log
+ 修复Bug：修复从 171 以下版本升级到高版本后可能出现无法连接 JPush 的问题。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush182.so ，同时删除原来各老版本的 so 包。
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush182.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush182.so 到你项目的 libs/mips/ 目录下。






### JPush Android SDK v1.8.1

#### 更新时间

+ 2015-09-07

#### Change Log
+ 优化改进：防止由于未添加富媒体页面的布局文件而导致的打开富媒体页面崩溃。

#### 升级提示

+ 建议升级！
+ 建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush181.so ，同时删除原来各老版本的 so 包。
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush181.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush181.so 到你项目的 libs/mips/ 目录下。



### JPush iOS SDK v1.8.5

#### 更新时间
2015-07-30

#### Change Log
+ 修复Bug：解决与第三方库冲突引起的编译出错.

#### 升级提示

+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


### JPush Android SDK v1.8.0

#### 更新时间

+ 2015-07-27

#### Change Log
+ 新增特性：支持集成了新版本 JPush SDK 的应用间进程拉起
+ 优化改进：优化富媒体模板展示效果准备。（更多功能待web后台更新后可以使用）

#### 升级提示

+ 建议升级！
+ 建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush180.so ，同时删除原来各老版本的 so 包。
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush180.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush180.so 到你项目的 libs/mips/ 目录下。



### JPush iOS SDK v1.8.4

#### 更新时间
2015-07-17

#### Change Log
+ 优化改进：改进域名劫持导致的无法登陆服务器

#### 升级提示

+ 可选升级！

#### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。

### JPush Android SDK v1.7.5

#### 更新时间

+ 2015-06-16

#### Change Log
+ 优化改进：优化注册逻辑，防止双卡手机重复注册。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush175.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush175.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush175.so 到你项目的 libs/mips/ 目录下。


### JPush Android SDK v1.7.4

#### 更新时间
+ 2015-05-11

#### Change Log
+ 新增功能：支持64bit CPU, 提供arm,x86,mips平台对应64位CPU的.so文件。
+ 优化改进：优化代码防止出现TransactionTooLargeException。
+ 优化改进：优化对本地数据库的操作代码。
+ 优化改进：catch AssertionError ，避免framework层的网络接口错误。
+ 优化改进：添加 API setLatestNotificationNum 的客户端打印。
+ 优化改进：Manifest中appKey填写为非Android平台的appKey时提示相应信息。
+ 修复bug：修复创建应用设置仅有iOS版本的应用时重复尝试注册。
+ 修复bug：修复appKey填写为null时会发起注册的问题。
+ 修复bug：特殊操作导致设置保留通知条数失效。
+ 修复bug：本地通知重复弹出。
+ 修复bug：修复由外部应用异常启动JPush内部组件出现的崩溃。
+ 修复bug：修复上报代码，防止出现ConcurrentModificationException。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush174.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush174.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush174.so 到你项目的 libs/mips/ 目录下。







### JPush iOS SDK v1.8.3

#### 更新时间
2015-03-25

#### Change Log
+ Bug修复：修复少数情况下 cpu 升至100%的问题
+ Bug修复：有极低几率写入文件 Crash
+ 优化改进：正式弃用 OpenUDID 接口

#### 升级提示

可选升级！

#### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


### JPush Android SDK v1.7.3

#### 更新时间
+ 2015-02-09

#### Change Log
+ 修复漏洞：修复代码中使用 webview 可能出现的安全问题
+ 修复 bug：修复之前的版本升级到 172，可能会出现 registration id 改变的问题

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush173.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush173.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush173.so 到你项目的 libs/mips/ 目录下。

### JPush Android SDK v1.7.2

#### 更新时间
+ 2015-01-16

#### Change Log
+ 优化改进：Android SDK 改进 SIS 多地址重试策略
+ 优化改进：Android SDK 支持更多备选接入 IP
+ 优化改进：优化 socket连接的策略
+ 优化改进：优化 DNS 域名解析
+ 修复 bug：修改 Android SDK 发起注册所需检查的条件

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush172.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush172.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush172.so 到你项目的 libs/mips/ 目录下。


### JPush iOS SDK v1.8.2 

#### 更新时间
2014-12-11

#### Change Log
+ 优化改进：修复一些可能引起崩溃问题
+ 优化改进：修复部分情况下获取不到 RegistrationID 的问题

#### 升级提示

建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。

### JPush Android SDK v1.7.1

#### 更新时间
2014-12-03

#### Change Log
+ 优化改进：内部协议由 32 位的升级为 64 位
+ 优化改进：优化 demo 的日志打印内容
+ 修复bug：在使用 TabActivity 的时候，不管是否集成了统计代码，都会提示没有集成的问题
+ 修复bug：修正由于配置文件中没有 MainActivity 或者 LAUNCHER 导致的空指针异常
+ 修复bug：支持推送自定义消息内容为空
+ 修复bug：修改提供设置最大通知条数的接口名
+ 修复bug：为 JS 调用的 java 代码添加 @JavascriptInterface 注解


#### 升级提示

建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush171.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush171.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush171.so 到你项目的 libs/mips/ 目录下。


###  JPush Android SDK v1.7.0

#### 更新时间 
2014-09-25

####Change Log

+ 优化改进：根据服务器时间优化统计信息时间准确性 
+ 修复bug：在集成统计分析的时候，调用onPause or onResume的时候，如果传入getApplicationContext() 会崩溃的问题
+ 修复bug： 设置tags , tags长度大于998报6008的问题

####升级提示

建议升级！

####升级指南

+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush170.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush170.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush170.so 到你项目的 libs/mips/ 目录下。


###  JPush iOS SDK v1.8.1

#### 更新时间 
2014-09-23

####Change Log

+ 优化改进：修改与部分第三方 SDK 变量冲突问题
+ 优化改进：修复 iOS5 版本 Demo 按钮异常
####升级提示

建议升级。

####升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


###  JPush iOS SDK v1.8.0 

#### 更新时间 
2014-09-19

####Change Log

+ 新增功能：增加 iOS8 支持
+ 新增功能：增加本地推送 API
+ 新增功能：增加地理位置信息上报
+ 新增功能：增加崩溃日志上报
+ 新增功能：增加日志等级修改
+ 优化改进：修改上报重试机制
+ 优化改进：修复 setTagAlias 时回调类被释放时崩溃bug
+ 优化改进：全新的参考 Demo

####升级提示

建议升级。

####升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


###  JPush Android SDK v1.6.4 

#### 更新时间 
2014-08-27

####Change Log

+ 新增功能：支持 Push v3 API 同时推送通知与自定义消息，接收后广播给 App；
+ 新增功能：本地通知API。通过API可定制一条本地通知，到点触发客户端通知；
+ 修复BUG：点击富媒体通知未上报统计数据问题；
+ 修复BUG：修复 r1.6.3 版本存在的心跳问题；

####升级提示

建议升级！

####升级指南

+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush164.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush164.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush164.so 到你项目的 libs/mips/ 目录下。


###  JPush WinPhone SDK v1.0.2 


#### 更新时间 
2014-08-14

####Change Log

+ 优化改进：Setup接口的获取RegistrationID的委托没有被调用
+ 优化改进：SDK cpu使用率过高，导致cocos2d-x for wp卡顿
+ 优化改进：SDK 使用更合理的策略，进一步降低对UI线程的影响
+ 优化改进：网络类型为NetworkUnkown时，SDK也可正常工作
+ 优化改进：优化统计代码

####升级提示
建议升级！

####升级指南

+ 新加入库：JPushSDK-v1.0.2.dll ，同时删除老版本的dll


###  JPush iOS SDK v1.7.4 

#### 更新时间 
2014-08-06

####Change Log
新增功能：增加设置 badge 值更新到 JPush 服务器功能。
此 SDK 版本配合服务器端推送通知 badge +1 功能使用，实现群推 iOS 通知时 badge 值各用户不同的值。
升级提示
建议升级。

升级指南
替换 lib 文件夹里的文件 .a 文件为新版本；
替换 lib 文件夹里的文件 .h 文件为新版本；
工程添加libz.dylib、Security.framework两个库；
新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


###  JPush Android SDK v1.6.3 

#### 更新时间
2014-07-01

####Change Log

+ 优化改进：提高JPush service 启动速度。
+ 优化改进：提供接口检查 JPush 连接状态。

####升级提示

建议升级！

####升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush163.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计消息API](../client/android_api/#api_2)
在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。


###  JPush iOS SDK v1.7.3 

#### 更新时间
2014-07-24

####Change Log

+ 优化改进：配合 API V3，更好的支持自定义消息的解析。

####升级提示

建议升级。

####升级指南
+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。

###  JPush iOS SDK v1.7.2 

#### 更新时间
2014-11-07

##### Change Log

+ 新增特性：新增对arm64架构的支持。
+ 优化改进：全面优化SDK架构，后台运行时会保持短时间网络连接。
+ 优化改进：将专门针对 simulator 的 x86 架构库统合并为一个文件，方便管理。

##### 升级提示
+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

##### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)


###  JPush iOS SDK v1.7.1 

#### 更新时间
2014-07-24

##### Change Log

+ 修复BUG：修复 target->general 页面的 version 为空会导致 crash 的问题；
+ 修复BUG：修复开发者打包静态库包含 JPush iOS SDK 并且 XCode 为 5.0 版本时，会出现编译错误的问题。

##### 升级提示

可选升级。

##### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。
  
###  JPush WinPhone SDK v1.0.0

####更新时间
2014-07-24

JPush 对 Windows Phone 推送的支持，与对 iOS 推送的支持类似，主要的功能是： 

+ 代理向官方推送通道 MPNs 推送通知；
+ 统一推送接口；
+ 推送统计等。

与 JPush 对 iOS 平台的推送稍有不同的是，Windows Phone 推送暂时未支持应用内推送，只有通知 toast。

上线的功能包括：

+ JPush WinPhone SDK 1.0.0 版本供 App 集成；
+ 控制台上设置应用支持 Windows Phone；
+ 控制台上对 Windows Phone 设备推送通知；
+ API 调用对 Windows Phone 设备推送通知；


###  JPush iOS SDK v1.7.0 

####更新时间
2014-09-17

#####Change Log

+ 新增功能：支持 RegistrationID 推送；
+ 新增功能：增加页面统计上报；
+ 修复BUG：修复上个版本在特定情况下崩溃的BUG。

##### 升级提示

建议升级

#####升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。



###  JPush Android SDK v1.6.1 

#### 更新时间
2014-03-09

####Change Log

+ 优化改进：stopPush 会彻底地停止 Push Service，并且不再响应 Receiver；
+ 优化改进：只在 Main Activity 未添加统计代码时才在通知栏提示。

#### 升级提示

建议升级！

####升级指南

1. 新加入 .jar 包：libs/jpush-sdk-release1.6.1.jar ，同时删除原来各老版本的 jar 包。
2. 新加入 .so 包：libs/armeabi/libjpush.so ，同时删除原来各老版本的 so 包。
3. 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [Andorid API](../client/android_api)
4. 在 AndroidManifest.xml 增加权限 `<uses-permission android:name="android.permission.WRITE_SETTINGS" />`
5. 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
6. 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
7. 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。

###  JPush Android SDK v1.6.0 

#### 更新时间
2014-02-25

#### Change Log
1. 新增功能：增加统计分析 API。
2. 新增功能：新增获取 RegistrationID 的方法。服务器端 Push API 可根据此 RegistrationID 来精确地点对点推送。

#### 升级提示
建议升级！

#### 升级指南

1. 新加入 .jar 包：libs/jpush-sdk-release1.6.0.jar ，同时删除原来各老版本的 jar 包。
2. 新加入 .so 包：libs/armeabi/libjpush.so ，同时删除原来各老版本的 so 包。
3. 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档[Andorid API](../client/android_api)
4. 在 AndroidManifest.xml 增加权限 `<uses-permission android:name="android.permission.WRITE_SETTINGS" />`
5. 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
6. 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
7. 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。

###  JPush iOS SDK v1.6.3 

#### 更新时间
2014-07-01

#### Change Log

+ 优化改进：bug fix

#### 升级提示

+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 



###  JPush Android SDK v1.5.6 

#### 更新时间
2014-01-03

#### Change Log

+ 优化改进：调整 SDK 网络策略，适应不稳定的网络互通环境

#### 升级提示

建议升级！

#### 升级指南

+ 新加入 .jar 包：libs/jpush-sdk-release1.5.6.jar ，同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush.so ，同时删除原来各老版本的 so 包。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。
+ 如果是从较早的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。


###  JPush iOS SDK v1.6.2 

#### 更新时间
2014-01-15

#### Change Log

+ 优化改进：调整 SDK 网络策略，适应不稳定的网络互通环境

#### 升级提示

+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 



###  JPush iOS SDK v1.6.0 

#### 更新时间
2014-02-25

#### Change Log

+ 新增特性：新增对arm64架构的支持。
+ 优化改进：全面优化SDK架构，后台运行时会保持短时间网络连接。
+ 优化改进：将专门针对 simulator 的 x86 架构库统合并为一个文件，方便管理。

#### 升级提示
+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client/ios_tutorials/#ios-7-background-remote-notification)


# 最近更新

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




### JMessage Android SDK v1.0.18

#### 更新时间
2015-04-01

#### Change Log
+ JMesssage Android SDK 首次发布
+ 聊天支持：单聊，群聊
+ 聊天内容：文本，图片，语音对讲
+ 提供用户管理 ，群组管理功能

#### 升级提示

可选升级！

#### 升级指南

+ 打开后请按照AndroidManifest的提示替换您的包名和APPKey；
+ 全局替换："import cn.jpush.im.android.demo.R;" 替换为 "import 您的包名.R;"
+ 如果是Android Studio用户注意检查 build.gradle 中的 applicationId 与你的包名一致


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


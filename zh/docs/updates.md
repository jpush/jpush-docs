# 最近更新

> 本页面持续发布极光推送各方面的更新信息，敬请持续关注！
> 
> Android SDK 最新版本下载：[Android](../resouces)
> 
> iOS SDK 最新版本下载：[iOS](../resouces)
> 
> WinPhone SDK 最新版本下载：[Windows Phone](../resouces)


## JPush iOS SDK v1.7.2 版本发布

### Change Log

+ 新增特性：新增对arm64架构的支持。
+ 优化改进：全面优化SDK架构，后台运行时会保持短时间网络连接。
+ 优化改进：将专门针对 simulator 的 x86 架构库统合并为一个文件，方便管理。

### 升级提示
+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../client_sdks/ios_tutorials)


## JPush iOS SDK v1.7.1 版本发布

### Change Log

+ 修复BUG：修复 target->general 页面的 version 为空会导致 crash 的问题；
+ 修复BUG：修复开发者打包静态库包含 JPush iOS SDK 并且 XCode 为 5.0 版本时，会出现编译错误的问题。

### 升级提示

+ 可选升级。

### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。
  
## JPush WinPhone 推送上线

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


## JPush iOS SDK v1.7.0 版本发布

###Change Log

+ 新增功能：支持 RegistrationID 推送；
+ 新增功能：增加页面统计上报；
+ 修复BUG：修复上个版本在特定情况下崩溃的BUG。

### 升级提示

建议升级

###升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 工程添加libz.dylib、Security.framework两个库
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。



## JPush Android SDK r1.6.1 发布

###Change Log

+ 优化改进：stopPush 会彻底地停止 Push Service，并且不再响应 Receiver；
+ 优化改进：只在 Main Activity 未添加统计代码时才在通知栏提示。

### 升级提示

建议升级！

###升级指南

1. 新加入 .jar 包：libs/jpush-sdk-release1.6.1.jar ，同时删除原来各老版本的 jar 包。
2. 新加入 .so 包：libs/armeabi/libjpush.so ，同时删除原来各老版本的 so 包。
3. 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [Andorid API](../clinet_sdks/android_api)
4. 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
5. 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
6. 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
7. 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。

## JPush Android SDK r1.6.0 发布

### Change Log
1. 新增功能：增加统计分析 API。
2. 新增功能：新增获取 RegistrationID 的方法。服务器端 Push API 可根据此 RegistrationID 来精确地点对点推送。
### 升级提示
建议升级！

### 升级指南

1. 新加入 .jar 包：libs/jpush-sdk-release1.6.0.jar ，同时删除原来各老版本的 jar 包。
2. 新加入 .so 包：libs/armeabi/libjpush.so ，同时删除原来各老版本的 so 包。
3. 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档[Andorid API](../clinet_sdks/android_api)
4. 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
5. 如果是从早期的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
6. 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
7. 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。

## JPush iOS SDK r1.6.3 版本发布

### Change Log

+ 优化改进：bug fix
### 升级提示

+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../clinet_sdks/ios_tutorials)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 



## JPush Android SDK r1.5.6 发布

### Change Log

+ 优化改进：调整 SDK 网络策略，适应不稳定的网络互通环境

### 升级提示

建议升级！

### 升级指南

+ 新加入 .jar 包：libs/jpush-sdk-release1.5.6.jar ，同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush.so ，同时删除原来各老版本的 so 包。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。
+ 如果是从较早的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。


## JPush iOS SDK r1.6.2 版本发布

### Change Log

+ 优化改进：调整 SDK 网络策略，适应不稳定的网络互通环境

### 升级提示

+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../clinet_sdks/ios_tutorials)
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 



## JPush iOS SDK r1.6.0 版本发布

### Change Log
+ 新增特性：新增对arm64架构的支持。
+ 优化改进：全面优化SDK架构，后台运行时会保持短时间网络连接。
+ 优化改进：将专门针对 simulator 的 x86 架构库统合并为一个文件，方便管理。

### 升级提示
+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 如果是1.2.7及之前版本升级 请在Build Settings里面，找到Other Linker Flags，去掉-all_load, -ObjC 
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](../clinet_sdks/ios_tutorials)


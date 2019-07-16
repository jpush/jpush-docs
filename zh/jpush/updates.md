# 最近更新

### JPush Android SDK v3.3.4

#### 更新时间

+ 2019-07-16

#### Change Log
+ 支持用户推送时自定义通知channel
+ 优化demo
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.3.4.jar 和 jcore-android-2.1.0.jar及以上版本 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcorexxx.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush iOS SDK v3.2.1

#### 更新时间
+ 2019-06-11

#### Change Log
+ 地理围栏新增回调及删除功能
+ 修复已知bug


#### 升级提示

+ 建议升级！

#### 升级指南
+ 3.2.1 版本的 JPush 只支持 2.0.0 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 注意 3.0.0 及以上版本 JPush SDK 将不再支持处理器为 i386 的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC
+ 使用地理围栏功能时涉及以下相关配置：
	- 位置权限配置。
	- 选择Background Modes配置。 target -> capabilities ->Background Modes 选中Location updates。
	- 注意registerLbsGeofenceDelegate: withLaunchOptions 方法最好在sdk初始化之前调用。


### JPush Android SDK v3.3.2

#### 更新时间

+ 2019-06-06

#### Change Log
+ 地理围栏新增回调及删除功能
+ 优化自定义消息、通知消息单进程回调方式
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.3.2.jar 和 jcore-android-2.0.1.jar及以上版本 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcorexxx.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush Android SDK v3.3.1

#### 更新时间

+ 2019-05-22

#### Change Log
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.3.1.jar 和 jcore-android-2.0.1.jar及以上版本 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcorexxx.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush Android SDK v3.3.0

#### 更新时间

+ 2019-05-16

#### Change Log
+ 长连接接入优化
+ 事件回调方式修改
+ AndroidManifest.xml新增组件配置
+ 适配Android Q
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.3.0.jar 和 jcore-android-2.0.1.jar及以上版本 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcorexxx.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush iOS SDK v3.2.0

#### 更新时间
+ 2019-04-28

#### Change Log
+ 根据JCore 2.0进行JPush重构，性能优化
+ JCore 要求版本在2.0以上
+ 删除了setupWithOption:launchingOption 初始化接口，不再支持pushConfig.plist方式集成
+ 优化消息状态上报逻辑
+ 修复已知bug


#### 升级提示

+ 建议升级！

#### 升级指南
+ 3.2.0 版本的 JPush 只支持 2.0.0 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.1.2 版本的 JPush 只支持 1.2.6 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.1.1 版本的 JPush 只支持 1.2.3 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.0.7 版本开始压缩包中 Lib 新增了 Notification Service Extension SDK ，可用于统计通知送达，开发者请注意添加到 Libs 中，使用方式见集成指南。
+ 注意 3.0.0 及以上版本 JPush SDK 将不再支持处理器为 i386 的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC
+ 使用地理围栏功能时涉及以下相关配置：
	- 位置权限配置。
	- 选择Background Modes配置。 target -> capabilities ->Background Modes 选中Location updates。
	- 注意registerLbsGeofenceDelegate: withLaunchOptions 方法最好在sdk初始化之前调用。
	- Info.plist file 文件中加入 NSLocationAlwaysUsageDescription 这个字段的描述，避免上架AppStore被拒


### JPush Android SDK v3.2.0

#### 更新时间

+ 2019-03-07

#### Change Log
+ 自定义通知布局增加设置时间
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.2.0.jar 和 jcore-android-1.2.7.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcorexxx.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。




### JPush iOS SDK v3.1.2

#### 更新时间
+ 2018-12-18

#### Change Log
+ 新增地理围栏功能


#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。
+ 需要在Info.plist file文件中加入 NSLocationAlwaysUsageDescription 这个字段的描述，避免上架被拒

#### 升级指南
+ 3.1.2 版本的 JPush 只支持 1.2.6 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.1.1 版本的 JPush 只支持 1.2.3 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.0.7 版本开始压缩包中 Lib 新增了 Notification Service Extension SDK ，可用于统计通知送达，开发者请注意添加到 Libs 中，使用方式见集成指南。
+ 注意 3.0.0 及以上版本 JPush SDK 将不再支持处理器为 i386 的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC
+ 使用地理围栏功能时涉及以下相关配置：
	- 位置权限配置。
	- 选择Background Modes配置。 target -> capabilities ->Background Modes 选中Location updates。
	- 注意registerLbsGeofenceDelegate: withLaunchOptions 方法最好在sdk初始化之前调用。
	- Info.plist file 文件中加入 NSLocationAlwaysUsageDescription 这个字段的描述，避免上架AppStore被拒


### JPush Android SDK v3.1.8

#### 更新时间

+ 2018-12-18

#### Change Log
+ 新增地理围栏功能
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.1.8.jar 和 jcore-android-1.2.6.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore126.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush Android SDK v3.1.7

#### 更新时间

+ 2018-11-06

#### Change Log
+ 支持自定义大图标功能
+ 支持点击通知栏跳转指定页面
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.1.7.jar 和 jcore-android-1.2.6.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore126.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。



### JPush iOS SDK v3.1.1

#### 更新时间
+ 2018-10-17

#### Change Log
+ 适配 iOS12 通知新特性
+ 修复 bug




#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 3.1.1 版本的 JPush 只支持 1.2.3 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.0.7 版本开始压缩包中 Lib 新增了 Notification Service Extension SDK ，可用于统计通知送达，开发者请注意添加到 Libs 中，使用方式见集成指南。
+ 注意 3.0.0 及以上版本 JPush SDK 将不再支持处理器为 i386 的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

### JPush Android SDK v3.1.6

#### 更新时间

+ 2018-09-10

#### Change Log
+ 增加通道共享功能
+ 修复已知问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.1.6.jar 和 jcore-android-1.2.5.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore125.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
	+ 老用户升级，请注意 3.0.9 版本之后新增了 ContentProvider 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。

### JPush Android SDK v3.1.5

#### 更新时间

+ 2018-07-20

#### Change Log
+ 支持接口设置 channel
+ 调整震动权限为可选权限，去掉 wakelock 权限检测.
+ 设置 tagalias 与设置手机号码增加 6026 错误码
+ 修改 targetversion 大于 21 时在 7.0 及以上手机上通知不显示时间的问题

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.1.5.jar 和 jcore-android-1.2.3.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore123.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
	+ 老用户升级，请注意 3.0.9 版本之后新增了 ContentProvider 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush iOS SDK v3.1.0

#### 更新时间
+ 2018-07-18

#### Change Log
+ 修改本地通知部分设置问题
+ 修复设置手机号码回调问题
+ 修复 tag 相关异常问题

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 3.1.0 版本的 JPush 只支持 1.1.9 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.0.7 版本开始压缩包中 Lib 新增了 Notification Service Extension SDK ，可用于统计通知送达，开发者请注意添加到 Libs 中，使用方式见集成指南。
+ 注意 3.0.0 及以上版本 JPush SDK 将不再支持处理器为 i386 的模拟器。
+ 添加libresolv.tbd库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

### JPush Android SDK v3.1.3

#### 更新时间

+ 2018-05-17

#### Change Log
+ 优化 SDK 加载过程.
+ 修复已知问题.

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.1.3.jar 和 jcore-android-1.2.1.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore121.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
	+ 老用户升级，请注意 3.0.9 版本之后新增了 ContentProvider 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush Android SDK v3.1.2

#### 更新时间

+ 2018-04-11

#### Change Log
+ 修复清理本地通知失败的 bug；
+ 修复 Android 8.0 + 设备上的若干崩溃情况；
+ 用户活跃上报的逻辑优化；

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。用 jpush-android-3.1.2.jar 和 jcore-android-1.2.0.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应CPU文件夹下的 libjcore120.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的so文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
	+ 老用户升级，请注意 3.0.9 版本之后新增了 ContentProvider 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目res/下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。


### JPush iOS SDK v3.0.9

#### 更新时间
+ 2018-04-08

#### Change Log
+ 使用 iOS 自定义消息不必再依赖 APNs Token 注册成功；
+ 将 iOS 自定义消息的 message id 回调给开发者；

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 3.0.9 版本的 JPush 只支持 1.1.9 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.0.7 版本开始压缩包中 Lib 新增了 Notification Service Extension SDK ，可用于统计通知送达，开发者请注意添加到 Libs 中，使用方式见集成指南。
+ 注意 3.0.0及以上版本 JPush SDK 将不再支持处理器为i386的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

### JPush iOS SDK v3.0.8

#### 更新时间
+ 2018-01-11

#### Change Log
+ SDK 端新增绑定手机号的 api 用于短信补充功能；
+ 在 Service Extension 中增加日志开关；
+ 修复若干已知问题；

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 3.0.8 版本的 JPush 只支持 1.1.7 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.0.7 版本开始压缩包中 Lib 新增了 Notification Service Extension SDK ，可用于统计通知送达，开发者请注意添加到 Libs 中，使用方式见集成指南。
+ 注意 3.0.0 及以上版本 JPush SDK 将不再支持处理器为i386的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

### JPush Android SDK v3.1.1

#### 更新时间

+ 2018-01-09

#### Change Log
+ SDK 端新增绑定手机号的 api 用于短信补充功能；
+ 将 DaemonService 组件从 JPush 模块移入 JCore 模块；
+ 优化 JPush 接入服务；
+ 修复若干已知 bugs；

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.1.1.jar 和 jcore-android-1.1.9.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应CPU文件夹下的 libjcore119.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在SDK下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
	+ 老用户升级，请注意 3.0.9 版本之后新增了 ContentProvider 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加 JPush 相关组件和资源，详细说明请参考官方集成指南。

### JPush Android SDK v3.1.0

#### 更新时间

+ 2017-11-17

#### Change Log
+ 优化进程间通信机制；
+ 优化维持长连接的心跳机制；
+ 代码结构调整以缩减动态库文件的大小；
+ 修复开发者反馈的问题；

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.1.0.jar 和 jcore-android-1.1.8.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore118.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在SDK下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
	+ 老用户升级，请注意 3.0.9 版本之后新增了 ContentProvider 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JPush iOS SDK v3.0.7

#### 更新时间
+ 2017-10-12

#### Change Log
+ 新增 iOS Extension sdk ，用来统计通知的送达情况
+ 优化 sdk 内部代码

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 3.0.7 版本的 JPush 只支持 1.1.6 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 3.0.7 版本开始压缩包中 Lib 新增了 Notification Service Extension SDK ，可用于统计通知送达，开发者请注意添加到 Libs 中，使用方式见集成指南。
+ 注意 3.0.0 及以上版本 JPush SDK 将不再支持处理器为i386的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

### JPush Android SDK v3.0.9

#### 更新时间

+ 2017-09-25

#### Change Log
+ 新增 ContentProvider 组件用于数据同步.
+ 优化 SDK 在 Android 8.0 上的兼容性.
+ 修复开发者反馈的问题.

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-3.0.9.jar 和 jcore-android-1.1.7.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore117.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新 JPush 相关的组件属性，Permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
	+ 老用户升级，请注意 3.0.9 版本新增了 ContentProvider 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。
    + Android 5.0 以上，使用应用图标做通知 icon 可能显示异常，请参考 res/drawable-xxxx/jpush_notification_icon 作为专门的通知 icon。
详细请见 Android SDK 集成指南中的说明，或者 example 中的示例。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JPush Android SDK v3.0.8

#### 更新时间

+ 2017-07-26

#### Change Log
+ 修复：若干开发者反馈的 bug

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。添加 jcore-android-1.1.6.jar。用 jpush-android-3.0.8.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore116.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JPush Android SDK v3.0.7

#### 更新时间

+ 2017-07-10

#### Change Log
+ 新增：一套 tag/alias 操作接口
+ 优化：tag/alias 设置超时的问题
+ 修复：若干开发者反馈的 bug

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。添加jcore-android_v1.1.5.jar。用 jpush-android_v3.0.7.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore115.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。


### JPush iOS SDK v3.0.6

#### 更新时间
+ 2017-07-03

#### Change Log
+ Tag 接口变动，建议使用新的增删改查接口
+ 优化连接协议，提高连接速度及稳定性

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 3.0.6 版本的 JPush 只支持 1.1.5 及以上的 JCore 版本，升级 SDK 的时候请将 JCore 一起升级。
+ 注意 3.0.0及以上版本将不再支持处理器为 i386 的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC


### JPush Android SDK v3.0.6

#### 更新时间

+ 2017-05-08

#### Change Log
+ 优化：数据存储性能
+ 优化：提升 sdk 安全性
+ 新增：设置 tag/alias 增加错误码 6013（时间轴错误）

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。添加 jcore-android_v1.1.3.jar。用 jpush-android_v3.0.6.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore113.so 文件，替换项目中原有的 libjpushXXX.so文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件。

+ 添加资源文件 
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JPush Android SDK v3.0.5

#### 更新时间

+ 2017-04-14

#### Change Log
+ 优化存储性能
+ 提升 sdk 稳定性

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。添加 jcore-android_v1.1.2.jar。用 jpush-android_v3.0.5.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore112.so 文件，替换项目中原有的 libjpushXXX.so文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。



### JPush iOS SDK v3.0.5

#### 更新时间
+ 2017-04-14

#### Change Log
+ 修改 Bug，提高与其他 SDK 兼容稳定性

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0 及以上版本将不再支持处理器为 i386 的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC



### JPush iOS SDK v3.0.3

#### 更新时间
+ 2017-04-01

#### Change Log
+ 优化：socket connect 机制
+ 修复：SDK HTTP 上报偶然崩溃的问题，增强健壮性

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0 及以上版本将不再支持处理器为 i386 的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和. h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h ）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

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
	+ 打开 libs 文件夹。添加 jcore-android_v1.1.1.jar。用 jpush-android_v3.0.3.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore111.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新跟 JPush 相关的组件属性，permission，Action等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。



### JPush iOS SDK v3.0.2

#### 更新时间
+ 2017-02-13

#### Change Log
+ 修复：DNS 解析失败带来的崩溃问题，提升稳定性 

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0 及以上版本将不再支持处理器为 i386 的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC


### JPush iOS SDK v3.0.1

#### 更新时间
+ 2017-01-09

#### Change Log
+ 修复：已知bug。
+ 优化：运行性能。 

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0 及以上版本将不再支持处理器为 i386 的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的.a和.h文件，重新导入新的.a和.h文件（注意新版本替换APService.h为JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC



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
	+ 打开 libs 文件夹。添加 jcore-android_v1.1.0.jar。用 jpush-android_v3.0.1.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore110.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件。

+ 添加资源文件
    + 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。

+ 如果使用 jcenter 的方式集成 JPush，不需要添加相关组件和资源，详细说明请参考官方集成指南。



### JPush Android SDK v3.0.0

#### 更新时间

+ 2016-12-02

#### Change Log
+ 新增：模块化分离为 JCore，JPush 两部分集成，原有使用的一个 jar 包，分为了 jcore 和 jpush 两个 jar 包。
+ 新增：消息通道加密。
+ 新增：支持原生 Android 的大文本，大图片，inbox 三种样式。
+ 新增：支持通知属性 priority 和 category 。
+ 新增：支持对通知栏添加 Actions 。
+ 修复一些用户反馈的 bug 。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。添加 jcore-android_v1.0.0.jar。用 jpush-android_v3.0.0.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore100.so 文件，替换项目中原有的 libjpushXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请对照示例 AndroidManifest 更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件。

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。


(注意：要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置组件)

### JPush iOS SDK v3.0.0

#### 更新时间
+ 2016-12-02

#### Change Log
+ 新增：模块化分离为 JCore，JPush 两部分，支持与极光统计 SDK 集成。


#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。
+ 极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+ N 种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

#### 升级指南
+ 注意 3.0.0 及以上版本将不再支持处理器为i386的模拟器。
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC




### JPush iOS SDK v2.2.0

#### 更新时间
+ 2016-10-20

#### Change Log
+ 修复已知 bug，运行更稳定。
+ 传输消息加密，信息更安全。
+ 优化版本信息上报、日志打印等，设计更合理。
+ 优化 IPv6 等网络处理，连接更可靠。


#### 升级提示

+ 建议升级！
+ 注意：添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）

#### 升级指南
+ 添加 libresolv.tbd 库，否则编译运行会报错（2.2.0 及以上版本要求）
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC


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
	+ 打开 libs 文件夹。用 jpush-android-2.2.0.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjpush220.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。


(注意：要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置组件)

### JPush iOS SDK v2.1.9

#### 更新时间
+ 2016-09-07

#### Change Log
+ 新增：全面支持 iOS 10 新特性。
+ 修复 bug：增加 SDK 的稳定性。
+ 优化改进：新增获取 registrationID 的接口，TagAlias 支持设置特殊字符。
+ 优化改进：SDK 全部使用 HTTPS 链接。


#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC




### JPush Android SDK v2.1.9

#### 更新时间

+ 2016-08-26

#### Change Log

+ 提升接入服务的稳定性。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.1.9.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush219.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。


(注意：要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置组件)




### JPush Android SDK v2.1.8

#### 更新时间

+ 2016-08-24

#### Change Log

+ 增加 jcenter 集成方式的支持。
+ 增加 crash log 及时上报的功能。
+ 优化代码结构，大幅缩减 jar 包大小。
+ 优化富媒体推送的功能。
+ 修复在若干机型上出现的 NegativeArraySizeException 异常。


#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.1.8.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush218.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。


(注意：要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置组件)

### JPush Android SDK v2.1.7

#### 更新时间

+ 2016-06-28

#### Change Log

+ 优化：修复一处空指针问题。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.1.7.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush217.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。


(注意：要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置组件)


### JPush Android SDK v2.1.6

#### 更新时间

+ 2016-06-22

#### Change Log
+ 新增：为 tag, alias 设置增加特殊字符，包括：@!#$&*+=.|￥
+ 修复：设置静音时间的问题。
+ 优化：debug 模式下 SDK 内部提示的通知图标。
+ 优化：处理一些可能出现的崩溃现象。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.1.6.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush216.so文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。


(注意：要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置组件)



### JPush iOS SDK v2.1.8

#### 更新时间
+ 2016-06-21

#### Change Log

+ 优化 IPv6 网络下的通信机制。
+ 支持 Tag 的数量到 1000 个，但总长度不能超过 7000 字节。
+ 统计上报升级为 https 上报。
+ 优化增加 SDK 稳定性。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC




### JPush iOS SDK v2.1.7

#### 更新时间
+ 2016-05-26

#### Change Log

+ 新增：对 IPv6 网络的支持。
+ 优化改进：改善用户备份 app，还原到新设备 RegistrationID 不变的问题。
+ 修复：SDK 存在的偶然崩溃问题。
+ 优化改进：使用页面时长统计信息。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC





### JPush Android SDK v2.1.5

#### 更新时间

+ 2016-05-06

#### Change Log
+ 修复：用 API 推送 通知＋自定义消息一起的消息在 2.1.3 版本上仅收到通知的问题。
+ 修复：在极端情况下 Tag/alias 清理后设置不成功的问题。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.1.5.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush215.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。


(注意：要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置组件)


### JPush iOS SDK v2.1.6

#### 更新时间
+ 2016-04-13

#### Change Log


+ 修复: 2.1.5 版本在模拟器调试运行报错的问题。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件:先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC





### JPush iOS SDK v2.1.5

#### 更新时间
+ 2016-04-07

#### Change Log

+ 功能增加：增加 IDFA（广告标识符）设置接口。开发者可通过上传 IDFA 值增加统计准确性。极光SDK不包含主动调用获取 IDFA 的代码。
+ 优化改进：修复 SDK 偶然崩溃的问题，增强健壮性。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC





### JPush Android SDK v2.1.3

#### 更新时间
+ 2016-04-07

#### Change Log
+ 新增：富媒体 popwin 和 landingPage 模版。
+ 优化：在 android 6.0 中已弃掉 aorg.apache.http 的引入，现在将 http 相关代码修改为 httpUrlconnection 的 google 推荐模式。
+ 优化：crash log 上报。
+ 修复：在 Android 5.0 以上系统通知栏图标显示不出来的问题，定制图标需替换文件 drawable-hdpi/jpush_notification_icon，或使用定制通知栏的接口。
+ 修复：小红伞扫描报错的问题。
+ 修复：一些可能导致崩溃的异常。

#### 升级提示

+ 建议升级

#### 升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.1.3.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush215.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。



### JPush Android SDK v2.1.0

#### 更新时间
+ 2016-03-04

#### Change Log
+ 新增：对 Android 6.0 的支持(注意：如果是 compileSdkVersion 23 上编译，请在 build.gradle 的 android 中加入 useLibrary 'org.apache.http.legacy'，用来支持 apache 的 http 类);
+ 新增：Android 6.0 请求权限接口：JPushInterface.requestPermission(Activity context)，开发者可以在自己的 Activity 页面调用此接口，请求权限包括： 

	{"android.permission.READ_PHONE_STATE",
	"android.permission.WRITE_EXTERNAL_STORAGE",
	"android.permission.READ_EXTERNAL_STORAGE",
	"android.permission.ACCESS_FINE_LOCATION"}.

+ 修复：setPushTime 接口的 bug。
+ 修复：setLatestNotificationNumber 接口的 bug。
+ 修复：分离进程导致的部分数据读写异常。
+ 修复：一些测试平台上报的 crash。
+ 修复：由 .so 库导致的异常不使应用崩溃，用 Log 提示开发者。
+ 优化：设备唯一性判断策略。
+ 优化：网络状态适配。
+ 优化：日志输出。

#### 升级提示

+ 强烈建议升级，适配 Android 6.0

#### 升级指南
+ 首先解压您获取到的 zip 压缩包
+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.1.0.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush210.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。





### JPush Android SDK v2.0.6

#### 更新时间
+ 2016-01-15

#### Change Log
+ 新功能：支持新的富媒体模版。
+ 修复 bug：设置别名/标签相关的 bug。
+ 修复 bug：在 2.3.x 系统上构建通知的 bug。
+ 优化：优化 init，sis，接入流程的日志。
+ 优化：处于静默时间，禁止推送时间的提示日志。


#### 升级提示

+ 建议升级！

#### 升级指南
+ 首先解压您获取到的 zip 压缩包
+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.0.6.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush206.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件。
官网默认压缩包仅提供了 arm 架构的 .so 文件，如要支持 x86 和 mips 架构，请到官网“资源下载”页面下载对应版本。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。

### JPush iOS SDK v2.1.0

#### 更新时间
+ 2016-01-12

#### Change Log

主要对 iOS 9 适配支持。

+ 功能增加：增加 bitcode 支持
+ 优化改进：Demo 增加 iPhone 6 和 6plus 支持
+ 优化改进：APService 变更为 JPUSHService
+ 功能增加：增加 appKey 和 channel 通过代码初始化 API
+ 优化改进：优化网路差环境 DNS 解析超时时间过长
+ 优化改进：修复注册时没有获取到 RegistrationID 的 bug
+ 优化改进：静态库文件名由 "libPushSDK-x.x.x.a" 变更为 "jpush-ios-x.x.x.a"

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件：先删除项目里旧的 .a 和 .h 文件，重新导入新的 .a 和 .h 文件（注意新版本替换 APService.h 为 JPUSHService.h）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC







### JPush Android SDK v2.0.5

#### 更新时间
+ 2015-11-06

#### Change Log
+ 新功能：支持将 PushService 配置成独立的进程
+ FixBug：解决有些设备的富媒体推送界面 actionBar 横向不能铺满的问题
+ FIxBug：解决富媒体页面点击返回可能造成的崩溃问题
+ 优化：重构富媒体推送相关代码
+ zip 包中的 demo 工程支持 AndroidStudio 和 Eclipse，有各自对应的 AndroidManifest 配置


#### 升级提示

+ 建议升级！

#### 升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件
	+ 打开 libs 文件夹。用 jpush-android-2.0.5.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。
用对应 CPU 文件夹下的 libjpush206.so 文件，替换项目中原有的极光 so 文件，并删除原有的极光 so 文件。
官网默认压缩包仅提供了 arm 架构的 .so 文件，如要支持 x86 和 mips 架构，请到官网“资源下载”页面下载对应版本。

+ 更新 AndroidManifest.xml
	+ 压缩包根目录下有针对 Eclipse 和 AndroidStudio 两种开发平台准备的两个 AndroidManifest 文件。请对照示例更新跟 JPush 相关的组件属性，permission，Action 等配置。要使用富媒体推送，请将压缩包 res 中的资源放到项目的对应文件夹，并按照示例 AndroidManifest 配置 PushActivity 组件

+ 添加资源文件
	+ 将 res 文件夹下的资源文件，添加到您项目 res/ 下对应的文件夹中。
根据您应用的界面风格，您可以修改 layout 文件的配色，字体等属性，或者修改 drawable 文件夹下的图标。但注意请不要修改所有的文件名，和布局文件中的组件 id。




### JPush iOS SDK v1.8.8

#### 更新时间
+ 2015-10-27

#### Change Log
+ 功能修正：修复了 1.8.7 在开启 bitcode 时，archive 编译失败的问题

#### 升级提示

+ 建议升级！

#### 升级指南
+ 替换 lib 文件夹里的文件
+ 删除项目里旧的 .a 文件，重新导入新的 .a 文件（特别留意）
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

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
+ Xcode 7 环境下，替换原先导入的 libz.dylib 框架为 libz.tbd （特别留意）
+ 需要删除旧的 libPushSDK-Simulator.a （如果存在）
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC

### JPush Android SDK v1.8.2

#### 更新时间

+ 2015-09-30

#### Change Log
+ 修复 Bug：修复从 171 以下版本升级到高版本后可能出现无法连接 JPush 的问题。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush182.so ，同时删除原来各老版本的 so 包。
+ 由于富媒体的展示需求，SDK 中增加一个 res 文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush182.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush182.so 到你项目的 libs/mips/ 目录下。






### JPush Android SDK v1.8.1

#### 更新时间

+ 2015-09-07

#### Change Log
+ 优化改进：防止由于未添加富媒体页面的布局文件而导致的打开富媒体页面崩溃。

#### 升级提示

+ 建议升级！
+ 建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置
+ 由于富媒体的展示需求，SDK 中增加一个 res 文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush181.so ，同时删除原来各老版本的 so 包。
+ 由于富媒体的展示需求，SDK 中增加一个 res 文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush181.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush181.so 到你项目的 libs/mips/ 目录下。



### JPush iOS SDK v1.8.5

#### 更新时间
2015-07-30

#### Change Log
+ 修复 Bug：解决与第三方库冲突引起的编译出错.

#### 升级提示

+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加 libz.dylib、Security.framework 两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


### JPush Android SDK v1.8.0

#### 更新时间

+ 2015-07-27

#### Change Log
+ 新增特性：支持集成了新版本 JPush SDK 的应用间进程拉起
+ 优化改进：优化富媒体模板展示效果准备。（更多功能待 web 后台更新后可以使用）

#### 升级提示

+ 建议升级！
+ 建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置
+ 由于富媒体的展示需求，SDK 中增加一个 res 文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush180.so ，同时删除原来各老版本的 so 包。
+ 由于富媒体的展示需求，SDK 中增加一个 res 文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
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
+ 工程添加 libz.dylib、Security.framework 两个库；
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
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush175.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush175.so 到你项目的 libs/mips/ 目录下。


### JPush Android SDK v1.7.4

#### 更新时间
+ 2015-05-11

#### Change Log
+ 新增功能：支持 64bit CPU, 提供 arm,x86,mips 平台对应 64 位 CPU 的 .so 文件。
+ 优化改进：优化代码防止出现 TransactionTooLargeException。
+ 优化改进：优化对本地数据库的操作代码。
+ 优化改进：catch AssertionError ，避免 framework 层的网络接口错误。
+ 优化改进：添加 API setLatestNotificationNum 的客户端打印。
+ 优化改进：Manifest 中 appKey 填写为非 Android 平台的 appKey 时提示相应信息。
+ 修复 bug：修复创建应用设置仅有 iOS 版本的应用时重复尝试注册。
+ 修复 bug：修复 appKey 填写为 null 时会发起注册的问题。
+ 修复 bug：特殊操作导致设置保留通知条数失效。
+ 修复 bug：本地通知重复弹出。
+ 修复 bug：修复由外部应用异常启动 JPush 内部组件出现的崩溃。
+ 修复 bug：修复上报代码，防止出现 ConcurrentModificationException。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush174.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush174.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush174.so 到你项目的 libs/mips/ 目录下。







### JPush iOS SDK v1.8.3

#### 更新时间
2015-03-25

#### Change Log
+ Bug 修复：修复少数情况下 cpu 升至 100% 的问题
+ Bug 修复：有极低几率写入文件 Crash
+ 优化改进：正式弃用 OpenUDID 接口

#### 升级提示

可选升级！

#### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加 libz.dylib、Security.framework 两个库；
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
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
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
+ 优化改进：优化 socket 连接的策略
+ 优化改进：优化 DNS 域名解析
+ 修复 bug：修改 Android SDK 发起注册所需检查的条件

#### 升级提示

+ 建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush172.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
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
+ 工程添加 libz.dylib、Security.framework 两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。

### JPush Android SDK v1.7.1

#### 更新时间
2014-12-03

#### Change Log
+ 优化改进：内部协议由 32 位的升级为 64 位
+ 优化改进：优化 demo 的日志打印内容
+ 修复 bug：在使用 TabActivity 的时候，不管是否集成了统计代码，都会提示没有集成的问题
+ 修复 bug：修正由于配置文件中没有 MainActivity 或者 LAUNCHER 导致的空指针异常
+ 修复 bug：支持推送自定义消息内容为空
+ 修复 bug：修改提供设置最大通知条数的接口名
+ 修复 bug：为 JS 调用的 java 代码添加 @JavascriptInterface 注解


#### 升级提示

建议升级！

#### 升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush171.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush171.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush171.so 到你项目的 libs/mips/ 目录下。


###  JPush Android SDK v1.7.0

#### 更新时间 
2014-09-25

####Change Log

+ 优化改进：根据服务器时间优化统计信息时间准确性 
+ 修复 bug：在集成统计分析的时候，调用 onPause or onResume的时候，如果传入 getApplicationContext() 会崩溃的问题
+ 修复 bug： 设置 tags，tags 长度大于 998 报 6008 的问题

####升级提示

建议升级！

####升级指南

+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush170.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush170.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush170.so 到你项目的 libs/mips/ 目录下。


###  JPush iOS SDK v1.8.1

#### 更新时间 
2014-09-23

####Change Log

+ 优化改进：修改与部分第三方 SDK 变量冲突问题
+ 优化改进：修复 iOS 5 版本 Demo 按钮异常
####升级提示

建议升级。

####升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加 libz.dylib、Security.framework 两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


###  JPush iOS SDK v1.8.0 

#### 更新时间 
2014-09-19

####Change Log

+ 新增功能：增加 iOS 8 支持
+ 新增功能：增加本地推送 API
+ 新增功能：增加地理位置信息上报
+ 新增功能：增加崩溃日志上报
+ 新增功能：增加日志等级修改
+ 优化改进：修改上报重试机制
+ 优化改进：修复 setTagAlias 时回调类被释放时崩溃 bug
+ 优化改进：全新的参考 Demo

####升级提示

建议升级。

####升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 替换 lib 文件夹里的文件 .h 文件为新版本；
+ 工程添加 libz.dylib、Security.framework 两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


###  JPush Android SDK v1.6.4 

#### 更新时间 
2014-08-27

####Change Log

+ 新增功能：支持 Push v3 API 同时推送通知与自定义消息，接收后广播给 App；
+ 新增功能：本地通知 API。通过 API 可定制一条本地通知，到点触发客户端通知；
+ 修复 BUG：点击富媒体通知未上报统计数据问题；
+ 修复 BUG：修复 r1.6.3 版本存在的心跳问题；

####升级提示

建议升级！

####升级指南

+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush164.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
+ 在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
+ 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush164.so 到你项目的 libs/x86/ 目录下。
+ 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush164.so 到你项目的 libs/mips/ 目录下。


###  JPush WinPhone SDK v1.0.2 


#### 更新时间 
2014-08-14

####Change Log

+ 优化改进：Setup 接口的获取 RegistrationID 的委托没有被调用
+ 优化改进：SDK cpu 使用率过高，导致 cocos2d-x for wp 卡顿
+ 优化改进：SDK 使用更合理的策略，进一步降低对 UI 线程的影响
+ 优化改进：网络类型为 NetworkUnkown时，SDK 也可正常工作
+ 优化改进：优化统计代码

####升级提示
建议升级！

####升级指南

+ 新加入库：JPushSDK-v1.0.2.dll ，同时删除老版本的 dll


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
工程添加 libz.dylib、Security.framework 两个库；
新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。


###  JPush Android SDK v1.6.3 

#### 更新时间
2014-07-01

####Change Log

+ 优化改进：提高 JPush service 启动速度。
+ 优化改进：提供接口检查 JPush 连接状态。

####升级提示

建议升级！

####升级指南
+ 新加入 .jar 包：同时删除原来各老版本的 jar 包。
+ 新加入 .so 包：libs/armeabi/libjpush163.so ，同时删除原来各老版本的 so 包。
+ 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
在 AndroidManifest.xml 增加权限 <uses-permission android:name="android.permission.WRITE_SETTINGS" />。
+ 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
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
+ 工程添加 libz.dylib、Security.framework 两个库；
+ 新版本不再需要 libPushSDK-Simulator.a 。如果你的老版本 SDK 包含此文件，请删除。

###  JPush iOS SDK v1.7.2 

#### 更新时间
2014-11-07

##### Change Log

+ 新增特性：新增对 arm64 架构的支持。
+ 优化改进：全面优化 SDK 架构，后台运行时会保持短时间网络连接。
+ 优化改进：将专门针对 simulator 的 x86 架构库统合并为一个文件，方便管理。

##### 升级提示
+ 本SDK支持 iOS 5.0 及以上版本
+ 建议升级！

##### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC 
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)


###  JPush iOS SDK v1.7.1 

#### 更新时间
2014-07-24

##### Change Log

+ 修复 BUG：修复 target->general 页面的 version 为空会导致 crash 的问题；
+ 修复 BUG：修复开发者打包静态库包含 JPush iOS SDK 并且 XCode 为 5.0 版本时，会出现编译错误的问题。

##### 升级提示

可选升级。

##### 升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 工程添加 libz.dylib、Security.framework 两个库；
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
+ 修复 BUG：修复上个版本在特定情况下崩溃的 BUG。

##### 升级提示

建议升级

#####升级指南

+ 替换 lib 文件夹里的文件 .a 文件为新版本；
+ 工程添加 libz.dylib、Security.framework 两个库
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
3. 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
4. 在 AndroidManifest.xml 增加权限 `<uses-permission android:name="android.permission.WRITE_SETTINGS" />`
5. 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
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
3. 如果使用的老版本统计的 API activityStarted/activityStopped, 请使用最新的 API onResume/onPause 替换，参考文档 [统计分析 API](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)
4. 在 AndroidManifest.xml 增加权限 `<uses-permission android:name="android.permission.WRITE_SETTINGS" />`
5. 如果是从早期的版本升级过来，建议参考 SDK 下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
6. 如果要支持 x86 CPU 的机型，请下载单独的 x86 JPush SDK 压缩包，解压缩后复制 libs/x86/libjpush.so 到你项目的 libs/x86/ 目录下。
7. 如果要支持 mips CPU 的机型，请下载单独的 mips JPush SDK 压缩包，解压缩后复制 libs/mips/libjpush.so 到你项目的 libs/mips/ 目录下。

###  JPush iOS SDK v1.6.3 

#### 更新时间
2014-07-01

#### Change Log

+ 优化改进：bug fix

#### 升级提示

+ 本 SDK 支持 iOS 5.0 及以上版本
+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC 



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

+ 本 SDK 支持 iOS 5.0 及以上版本
+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC 



###  JPush iOS SDK v1.6.0 

#### 更新时间
2014-02-25

#### Change Log

+ 新增特性：新增对 arm64 架构的支持。
+ 优化改进：全面优化 SDK 架构，后台运行时会保持短时间网络连接。
+ 优化改进：将专门针对 simulator 的 x86 架构库统合并为一个文件，方便管理。

#### 升级提示
+ 本 SDK 支持 iOS 5.0 及以上版本
+ 建议升级！

#### 升级指南

+ 替换 lib 文件夹里的文件
+ 需要删除旧的 libPushSDK-Simulator.a
+ 如果是 1.2.7 及之前版本升级 请在 Build Settings 里面，找到 Other Linker Flags，去掉 -all_load, -ObjC 
+ 关于 iOS 7 Background Push，JPush 提供一个教程文档：[iOS 7 Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification)


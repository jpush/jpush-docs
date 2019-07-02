# 最近更新
### JAnalytics Android SDK v2.1.0

#### 更新时间

+ 2019-07-02

#### Change Log 
+ 优化动态圈选埋点功能，新增支持Dialog、Popmenu控件圈选。
+ 修复一些已知的问题。

#### 升级提示

+ 如果想使用动态圈选功能，必须升级。
+ 在使用动态圈选功能时，如遇到问题，欢迎随时反馈。
+ 升级后若不想启动态圈选功能，请移除动态圈选插件的依赖：apply plugin: 'cn.jiguang.android.analytics'。

#### 手动集成升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。
打开libs文件夹。
用janalytics-android-x.y.z.jar 替换项目中原有的极光统计sdk的jar文件，并删除原有极光统计sdk的jar文件。
用jcore-android-x.y.z.jar 替换项目中原有的极光jcore的jar文件，并删除原有极光jcore的jar文件。
用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 更新AndroidManifest.xml。
可根据压缩包根目录下的AndroidManifest文件（或集成指南），更新统计sdk所需权限、及相关组件等。

```
  注意:如同一个应用集成了多个极光SDK，只需配置一次appkey与channel。
``` 

+ 配置动态圈选插件
参考【集成指南】的【本地工程配置】部分进行配置。

#### Jcenter方式集成升级指南
如果使用jcenter的方式集成JAnalytics，请参考官方【集成指南】的【JCenter 自动集成方式】部分。




### JAnalytics Web SDK v1.0.0

#### 更新时间

+ 2019-06-25

#### Change Log 
+ 支持自定义事件。
+ 用户行为数据上报。
+ 位置数据可选上报。

#### 升级提示

+ 我是第一版！

#### 升级指南

+ 首先解压您获取到的zip压缩包；
+ 导入 SDK 开发包：janalytics-web-1.x.x.js；
详细请见JAnalytics Web SDK 集成指南中的说明，或者 example 中的示例。




### JAnalytics MiniProgram SDK v1.0.0

#### 更新时间

+ 2019-04-17

#### Change Log 
+ 微信小程序平台的数据统计，目前支持自定义事件。

#### 升级提示

+ 我是第一版！

#### 升级指南

+ 首先解压您获取到的zip压缩包；
+ 导入 SDK 开发包：janalytics-m-1.x.x.js；
+ 导入SDK analysis 配置文件: janalytics-conf.js，并根据注释配置。详细请见JAnalytics MiniProgram SDK 集成指南中的说明，或者example中的示例。



### JAnalytics Android SDK v2.0.0

#### 更新时间

+ 2019-02-14

#### Change Log 
+ 新增动态圈选埋点功能(Beta版)。
+ 修复一些已知问题。

#### 升级提示

+ 如果想使用动态圈选功能，必须升级。
+ 动态圈选功能尚处于Beta版，如遇到问题欢迎反馈帮助改进。
+ 升级后若不想启动态圈选功能，请移除动态圈选插件的依赖：apply plugin: 'cn.jiguang.android.analytics'。

#### 手动集成升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。
打开libs文件夹。
用janalytics-android-2.x.y.jar 替换项目中原有的极光统计sdk的jar文件，并删除原有极光统计sdk的jar文件。
用jcore-android-1.x.y.jar 替换项目中原有的极光jcore的jar文件，并删除原有极光jcore的jar文件。
用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 更新AndroidManifest.xml。
可根据压缩包根目录下的AndroidManifest文件（或集成指南），更新统计sdk所需权限、及相关组件等。

```
  注意:如同一个应用集成了多个极光SDK，只需配置一次appkey与channel。
``` 

+ 配置动态圈选插件
参考【集成指南】的【本地工程配置】部分进行配置。

#### Jcenter方式集成升级指南
如果使用jcenter的方式集成JAnalytics，请参考官方【集成指南】的【JCenter 自动集成方式】部分。


### JAnalytics iOS SDK v2.0.0

#### 更新时间

+ 2019-02-14

#### Change Log 
+ 支持动态圈选(Beta版)，以及圈选数据统计上报。
+ 修改已知问题。

#### 升级提示

+ 建议升级！
+ 动态圈选功能尚处于Beta版，如遇到问题欢迎反馈帮助改进。

#### 升级指南

+ 需要集成JCore1.1.8及以上版本，否则编译运行会报错。


### JAnalytics QuickApp SDK v1.1.0

#### 更新时间

+ 2018-11-07

#### Change Log 
+ 修复已知问题。
+ 增加deviceInfo和locInfo上报。
+ 新增账户维度统计。


#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件，打开libs文件夹。用janalytics-quickapp-sdk_1.x.x.js 替换项目中原有的极光统计sdk的js文件，并删除原有极光统计sdk的js文件。
+ 详细请见JAnalytics QuickApp SDK 集成指南中的说明，或者example中的示例。首先解压您获取到的zip压缩包。

### JAnalytics Android SDK v1.2.2

#### 更新时间

+ 2018-09-19

#### Change Log 
+ 增加setChannel接口，允许开发者动态配置channel。
+ 修复已知问题。


#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。 打开libs文件夹。 用janalytics-android-v1.x.x.jar 替换项目中原有的极光统计sdk的jar文件，并删除原有极光统计sdk的jar文件。 用jcoe-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件，并删除原有极光jcore的jar文件。 用对应CPU文件夹下的 libjcore1xx.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 更新AndroidManifest.xml。 压缩包根目录下有AndroidManifest文件，里面配有统计sdk需要的权限。 请对照示例更新跟JAnalytics相关的组件属性，permission 等配置。 注:其中极光所有的android sdk使用同一个key与channel。详细请见JAnalytics Android SDK 集成指南中的说明，或者example中的示例。
+ 如果使用jcenter的方式集成JAnalytics，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JAnalytics QuickApp SDK v1.0.0

#### 更新时间

+ 2018-08-10

#### Change Log 
+ QuickApp 平台统计SDK。


#### 升级提示

+ 我是第一版！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件，打开libs文件夹。用janalytics-quickapp-sdk_1.x.x.js 替换项目中原有的极光统计sdk的js文件，并删除原有极光统计sdk的js文件。
+ 详细请见JAnalytics QuickApp SDK 集成指南中的说明，或者example中的示例。首先解压您获取到的zip压缩包。


### JAnalytics Android SDK v1.2.1

#### 更新时间

+ 2018-04-12

#### Change Log 
+ 新增即时上报功能，默认及时上报，通过API可关闭该功能或调整上报频率。
+ 内部策略优化，调用identify_account和detach_account时，如未成功初始化SDK自动触发初始化方法然后继续执行对应API功能。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。
打开libs文件夹。
用janalytics-android-v1.x.x.jar 替换项目中原有的极光统计sdk的jar文件，并删除原有极光统计sdk的jar文件。
用jcoe-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件，并删除原有极光jcore的jar文件。
用对应CPU文件夹下的 libjcore1xx.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 更新AndroidManifest.xml。
压缩包根目录下有AndroidManifest文件，里面配有统计sdk需要的权限。
请对照示例更新跟JAnalytics相关的组件属性，permission 等配置。
注:其中极光所有的android sdk使用同一个key与channel。详细请见JAnalytics Android SDK 集成指南中的说明，或者example中的示例。
+ 如果使用jcenter的方式集成JAnalytics，不需要添加相关组件和资源，详细说明请参考官方集成指南。


### JAnalytics iOS SDK v1.2.1

#### 更新时间

+ 2018-03-12

#### Change Log 
+ 新增即时上报功能，默认及时上报，通过API可关闭该功能或调整上报频率。
+ 内部策略优化，调用identify_account和detach_account时，如未成功初始化SDK自动触发初始化方法然后继续执行对应API功能。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。


### JAnalytics iOS SDK v1.2.0

#### 更新时间

+ 2018-01-15

#### Change Log 
+ 增加用户维度绑定/解绑功能。
+ 增加定时上报功能。
+ 优化内部逻辑。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。



### JAnalytics Android SDK v1.2.0

#### 更新时间

+ 2018-01-15

#### Change Log 
+ 新增统计维度-账号，用户可以登记账号信息、解除关联信息。
+ 新增统计频率设置，用户可以设定统计数据的自动上报周期。
+ 修复一些已知问题。

#### 升级提示

+ 建议升级！


#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。
打开libs文件夹。
用janalytics-android-v1.x.x.jar 替换项目中原有的极光统计sdk的jar文件，并删除原有极光统计sdk的jar文件。
用jcoe-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件，并删除原有极光jcore的jar文件。
用对应CPU文件夹下的 libjcore1xx.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 更新AndroidManifest.xml。
压缩包根目录下有AndroidManifest文件，里面配有统计sdk需要的权限。
请对照示例更新跟JAnalytics相关的组件属性，permission 等配置。
注:其中极光所有的android sdk使用同一个key与channel。详细请见JAnalytics Android SDK 集成指南中的说明，或者example中的示例。
+ 如果使用jcenter的方式集成JAnalytics，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JAnalytics Android SDK v1.1.2

#### 更新时间

+ 2017-07-26

#### Change Log 
+ 修复一些用户反馈的 bug。
+ 修复一些已知问题。
+ 不再提供集成指南.pdf文档，改用README.txt。

#### 升级提示

+ 建议升级！


#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。
打开libs文件夹。
用janalytics-android-v1.x.x.jar 替换项目中原有的极光统计sdk的jar文件，并删除原有极光统计sdk的jar文件。
用jcoe-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件，并删除原有极光jcore的jar文件。
用对应CPU文件夹下的 libjcore1xx.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 更新AndroidManifest.xml。
压缩包根目录下有AndroidManifest文件，里面配有统计sdk需要的权限。
请对照示例更新跟JAnalytics相关的组件属性，permission 等配置。
注:其中极光所有的android sdk使用同一个key与channel
详细请见JAnalytics Android SDK 集成指南中的说明，或者example中的示例。
+ 如果使用jcenter的方式集成JAnalytics，不需要添加相关组件和资源，详细说明请参考官方集成指南。


### JAnalytics iOS SDK v1.1.3

#### 更新时间

+ 2017-07-05

#### Change Log 
+ 修复了几个统计时会影响数据采集的bug。
+ 将原来的pdf文档更换为README。
+ 优化了sdk结构。

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。


#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。



### JAnalytics Android SDK v1.1.1

#### 更新时间

+ 2017-04-21

#### Change Log 
+ 修复一些用户反馈的BUG。
+ 修复一些已知问题。
+ 增加CrashLog上报的开关接口：initCrashHandler(开启上报)和stopCrashHandler(停止上报)。

#### 升级提示

+ 建议升级！


#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。
打开libs文件夹。
用janalytics-android-v1.x.x.jar 替换项目中原有的极光统计sdk的jar文件，并删除原有极光统计sdk的jar文件。
用jcoe-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件，并删除原有极光jcore的jar文件。
用对应CPU文件夹下的 libjcore1xx.so文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 更新AndroidManifest.xml。
压缩包根目录下有AndroidManifest文件，里面配有统计sdk需要的权限。
请对照示例更新跟JAnalytics相关的组件属性，permission 等配置。
注:其中极光所有的android sdk使用同一个key与channel
详细请见JAnalytics Android SDK 集成指南中的说明，或者example中的示例。
+ 如果使用jcenter的方式集成JAnalytics，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JAnalytics iOS SDK v1.1.2

#### 更新时间

+ 2017-04-14

#### Change Log 
+ 增加pdf说明文档。
+ 修正一部分日志记录。
+ 修复BUG。
+ 增加统计上报数据。

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。


#### 升级指南
+ 首先解压您获取到的zip压缩包。
+ 更新库文件。


### JAnalytics iOS SDK v1.1.1

#### 更新时间

+ 2017-02-13

#### Change Log
+ 修复：JCore DNS解析失败带来的崩溃问题。

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。


#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。

### JAnalytics Android SDK v1.1.0

#### 更新时间

+ 2017-02-08

#### Change Log

+ 修复用户反馈的 bug.
+ 修复一些已知问题。
 
#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 导入 SDK 开发包
    + 用 janalytics-android-v1.1.0.jar 替换项目中原有的极光统计 sdk 的 jar 文件，并删除原有极光统计 sdk 的 jar 文件。
    + 用 jcoe-android-v1.1.0.jar 替换项目中原有的极光 jcore 的 jar 文件，并删除原有极光 jcore 的 jar 文件。
    + 用对应CPU文件夹下的 libjcore110.so 文件，替换项目中原有的极光so文件，并删除原有的极光so文件。
+ 配置 AndroidManifest.xml
    + 压缩包根目录下有 AndroidManifest 文件，里面配有统计sdk需要的权限。
    + 请对照示例更新跟 JAnalytics 相关的组件属性，permission 等配置。
    + 注：其中极光所有的 android sdk 使用同一个 key 与 channel。
+ 如果使用 jcenter 的方式集成 JAnalytics，不需要添加相关组件和资源，详细说明请参考官方集成指南。

### JAnalytics iOS SDK v1.1.0

#### 更新时间
+ 2017-01-09

#### Change Log
+ 修复：JANALYTICSLaunchConfig 对象中 isProduction 属性的错误。
+ 修复：部分内部bug。
+ 优化：运行性能。

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。


#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。


### JAnalytics iOS SDK v1.0.0

#### 更新时间
+ 2016-12-02

#### Change Log
+ 支持用户活跃，新增用户等基础项统计。
+ 支持应用崩溃信息统计。
+ 支持购买，内容浏览，登录，注册等模版型事件。
+ 支持自定义计算事件和自定义计数事件。
+ 支持页面流统计。

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。


#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 更新库文件。

### JAnalytics Android SDK v1.0.0

#### 更新时间

+ 2016-12-02

#### Change Log
+ 支持用户活跃，新增用户等基础项统计。
+ 支持应用崩溃信息统计。
+ 支持购买，内容浏览，登录，注册等模版型事件。
+ 支持自定义计算事件和自定义计数事件。
+ 支持页面流统计。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的zip压缩包。
+ 导入 SDK 开发包。
+ 配置 AndroidManifest.xml。
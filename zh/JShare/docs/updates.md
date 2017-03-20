# 最近更新
### JAnalytics iOS SDK v1.1.1

#### 更新时间
+ 2017-02-13

#### Change Log
+ 修复：JCore DNS解析失败带来的崩溃问题。

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。


#### 升级指南

+ 首先解压您获取到的zip压缩包
+ 更新库文件

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
+ 修复：JANALYTICSLaunchConfig 对象中 isProduction 属性的错误
+ 修复：部分内部bug
+ 优化：运行性能

#### 升级提示

+ 建议升级！
+ 注意：不支持 Xcode 8.0 以下版本 开启 bitcode。


#### 升级指南

+ 首先解压您获取到的zip压缩包
+ 更新库文件


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

+ 首先解压您获取到的zip压缩包
+ 更新库文件

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

+ 首先解压您获取到的zip压缩包
+ 导入 SDK 开发包
+ 配置 AndroidManifest.xml


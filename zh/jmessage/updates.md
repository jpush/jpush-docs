# 最近更新

### iOS SDK v3.9.1

#### 更新时间
2019-07-19

#### ChangeLog
##### NewFeature
+ 新增崩溃日志上报接口

##### BugFix
+ 优化多线程处理方式
+ 修复已知 bug

#### 升级提示
+ 建议升级！
+ JMessage 从 3.9.0 开始只支持 JCore2.0.0 及以上的版本，升级 SDK 的时候请将 JCore 一起升级。

#### 升级指南
+ 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件


### iOS SDK v3.9.0

#### 更新时间

2019-05-07

#### ChangeLog
##### NewFeature

+ 适配 JCore2.0.0
+ 支持消息发送时自定义未读消息数

#### 升级提示

+ 建议升级！
+ JMessage 从 3.9.0 开始只支持 JCore2.0.0 及以上的版本，升级 SDK 的时候请将 JCore 一起升级。

#### 升级指南
+ 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件


### Android SDK v2.9.0

#### 更新时间
2019-05-06

#### ChangeLog

##### BugFix:
+ 修复聊天室消息发送的一些问题
+ 修复用户反馈的一些其他bug

##### BehaviorChange
+ ***JMessage 从2.9.0版本开始自定义消息默认行为发生变化：默认将展示通知栏和增加会话未读数，请开发者注意***

##### NewFeature
+ 适配JCore2.0.0
+ 支持消息发送时自定义未读消息数

#### 升级提示
+ 建议升级！
+ JMessage从2.9.0开始只支持2.0.0及以上的JCore版本，升级 SDK 的时候请将 JCore 一起升级。

#### 升级指南
+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android-2.0.0.jar。用 jmessage-sdk-android-2.9.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore200.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。
	***注意JCore从2.0.0版本开始原有PushService不再使用，改使用JCommonService，如果项目中使用的JCore是2.0.0之前的版本，集成时需要注意修改manifest中的PushService的配置***
```
 <!-- Since JCore2.0.0 Required SDK核心功能-->
 <!-- 这个Service要继承JCommonService 可参考demo用法-->
 <service android:name="xx.xx.XService"
         android:process=":pushcore">
         <intent-filter>
             <action android:name="cn.jiguang.user.service.action" />
         </intent-filter>
 </service>
```
+ 添加资源文件
    + Android5.0以上，使用应用图标作为通知栏小图标可能显示异常，请参考res/drawable-xxxx/jmessage_notification_icon作为通知栏小图标。详情请见
    Android SDK集成指南中的说明，或者demo中的示例
+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

### iOS SDK v3.8.1

#### 更新时间

2019-04-02

#### ChangeLog

##### BugFix

+ 修改一些已知 bug

#### Feature

+ 新增：取消消息发送接口
+ 新增：取消多媒体消息下载接口
+ 新增：可设置时间的群禁言接口
+ 新增：聊天室禁言功能

#### 升级提示

+ 建议升级

#### 升级指南
+ 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件


### Android SDK v2.8.2

#### 更新时间

2019-03-27

#### ChangeLog

##### BugFix:
+ 修复某些情况下用户信息extras未更新的问题
+ 修复用户反馈的一些其他bug

##### NewFeature
+ 新增“取消消息发送”和“取消消息附件下载”功能
+ 群组和聊天室新增带时间参数的禁言接口，建议使用新的禁言接口

#### 升级提示
+ 建议升级！

#### 升级指南
+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.2.7.jar。用 jmessage-android_v2.8.2.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore127.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。
	***注意JMessage 从2.7.0版本开始新增了provider组件，如果项目中使用的JMessage是2.7.0之前的版本，集成时需要注意manifest中新增的provider组件的配置，  
	新增组件：***
```
<!-- Required since JMessage 2.7.0 SDK 核心功能-->
        <provider
            android:name="cn.jpush.im.android.helpers.ipc.IMProvider"
            android:authorities="您自己的包名.IMProvider"
            android:exported="false" />
```
+ 添加资源文件
    + Android5.0以上，使用应用图标作为通知栏小图标可能显示异常，请参考res/drawable-xxxx/jmessage_notification_icon作为通知栏小图标。详情请见
    Android SDK集成指南中的说明，或者demo中的示例
+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

### Android SDK v2.8.1

#### 更新时间

2019-01-25

#### ChangeLog

##### BugFix:
+ 修复某些情况下导致的会话刷新事件频繁下发的问题
+ 修复某些情况下更新用户信息extras失败的问题
+ 修复用户反馈的一些其他bug

#### 升级提示
+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.2.6.jar。用 jmessage-android_v2.8.1.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore126.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。
	***注意JMessage 从2.7.0版本开始新增了provider组件，如果项目中使用的JMessage是2.7.0之前的版本，集成时需要注意manifest中新增的provider组件的配置，  
	新增组件：***
```
<!-- Required since JMessage 2.7.0 SDK 核心功能-->
        <provider
            android:name="cn.jpush.im.android.helpers.ipc.IMProvider"
            android:authorities="您自己的包名.IMProvider"
            android:exported="false" />
```
+ 添加资源文件
    + Android5.0以上，使用应用图标作为通知栏小图标可能显示异常，请参考res/drawable-xxxx/jmessage_notification_icon作为通知栏小图标。详情请见
    Android SDK集成指南中的说明，或者demo中的示例
+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

### PC SDK V1.2.3

#### 更新时间

- 2019-01-15

#### ChangeLog

##### BugFix:

- 修复反馈的bug

##### NewFeature:

- Windows 新增64位版本SDK
- MacOS 更新至Xcode 10

#### 升级提示

- 建议升级！

#### 升级指南

- 从官网下载SDK包,直接全部替换即可
- 如果使用的NuGet包,可以使用NuGet包管理器直接更新jmessage-cpp


### iOS SDK v3.8.0

#### 更新时间

2019-01-09

#### ChangeLog

##### BugFix

+ 修复用户反馈的一些 bug

##### NewFeature:

+ 新增：群公告
+ 新增：群组黑名单
+ 新增：创建群组时可设置成员上限
+ 新增：聊天室黑名单
+ 新增：聊天室管理员
+ 新增：聊天室管理员变更、黑名单变更事件

#### 升级指南
+ 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
+ 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档


### Android SDK v2.8.0

#### 更新时间

2019-01-02

#### ChangeLog

##### BugFix:
+ 修复用户反馈的一些bug

##### NewFeature:
+ 支持群公告功能
+ 支持群组黑名单功能
+ 支持聊天室管理员功能
+ 支持聊天室黑名单功能

#### 升级提示
+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.2.6.jar。用 jmessage-android_v2.8.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore126.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。
	***注意JMessage 从2.7.0版本开始新增了provider组件，如果项目中使用的JMessage是2.7.0之前的版本，集成时需要注意manifest中新增的provider组件的配置，  
	新增组件：***
```
<!-- Required since JMessage 2.7.0 SDK 核心功能-->
        <provider
            android:name="cn.jpush.im.android.helpers.ipc.IMProvider"
            android:authorities="您自己的包名.IMProvider"
            android:exported="false" />
```
+ 添加资源文件
    + Android5.0以上，使用应用图标作为通知栏小图标可能显示异常，请参考res/drawable-xxxx/jmessage_notification_icon作为通知栏小图标。详情请见
    Android SDK集成指南中的说明，或者demo中的示例
+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)


### Android SDK v2.7.1

#### 更新时间

2018-10-29

#### ChangeLog

##### BugFix:
+ 修复用户反馈的一些bug

##### NewFeature:
+ 支持上层自定义通知栏小图标

#### 升级提示
+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.2.5.jar。用 jmessage-android_v2.7.1.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore125.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。
	***注意JMessage 从2.7.0版本开始新增了provider组件，如果项目中使用的JMessage是2.7.0之前的版本，集成时需要注意manifest中新增的provider组件的配置,
	新增组件：***
```
<!-- Required since JMessage 2.7.0 SDK 核心功能-->
        <provider
            android:name="cn.jpush.im.android.helpers.ipc.IMProvider"
            android:authorities="您自己的包名.IMProvider"
            android:exported="false" />
```
+ 添加资源文件
    + Android5.0以上，使用应用图标作为通知栏小图标可能显示异常，请参考res/drawable-xxxx/jmessage_notification_icon作为通知栏小图标。详情请见
    Android SDK集成指南中的说明，或者demo中的示例
+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

### iOS SDK v3.7.0

#### 更新时间

2018-09-05

#### ChangeLog

##### BugFix

+ 修复用户反馈的一些 bug
+ 修改 iOS 发视频消息 Android 下载缩略图失败

##### NewFeature:

+ 新增：群组成员上限修改通知
+ 新增：群昵称功能
+ 新增：群组成员信息类 [JMSGGroupMemberInfo](./client/jmessage_ios_appledoc_html/Classes/JMSGGroupMemberInfo.html)
+ 新增：获取群成员信息接口 [-(void)memberInfoList:](./client/jmessage_ios_appledoc_html/Classes/JMSGGroup.html#//api/name/memberInfoList:)

#### 升级指南
+ 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
+ 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档


### Android SDK v2.7.0

#### 更新时间

2018-08-30

#### ChangeLog

##### BugFix:
+ 修复用户反馈的一些bug

##### NewFeature:
+ 群组成员信息重构，新增GroupMemberInfo代表群组成员信息，原有获取群成员信息返回UserInfo的接口deprecated,新增接口返回GroupMemberInfo
+ 支持获取入群时间
+ 支持群成员昵称功能

#### 升级提示
+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.2.3.jar。用 jmessage-android_v2.7.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore123.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。
	***注意JMessage 从2.7.0版本开始新增了provider组件，如果项目中使用的JMessage是2.7.0之前的版本，集成时需要注意manifest中新增的provider组件的配置，新增组件：***  
```
<!-- Required since JMessage 2.7.0 SDK 核心功能-->
        <provider
            android:name="cn.jpush.im.android.helpers.ipc.IMProvider"
            android:authorities="您自己的包名.IMProvider"
            android:exported="false" />
```

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)


### JMRTC Android SDK v1.0.2
#### 更新时间

+ 2018-08-24

#### ChangLog
+ 域名更新，老版本将在9月份停用，请开发者尽快更新sdk


#### 集成指南
+ 集成jmessage(需要2.6.0或以上版本)。集成文档见官方[JMessage集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

+ 拷贝jmrtc相关库文件
	+ 打开libs文件夹。拷贝jmrtc-android_v1.0.2.jar以及agora-rtc-sdk.jar。
	+ 拷贝CPU文件夹下的.so 文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 权限声明处增加：
```
	<uses-permission android:name="android.permission.RECORD_AUDIO" />  
	<uses-permission android:name="android.permission.CAMERA" />  
	<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```

+ 如果使用jcenter的方式集成JMRTC，不需要添加相关组件和资源，详细集成说明请参考官方[JMRTC集成指南](https://docs.jiguang.cn/jmessage/client/im_jmrtc_android/)

### JMRTC Android SDK v1.0.1

#### 更新时间

+ 2018-07-27

#### ChangLog

##### Bugfix
+ 修复用户反馈的一些bug

#### 集成指南
+ 集成jmessage(需要2.6.0或以上版本)。集成文档见官方[JMessage集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

+ 拷贝jmrtc相关库文件
	+ 打开libs文件夹。拷贝jmrtc-android_v1.0.1.jar以及agora-rtc-sdk.jar。
	+ 拷贝CPU文件夹下的.so 文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 权限声明处增加：
```
	<uses-permission android:name="android.permission.RECORD_AUDIO" />  
	<uses-permission android:name="android.permission.CAMERA" />  
	<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```

+ 如果使用jcenter的方式集成JMRTC，不需要添加相关组件和资源，详细集成说明请参考官方[JMRTC集成指南](https://docs.jiguang.cn/jmessage/client/im_jmrtc_android/)

### Android SDK v2.6.1

#### 更新时间

2018-07-10

#### ChangeLog

##### BugFix:
+ 修复用户反馈的一些bug

##### NewFeature:
+ 支持批量同意审批事件操作
+ 支持修改群组类型
+ 审批事件中增加获取待审批用户人数的接口
+ 添加群成员接口增加reason
+ 增加群组成员上限调整通知
+ 加人进群事件支持自定义扩展字段
+ Model类提供toJson方法

#### 升级提示
+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.2.1.jar。用 jmessage-android_v2.6.1.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore121.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

### JMRTC iOS SDK v1.0.0

#### 更新时间

2018-07-06

#### ChangeLog

+ JMRTC 首次发布
+ 支持多人实时音视频通话
+ 支持通话中设备控制（切换摄像头、免提模式等）
+ 支持视频输出分辨率设置

#### 升级提示

+ 可选升级

#### 升级指南
+ 集成 JMessage
+ 将新版本的 JMRTC.framework 加到工程中，详细参见官网集成文档

### iOS SDK v3.6.2

#### 更新时间

2018-07-06

#### ChangeLog

##### NewFeature:

+ 支持 JMRTC

#### 升级指南
+ 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
+ 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档


### JMRTC Android SDK v1.0.0

#### 更新时间

2018-06-22

#### ChangeLog

+ JMRTC 首次发布
+ 支持多人实时音视频通话
+ 支持通话中设备控制（切换摄像头、免提模式等）
+ 支持视频输出分辨率设置

#### 升级指示
+ 可选升级！

#### 升级指南

+ 集成jmessage
+ 拷贝jmrtc相关jar和so
	+ 打开libs文件夹。拷贝jmrtc-android_v1.0.0.jar以及agora-rtc-sdk.jar。
	+ 拷贝CPU文件夹下的.so 文件，每种型号的so文件都可以在SDK下载包中找到。
+ 更新AndroidManifest.xml
  权限声明处增加：
```
  <uses-permission android:name="android.permission.RECORD_AUDIO" />
  <uses-permission android:name="android.permission.CAMERA" />
  <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```

### iOS SDK v3.6.1

#### 更新时间

2018-06-04

#### ChangeLog

##### BugFix:

* 修复获取群列表接口返回类型错误的问题

#### 升级提示

+ 建议升级！

#### 升级指南
* 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
* 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档



### iOS SDK v3.6.0

#### 更新时间

2018-05-25

#### ChangeLog

##### BugFix:

* 修复用户反馈的一些 bug

##### NewFeature

* 新增：修改群组类型接口
* 新增：video 视频类型消息
* 新增：批量增加、删除管理员接口
* 新增：公开群添加群成员可填写理由接口
* 新增：批量审批入群申请接口

#### 升级指南
* 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
* 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档

#### 接口变更
因为 swift 版本兼容问题，登录返回设备记录接口修改为:  
`+(void)loginWithUsername:password:devicesInfo:completionHandler:`


### Android SDK v2.6.0

#### 更新时间

+ 2018-05-09

#### ChangeLog

##### BugFix:

+ 修复其他用户反馈的一些bug

##### NewFeature:
+ 新增VideoContent消息类型
+ model类实现序列化
+ 收到dev api更新好友关系事件之后，sdk上抛好友关系变更事件

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.2.0.jar。用 jmessage-android_v2.6.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore120.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。
	***注意JCore 从1.1.7版本开始新增了provider组件，如果项目中使用的JCore是1.1.7之前的版本，集成时需要注意manifest中新增的provider组件的配置***

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)

### PC SDK V1.2.1

#### 更新时间

+ 2018-04-12

#### ChangeLog

##### NewFeature:

+ 全新 PC 端 SDK，同时支持Windows、macOS
+ 同步 Windows v1.2.0 的所有功能

#### 升级提示

+ 建议升级！

#### 升级指南

+ 从官网下载SDK包,直接全部替换即可
+ 如果使用的NuGet包,可以使用NuGet包管理器直接更新


### iOS SDK v3.5.0

#### 更新时间

* 2018-03-01

#### ChangeLog

##### BugFix:

* 修复用户反馈的一些 bug

##### NewFeature

* 设置群组管理员功能
* 解散群组功能
* 移交群主权限功能
* 设备间消息透传功能
* 登录接口返回用户登录设备记录

#### 升级指南
* 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
* 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档

#### 接口变更
+ `-(void)onReceiveNotificationEvent:` 接口细分为 `-(void)onReceiveUserLoginStatusChangeEvent:` 和 `-(void)onReceiveFriendNotificationEvent:`



### Android SDK v2.5.0

#### 更新时间

+ 2018-03-01

#### Change Log
##### BugFix:
+ 修复老版本升级时禁言列表获取不到问题
+ 修复其他用户反馈的一些bug

##### NewFeature:
+ Android O系统适配
+ 新增群组管理员
+ 支持解散群组
+ 支持获取设备登陆记录
+ 支持移交群主权限
+ 支持设备间消息透传

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.9.jar。用 jmessage-android_v2.5.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore119.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。  
	***注意JCore 从1.1.7版本开始新增了provider组件，如果项目中使用的JCore是1.1.7之前的版本，集成时需要注意manifest中新增的provider组件的配置***

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)


### Windows SDK V1.2.0

#### 更新时间

+ 2018-02-02

#### ChangeLog

##### NewFeature:

+ 登录设备历史记录
+ 解散群
+ 设置群管理员
+ 获取公开群列表
+ 转让群主身份
+ 设备间消息透传

#### 升级提示

+ 建议升级！

#### 升级指南

+ 从官网下载SDK包,直接全部替换即可

+ 如果使用的NuGet包,可以使用NuGet包管理器直接更新


### Web SDK v2.6.0

#### 更新时间

+ 2018-01-26

#### Change Log

##### NewFeature:
+ 新增：群组管理员角色
+ 新增：解散群、移交群主功能
+ 新增：设备间消息透传、登录设备记录获取
+ 新增：获取 appkey 下所有公开群

#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的 jmessage-sdk-web.2.6.0.min.js 替换掉老版本的 sdk



### iOS SDK v3.4.1

#### 更新时间

2018-01-03

#### ChangeLog

##### BugFix:

* 修复用户反馈的一些 bug

##### NewFeature

* 新增：获取 AppKey 下所有公开群接口

#### 升级指南
* 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
* 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档




### Android SDK v2.4.1

#### 更新时间

+ 2018-01-02

#### Change Log
##### BugFix:
+ 修复处理离线群成员删除和退出事件时禁言列表未更新问题
+ 提升sdk稳定性

##### NewFeature:
+ 新增获取指定应用下所有公开群组的接口
+ 自定义消息和消息的extras支持获取value为Object类型的数据

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.8.jar。用 jmessage-android_v2.4.1.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore118.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。  
	***注意JCore 从1.1.7版本开始新增了provider组件，如果项目中使用的JCore是1.1.7之前的版本，集成时需要注意manifest中新增的provider组件的配置***

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)



### iOS SDK v3.4.0

#### 更新时间

2017-12-11

#### ChangeLog

##### BugFix:

* 修复用户反馈的一些 bug

##### NewFeature

* 新增：聊天室功能
* 新增：群成员禁言功能
* 新增：公开群组功能，支持申请入群
* 新增：发送文件消息时支持设置文件类型

#### 升级指南
* 使用新版本的JMessage.framework文件替换原工程下的同名旧文件
* 将新版本的JMessage.framework里的JCore link到工程中，详细参见官网集成文档



### Android SDK v2.4.0

#### 更新时间

+ 2017-12-11

#### Change Log
##### BugFix:
+ 修复从数据库中读取conversation时，targetAppkey没有设置导致title和avatar不正确
+ 提升sdk稳定性

##### NewFeature:
+ 新增聊天室功能
+ 新增公开群组类型，支持申请入群
+ 新增群成员禁言功能

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.8.jar。用 jmessage-android_v2.4.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore118.so 文件，替换项目中原有 的libjcoreXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。  
	***注意JCore 从1.1.7版本开始新增了provider组件，如果项目中使用的JCore是1.1.7之前的版本，集成时需要注意manifest中新增的provider组件的配置***

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)



### Windows SDK v1.1.0

#### 更新时间

+ 2017-12-04

#### Change Log

##### NewFeature:
+ 聊天室功能
+ 公开群类型，用户可申请入群
+ 支持群禁言
+ 消息透传
+ 提供NuGet程序包
+ 添加 GroupId 类型,代替int64_t , 使用GroupId::get 获取值

#### 升级提示

+ 建议升级！

#### 升级指南

+ 查阅最新的[SDK文档](https://docs.jiguang.cn/jmessage/client/im_win_api_docs/)



### Web SDK v2.5.0

#### 更新时间

+ 2017-11-29

#### Change Log

##### NewFeature:
+ 新增聊天室功能
+ 新增公开群类型，用户可申请入群
+ 支持群禁言

#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的 jmessage-sdk-web.2.5.0.min.js 替换掉老版本的 sdk





### Web SDK v2.4.1

#### 更新时间

+ 2017-11-02

#### Change Log

##### BugFix:

+ 未读数逻辑优化

#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的 jmessage-sdk-web.2.4.1.min.js 替换掉老版本的 sdk


### iOS SDK v3.3.0

#### 更新时间

2017-10-27

#### ChangeLog

##### BugFix:

* 修复用户反馈的一些 bug

##### NewFeature

* 支持多端同时在线
* 支持群组头像
* 支持消息透传
* 新增消息已读回执功能
* 新增消息转发接口
* JMSGConversation 类新增 extras 扩展字段
* JMSGUser 类新增 extras 扩展字段
* 用户注册接口支持其他属性值设置

#### 升级指南
* 使用新版本的JMessage.framework文件替换原工程下的同名旧文件
* 将新版本的JMessage.framework里的JCore link到工程中，详细参见官网集成文档



### Android SDK v2.3.0

#### 更新时间

+ 2017-10-20

#### Change Log
##### BugFix:
+ 修复deleteSingleConversation接口可能出现的删除失败的问题
+ 提升sdk稳定性

##### NewFeature:
+ 支持多端同时在线
+ 新增消息已读回执功能
+ 新增消息转发接口
+ 支持命令透传
+ Conversation类新增extra扩展字段
+ 支持群组头像
+ UserInfo支持扩展字段extras
+ 用户注册接口支持其他属性设置

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.7.jar。用 jmessage-android_v2.3.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore117.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。  
	***注意JCore 1.1.7版本新增了provider组件，集成时需要注意manifest中新增的provider组件的配置***

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)



### Web SDK v2.4.0

#### 更新时间

+ 2017-10-16

#### Change Log

##### NewFeature:

+ 支持消息透传
+ 支持群组头像
+ 支持多端同时在线
+ 消息已读回执
+ 会话、用户信息支持扩展字段
+ 注册支持扩展字段
+ 支持会话未读数获取、重置会话未读数

#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的 jmessage-sdk-web.2.4.0.min.js 替换掉老版本的 sdk





### Windows SDK v1.0.0

#### 更新时间

+ 2017-10-13

#### Change Log
+ JMessage Windows C++ SDK 首次发布， 涵盖当前 Web SDK v2.3.1 的全部功能，基于最新 C++17 语言标准(需要VS2017)， 使用了大量方便开发的新特性，基于[cpprestsdk](https://github.com/Microsoft/cpprestsdk/wiki/Programming-with-Tasks)的task/then异步接口[(更多关于task)](https://docs.microsoft.com/zh-cn/cpp/parallel/concrt/reference/task-class?f1url=https%3A%2F%2Fmsdn.microsoft.com%2Fquery%2Fdev15.query%3FappId%3DDev15IDEF1%26l%3DZH-CN%26k%3Dk(PPLTASKS%2FConcurrency%3A%3Atask)%3Bk(Concurrency%3A%3Atask)%3Bk(task)%3Bk(DevLang-C%2B%2B)%3Bk(TargetOS-Windows)%26rd%3Dtrue) ，上层可以使用回调或者co_await方式使用SDK

##### NewFeature:
+ 支持多端同时在线
+ 消息已读回执
+ 群组头像

#### 升级提示

+ 建议升级！

#### 升级指南

+ 下载 SDK ，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/im_sdk_win/)



### iOS SDK v3.2.1

#### 更新时间

2017-08-29

#### ChangeLog

##### BugFix:

* 修复用户反馈的一些 bug

##### NewFeature

* 离线事件处理升级为事件同步机制，大幅提升处理大量事件的性能，上层无需改动和适配  
* 创建 imageContent 时，可指定后缀名
* 上传头像时，指定后缀名

* 新增接口：
	* JMSGUser
		* +(void)updateMyAvatarWithData:avatarFormat:completionHandler;//指定头像后缀名
	* JMSGImageContent
		* @property(nonatomic, strong) NSString *format;//指定图片后缀名
	* JMSGFileContent
		* -(void)fileDataWithProgress:completionHandler: ;// 带下载进度的文件下载接口

#### 升级指南
* 使用新版本的JMessage.framework文件替换原工程下的同名旧文件
* 将新版本的JMessage.framework里的JCore link到工程中，详细参见官网集成文档



### Android SDK v2.2.1

#### 更新时间

+ 2017-08-15

#### Change Log
##### BugFix:
+ 修复发送自定义类型消息时，自定义通知栏文字不生效
+ 提升sdk稳定性

##### NewFeature:
+ 离线事件处理升级为事件同步机制，大幅提升处理大量事件的性能，上层无需改动和适配
+ 群事件`EventNotificationContent`中新增一个类型`group_info_updated`表示群信息被更新。代码示例见[事件处理](https://docs.jiguang.cn/jmessage/client/im_sdk_android/#_46)一节中“接收消息事件”部分
+ 新增创建ImageContent时，指定存储时的扩展名的接口

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.6.jar。用 jmessage-android_v2.2.1.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore116.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)



### Web SDK v2.3.1

#### 更新时间

+ 2017-08-11

#### Change Log

##### NewFeature:
+ 事件同步
+ 自定义通知栏
+ 消息转发
+ 群屏蔽列表

#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的 jmessage-sdk-web.2.3.1.min.js 替换掉老版本的 sdk


### iOS SDK v3.2.0

#### 更新时间

2017-06-30

#### ChangeLog

##### BugFix:

+ 修复：用户信息自动更新问题

##### NewFeature

+ 新增：消息撤回功能
+ 新增：离线消息存储控制功能
+ 新增：通知栏消息显示控制功能
+ 新增：自定义通知栏功能
+ 新增：统一上传用户信息接口

+ 新增类：
	+ 提示性消息内容类 JMSGPromptContent
		+ @property(nonatomic, readonly, copy) NSString *promptText；//提示信息
	+ 发送消息可选功能类 JMSGOptionalContent
		+ @property(nonatomic, assign) BOOL noSaveOffline;//不保存离线消息
		+ @property(nonatomic, assign) BOOL noSaveNotification;//不保存通知消息
		+ @property(nonatomic, strong) JMSGCustomNotification * customNotification; //自定义通知栏
	+ 用户信息类 JMSGUserInfo
		+ 此类仅用于修改用户信息
+ 新增接口：
	+ JMSGEventDelegate
		+ -(void)onReceiveMessageRetractEvent:;//监听消息撤回事件
	+ JMSGConversation
		+ -(void)retractMessage: completionHandler: ;//消息撤回
		+ -(void)sendMessage: optionalContent:;//自定义通知栏内容、控制离线消息存储
		+ -(NSString *)avatarLocalPath;//获取会话头像的本地路径
	+ JMSGMessage
		+ +(void)retractMessage: completionHandler: ;//消息撤回
		+ +(void)sendMessage: optionalContent:;//自定义通知栏内容、控制离线消息存储
	+ JMSGUser
		+ +(void)updateMyInfoWithUserInfo: completionHandler:;//更新用户信息（支持将字段统一上传）
		+ -(NSString *)thumbAvatarLocalPath;//获取用户头像缩略图文件的本地路径
		+ -(NSString *)largeAvatarLocalPath;//获取用户头像大图文件的本地路径
	+ JMSGMediaAbstractContent
		+ @property(nonatomic, strong, readonly) NSString * originMediaLocalPath; //获取原文件的本地路径
	+ JMSGImageContent
		+ @property(nonatomic, strong, readonly) NSString *thumbImageLocalPath;//获取缩略图的本地路径


#### 升级指南
+ 使用新版本的 JMessage.framework 文件替换原工程下的同名旧文件
+ 将新版本的 JMessage.framework 里的 JCore link 到工程中，详细参见官网集成文档




### Android SDK v2.2.0

#### 更新时间

+ 2017-6-15

#### Change Log
##### BugFix:
+ 提升sdk稳定性

##### NewFeature:
+ 支持[消息撤回](https://docs.jiguang.cn/jmessage/client/im_sdk_android/#_42)
+ 支持消息发送时的各种控制,包括：
	+ 离线消息存储控制
	+ 消息通知栏显示控制
	+ 自定义消息通知栏文字  
具体见开发指南[消息管理](https://docs.jiguang.cn/jmessage/client/im_sdk_android/#_30)一节

+ 新增统一更新用户所有信息的接口
+ 支持群聊@所有人
+ 支持用户信息自动更新
+ 支持通知栏通知点亮呼吸灯

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.3.jar。用 jmessage-android_v2.2.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore113.so 文件，替换项目中原有的libjcoreXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。

+ 如果使用jcenter的方式集成JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)




### Web SDK v2.3.0

#### 更新时间

+ 2017-6-15

#### Change Log

##### NewFeature:
+ 离线消息存储控制及消息通知栏显示控制
+ 消息撤回
+ 用户信息更新监听
+ 可获取 SDK 连接、初始化以及登录状态
+ 事件监听字段优化

#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的 jmessage-sdk-web.2.3.0.min.js 替换掉老版本的 sdk



### Web SDK v2.2.1

#### 更新时间

+ 2017-05-09

#### Change Log

##### BugFix:

+ 修复：页面加载完立刻初始化报异常 bug
+ 修复：在漫游模式下，部分场景不能获取历史消息 bug


##### NewFeature:

+ 获取群成员接口新增昵称、头像字段
+ 获取会话列表接口：单聊新增昵称、头像字段，群聊新增群名称字段

#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的 jmessage-sdk-web.2.2.1.min.js 替换掉老版本的 sdk



### iOS SDK v3.1.1

#### 更新时间

2017-05-05

#### ChangeLog

##### BugFix:

* 修复：allConversations 接口排序逻辑问题
* 修复：下载多媒体文件时下载进度回调错误的问题

##### NewFeature

* Conversation 新增 latestMsgTime 属性，用于会话排序
	* @property(nonatomic, strong, readonly) NSNumber *latestMsgTime;


#### 升级指南
* 使用新版本的JMessage.framework文件替换原工程下的同名旧文件
* 将新版本的JMessage.framework里的JCore link到工程中，详细参见官网集成文档


### Android SDK v2.1.2

#### 更新时间

+ 2017-4-28

#### Change Log
##### BugFix:
+ 提升sdk稳定性

##### NewFeature:
+ 新增获取全局未读数接口JMessageClient.getAllUnReadMsgCount()
+ 支持 jcenter 自动集成

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开 libs 文件夹。添加 jcore-android_v1.1.2.jar。用 jmessage-android_v2.1.2.jar 替换项目中原有的极光 jar 文件，并删除原有极光 jar 文件。用对应 CPU 文件夹下的 libjcore112.so 文件，替换项目中原有的 libjcoreXXX.so 文件，并删除原有的极光 so 文件，每种型号的 so 文件都可以在 SDK 下载包中找到。

+ 更新 AndroidManifest.xml
	+ 请参考 SDK 下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置。

+ 如果使用 jcenter 的方式集成 JMessage，不需要添加相关组件和资源，详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)



### iOS SDK v3.1.0

#### 更新时间

2017-04-05

#### ChangeLog

##### BugFix:

+ 修复:小概率出现的由于mediaID重复导致的消息发送失败问题。
+ 修复:获取群成员列表未按入群时间排序返回问题。

##### NewFeature

+ 新的消息同步机制
+ 支持消息漫游
+ 群组@功能
+ 群消息屏蔽
+ 支持用户信息自动更新
+ 媒体消息新增一种校验方式：hash校验。用来兼容web sdk发送的媒体消息

+ 新增接口：  
	+ 消息同步代理 
		+ 离线消息[- (void)onSyncOfflineMessageConversation:offlineMessages:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncOfflineMessageConversation:offlineMessages:)
		+ 漫游消息[- (void)onSyncRoamingMessageConversation:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncRoamingMessageConversation:)
		+ 设置消息漫游 [+ (void)setupJMessage:appKey:channel:apsForProduction:category:messageRoaming:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMessage.html#//api/name/setupJMessage:appKey:channel:apsForProduction:category:messageRoaming:)
	+ 群组@功能相关
		+ 创建包含 atList 的群消息 ：[+ (JMSGMessage *)createGroupMessageWithContent:groupId:at_list:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGMessage.html#//api/name/createGroupMessageWithContent:groupId:at_list:)
		+ 发送 atList 的消息：[- (void)sendMessage: at_list:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGConversation.html#//api/name/sendMessage:at_list:)
		+ 创建 @ 所有人的群消息 ：[+ (JMSGMessage *)createGroupAtAllMessageWithContent:groupId:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGMessage.html#//api/name/createGroupAtAllMessageWithContent:groupId:)
		+ 发送 @ 所有人的消息：[- (void)sendAtAllMessage:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGConversation.html#//api/name/sendAtAllMessage:)
		+ 判断消息中是否 @ 了自己：[- (BOOL)isAtMe](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGMessage.html#//api/name/isAtMe)
		+ 判断消息中是否 @ 了所有人：[- (BOOL)isAtAll](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGMessage.html#//api/name/isAtAll)
		+ 获取消息 @ 的群成员列表：[- (void)getAt_List:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGMessage.html#//api/name/getAt_List:)
	+ 群消息屏蔽相关
		+ 设置群消息屏蔽：[- (void)setIsShield:handler:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGGroup.html#//api/name/setIsShield:handler:)
		+ 判断群组是否被屏蔽：[group.isShieldMessage](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGGroup.html#//api/name/isShieldMessage)
		+ 获取当前用户的群屏蔽列表：[+ (void)shieldList:](https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/Classes/JMSGGroup.html#//api/name/shieldList:)

+ 接口变动：
	+ 为适配Swift的使用，allConversationsByDefault接口名改为allUnsortedConversations，只修改接口名，接口的功能保持不变。

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件

#### 升级提示
+ 升级版本后，上层需要添加消息同步的监听代理方法，不然上层无法感知
+ 需要设置消息记录漫游的开发者，调用新的初始化方法设置是否启用消息漫游



### Android SDK v2.1.1

#### 更新时间

+ 2017-03-22

#### Change Log
##### BugFix:
+ 修复某些情况下，获取不到用户头像的问题
+ 修复其他一些用户反馈的bug

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.0.jar。用 jmessage-android_v2.1.1.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore110.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。

+ 详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)



### Web SDK v2.2.0

#### 更新时间

+ 2017-03-17

#### Change Log

+ 新增：群聊@功能
+ 新增：群屏蔽功能
+ 新增：获取资源访问路径接口
+ 新增：离线消息同步监听接口（优化性能）
+ 新增：异常断线监听


#### 升级提示

+ 建议升级！

#### 升级指南

+ 用最新的jmessage-sdk-web.2.2.0.min.js替换掉老版本的sdk




### Android SDK v2.1.0

#### 更新时间

+ 2017-03-10

#### Change Log
##### BugFix:
+ 修复获取群组信息成功后，会概率出现getgroupowner()为空的情况
+ 修复发送多张图片，概率出现发送图片失败
+ 修复会话不存在时，不会上抛相关群成员变化事件
+ 修复小概率出现的由于mediaID重复导致的消息发送失败问题
+ 修复其他一些用户反馈的bug

##### NewFeature

+ 新的消息同步机制
+ 支持消息漫游
+ 群组@功能
+ 群消息屏蔽
+ 支持Dev-api好友更新事件
+ 新增一个用户离线原因：登陆状态异常
+ 支持Dev-api用户信息更新事件

##### 新增接口：
+ 群组@功能相关接口
	+ 创建包含atList的群消息 ：[conversation.createSendMessage(content,atlist,string)](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/Conversation.html#createSendMessage(cn.jpush.im.android.api.content.MessageContent,%20java.util.List,%20java.lang.String))、[JMessageClient. createAtGroupMembersMessage(long,atlist,content)](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#createAtGroupMembersMessage(long,%20java.util.List,%20cn.jpush.im.android.api.content.MessageContent))

	+ 判断消息是否@了自己：[message.isAtMe()](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/Message.html#isAtMe())

	+ 获取消息中@的群成员列表：[message.getAtUserList(callback)](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/Message.html#getAtUserList(cn.jpush.im.android.api.callback.GetUserInfoListCallback))

+ 群屏蔽功能相关接口
	+ 设置群消息屏蔽：[groupInfo.setBlockGroupMessage(int,callback)](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/GroupInfo.html#setBlockGroupMessage(int,%20BasicCallback))
	+ 判断群组是否被屏蔽：[groupInfo.isGroupBlocked()](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/GroupInfo.html#isGroupBlocked())
	+ 获取当前用户的群屏蔽列表：[JMessageClient.getBlockedGroupsList(callback)](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#getBlockedGroupsList(cn.jpush.im.android.api.callback.GetGroupInfoListCallback))

+ 设置是否需要消息漫游：[JMessageClient.init(context,boolean)](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#init(android.content.Context,%20boolean))

+ 新增离线消息事件：[OfflineMessageEvent](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/event/OfflineMessageEvent.html)

+ 新增漫游消息同步完成事件：[ConversationRefreshEvent](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/event/ConversationRefreshEvent.html)

+ 新增用户信息被更新事件： [MyInfoUpdatedEvent](https://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/event/MyInfoUpdatedEvent.html)


#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.0.jar。用 jmessage-android_v2.1.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore110.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。

+ 详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)



### iOS SDK v3.0.1

#### 更新时间

2017-02-15

#### ChangeLog

##### BugFix:

+ 修复：SDK启动时小概率出现crash。
+ 修复：从分离前版本升级到分离后版本，如果集成JPush时，需要重新登录才能收到消息的问题。
+ 修复：偶现调用登录接口没有回调的问题。

##### NewFeature

+ 在JMessage提供设计角标的方法（原来通过JPush中提供的方法进行设置）

+ 新增接口：
   + 设置角标：+ (BOOL)setBadge:(NSInteger)value;
   + 重置角标：+ (void)resetBadge;


#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件
+ 将新版本的JMessage.framework里的JCore link到工程中，详细参见官网集成文档

#### 升级提示
+ 升级版本后，因为JCore更新为v1.1.1版本,需要重要手动引入到工程中


### iOS SDK v3.0.0

#### 更新时间

2017-01-10

#### ChangeLog

+ 模块化分离为 JCore、JMessage 两部分集成，并且脱离和JPush的依赖关系。      
极光开发者服务 SDK 采用了模块化的使用模式，即一个核心（JCore）+N种服务（JMessage，JPush...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。

+ 新增接口：

	+ 注册远程推送： + (void)registerForRemoteNotificationTypes:(NSUInteger)types categories:(NSSet *)categories;
	+ 注册DeviceToken：+ (void)registerDeviceToken:(NSData *)deviceToken;

#### 升级指南
+ 注意 3.0.0及以上版本将不再支持处理器为i386的模拟器
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件
+ 将新版本的JMessage.framework里的JCore link到工程中，详细参见官网集成文档



### Android SDK v2.0.0

#### 更新时间

+ 2017-01-09

#### Change Log

+ 新增：模块化分离为 JCore，JMessage 两部分集成，原有使用的一个 jar 包，分为了 jcore 和 jmessage 两个jar 包。并且脱离和JPush的依赖关系

+ 修复一些用户反馈的bug 。

#### 升级提示

+ 建议升级！

#### 升级指南

+ 首先解压您获取到的 zip 压缩包

+ 更新库文件
	+ 打开libs文件夹。添加jcore-android_v1.1.0.jar。用 jmessage-android_2.0.0.jar 替换项目中原有的极光jar文件，并删除原有极光jar文件。用对应CPU文件夹下的 libjcore110.so 文件，替换项目中原有的libjpushXXX.so文件，并删除原有的极光so文件，每种型号的so文件都可以在SDK下载包中找到。

+ 更新AndroidManifest.xml
	+ 请参考 SDK下载包最新版本的 demo 来更新AndroidManifest.xml 文件配置。

+ 详细集成说明请参考官方[集成指南](https://docs.jiguang.cn/jmessage/client/jmessage_android_guide/)


### iOS SDK v2.2.4

#### 更新时间

+ 2016-12-19

#### Change Log

##### BugFix
+ 修复：下载缩略图大小固定的问题
+ 修改：部分地区发送图片、语音失败的问题

##### NewFeature 
+ 新增：当前登录用户信息变更通知事件 [kJMSGEventNotificationCurrentUserInfoChange](./client/jmessage_ios_appledoc_html/Constants/JMSGEventNotificationType.html)
+ 新增：修改消息 extra 字段接口[- (void)updateMessageExtra:extraValue:extraKey:](./client/jmessage_ios_appledoc_html/Classes/JMSGMessage.html#//api/name/updateMessageExtraValue:forKey:)
+ 新增：获取当前所有会话的未读消息的总数接口 [+ (NSNumber *)getAllUnreadCount](./client/jmessage_ios_appledoc_html/Classes/JMSGConversation.html#//api/name/getAllUnreadCount)

 

#### 升级指南

+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件



### Web SDK v2.1.0

#### 更新时间

+ 2016-12-14

#### Change Log

+ 新增：好友模块（添加好友，删除好友，修改好友备注，好友列表）
+ 新增：新增登出接口
+ 优化：发送消息成功回调函数新增一个参数，用于获取发送内容
+ 优化：被迫下线（sdk层面自动下线）


#### 升级指南

+ 使用新版本的 jmessage-sdk-web.js 文件替换原工程下的同名旧文件


### Web SDK v1.2.1
#### 更新时间
+ 2016-12-05

#### Change Log

+ 修复：Web SDK v1.2.0上传图片问题

#### 下载地址

+ [点击下载 Web SDK v1.2.1](https://sdkfiledl.jiguang.cn/jmessage-web-sdk.1.2.1.zip)


#### 特别说明

+ v1.x版本将不再提供新功能，仅维护因bug导致的问题，建议尽快切换到2.x版本



### iOS SDK v2.2.3
#### 更新时间
+ 2016-11-30

#### Change Log

+ 优化改进：SDK内HTTP全面更换HTTPS
+ 修复：群组事件无法创建会话的问题
+ 修复：循环发送消息导致崩溃问题


#### 升级指南

+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件



### Web SDK v2.0.0

#### 更新时间

+ 2016-11-23

#### Change Log

+ 全面升级API，支持Promise风格API
+ 新增修改用户信息功能
+ 新增更新头像功能
+ 新增更新用户密码功能
+ 新增接收位置功能
+ 新增文件上传下载功能
+ 新增支持发送和接收emoij表情功能
+ 新增跨应用消息免打扰功能
+ 新增消息自动重试逻辑功能

#### 升级指南

+ 在页面引入最新的`jmessage-sdk-web.min.js`。

#### 升级提示

+ 因为API调用方式都改变了，需要修改所有接入代码才能进行升级。

#### 特别说明

+ v1.x版本将不再提供新功能，仅维护因bug导致的问题，建议更新到v2.0版本


### iOS SDK v2.2.1
#### 更新时间
+ 2016-11-04

#### Change Log

+ 优化改进：适配JPush SDK 2.2.0，增加SDK稳定性
+ 修复：消息展示名获取不正确的问题

+ 新增事件：
	+ kJMSGEventNotificationReceiveServerFriendUpdate; //事件类型：非客户端修改好友关系收到好友更新事件


#### 升级指南

+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件

#### 升级提示

+ 注意：项目中添加libresolv.tbd库，否则编译运行会报错（2.2.1及以上版本要求）



### iOS SDK v2.2.0

#### 更新时间
+ 2016-10-18

#### Change Log
##### New Feature
+ 新增：好友功能

+ 新增：好友备注名和备注信息设置

+ 新增：发送文件消息

+ 新增：发送位置消息

+ 新增：适配 iOS 10

+ 新增事件：
    + kJMSGEventNotificationServerAlterPassword       = 2,  // 事件类型: 非客户端修改密码强制登出事件
    
    + kJMSGEventNotificationUserLoginStatusUnexpected   = 70,// 事件类型：用户登录状态异常事件（需要重新登录）
    
    + kJMSGEventNotificationReceiveFriendInvitation    = 51,// 事件类型: 收到好友邀请
    
    + kJMSGEventNotificationAcceptedFriendInvitation  = 52,// 事件类型: 对方接受了你的好友邀请
    
    + kJMSGEventNotificationDeclinedFriendInvitation   = 53,// 事件类型: 对方拒绝了你的好友邀请
    
    + kJMSGEventNotificationDeletedFriend                   = 6, // 事件类型: 对方将你从好友中删除

##### 新增接口：
+ JMSGEventDelegate
	+ -(void)onReceiveNotificationEvent:(JMSGNotificationEvent *)event;//监听事件通知，如：好友事件、被踢事件等都可以用此函数监听
+ JMSGFriendManager
	+ +(void)getFriendList:;//获取好友列表
	+ +(void)sendInvitationRequestWithUsername: appKey: reason: completionHandler: ;//发送添加好友请求
	+ +(void)acceptInvitationWithUsername: appKey: completionHandler: ;//接受好友邀请
	+ +(void)rejectInvitationWithUsername: appKey: reason: completionHandler: ;//拒绝好友邀请
	+ +(void)removeFriendWithUsername: appKey: completionHandler: ;//删除好友
+ JMSGUser
	+ @property(nonatomic, assign, readonly) BOOL isFriend;//好友关系状态
	+ @property(nonatomic, copy, readonly) NSString *noteName;//备注名
	+ @property(nonatomic, copy, readonly) NSString *noteText;//备注信息
	+ -(void)updateNoteName: completionHandler: ;//修改用户备注名
	+ -(void)updateNoteText: completionHandler: ;//修改用户备注信息
+ JMSGFriendNotificationEvent
	+ @property(nonatomic, assign, readonly) JMSGEventNotificationType eventType;//好友通知事件类型
	+ -(NSString *JMSG_NULLABLE)getReason;//获取事件发生的理由
	+ -(NSString *JMSG_NULLABLE)getFromUsername;//事件发送者的username
	+ -(JMSGUser *JMSG_NULLABLE)getFromUser;//获取事件发送者user
+ JMSGConversation
	+ -(void)sendFileMessage: fileName: ;//发送文件消息
	+ -(void)sendLocationMessage: longitude: scale: address: ;发送地理位置消息
+ JMSGMessage
	+ +(void)sendSingleFileMessage: fileName: toUser: ;//发送单聊文件消息
	+ +(void)sendSingleFileMessage: fileName: toUser: appKey: ;//发送跨应用单聊文件消息
	+ +(void)sendGroupFileMessage: fileName:toGroup: ;//发送群聊文件消息
	+ +(void)sendSingleLocationMessage: longitude: scale: address: toUser: ;//发送单聊地理位置消息
	+ +(void)sendSingleLocationMessage: longitude: scale: address: toUser: appKey: ;//发送跨应用单聊地理位置消息
	+ +(void)sendGroupLocationMessage: longitude: scale: address: toGroup: ;发送群聊地理位置消息
+ JMSGFileContent
	+ @property(nonatomic, copy, readonly) NSString *fileName;//文件名
	+ -(instancetype)initWithFileData: fileName: ;//初始化文件内容
	+ -(void)fileData:(JMSGAsyncDataHandler)handler;获取文件内容的数据
+ JMSGLocationContent
	+ @property(nonatomic, strong, readonly) NSNumber *latitude;//纬度
	+ @property(nonatomic, strong, readonly) NSNumber *longitude;//经度
	+ @property(nonatomic, strong, readonly) NSNumber *scale;//缩放
	+ @property(nonatomic, copy, readonly) NSString *address;//详细地址信息
	+ -(instancetype)initWithLatitude: longitude: scale: address: ;//初始化文件内容

##### 已过时接口：
+ JMSGUserDelegate
	+ -(void)onLoginUserKicked;// 改用JMSGEventDelegate类中的 onReceiveNotificationEvent 方法统一监听被踢、用户信息过期、好友等通知事件

##### Bug Fix
+ 修复：版本升级后会聊头像无法获取问题；
+ 修复：创建群聊会话时，如果创建群成功并且初始化成员失败时，会同时返回群信息和错误信息

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件

 


### Web SDK v1.2.0

#### 更新时间
+ 2016-10-10

#### Change Log
##### New Feature

+ 增加发送图片接口
+ 增加用户注册接口
+ 增加黑名单的跨应用接口
+ 增加群组跨应用支持
+ 优化Demo

#### 升级提示
+ 建议升级！


### iOS SDK v2.1.8

#### 更新时间
+ 2016-09-22

#### Change Log
##### Bug Fix
+ 修复：在收到大量消息的同时进行前后切换，会导致应用crash的问题；
+ 修复：在登录时偶现crash的问题
+ 修复：网络或者后台出现问题导致的下发重复事件问题

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件



### Android SDK v1.4.2
#### 更新时间
+ 2016-09-21

#### SDK Change Log

##### Bug Fix

+ 修复媒体消息发送问题

#### 升级指南

+ jar包更新至jmessage-sdk-1.4.2.jar更新时需删除老版本jar包
+ 将so库更新至 libjpush220.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置


### Android SDK v1.4.1
#### 更新时间
+ 2016-09-14

#### SDK Change Log

##### Bug Fix

+ 修复某些型号的手机应用启动时会弹出位置权限授权框的问题

#### 升级指南

+ jar包更新至jmessage-sdk-1.4.1.jar更新时需删除老版本jar包
+ 将so库更新至 libjpush220.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置


### iOS SDK v2.1.7

#### 更新时间
+ 2016-09-09

#### Change Log
##### Bug Fix
+ 修复：在32位系统下，message的时间戳不正确的问题

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### Android SDK v1.4.0
#### 更新时间
+ 2016-09-09

#### SDK Change Log

##### Bug Fix

+ 修复跨应用添加用户进黑名单时可添加自己进黑名单
+ 修复跨应用免打扰中自己可以给自己设置免打扰
+ 修复上层应用进程崩溃重启后，导致im请求发送超时。
+ 修复点击通知栏时，有一定几率message对象为空
+ 修复特殊用户名下，相关内部逻辑错误
+ 修复本地会话过多时，数据库访问的问题。

##### New Feature

+ 新增好友模块
+ 新增用户备注名和备注信息设置
+ 新增文件信息发送接口
+ 新增位置信息发送接口
+ GroupInfo中增加获取群主用户所属应用appkey的实例接口
+ getConversationList默认按时间降序排序。
+ 优化接口执行效率

##### 新增接口

+ ContactManager 好友管理接口入口类。
	+ 具体定义见api doc: [ContactManager](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/ContactManager.html)
+ UserInfo类中新增实例接口：
	+ 设置备注名：[updateNotename](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html#updateNoteName(java.lang.String,%20cn.jpush.im.api.BasicCallback))
	+ 设置备注信息：[updateNoteText](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html#updateNoteText(java.lang.String,%20cn.jpush.im.api.BasicCallback))
	+ 将用户从好友列表中移除：[removeFromFriendList](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html#removeFromFriendList(cn.jpush.im.api.BasicCallback))
  
+ ContactNotifyEvent 好友相关通知事件类
	+ 具体定义见api doc: [ContactNotifyEvent](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/event/ContactNotifyEvent.html)
  
+ 增加两种message content类型：
	+ 文件消息：[FileContent](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/content/FileContent.html)
	+ 位置消息：[LocationContent](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/content/LocationContent.html)

+ GroupInfo类中新增实例接口：[getOwnerAppkey](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/GroupInfo.html#getOwnerAppkey())

##### 注意
从此版本开始，JChat源码将不再作为sdk zip的一部分随sdk发布，取而代之的是一个界面简化的仅仅用来展示接口用法的JMessage Demo。

之前JChat的源码见[GitHub](https://github.com/jpush/jchat-android)


#### 升级指南

+ jar包更新至jmessage-sdk-1.4.0.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush219.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置。


### iOS SDK v2.1.6

#### 更新时间
+ 2016-09-01

#### Change Log
##### Bug Fix
+ 修复：网络或者后台出现问题导致的下发重复消息问题

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### Web SDK v1.1.2

#### 更新时间
+ 2016-08-31

#### Change Log
+ 添加类型转换，iOS端接收消息问题

#### 升级提示
+ 建议升级！


### Web SDK v1.1.1

#### 更新时间
+ 2016-08-30

#### Change Log
+ 修复发送群组消息问题

#### 升级提示
+ 建议升级！

### Web SDK v1.1.0

#### 更新时间
+ 2016-08-26

#### Change Log
##### New Feature
+ 增加免打扰功能
+ 支持图片，音频消息的接收功能

#### 升级提示
+ 建议升级！

### Web SDK v1.0.1

#### 更新时间
+ 2016-08-19

#### Change Log
##### New Feature
+ 增加获取用户信息的跨应用接口
+ 增加发送单聊消息的跨应用接口

#### 升级提示
+ 可选升级！


### iOS SDK v2.1.5
#### 更新时间
+ 2016-08-13

#### SDK Change Log

##### BugFix:
+ 修复本地时间和服务器时间不一致时，消息顺序错乱的问题

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### Android SDK v1.3.1
#### 更新时间
+ 2016-08-13

#### SDK Change Log

##### Bug Fix

+ 修复：本地时间与后台时间不一致导致的消息顺序错乱


#### JChat Change Log
+ 适配JMessage SDK 1.3.1


#### 升级指南

+ jar包更新至jmessage-sdk-1.3.1.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush216.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置。


### iOS SDK v2.1.3

#### 更新时间
+ 2016-07-15

#### SDK Change Log

##### New Feature
+ 新增：本应用和跨应用的免打扰功能；
+ 新增：跨应用群聊功能；
+ 新增：本应用和跨应用的黑名单功能；
+ 新增：暴露event msg作用对象的username(s),用户开发者定制event msg；
+ 新增：JMGGroup 增加一个属性 max_member_count，表示当前群成员最大人数；
+ 新增：JMGGroup 增加一个属性 ownerAppKey，表示当前群群主的appKey。
+ 新增接口：
	+ JMessage
		+ +(void)noDisturbList:(JMSGCompletionHandler)handler;//用户免打扰列表
		设置全局免打扰标识。
        + +(BOOL)isSetGlobalNoDisturb;//获取全局免打扰状态
        + +(void)setIsGlobalNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//设置是否全局免打扰
        + +(void)balckList:(JMSGCompletionHandler)handler;//获取黑名单列表
    + JMSGUser
        + @property(nonatomic, assign, readonly) BOOL isNoDisturb;//获取免打扰状态
        + -(void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//设置用户免打扰（支持跨应用设置）
        + @property(nonatomic, assign, readonly) BOOL isInBlacklist;//获取黑名单状态
        + +(void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray completionHandler:(JMSGCompletionHandler)handler;//添加黑名单
        + +(void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray completionHandler:(JMSGCompletionHandler)handler;//删除黑名单
        + +(void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler)handler;//跨应用添加黑名单
        + +(void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler)handler;//跨应用删除黑名单
    + JMSGGroup
        + @property(nonatomic, copy, readonly) NSString *ownerAppKey;//群主的appKey
        + @property(nonatomic, strong, readonly) NSString     *maxMemberCount;//获取群组人数上限
        + @property(nonatomic, assign, readonly) BOOL isNoDisturb;//获取免打扰状态
        + -(void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//设置群组消息免打扰（支持跨应用设置）
    + JMSGEventContent
        + -(NSString *JMSG_NULLABLE)getEventFromUsername;//获取事件发起者的用户名
        + -(NSArray *JMSG_NULLABLE)getEventToUsernameList;//获取事件作用对象用户名列表
    + JMSGMessage
        + +(void)sendSingleTextMessage:(NSString *)text toUser:(NSString *)username appKey:(NSString *)userAppKey; //发送跨应用单聊文本消息
        + (void)sendSingleImageMessage:(NSData *)imageData toUser:(NSString *)username appKey:(NSString *)userAppKey; //发送跨应用单聊图片消息
        + (void)sendSingleVoiceMessage:(NSData *)voiceData voiceDuration:(NSNumber *)duration toUser:(NSString *)username appKey:(NSString *)userAppKey; //发送跨应用单聊语音消息
    + 跨应用群聊
        + -(void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;//添加群组跨应用成员
        + -(void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;//删除群组跨应用成员

##### Bug Fix

+ 修复：群event msg 事件不能定制问题；

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件！

### Web SDK v1.0.0

#### 更新时间
+ 2016-07-13

#### Change Log
+ JMessage Web SDK 首次发布
+ 聊天支持：单聊，群聊
+ 聊天内容：文本
+ 提供用户管理 ，群组管理，会话列表获取功能

#### 升级提示
+ 可选升级！


### Android SDK v1.3.0

#### 更新时间
+ 2016-07-12

#### SDK Change Log

##### New Feature
+ 增加群组、黑名单、免打扰功能的跨应用能力
+ 新增全局免打扰接口
+ 新增接口：
	+ JMessageClient
		+ setNoDisturbGlobal
		设置全局免打扰标识。
		+ getNoDisturbGlobal
		获取全局免打扰标识
		+ addGroupMembers
		添加群成员（跨应用)
		+ removeGroupMembers
		移出群成员（跨应用）
		+ addUsersToBlacklist
		将用户加入黑名单（跨应用）
		+ delUsersFromBlacklist 
		将用户移出黑名单（跨应用）
	+ GroupInfo
		+ getGroupMemberInfo
		获取群成员信息（跨应用）


##### Bug Fix

+ 修复：小概率出现的无法收到消息的问题
+ 修复：偶现的native层崩溃


#### JChat Change Log
+ 适配JMessage SDK 1.3.0

##### New Feature

+ 适配：群聊、黑名单、免打扰的跨应用功能
+ 新增：全局免打扰功能


#### 升级指南

+ jar包更新至jmessage-sdk-1.3.0.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush216.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置。


### iOS SDK v2.1.1

#### 更新时间
* 2016-06-15

#### 版本号
* JMessage SDK 2.1.1
* JChat 1.1.0b1893

#### Change Log

+ 新增：对IPv6网络的支持。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件




### Android SDK v1.2.5

#### 更新时间
+ 2016-06-12

#### SDK Change Log

##### New Feature
+ Conversation对象新增设置本地未读消息数的接口
+ 新增接口：
	+ conversation.setUnReadMessageCnt
	
##### Bug Fix

+ 修复：群成员退群时，其他成员处显示的提示文字不正确
+ 修复：群主退群后，本地群主信息没有更新。
+ 修复：用户首次收到消息，打印收到的message 中targetName为空
+ 修复：概率出发送群聊消息，应用崩溃
+ 修复：登录一个帐号A，快速再登录帐号B概率出现数据库操作异常
+ 修复：dev api移除群聊免打扰后，sdk没有更新状态
+ 修复：SDK接收到group event后messageid字段值为0
+ 优化：有大量群成员的群组中，数据的处理效率


#### JChat Change Log
+ 适配 JMessage SDK 1.2.5
								
##### Bug Fix

+ 修复：1.2.9下拉刷新bug
+ 修复：1.2.9收到消息后可能出现会话丢失的bug
+ 优化：收到大量离线消息后UI卡顿现象

#### 升级指南

+ jar包更新至jmessage-sdk-1.2.5.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush211.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。


### iOS SDK v2.1.0

#### 更新时间
* 2016-05-10

#### 版本号
* JMessage SDK 2.1.0
* JChat 1.1.0b1870

#### Change Log
+ 实现跨应用单聊
+ 支持VIP用户群组上限突破200

#### 升级提示

+ 建议升级！

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### Android SDK v1.2.3

#### 更新时间
+ 2016-04-07

#### SDK Change Log

##### Bug Fix

+ 修复：从旧版本升级到1.2.1导致的崩溃问题


#### JChat Change Log
+ 更新JMessage jar到1.2.3
								


#### 升级指南

+ jar包更新至jmessage-sdk-1.2.3.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush213.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。


### Android SDK v1.2.1

#### 更新时间
+ 2016-03-31

#### SDK Change Log

##### New Feature
+ 新增免打扰功能
+ 支持VIP用户群组上限突破200
	+ groupInfo中新增max_member_count属性，表示当前群成员最大人数。
+ 对外接口中需要传List作为参数的，对List size做限制。
+ 新增接口：
	+ JMessageClient
		+ JMessageClient.getNoDisturbList(GetNoDisturbListCallback callback) 获取用户的免打扰名单
	+ UserInfo
		+ userinfo.setNoDisturb(int noDisturb,Callback callback) 设置用户的免打扰状态
		+ userinfo.getNoDisturb() 获取用户的免打扰状态
		
	+ GroupInfo：
		+ groupinfo.setNoDisturb（int noDisturb,Callback callback）设置群组的免打扰状态
		+ groupinfo.getNoDisturb() 获取群组的免打扰状态
		+ groupinfo.getMaxMemberCount() 获取群成员的最大上限



##### Bug Fix

+ 修复：api 调用GetGroupInfo 获取一个已经被销毁的群组，返回码为0
+ 修复：消息正在发送的过程中，调用Login有可能导致数据库报错


#### JChat Change Log
+ 适配JMessage SDK 1.2.1
								
##### New Feature

+ 新增免打扰功能.

##### Bug Fix

+ 修复compileSdkVersion 改到23（android 6.0）后，工程报错。
+ 修复添加群组成员，界面无变化
+ 群成员搜索优化


#### 升级指南

+ jar包更新至jmessage-sdk-1.2.1.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush211.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。

### iOS SDK v2.0.1

#### 更新时间
* 2016-03-22

#### 版本号
* JMessage SDK 2.0.1
* JChat 1.1.0b1611

#### Change Log
+ 修复：由于切换设备变更群成员， 群组信息不同步引起的消息发送失败。

#### 升级提示

+ 建议升级！
+ 由于 API 与 Model 层面很大范围的变更，建议参考 JChat 项目来适配新的 JMessage iOS SDK。

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### Android SDK v1.2.0

#### 更新时间

+ 2016-03-07

#### SDK Change Log

##### New Feature
+ 实现跨应用聊天
+ message中新增getServerMessageId接口
+ 新增setDebugMode接口
+ 新增服务器修改用户密码的event处理
+ 新增接口
	+ Conversation
		+ conversation.getTargetAppkey 获取会话对象的appkey（仅单聊）
		+ Conversation.createSingleConversation(username,appkey) 创建指定appkey的跨应用会话。
		+ JMessageClient.getSingleConversation(username,appkey) 获取与指定appkey下user的会话。
		+ JMessageClient.enterSingleConversation(username,appkey) 进入与指定appkey下user的会话。
		+ JMessageClient.deleteSingleConversation(username,appkey) 删除与指定appkey下user的会话
	+ Message
		+ message.getTargetAppKey 获取消息对象的appkey.（仅单聊消息）
		+ message.getFromAppKey 获取消息发送这个的appkey。
		+ message.getServerMessageId 获取消息对应服务端的messageId。
	+ UserInfo
		+ userinfo.getAppKey 获取用户所属的appkey。
		+ JMessageClient.getUserInfo(username,appkey,callback) 获取指定appkey下的用户信息。
	+ JMessageClient
		+ setDebugMode 打开JMessage的debug模式，作用等同于JPush的setDebugMode.

	+ 已过时接口
		+ JMessageClient.enterSingleConversaion 接口名拼写错误，使用JMessageClient.enterSingleConversation替代。
		+ JMessageClient.exitConversaion 接口名拼写错误, 使用JMessageClient.exitConversation替代。
		+ UserDeletedEvent 、 UserLogoutEvent 统一使用LoginStateChangeEvent替代。


##### Bug Fix

+ 修复通过getGroupList拿到gid之后，直接拿groupMembers返回空的问题
+ 修复删除会话时未删除通知栏消息
+ 修复conversation 接口名拼写错误
+ 修复首次收到消息创建会话的title错误。
+ 修复createConversation接口没有做登陆验证。
+ 修复跨应用某种情况下会出现循环获取userinfo的bug
+ 修复多次调用login而不调logout导致上一个登陆用户的缓存信息未清掉

#### JChat Change Log
+ 适配JMessage SDK 1.2.0
								
##### New Feature

+ 会话列表提供断网提示
+ 草稿可以在会话列表显示

##### Bug Fix

+ 修复：某些机型拍照上传图片失败bug
+ 修复：App启动时抛出WindowWarning的bug
+ 修复：对话框裁剪成圆角后有黑色阴影的bug
+ 修复：删除本地跨应用会话，对应通知栏消息未清掉
+ 修复：群聊天详情里，点击删除成员，进入到聊天成员中，群成员不显示用户名
+ 修复：群聊天详情界面中，点击全部群成员界面添加不存在的用户，界面停留在转圈的状态
+ 修复：用户主动退出群，退出群时会被系统桌面覆盖


#### 升级指南

+ jar包更新至jmessage-sdk-1.2.0.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush207.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。

### iOS SDK v2.0.0

#### 更新时间
* 2016-02-22

#### 版本号
* JMessage SDK 2.0.0
* JChat 1.1.0b1460

#### Change Log
+ 消息结构调整：现在一条消息由一个 JMSGMessage 类加上多个类型的 Content 组成，如 JMSGTextContent;
+ 对象化：会话里有 target 对象（JMSGUser 或者 JMSGGroup），消息里有 target JMSGUser 对象，fromUser 对象；
+ 通知调整：由之前的 NSNotification 换成 Delegate 的方式，使用更简单、直观；
+ 性能优化：对常用的信息，SDK内部做了缓存，以减少文件、网络访问；
+ 对外 API 头文件加了完善的文档注释，包含使用建议。

#### 升级提示

+ 建议升级！
+ 由于 API 与 Model 层面很大范围的变更，建议参考 JChat 项目来适配新的 JMessage iOS SDK。

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件

### Android SDK v1.1.5

#### 更新时间

* 2015-12-11

#### SDK Change Log

##### New Feature

* 群成员变化event全部上抛sdk不过滤
* 用户小头像sdk内部作缓存
* 内部并发线程数控制，防止太多线程并发执行导致问题
* 优化网络任务执行效率
* 本地媒体文件存储按会话分类，方便之后清理。
* 新增接口:
	* ImageContent 新增通过传Bitmap来构造实例的接口
	* Conversation.CreateMessage 新增自定义FromName的接口，开发者可以自定义message的FromName
	* UserInfo 新增获取头像bitmap的异步接口getAvatarBitmap、getBigAvatarBitmap，并且sdk会在内部会对小头像的bitmap做缓存。
* 已过时接口:
	* EventNotificationContent.containsGroupOwner
	* UserInfo.getAvatarFileAsync


##### Bug Fix


* 使用自定义类继承BasicCallback时，请求会报错
* 一些对外接口没有做登陆检查,未登录时调用接口会有问题
* 修复发送大语音文件，对方收到后下载失败的bug
* 修复首次收到群消息展示的群组的ID
* 修复同时调用拿大头像和小头像时，其中有一个返回Null。

#### JChat Change Log
* 适配JMessage1.1.5

#### New Feature


* 发送多张图片时，逐张发送
* 相册按照修改时间进行排序
* 上传头像时进行裁剪
* 优化：一次发送9张图片，能发送成功，但效率比较低
* 优化：点击jchat 用户在【我】处查看自己头像，提示正在加载，体验待优化


##### Bug Fix


* 修复：加载上一页消息时如果不存在上一页消息，会多次刷新的问题
* 修复：单聊清空聊天记录异常的问题
* 修复：发送多张图片有时出现NPE异常
* 修复：发送9张图片，可能会卡在正在发送的提示界面，图片实际没有发送成功
* 修复：小米4手机更新头像，从文件管理处选择图片无法更新头像


#### 升级提示

+ 建议升级！

#### 升级指南
* 将jar包更新至 jmessage-sdk-1.1.5.jar更新时需删除老版本jar包。
* 将so库更新至 libjpush205.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
* 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
* 如果是从更早的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。


### Android SDK v1.1.4
#### 更新时间

* 2015-09-28

#### SDK Change Log

##### New Feature

* 新增黑名单功能
* 新增用户被删除事件
* 收到群聊消息时，通知栏的tickerText显示消息发送者的displayName而不是群名
* 新增接口：createGroupConversation(long)、createSingleConversation(String)、getTargetInfo()、getLatestMessage()
* 过时接口：createConversation(ConversationType,long)、createConversation(ConversationType,String)、getTargetID()、getLatestMsgDate()
getLatestType()、getLatestText()
* 新增接口：getTargetInfo()、getFromUser()
* 已过时接口：getTargetID()、getTargetName()、getFromID()、getFromName()、getFromType()
* 新增接口：ImageContent类中新增createImageContentAsync异步创建ImageContent的接口

##### Bug Fix

* 修复dev api 添加删除群用户，群的聊天详情UI没有更新
* 修复customContent.setContentType方法文档没有说明其作用
* 修复昵称设置仅仅是表情会出现异常，返回服务端错误
* 修复调用stopPush后IM无法登录。
* 修复JMessage配置文件包名和appkey不匹配的，Demo APP依然能注册成功。
* 修复createSendMessage接口在用户未登录时调用直接崩溃。
* 修复用户发媒体信息时被踢下线，之前发送的消息状态一直处于"sending"
* 修复dev api添加/删除群用户时，相应事件未抛给上层
* 修复收到富媒体推送时，点击通知栏没有跳转的问题

#### JChat Change Log

#### New Feature

* 聊天消息支持分页加载
* 增加"关于"页面
* 优化聊天、聊天详情界面加载的性能
* 被拉黑时，使用自定义消息"消息已发出，但被对方拒收了"提示用户

##### Bug Fix

* 修复发送图片成功，但UI界面显示100%
* 修复群主点击进入群【聊天详情】，减号有时候加载5/6s才显示
* 修复如果一个会话窗口的消息过多，点击会话出现加载无响应的情况
* 修复软键盘弹出后，点击软键盘上的收起按钮，界面不会收回的bug
* 修复在被踢下线后，点击确定按钮抛出WindowLeak异常的bug
* 修复在启动APP后可能出现的异常：RuntimeException：Performing stop activity that is not resume
* 修复某些手机设置录音为询问或禁止时，点击录音崩溃bug
* 修复聊天标题设置emoji后显示不正常bug
* 修复在聊天界面预览大图与聊天界面图片消息顺序不一致bug
* 修复通过接口不填写昵称时，进入聊天界面不显示用户名的bug
* 修复选择图片后，点击原图后发送图片，APP崩溃bug
* 修复发送图片时，通过聊天详情再次进入聊天界面时，图片进度不更新bug
* 图片发送成功后，删除生成的图片
* 修复接收离线消息时，APP崩溃bug

#### 升级提示

+ 建议升级！

#### 升级指南
* 将jar包更新至 jmessage-sdk-1.1.4.jar更新时需删除老版本jar包。
* 将so库更新至 libjpush205.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
* 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
* 如果是从更早的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。




### iOS SDK v1.0.6

#### 更新时间
* 2015-09-14

#### 版本号
* JMessage 1.0.6b283
* JChat 1.0.2b11

#### Change Log
+ 收发消息过多时引起的bug
+ 解决引用第三方库冲突
+ 七牛Token失效无法恢复。
+ 发送语音或者图片七牛上传时候崩溃
+ 接收宽图收到为长图
+ 下载原图实际为缩略图
+ 解决custom类型消息收发崩溃问题
+ 播放语音和录制语音不能同时进行
+ 修复iOS端发送给安卓端无法下载大图
+ 修复语音不能正常下载问题
+ 修复了APNS用户不显示昵称而是username问题
+ 修复了转换json错误信息
+ 增加了API的登陆校验
+ 解决badge上报bug

#### 升级提示

+ 建议升级！

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件

### Android SDK v1.1.3

#### 更新时间
2015-08-17

#### Change Log
+ 修复断开网络，群聊的会话界面里，进入【聊天详情】的按钮会消失
+ 修复发送自定义类型消息，jchat 接收方通知栏会有展示
+ 修复异步获取用户头像的接口getAvatarFileAsync，获取无头像的用户信息，返回码不合理
+ 修复没有昵称的群主在邀请人进群后，被邀请方显示的通知中没有显示群主的username
+ 修复收到加群事件时，由于网络不稳定导致事件有小概率丢失
+ JChat:修复收到的首张图片不会自动下载
+ JChat:修复从群详情里，选择里面的群成员发送消息，应用崩溃


#### 升级提示

+ 建议升级！

#### 升级指南
+ jar包更新至jmessage-android-1.1.3.jar，更新时需删除老版本jar
+ so库更新，/libs/armeabi/libjpush205.so.同时删除原来老版本的so


### Android SDK v1.0.18
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

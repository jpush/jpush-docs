# JPush 产品简介

<br/>

JPush 是经过考验的大规模 App 推送平台，每天推送消息数超过 5 亿条。
开发者集成 SDK 后，可以通过调用 API 推送消息。同时，JPush 提供可视化的 web 端控制台发送通知，统计分析推送效果。
JPush 全面支持 Android, iOS, Winphone 三大手机平台。


## 消息形式
JPush 提供四种消息形式：通知，自定义消息，富媒体和本地通知。

### 通知

或者说 Push Notification，即指在手机的通知栏（状态栏）上会显示的一条通知信息。
通知主要用来达到提示用户的目的，应用于新闻内容、促销活动、产品信息、版本更新提醒、订单状态提醒等多种场景

开发者参考文档：[Push API v3 notification](../server/push/rest_api_v3_push/#notification)


### 自定义消息

自定义消息不是通知，所以不会被 SDK 展示到通知栏上。其内容完全由开发者自己定义。
自定义消息主要用于应用的内部业务逻辑。一条自定义消息推送过来，有可能没有任何界面显示。

开发者参考文档：[Push API v3 message](../server/push/rest_api_v3_push/#message)


<a name="rich_push"></a>
### 富媒体
JPush 支持开发者发送图文并茂的通知，从而更好的传达信息，带来更丰富的用户互动。
JPush 提供了 5 种模板，开发者可以通过填充模板的内容，发送 landing page、弹窗、信息流形式的富媒体通知。
开发者还可以直接通过 URL 发送预先编辑好的页面。
富媒体当前支持 Android 平台，为更好的使用富媒体的功能，建议更新当前 SDK 版本至 v2.1.8 及以上。
暂时只能通过极光推送的控制台发送，不支持 API 形式。

Android 开发者参考文档：[Rich Push 开发指南](../advanced/rich_push/)


### 地理围栏
JPush 支持开发者直接通过极光推送的控制台，通过地图圈选一个经纬度范围，创建一个虚拟的栅栏围出一个虚拟地理边界，当开发者APP的用户进入、离开这个区域，或在该区域内活动时，设备APP可以自动接收通知，实现准确的消息推送，把有用的信息，在合适的地方，推送给合适的人。
地理围栏当前支持 Android、iOS 平台，为更好的使用地理围栏的功能，建议更新当前 Android SDK 版本至 v3.1.8 及以上，更新当前 iOS SDK 版本至 v3.1.2 及以上。


控制台操作文档：[地理围栏](https://docs.jiguang.cn/jpush/console/Instructions/#_18) <br/>
Android 开发者参考文档：[地理围栏](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_11) <br/>
iOS 开发者参考文档：[地理围栏](https://docs.jiguang.cn/jpush/client/iOS/ios_api/#_158)


### 日活优化
为了帮助开发者增加其APP的用户粘性，提升活跃度，尽可能的唤醒其APP沉默用户，JPush 提供了“早上好” 的功能。<br/>

#### 早上好
可以通过极光推送的控制台自行开启，开启后将会每天自动推送最新的天下大事或者生活小贴士等多类型视频多媒体消息到开发者APP的全量用户，从而更好的传达信息，带来更丰富的用户互动。<br/>
使用指南参考文档：[早上好](https://docs.jiguang.cn/jpush/console/Instructions/#_19)<br/>
此功能目前仅支持 Android 平台，为更好的使用早上好的功能，需要更新您集成的 Android SDK 版本至官方最新版本。<br/>


### 本地通知
本地通知 API 不依赖于网络，无网条件下依旧可以触发；本地通知的定时时间是自发送时算起的，不受中间关机等操作的影响。
本地通知与网络推送的通知是相互独立的，不受保留最近通知条数上限的限制。
本地通知适用于在特定时间发出的通知，如一些 Todo 和闹钟类的应用，在每周、每月固定时间提醒用户回到应用查看任务。

Android 开发者参考文档：[Android 本地通知](../client/Android/android_api/#api_10)
iOS 开发者参考文档：[iOS 本地通知](../client/iOS/ios_api/#_67)

## 推送目标
通过使用标签，别名，Registration ID 和用户分群，开发者可以向特定的一个或多个用户推送消息。

### 标签
为安装了应用程序的用户打上标签，其目的主要是方便开发者根据标签，来批量下发 Push 消息。
可为每个用户打多个标签。
举例： game, old_page, women


### 别名
每个用户只能指定一个别名。
同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

Android 开发者参考文档：[Android 标签和别名](../client/Android/android_api/#api_3)
iOS 开发者参考文档：[iOS 标签和别名](../client/iOS/ios_api/#apiios)
使用别名和标签推送请参考文档：[Push API v3 Audience](../server/push/rest_api_v3_push/#audience)

### Registration ID
客户端初始化 JPush 成功后，JPush 服务端会分配一个 Registration ID，作为此设备的标识（同一个手机不同 App 的 Registration ID 是不同的）。开发者可以通过指定具体的 Registration ID 来进行对单一设备的推送。

### 用户分群
用户分群的筛选条件有：标签、地理位置、活跃用户、系统版本、智能标签。
比如，开发者可以设置这样的用户分群：位于北京、上海、广州和深圳，并且最近 7 天内的活跃用户。
开发者可以通过在控制台设置好用户分群之后，在控制台推送时指定该分群的名称或使用 API 调用该分群的 id 发送。

用户分群控制台使用指南：[用户分群](../console/Instructions/#_16)


## 统计分析
JPush 支持推送数量、用户打开次数、用户使用时长、新增用户、活跃用户等数据的统计。
Android 开发者需要实现了相关的统计 API，才可以进行用户相关的统计。
iOS 开发者不需要实现统计 API，可以直接在【控制台】-【统计】页面查看相关数据。

Android 开发者参考文档：[统计分析 API](../client/Android/android_api/#api_4)


## 快速开始
+  到极光推送官方网站[注册开发者帐号](https://www.jiguang.cn/accounts/register)；
+  [登录](https://www.jiguang.cn/accounts/login/form)进入管理控制台，创建应用程序，得到 Appkey（SDK 与服务器端通过 Appkey 互相识别）；
+  在推送设置中给 Android 设置包名、给 iOS 上传证书、启用 WinPhone，根据你的需求进行选择；
+  [下载 SDK](../resources/) 集成到 App 里。


## 技术支持
当出现问题时：

+ 请仔细阅读文档，查看是否有遗漏。 [Android FAQ](../client/Android/android_faq/) 、 [iOS FAQ](../client/iOS/ios_faq/)
+ 你可以到极光社区搜索类似问题
+ 给我们的 support 发邮件 support&#64;jpush.cn

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

+ 你需要咨询的产品是 JPush，是否同时使用了极光其他的产品
+ 你所调用的是什么 API，所传参数，完整的报错信息，出现异常的时间点
+ 如果收不到消息，提供应用的 Appkey，消息的 Message ID，设备的 registration ID 信息
+ 如果是 SDK 问题请提供对应的 SDK 版本和完整的日志记录，日志信息请使用 TXT 文件上传
+ 出现异常的设备是 iOS 还是 Android，列出具体的机型和系统





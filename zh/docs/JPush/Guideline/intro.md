#JPush产品简介
<style>
img[alt=jpush_ios_v] { width: 500px; }
img[alt=jpush_android_so] { width: 800px; }

</style>
JPush是经过考验的大规模APP推送平台，每天推送消息数超过5亿条。
开发者集成SDK后，可以通过调用API推送消息。同时，JPush提供可视化的web端控制台发送通知，统计分析推送效果。
JPush全面支持 Android, iOS, Winphone 三大手机平台。


<br />
#消息形式
JPush提供四种消息形式：通知，自定义消息，富媒体和本地通知。

###**通知**

或者说 Push Notification，即指在手机的通知栏（状态栏）上会显示的一条通知信息。

通知主要用于提示用户的目的，应用于新闻内容、促销活动、产品信息、版本更新提醒、订单状态提醒等多种场景

Android 开发者参考：[相应的API文档](http://www.baidu.com)

iOS 开发者参考：[相应的API文档](http://www.baidu.com)

###**自定义消息**

自定义消息不是通知，所以不会被SDK展示到通知栏上。其内容完全由开发者自己定义。

自定义消息主要用于应用的内部业务逻辑。一条自定义消息推送过来，有可能没有任何界面显示。

Android 开发者参考：[相应的API文档](http://www.baidu.com)

iOS 开发者参考：[相应的API文档](http://www.baidu.com)


###**富媒体**
JPush支持开发者发送图文并茂的通知，从而更好的传达信息，带来更丰富的用户互动。

JPush提供了5种模板，开发者可以通过填充模板的内容，发送landing page、弹窗、信息流形式的富媒体通知。

开发者还可以直接通过URL发送预先编辑好的页面。

富媒体暂时只能通过极光推送的控制台发送，不支持API形式。

富媒体当前支持Android平台，Android开发者参考：[相应的API文档](http://www.baidu.com)

### **本地通知**
本地通知API不依赖于网络，无网条件下依旧可以触发；本地通知的定时时间是自发送时算起的，不受中间关机等操作的影响。

本地通知与网络推送的通知是相互独立的，不受保留最近通知条数上限的限制。

本地通知适用于在特定时间发出的通知，如一些Todo和闹钟类的应用，在每周、每月固定时间提醒用户回到应用查看任务。

Android 开发者参考：[相应的API文档](http://www.baidu.com)

iOS 开发者参考：[相应的API文档](http://www.baidu.com)


<br/>
#推送目标
通过使用标签，别名，Registration ID 和用户分群，开发者可以向特定的一个或多个用户推送消息。




### **标签**
为安装了应用程序的用户打上标签，其目的主要是方便开发者根据标签，来批量下发 Push 消息。

可为每个用户打多个标签。

举例： game, old_page, women

Android 开发者参考：[相应的API文档](http://www.baidu.com)

iOS 开发者参考：[相应的API文档](http://www.baidu.com)


### **别名**
每个用户只能指定一个别名。

同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

Android 开发者参考：[相应的API文档](http://www.baidu.com)

iOS 开发者参考：[相应的API文档](http://www.baidu.com)


### **用户分群**
用户分群的筛选条件有：标签、地理位置、系统版本、注册时间、活跃用户和在线用户。

比如，开发者可以设置这样的用户分群：位于北京、上海、广州和深圳，并且最近7天在线的用户。

开发者可以通过在控制台设置好用户分群之后，在控制台推送时指定该分群的名称或使用API调用该分群的id发送。

Android 开发者参考：[相应的API文档](http://www.baidu.com)

iOS 开发者参考：[相应的API文档](http://www.baidu.com)



<br/>
# 统计分析
JPush支持推送数量、用户打开次数、用户使用时长、新增用户、活跃用户等数据的统计。

Android开发者需要实现了相关的统计API，才可以进行用户相关的统计。

iOS的开发者不需要实现统计API，可以直接在【控制台】-【统计】页面查看相关数据。

Android 开发者参考：[相应的API文档](http://www.baidu.com)

iOS 开发者参考：[相应的API文档](http://www.baidu.com)



<br/>
#快速开始
1. 到极光推送官方网站[注册开发者帐号](https://www.jiguang.cn/accounts/register/form)；
2. [登录](https://www.jiguang.cn/accounts/login/form)进入管理控制台，创建应用程序，得到 Appkey（SDK与服务器端通过Appkey互相识别）；
3. [下载SDK](http://www.baidu.com) 集成到 App 里。


<br/>
#技术支持
当出现问题时：

+ 请仔细阅读文档，查看是否有遗漏。 [Android FAQ](http://www.baidu.com)  [iOS FAQ](http://www.baidu.com)
+ 你可以到极光社区搜索类似问题
+ 给我们的support发邮件support@jpush.cn

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

+ 使用的什么 API 的接口，比如：https://api.jpush.cn/v3/push  （这个要换）
+ 提供appkey，message id信息
+ 提供调用 API 出现问题时的时间
+ 如果是 SDK 问题请提供对应的 SDK 版本和完整的日志记录




